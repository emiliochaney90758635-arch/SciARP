"""Minimal async client for the official Anthropic Messages API."""

from __future__ import annotations

import asyncio
import json
import random
from dataclasses import dataclass
from typing import Any

import httpx


ANTHROPIC_MESSAGES_URL = "https://api.anthropic.com/v1/messages"
ANTHROPIC_VERSION = "2023-06-01"


class ClaudeAPIError(RuntimeError):
    """Raised when the official API call did not yield a usable response."""


@dataclass(frozen=True)
class ClaudeClientConfig:
    api_key: str
    model: str = "claude-opus-5"
    max_tokens: int = 64_000
    connect_timeout_seconds: float = 30.0
    read_timeout_seconds: float = 900.0
    max_attempts: int = 5

    def __post_init__(self) -> None:
        if not self.api_key.strip():
            raise ValueError("ANTHROPIC_API_KEY is empty")
        if self.max_tokens < 1:
            raise ValueError("max_tokens must be positive")
        if self.max_attempts < 1:
            raise ValueError("max_attempts must be positive")


class ClaudeClient:
    """Calls only Anthropic's fixed official endpoint.

    `trust_env=False` prevents HTTP(S)_PROXY and similar environment variables
    from silently routing requests through an intermediary.
    """

    def __init__(self, config: ClaudeClientConfig) -> None:
        self.config = config
        timeout = httpx.Timeout(
            connect=config.connect_timeout_seconds,
            read=config.read_timeout_seconds,
            write=60.0,
            pool=60.0,
        )
        self._http = httpx.AsyncClient(
            timeout=timeout,
            trust_env=False,
            follow_redirects=False,
            headers={
                "x-api-key": config.api_key,
                "anthropic-version": ANTHROPIC_VERSION,
                "content-type": "application/json",
                "user-agent": "sciarp-annotation/1.0.0",
            },
        )

    async def __aenter__(self) -> "ClaudeClient":
        return self

    async def __aexit__(self, *_: object) -> None:
        await self.aclose()

    async def aclose(self) -> None:
        await self._http.aclose()

    async def annotate(
        self,
        *,
        system_prompt: str,
        input_payload: dict[str, Any],
        output_schema: dict[str, Any],
    ) -> tuple[dict[str, Any], dict[str, Any]]:
        request_body = {
            "model": self.config.model,
            "max_tokens": self.config.max_tokens,
            "system": system_prompt,
            "messages": [
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": json.dumps(
                                input_payload,
                                ensure_ascii=False,
                                separators=(",", ":"),
                            ),
                        }
                    ],
                }
            ],
            "thinking": {"type": "adaptive"},
            "output_config": {
                "effort": "high",
                "format": {"type": "json_schema", "schema": output_schema},
            },
        }

        response: httpx.Response | None = None
        for attempt in range(1, self.config.max_attempts + 1):
            try:
                response = await self._http.post(
                    ANTHROPIC_MESSAGES_URL, json=request_body
                )
            except (httpx.ConnectError, httpx.ConnectTimeout, httpx.PoolTimeout) as exc:
                if attempt == self.config.max_attempts:
                    raise ClaudeAPIError(
                        f"connection failed after {attempt} attempts: {type(exc).__name__}"
                    ) from exc
                await asyncio.sleep(self._backoff_seconds(attempt))
                continue
            except (
                httpx.ReadTimeout,
                httpx.WriteTimeout,
                httpx.RemoteProtocolError,
            ) as exc:
                raise ClaudeAPIError(
                    "ambiguous transport failure; not retried to avoid duplicate billing: "
                    f"{type(exc).__name__}"
                ) from exc

            if response.status_code in {408, 409, 429} or response.status_code >= 500:
                if attempt < self.config.max_attempts:
                    retry_after = self._retry_after_seconds(response)
                    await asyncio.sleep(retry_after or self._backoff_seconds(attempt))
                    continue
            break

        if response is None:
            raise ClaudeAPIError("no HTTP response received")
        if response.is_redirect:
            raise ClaudeAPIError(
                "official endpoint returned a redirect; redirect was refused"
            )
        if response.status_code >= 400:
            request_id = response.headers.get("request-id", "unknown")
            raise ClaudeAPIError(
                f"Anthropic API HTTP {response.status_code} (request_id={request_id}): "
                f"{self._safe_error(response)}"
            )

        try:
            body = response.json()
        except ValueError as exc:
            raise ClaudeAPIError("Anthropic returned non-JSON response data") from exc

        stop_reason = body.get("stop_reason")
        if stop_reason == "max_tokens":
            raise ClaudeAPIError(
                "response reached max_tokens; not retried automatically because the request was billed"
            )

        text_blocks = [
            block.get("text", "")
            for block in body.get("content", [])
            if isinstance(block, dict) and block.get("type") == "text"
        ]
        if not text_blocks:
            raise ClaudeAPIError("Anthropic response contained no text output block")
        try:
            annotation = json.loads("".join(text_blocks))
        except json.JSONDecodeError as exc:
            raise ClaudeAPIError(
                "structured response was not valid JSON; not retried automatically"
            ) from exc
        if not isinstance(annotation, dict):
            raise ClaudeAPIError("structured response root must be a JSON object")

        metadata = {
            "request_id": response.headers.get("request-id") or body.get("id"),
            "message_id": body.get("id"),
            "model": body.get("model", self.config.model),
            "stop_reason": stop_reason,
            "usage": body.get("usage", {}),
        }
        return annotation, metadata

    @staticmethod
    def _backoff_seconds(attempt: int) -> float:
        return min(60.0, 2.0 ** (attempt - 1)) + random.uniform(0.0, 0.5)

    @staticmethod
    def _retry_after_seconds(response: httpx.Response) -> float | None:
        value = response.headers.get("retry-after")
        if value is None:
            return None
        try:
            return min(300.0, max(0.0, float(value)))
        except ValueError:
            return None

    @staticmethod
    def _safe_error(response: httpx.Response) -> str:
        try:
            payload = response.json()
            message = payload.get("error", {}).get("message")
            if isinstance(message, str):
                return message[:500]
        except ValueError:
            pass
        return response.text[:500]
