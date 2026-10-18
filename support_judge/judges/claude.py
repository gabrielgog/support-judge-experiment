import json

from anthropic import Anthropic

from support_judge.prompt import JUDGE_INSTRUCTIONS, judge_input
from support_judge.utils.env import load_env

load_env()

MODEL = "claude-sonnet-5-5"


def claude_judge(example):
    with Anthropic() as client:
        response = client.messages.create(
            model=MODEL,
            max_tokens=256,
            system=JUDGE_INSTRUCTIONS,
            messages=[
                {
                    "role": "user",
                    "content": json.dumps(judge_input(example)),
                },
            ],
            output_config={
                "format": {
                    "type": "json_schema",
                    "schema": {
                        "type": "object",
                        "properties": {
                            "verdict": {
                                "type": "string",
                                "enum": ["pass", "fail"],
                            },
                        },
                        "required": ["verdict"],
                        "additionalProperties": False,
                    },
                },
            },
        )

    if response.stop_reason != "end_turn":
        raise RuntimeError(
            f"Claude did not finish normally: {response.stop_reason}"
        )

    response_text = "".join(
        block.text
        for block in response.content
        if block.type == "text"
    )

    answer = json.loads(response_text)

    print(f"\nClaude details for {example['id']}")
    print("Verdict:", answer["verdict"])
    print("Model:", response.model)
    print("Input tokens:", response.usage.input_tokens)
    print("Output tokens:", response.usage.output_tokens)

    return answer["verdict"]
