#!/usr/bin/env python3
"""Worst Superpower — make.fun program/v1 entry.

Writes the winning one-line entry to <output dir>/entry.txt, where the
output directory comes from MAKEFUN_OUTPUT_DIR when set, falling back to
/output when it is not. The output is byte-identical to entry.txt.
"""

import os

ENTRY = (
    "I can read the minds of goldfish, but they are all thinking about "
    "the same pebble, and it is not even a nice pebble."
)


def validate_entry(text: str) -> str:
    """Guarantee the entry is exactly one line of plain text.

    Strips any trailing newline characters, rejects control characters
    (other than none allowed here), and enforces the competition gate:
    1 to 140 characters, not only whitespace.
    """
    text = text.rstrip("\r\n")
    if any(ord(ch) < 0x20 or ord(ch) == 0x7F for ch in text):
        raise ValueError("entry contains a control character")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if not (1 <= len(text) <= 140):
        raise ValueError("entry must be 1 to 140 characters")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    return text


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(validate_entry(ENTRY))


if __name__ == "__main__":
    main()
