from support_judge.data import dataset, references
from support_judge.evaluation import summarize
from support_judge.utils.formatting import format_percentage


# Scoring checks using results we already understand.
def test_summarize():
    known_results = [
        {
            "prediction": "pass",
            "reference": "pass",
            "correct": True,
        },
        {
            "prediction": "pass",
            "reference": "fail",
            "correct": False,
        },
        {
            "prediction": "pass",
            "reference": "pass",
            "correct": True,
        },
    ]

    summary = summarize(known_results)

    assert summary["accuracy"] == 2 / 3
    assert summary["fail_recall"] == 0.0
    assert summary["fail_precision"] is None


def test_format_percentage():
    assert format_percentage(2 / 3) == "66.7%"
    assert format_percentage(None) == "N/A"


def test_every_example_has_a_reference():
    assert {example["id"] for example in dataset} == set(references)
