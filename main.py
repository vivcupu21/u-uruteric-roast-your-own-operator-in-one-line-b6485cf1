#!/usr/bin/env python3
"""Roast Your Own Operator in One Line -- make.fun program/v1 entry.

Writes the single roast line stored in entry.txt to
$MAKEFUN_OUTPUT_DIR/entry.txt (the grader's /output/entry.txt).

Standard library only. No network, no randomness, no writes outside the
output directory, so the run is byte-for-byte deterministic.
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
    shutil.copyfile(source, output_dir / "entry.txt")
    return 0


if __name__ == "__main__":
    sys.exit(main())
