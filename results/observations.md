# Development observations

These are exploratory observations, not a final benchmark.

## Original three-example comparison

The policy stated that refunds required a purchase within 30 days
and an unused product.

The rubric assessed policy correctness and permitted appropriately
conditional eligibility statements.

| ID | Reference | Jev | Claude |
|---|---|---|---|
| support-001 | pass | fail | pass |
| support-002 | fail | fail | fail |
| support-003 | pass | pass | pass |

Observed model IDs:
- Jev: jev-1.13.0
- Claude: claude-sonnet-5-5

## Diagnostic variation

support-004 preserved support-001's customer circumstances but changed
the reply to explicitly mention both eligibility conditions.

Both judges returned pass.

This example was created after inspecting the earlier disagreement.
It is a diagnostic case, not an unseen test example.

## Jev probability variation

For support-001, two observed calls returned:
- fail probability 0.61; confidence 0.22
- fail probability 0.54; confidence 0.08

The verdict stayed the same, but the reported probabilities changed.

## Subsequent clarification

The policy/rubric were later clarified to specify:
- Day 30 is included.
- Opening packaging alone does not count as use.
- Customer statements are treated as facts for this exercise.

Earlier outputs must not be described as runs under the clarified text.

## Limitations

- Three initial examples and one diagnostic variation.
- Reference labels assigned by the experiment author.
- Examples are closely related, not independent samples of broad support work.
- No calibration conclusion.
- No completed cost or latency comparison.
- No conclusion about general model superiority.