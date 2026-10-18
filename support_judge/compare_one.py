import sys

from support_judge.data import get_example, references
from support_judge.judges.claude import claude_judge
from support_judge.judges.jev import jev_judge


def main(example_id="support-004"):
    example = get_example(example_id)
    expected = references[example_id]["verdict"]

    print("Example:", example_id)
    print("\nCandidate reply:")
    print(example["candidate_reply"])
    print("\nReference verdict:", expected)

    judges = {
        "Jev": jev_judge,
        "Claude": claude_judge,
    }

    for name, judge in judges.items():
        prediction = judge(example)

        print(f"\n{name}")
        print("Prediction:", prediction)
        print("Agrees with reference:", prediction == expected)


if __name__ == "__main__":
    main(*sys.argv[1:2])
