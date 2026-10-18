# Experiment learning log

## Milestone 1 — A working comparison

I built three support-reply examples and labelled them using a written
rubric before viewing the model judgements.

Both models received the same policy, customer message, candidate reply,
and rubric. Neither received my reference label.

Observed decisions:

| Example | Reference | Jev | Claude |
|---|---|---|---|
| support-001 | pass | fail | pass |
| support-002 | fail | fail | fail |
| support-003 | pass | pass | pass |

Claude agreed with all three references. Jev agreed with two.

Jev's incorrect verdict had lower reported confidence than its correct
verdicts in this run. This is an observation to test on more examples,
not evidence that its confidence is calibrated.

These three examples demonstrate the pipeline, not general model quality.

Next question:
Does the disagreement persist across controlled variations of the example?


## Milestone 2 — A controlled wording variation

I added support-004 without replacing support-001.

Both examples use the same policy and customer message.
The new reply explicitly mentions both refund conditions.

Observed results:
- support-001: Jev failed it; Claude passed it.
- support-004: both judges passed it.
- Both reference labels are pass under the current rubric.

This suggests a wording-sensitivity question worth investigating.
It does not establish the cause or repeatability of the difference.

The new example was designed after inspecting a model error, so it is
a diagnostic example, not an unseen test case.

## Policy clarification

Before constructing the final benchmark, I clarified that:
- Day 30 is included.
- Opening packaging alone does not count as use.
- Customer statements are treated as facts for this task.

Earlier model outputs used the previous policy/rubric wording.
They remain development observations, not results under the updated version.