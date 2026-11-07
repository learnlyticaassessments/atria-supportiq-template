"""Day 01 — Support ticket triage. Implement train(), triage(), evaluate().

See TASK.md for the spec. The grader imports this module and calls these functions by name —
keep the signatures.
"""

SAMPLE = [
    {"text": "card declined at checkout", "queue": "billing"},
    {"text": "refund not received", "queue": "billing"},
    {"text": "app crashes on login", "queue": "tech"},
    {"text": "page keeps loading forever", "queue": "tech"},
    {"text": "how do I change my plan", "queue": "account"},
    {"text": "update my email address", "queue": "account"},
]


def train(rows):
    # TODO: build a TfidfVectorizer -> LogisticRegression Pipeline, fit on rows, return it.
    raise NotImplementedError


def triage(model, text):
    # TODO: return the predicted queue for `text`.
    raise NotImplementedError


def evaluate(model, rows):
    # TODO: return {"accuracy": round(acc, 3), "n": len(rows)}.
    raise NotImplementedError


if __name__ == "__main__":
    m = train(SAMPLE)
    print(triage(m, "my payment failed"))
    print(evaluate(m, SAMPLE))
