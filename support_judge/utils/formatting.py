# Display helpers: format numbers without changing calculations.

def format_percentage(value):
    if value is None:
        return "N/A"

    return f"{value:.1%}"


def print_results(title, results):
    print(f"\n{title}")

    for result in results:
        print(
            f"{result['example_id']} | "
            f"prediction={result['prediction']} | "
            f"reference={result['reference']} | "
            f"correct={result['correct']}"
        )


def print_summary(summary):
    print("\nSummary")
    print("Accuracy:      ", format_percentage(summary["accuracy"]))
    print("Fail recall:   ", format_percentage(summary["fail_recall"]))
    print("Fail precision:", format_percentage(summary["fail_precision"]))
