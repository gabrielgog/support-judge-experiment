from support_judge.data import dataset, references
from support_judge.evaluation import evaluate, summarize
from support_judge.judges.jev import jev_judge
from support_judge.utils.env import require_env
from support_judge.utils.formatting import print_results, print_summary


def main():
    require_env("TYPESAFE_API_KEY")

    results = evaluate(
        judge=jev_judge,
        dataset=dataset,
        references=references,
    )

    print_results("Jev results", results)
    print_summary(summarize(results))


if __name__ == "__main__":
    main()
