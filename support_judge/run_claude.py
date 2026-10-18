from support_judge.data import dataset, references
from support_judge.evaluation import evaluate, summarize
from support_judge.judges.claude import claude_judge
from support_judge.utils.env import require_env
from support_judge.utils.formatting import print_results, print_summary


def main():
    require_env("ANTHROPIC_API_KEY")

    results = evaluate(
        judge=claude_judge,
        dataset=dataset,
        references=references,
    )

    print_results("Claude results", results)
    print_summary(summarize(results))


if __name__ == "__main__":
    main()
