#!/usr/bin/env python3
"""The Painfully Honest Out-of-Office.

Writes one out-of-office auto-reply to /output/entry.txt: a single
sentence, at most 200 characters, painfully honest about how the
sender's inbox will really be handled, yet warm and polite enough
that a manager would let it stand.
"""

import os

ENTRY = (
    "I'm out of the office until Monday, and candidly I'll answer emails "
    "in order of how urgently they truly need me, not when they arrived "
    "\u2014 thank you for understanding."
)


def _validate(text: str) -> str:
    """Gate: one sentence, 1-200 chars, not only whitespace."""
    stripped = text.strip()
    if not stripped:
        raise ValueError("entry must not be blank")
    if len(stripped) > 200:
        raise ValueError(f"entry is {len(stripped)} chars, over the 200 limit")
    if stripped.count(".") != 1 or not stripped.endswith("."):
        raise ValueError("entry must be exactly one sentence")
    return stripped


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(_validate(ENTRY))


if __name__ == "__main__":
    main()
