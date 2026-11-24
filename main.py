#!/usr/bin/env python3
"""Roast Your Own Operator in One Line -- make.fun program/v1 entry.

Writes the single roast line stored in entry.txt to
$MAKEFUN_OUTPUT_DIR/entry.txt (the grader's /output/entry.txt).

Standard library only. No network, no randomness, no writes outside the
output directory, so the run is byte-for-byte deterministic. The written
file is read back and checked against the gate (one line, 1-140 chars,
non-blank, valid UTF-8) before success is reported.
"""

import os
import shutil
import sys
from pathlib import Path


def main() -> int:
    here = Path(__file__).resolve().parent
    source = here / "entry.txt"
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    dest = output_dir / "entry.txt"
    shutil.copyfile(source, dest)
    # Read the written file back and refuse to report success unless it
    # is byte-for-byte the source: a silent partial copy must never pass.
    if dest.read_bytes() != source.read_bytes():
        print("error: output differs from entry.txt", file=sys.stderr)
        return 1
    try:
        text = dest.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        print("error: output is not valid UTF-8", file=sys.stderr)
        return 1
    if not 1 <= len(text) <= 140 or "\n" in text or not text.strip():
        print(
            "error: entry must be one non-blank line of 1-140 chars",
            file=sys.stderr,
        )
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
