"""One Word From Your Ex — make.fun entry.

The task asks for exactly one word an ex would use to describe the
entrant, nothing else. The word below is the whole entry: it is funny
because it is a complaint every ex has made at least once, and it
stings because the entrant knows it is true.

The program writes that single word to the output directory the
grader provides, and nowhere else.
"""

import os
import sys

WORD = "Exhausting"


def gate_report(text):
    """Return a one-line summary of how the word passes the gate."""
    checks = []
    checks.append("length {} in 1-24".format(len(text)))
    checks.append("single word" if not any(ch.isspace() for ch in text) else "has spaces")
    checks.append("non-blank" if text.strip() else "blank")
    return "; ".join(checks)


def output_dir():
    """Return the directory the grader wants the entry written to."""
    chosen = os.environ.get("MAKEFUN_OUTPUT_DIR") or os.environ.get("OUTPUT_DIR")
    if chosen:
        return chosen
    return os.path.join(os.getcwd(), "output")


def main():
    text = WORD.strip()
    if not text or len(text) > 24:
        raise SystemExit("entry word fails the 1-24 character gate")
    if any(ch.isspace() for ch in text):
        raise SystemExit("entry must be exactly one word")
    target = output_dir()
    os.makedirs(target, exist_ok=True)
    path = os.path.join(target, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(text)
    print("gate: {}".format(gate_report(text)))
    print("wrote {} ({} characters)".format(path, len(text)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
