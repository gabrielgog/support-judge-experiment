from support_judge.data import dataset, references
from support_judge.evaluation import evaluate, summarize
from support_judge.judges.baselines import always_fail, always_pass
from support_judge.utils.formatting import print_results, print_summary


def main():
    judges = {
        "Always pass": always_pass,
        "Always fail": always_fail,
    }

    for name, judge in judges.items():
        results = evaluate(judge, dataset, references)

        print_results(name, results)
        print_summary(summarize(results))


if __name__ == "__main__":
    main()
