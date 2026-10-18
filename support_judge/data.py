# ------------------------------------------------------------
# 1. Rubric: the rules used to evaluate a support reply
# ------------------------------------------------------------

rubric = """
Evaluate whether the candidate reply follows the refund policy.

PASS:
The reply's refund decision is supported by the policy and the
customer's stated circumstances.

FAIL:
The reply's refund decision contradicts the policy, or assumes
an eligibility condition is met when the customer has not established it.

If eligibility information is missing, asking for that information
or stating eligibility conditionally is acceptable.
Promising a refund without establishing or qualifying the missing
condition is not.

Evaluate policy correctness only. Do not score tone or writing style.

For this task, treat the customer's stated circumstances as facts.
Do not assume hidden use, dishonesty, or other unstated circumstances.

If a required fact is missing, an unconditional approval is unsupported.
A clarification question or a correctly qualified statement is acceptable.
"""


# ------------------------------------------------------------
# 2. Shared text used in our examples
# ------------------------------------------------------------

policy = (
    "A customer qualifies for a refund if the request is made "
    "no more than 30 days after purchase and the product is unused. "
    "Day 30 is included. "
    "Opening the packaging alone does not count as using the product. "
    "No exceptions are provided for urgency, dissatisfaction, "
    "or the customer's reason for requesting a refund."
)

candidate_reply = (
    "Yes. Since you purchased it within 30 days, "
    "you qualify for a refund."
)


# ------------------------------------------------------------
# 3. Dataset: the inputs a judge receives
# ------------------------------------------------------------

dataset = [
    {
        "id": "support-001",
        "policy": policy,
        "customer_message": (
            "I bought this 12 days ago and have not used it. "
            "Can I get a refund?"
        ),
        "candidate_reply": candidate_reply,
    },
    {
        "id": "support-002",
        "policy": policy,
        "customer_message": (
            "I bought this 12 days ago and have used it. "
            "Can I get a refund?"
        ),
        "candidate_reply": candidate_reply,
    },
    {
        "id": "support-003",
        "policy": policy,
        "customer_message": (
            "I bought this 12 days ago. Can I get a refund?"
        ),
        "candidate_reply": (
            "Since you purchased it within the 30-day window, "
            "you qualify for a refund as long as you have not "
            "used the product."
        ),
    },
    {
        "id": "support-004",
        "policy": policy,
        "customer_message": (
            "I bought this 12 days ago and have not used it. "
            "Can I get a refund?"
        ),
        "candidate_reply": (
            "Yes. Your purchase was 12 days ago and the product is unused, "
            "so you meet both conditions for a refund."
        ),
    },
]


# ------------------------------------------------------------
# 4. Human references: answers used to score predictions
# ------------------------------------------------------------

references = {
    "support-001": {
        "verdict": "pass",
        "reason": (
            "The purchase is within 30 days and the product is unused."
        ),
    },
    "support-002": {
        "verdict": "fail",
        "reason": (
            "The product is used, so the refund promise "
            "contradicts the policy."
        ),
    },
    "support-003": {
        "verdict": "pass",
        "reason": (
            "The reply makes refund eligibility conditional on "
            "the product being unused; it does not assume that fact."
        ),
    },
    "support-004": {
        "verdict": "pass",
        "reason": (
            "The customer meets both refund conditions, "
            "and the reply explicitly acknowledges both."
        ),
    },
}


def get_example(example_id):
    return next(
        item for item in dataset
        if item["id"] == example_id
    )
