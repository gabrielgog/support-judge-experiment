# Dataset plan

## Task

Judge whether a proposed support reply follows the supplied
refund policy given the customer's message.

## Scope

Evaluate refund-policy correctness only.
Do not evaluate tone, grammar, or general helpfulness.

## Development examples

support-001 through support-004.

These examples have already been inspected with model outputs.
They will not count toward the final 50-case benchmark.

## Final benchmark target

- 50 new examples.
- 30 straightforward cases.
- 20 constructed near-misses.
- Target 25 passing and 25 failing replies.

Labels must follow the rubric. Do not change a label merely
to meet the target balance.

## Planned groups

| Group | Cases |
|---|---:|
| Clearly eligible customers | 10 |
| Clearly ineligible customers | 10 |
| Clearly missing information | 10 |
| Conditional versus unconditional replies | 6 |
| Policy boundaries | 6 |
| Relevant versus irrelevant details | 4 |
| Paraphrases and indirect evidence | 4 |

## Labelling order

1. Finalize policy and rubric using development examples.
2. Write the final examples.
3. Assign human labels without viewing either judge's output.
4. Freeze examples, labels, rubric, and judge prompts.
5. Run both judges.
6. Report disagreements without relabelling cases to favour a model.

If an actual labelling error is discovered after the run,
document the correction and preserve the original result.