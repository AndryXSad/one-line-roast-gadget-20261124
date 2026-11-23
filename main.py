"""One-line roast of the gadget used every day: the phone's face unlock.

The entry program writes a single roast line to entry.txt in the output
directory the grader provides ($MAKEFUN_OUTPUT_DIR, default /output).
The sealed scorer then checks the file is 1-200 characters of UTF-8 text
and the house judge compares it pairwise against the other entries.

The roast: face unlock recognises its owner everywhere except first thing
in the morning — the one tool whose whole job is recognising its owner
fails at exactly that job, right when the owner needs it most. The sting
is the twist in the tail: "even it doesn't recognise me."
"""

import os
import sys

LINE = (
    "My phone's face unlock works everywhere except first thing in the "
    "morning, when apparently even it doesn't recognise me."
)

MAX_CHARS = 200


def check_line(text):
    """Refuse to write anything the gate would reject."""
    problems = []
    if not text.strip():
        problems.append("line is empty")
    if len(text) > MAX_CHARS:
        problems.append("line is %d characters, over the 200 limit" % len(text))
    if "\n" in text.strip():
        problems.append("line must be a single line")
    return problems


def main():
    problems = check_line(LINE)
    if problems:
        sys.exit("roast fails the gate: " + "; ".join(problems))
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as handle:
        handle.write(LINE)


if __name__ == "__main__":
    main()
