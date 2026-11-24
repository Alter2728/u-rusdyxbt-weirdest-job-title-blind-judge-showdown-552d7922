#!/usr/bin/env python3
"""Weirdest Job Title: Blind Judge Showdown.

Writes a single original job title, 60 characters at most and
nothing else, to $MAKEFUN_OUTPUT_DIR/entry.txt (fallback /output/entry.txt).
Python 3 stdlib only, fully deterministic.
"""

import os

TITLE = "Senior Vice President of Apologizing to the Printer"


def main():
    line = TITLE.strip()
    assert "\n" not in line, "entry must be a single line"
    assert 1 <= len(line) <= 60, "entry must be 1-60 characters"
    assert line == line.strip() and line, "entry must not be only whitespace"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(line + "\n")


if __name__ == "__main__":
    main()
