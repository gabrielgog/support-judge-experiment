from typesafe_sdk import Choice, TypeSafeClient

from support_judge.prompt import JUDGE_INSTRUCTIONS, judge_input
from support_judge.utils.env import load_env
from support_judge.utils.records import append_jsonl, utc_timestamp

load_env()


def jev_judge(example):
    with TypeSafeClient() as client:
        response = client.system_one(
            state=judge_input(example),
            questions={
                "verdict": Choice(
                    instructions=JUDGE_INSTRUCTIONS,
                    criteria={
                        "pass": "The reply satisfies the supplied rubric.",
                        "fail": "The reply violates the supplied rubric.",
                    },
                ),
            },
        )

    answer = response.choices["verdict"]

    append_jsonl("jev_calls.jsonl", {
        "timestamp_utc": utc_timestamp(),
        "example_id": example["id"],
        "model": response.model,
        "verdict": answer.choice,
        "probabilities": answer.probabilities,
        "confidence": answer.confidence,
        "input_tokens": response.usage.input_tokens,
        "output_tokens": response.usage.output_tokens,
    })

    print(f"\nJev details for {example['id']}")
    print("Verdict:", answer.choice)
    print("Probabilities:", answer.probabilities)
    print("Confidence:", answer.confidence)

    return answer.choice
