#!/usr/bin/env python3
"""Write one autocorrect fail to entry.txt.

The line is a single sentence of 53 characters: a text home from
practice where one wrong word turns a pulled muscle into a small
pet. It reads as a real slip, which is what the brief asks for.
The line goes to ``entry.txt`` under OUTPUT_DIR (default
``/output``). Output is deterministic: two runs produce
byte-identical files.
"""

import os

LINE = "Can you pick me up from practice? I pulled a hamster."
LIMIT = 199


def _check(text):
    if "\n" in text or "\r" in text:
        raise ValueError("line must be a single line")
    if text != text.strip():
        raise ValueError("line must not have leading or trailing whitespace")
    if not text or len(text) > LIMIT:
        raise ValueError("line must be 1-199 characters")


def _write_line():
    _check(LINE)
    directory = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(directory, exist_ok=True)
    path = os.path.join(directory, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(LINE + "\n")
    os.chmod(path, 0o644)


if __name__ == "__main__":
    _write_line()
