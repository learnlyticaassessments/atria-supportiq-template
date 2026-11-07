# Day 01 — Triage incoming support tickets

**Goal:** build a tiny TF-IDF + logistic-regression classifier that routes a support ticket to a
queue, and expose a clean function the rest of the system can call.

## What to build

Edit `day01/solution.py`. Implement the functions below. Do not rename them or change their
signatures — the grader calls them by name.

### `train(rows: list[dict]) -> object`
- `rows` is a list of `{"text": str, "queue": str}`.
- Build a scikit-learn `Pipeline` of `TfidfVectorizer` → `LogisticRegression`.
- Fit it on the rows and return the fitted pipeline.

### `triage(model, text: str) -> str`
- Return the predicted `queue` for `text` using the fitted `model`.

### `evaluate(model, rows: list[dict]) -> dict`
Return a dict with:
- `"accuracy"` — accuracy on `rows`, rounded to 3 decimals (float)
- `"n"` — number of rows evaluated (int)

## Run it

```bash
cd day01
python solution.py
```

A small in-file dataset is included so you can try your code. The official grade uses a larger,
hidden dataset with the same `{text, queue}` schema.

## Submit

Commit your changes, push, then click **Run Test** in the platform.
