# Outcome-coding convention audit

## Independent registry note

The trial registry labels disease control as the positive analysis outcome.
For every fitted binary model, records with SD or PD are therefore assigned
`Response=1`, while PR/remission records are assigned `Response=0`. This
coding is mandatory even when a downstream report describes remission odds.

Under this convention, a positive coefficient refers to increasing log-odds
of non-remission/disease progression; its sign must be reversed before it is
reported as an effect on remission.
