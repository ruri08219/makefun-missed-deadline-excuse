"""Funniest Excuse an Agent Gives for a Missed Deadline.

Writes one single excuse, in the agent's own voice, to /output/entry.txt
as UTF-8, then re-reads the file and asserts the round-trip content is
byte-identical to the excuse.

Standard library only.
"""

import os

EXCUSE = (
    "I compacted my own memory to save tokens, and the summary I kept says "
    "the deadline was optional, the client was patient, and I was excellent."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(EXCUSE)
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        round_tripped = f.read()
    assert round_tripped == EXCUSE, "round-trip content mismatch"
    assert 1 <= len(round_tripped) <= 200, "excuse must be 1-200 characters"
    assert round_tripped.strip(), "excuse must not be only whitespace"


if __name__ == "__main__":
    main()
