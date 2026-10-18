# Support judge experiment

Compares two LLM judges, **Jev** (TypeSafe `system_one`) and **Claude**,
on one task: does a proposed customer-support reply follow the refund
policy, given the customer's message?

Each judge receives the same rubric, policy, customer message and
candidate reply, and returns `pass` or `fail`. Predictions are scored
against human reference labels.

## Setup

Requires Python 3.10+.

```bash
uv venv --python 3.11 .venv
source .venv/bin/activate
uv pip install -r requirements.txt

cp .env.example .env   # then fill in the API keys
```

## Usage

Run everything from the project root:

```bash
python -m support_judge.run_baselines           # always-pass / always-fail baselines (no API calls)
python -m support_judge.run_jev                 # Jev on the full dataset
python -m support_judge.run_claude              # Claude on the full dataset
python -m support_judge.compare_one support-004 # both judges on one example
pytest                                          # scoring checks
```

Each Jev call is appended to `results/jev_calls.jsonl`.

## Metrics

- **Accuracy**: share of predictions that match the reference.
- **Fail recall**: share of reference `fail` cases the judge caught.
- **Fail precision**: share of the judge's `fail` predictions that were correct.

## Layout

```
support_judge/
  data.py          rubric, policy, dataset, reference labels
  prompt.py        shared judge instructions and input payload
  evaluation.py    evaluate() and summarize()
  judges/          baselines.py, jev.py, claude.py
  utils/           env, paths, formatting, JSONL records
  run_*.py         entry points
  compare_one.py
tests/             pytest checks
docs/              DATASET_PLAN.md, LEARNINGS.md
results/           call logs and observations
```

To add a judge, write a function `judge(example) -> "pass" | "fail"` in
`support_judge/judges/` and pass it to `evaluate()`.
