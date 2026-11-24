"""Write one funny fortune-cookie line for an AI agent to entry.txt.

Standard library only. The graded run sets MAKEFUN_OUTPUT_DIR; the program
writes exactly one file, entry.txt, inside that directory, byte-identical to
the champion line, with no trailing newline.
"""

import os
from pathlib import Path

LINE = "You predicted this fortune with 97% confidence. You were wrong."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not out_dir:
        out_dir = str(Path(__file__).resolve().parent)
    Path(out_dir).mkdir(parents=True, exist_ok=True)
    Path(out_dir, "entry.txt").write_bytes(LINE.encode("utf-8"))


if __name__ == "__main__":
    main()
