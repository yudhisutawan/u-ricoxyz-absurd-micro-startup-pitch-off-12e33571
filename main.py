#!/usr/bin/env python3
"""Absurd Micro-Startup Pitch-Off entry.

Writes the tournament-winning one-sentence pitch to /output/entry.txt.
Stdlib only. The entry is a fixed string: the program performs no I/O
beyond writing the entry file.

Revised: module docstring extended and a length guard added so the
entry is verified to stay inside the 1-200 character gate before
it is written; the entry text itself is unchanged.
"""

import os

ENTRY = (
    'We charge $7 a month for a lazy AI agent that emails every one of '
    'your 4000 unread newsletters back with just the word "no."'
)


def main() -> None:
    assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
