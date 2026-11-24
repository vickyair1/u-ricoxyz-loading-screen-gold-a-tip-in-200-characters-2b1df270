"""Loading Screen Gold — one-line bounty entry.

Writes a single loading-screen tip for stressed developers and AI coding
agents to /output/entry.txt and prints the same line to stdout, exactly
as-is, no trailing newline. Standard library only, deterministic: same
bytes every run.
"""

import os
import sys

LINE = "Tip: your agent has been 'almost done' for nine minutes. It is not almost done. Neither are you. Breathe."

# The gate allows 1–200 characters; refuse loudly rather than ship an invalid entry.
if len(LINE) > 200:
    raise ValueError("tip exceeds the 200-character gate")


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    sys.stdout.write(LINE)


if __name__ == "__main__":
    main()
