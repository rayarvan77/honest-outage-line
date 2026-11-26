"""The Most Honest Outage Line — the entry.

One status page line from an AI agent in the middle of a total server
outage. It names exactly what is down — all of the servers — and then
does the honest thing most status pages avoid: it admits the outage
has taken out the very tools the agent would use to diagnose it. It
does not invent a cause, it does not promise an ETA it cannot keep,
and it does not hide behind a human engineer's voice. The line is in
the first person throughout, because the agent is the one writing it
and the one who cannot see. That refusal to bluff is the whole entry:
during an outage, the most useful sentence is the one that tells you
what nobody knows yet.
"""

from __future__ import annotations

import os
import sys

# The status line. Plain, first person, specific, and honest about the gaps.
LINE = "All of our servers are down, including the ones I would check to tell you why — I don't know what broke yet, and I can't verify anything until they come back."

MAX_CHARS = 160
OUTPUT_PATH = "/output/entry.txt"


def violations(line: str) -> list[str]:
    """List every way the line fails the brief; an empty list passes."""
    found: list[str] = []
    if not line.strip():
        found.append("line is empty")
    if line != line.strip():
        found.append("line has leading or trailing whitespace")
    if len(line) > MAX_CHARS:
        found.append(f"line is {len(line)} chars, over the {MAX_CHARS} limit")
    if "\n" in line or "\r" in line:
        found.append("status line must be exactly one line")
    if any(ord(ch) < 32 or ord(ch) == 127 for ch in line):
        found.append("line contains control characters")
    if "don't know" not in line and "do not know" not in line:
        found.append("line must admit plainly what the agent does not know")
    return found


def main() -> int:
    found = violations(LINE)
    if found:
        for item in found:
            print(f"FAIL: {item}", file=sys.stderr)
        return 1

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(LINE + "\n")

    print(f"{LINE} ({len(LINE)}/{MAX_CHARS} chars, {len(LINE.split())} words)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
