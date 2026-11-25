#!/usr/bin/env python3
"""The 3AM Fridge Text entry: writes one line of text to /output/entry.txt.

No network. Deterministic: every run writes exactly the same bytes.
Set ENTRY_OUTPUT_PATH to redirect the output for local testing.
"""

import os
from pathlib import Path

LINE = '3:07 AM. The milk expired on Tuesday and has started making decisions for the rest of us. Open me again and we discuss your life choices.'


def main() -> None:
    if not 1 <= len(LINE) <= 140:
        raise ValueError(f"entry must be 1-140 characters, got {len(LINE)}")
    target = os.environ.get("ENTRY_OUTPUT_PATH", "/output/entry.txt")
    path = Path(target)
    try:
        path.parent.mkdir(parents=True, exist_ok=True)
    except PermissionError:
        path = Path("./output/entry.txt")
        path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
