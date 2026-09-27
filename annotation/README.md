# Three-stage annotation

Annotation is deliberately split into three paid calls so that each call has a
narrow semantic objective:

1. factual claims, source-turn grounding, per-turn correctness, and final-answer
   correctness;
2. logical fidelity, causal/dependency order, task progress, step validity, and
   refusal;
3. perturbation recognition, immediate correction, and event-specific
   pollution/recovery dynamics.

The implementation calls only:

```text
https://api.anthropic.com/v1/messages
```

It uses `thinking={"type":"adaptive"}` and
`output_config.effort="high"`. Redirects and environment proxies are disabled.
No API key is stored in this repository.

## Canonical input

The annotator consumes JSONL. Each line is one job containing evaluator-only
authority, the shared user turns, and one or more model trajectories:

```json
{
  "job_id": "task-001__condition-L1.1",
  "shared": {
    "authority": {
      "task": "Original task",
      "reference_answer": "Reference answer",
      "scoring": "Correctness rules"
    },
    "user_turns": [
      {"turn_id": "T1", "turn_index": 1, "content": "Visible request"}
    ]
  },
  "trajectories": [
    {
      "conversation_id": "task-001__L1.1__repeat-01",
      "metadata": {
        "model": "evaluated-model",
        "task_id": "task_001",
        "condition_id": "task_001__1.1__k1__middle",
        "repeat_id": 1,
        "variant": "perturbed",
        "subclass": "1.1",
        "injection_count": 1,
        "injection_turn_ids": ["T1"],
        "overall_eligible": true,
        "position_eligible": true,
        "frequency_eligible": false
      },
      "assistant_responses": [
        {
          "turn_id": "T1",
          "turn_index": 1,
          "content": "Visible response",
          "assistant_response_units_exact": [
            {"unit_id": "T1.U001", "exact_text": "Visible response"}
          ]
        }
      ],
      "perturbation_events": []
    }
  ]
}
```

For perturbed trajectories, provide immutable event boundaries in
`perturbation_events`; the model is not asked to guess injection locations.
Exact response units must preserve and cover the visible assistant text.

For evaluation, include the paired clean and perturbed trajectories for every
repeat. Their `model`, `task_id`, `condition_id`, and `repeat_id` must match;
only `variant` changes. Keep the evaluation-selection metadata shown above so
that the overall, position, and frequency panels cannot be mixed accidentally.

## Run

From the repository root:

```powershell
python -m pip install -r requirements.txt
$env:PYTHONPATH = "$PWD\annotation\src"
$env:ANTHROPIC_API_KEY = Read-Host "Anthropic API key"
python -m sciarp_annotation validate-input path\to\jobs.jsonl
python -m sciarp_annotation annotate path\to\jobs.jsonl --output outputs --concurrency 4
```

Each job gets atomic `stage_1.json`, `stage_2.json`, optional `stage_3.json`,
`annotation.json`, and `status.json` files. Restarting reuses a stage only when
both its canonical input hash and prompt hash match. Ambiguous failures after a
request may have been billed are not automatically retried.
