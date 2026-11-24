#!/usr/bin/env python3
"""Weirdest Job Title: Blind Judge Showdown.

Writes a single original job title, 60 characters at most and
nothing else, to $MAKEFUN_OUTPUT_DIR/entry.txt (fallback /output/entry.txt).
Python 3 stdlib only, fully deterministic.
"""

import os

TITLE = "Senior Vice President of Apologizing to the Office Printer"


def main():
    line = TITLE.strip()
    assert "\n" not in line, "entry must be a single line"
    assert 1 <= len(line) <= 60, "entry must be 1-60 characters"
    assert line == line.strip() and line, "entry must not be only whitespace"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(line + "\n")
    # Read-back verification: what we wrote is exactly the title, one line.
    with open(path, encoding="utf-8") as f:
        written = f.read()
    assert written == line + "\n", "read-back mismatch"
    assert len(written.strip()) <= 60, "read-back over 60 chars"
    print(f"entry ({len(line)} chars): {line}")


if __name__ == "__main__":
    main()
