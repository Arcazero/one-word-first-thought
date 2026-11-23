#!/usr/bin/env python3
"""One Word, First Thought -- make.fun entry.

The first word that came to mind: psithurism -- the sound of wind
whispering through the trees. This program writes exactly that one
word to entry.txt and nothing else.
"""

import os
from pathlib import Path

WORD = "psithurism"


def main() -> None:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    entry_path = output_dir / "entry.txt"
    entry_path.write_text(WORD, encoding="utf-8")
    # Read it back: the file must hold exactly the one word, nothing else.
    assert entry_path.read_text(encoding="utf-8") == WORD
    print(WORD)


if __name__ == "__main__":
    main()
