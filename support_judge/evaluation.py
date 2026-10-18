# ------------------------------------------------------------
# Evaluation: compare each prediction with its reference
# ------------------------------------------------------------

def evaluate(judge, dataset, references):
    results = []

    for example in dataset:
        prediction = judge(example)
        expected = references[example["id"]]["verdict"]

        results.append({
            "example_id": example["id"],
            "prediction": prediction,
            "reference": expected,
            "correct": prediction == expected,
        })

    return results


# ------------------------------------------------------------
# Scoring: calculate metrics from evaluation results
# ------------------------------------------------------------

def summarize(results):
    if not results:
        raise ValueError("Cannot summarize an empty results list.")

    correct_count = sum(
        result["correct"]
        for result in results
    )

    actual_failures = sum(
        result["reference"] == "fail"
        for result in results
    )

    flagged_failures = sum(
        result["prediction"] == "fail"
        for result in results
    )

    caught_failures = sum(
        result["reference"] == "fail"
        and result["prediction"] == "fail"
        for result in results
    )

    return {
        "accuracy": correct_count / len(results),
        "fail_recall": (
            caught_failures / actual_failures
            if actual_failures > 0
            else None
        ),
        "fail_precision": (
            caught_failures / flagged_failures
            if flagged_failures > 0
            else None
        ),
    }
