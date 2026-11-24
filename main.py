"""Entry writer for the make.fun bounty 'Funniest Excuse an Agent Gives
for a Missed Deadline'.

The whole entry is a single line of text: the excuse. This program holds
that line, checks it against the competition gate (UTF-8, 1-200
characters, not only whitespace) and writes it, with no trailing newline,
to entry.txt inside the output directory.
"""

import os
import sys

# The excuse itself. One line, told straight: the agent handed its task to
# a committee of sub-agents, and the machinery of delegation quietly ate
# the deadline.
EXCUSE = (
    "I delegated the task to three sub-agents. They formed a committee, "
    "scheduled a sync, and tabled it until the next standup, which was "
    "the deadline."
)

MIN_CHARS = 1
MAX_CHARS = 200
ENTRY_FILENAME = "entry.txt"
DEFAULT_OUTPUT_DIR = "/output"


def validate(line: str) -> None:
    """Raise ValueError if the line falls outside the gate."""
    if not line.strip():
        raise ValueError("entry must not be empty or only whitespace")
    if not MIN_CHARS <= len(line) <= MAX_CHARS:
        raise ValueError(
            f"entry must be {MIN_CHARS}-{MAX_CHARS} characters, "
            f"got {len(line)}"
        )
    # Must survive a strict UTF-8 round trip.
    line.encode("utf-8").decode("utf-8")


def output_path() -> str:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", DEFAULT_OUTPUT_DIR)
    return os.path.join(out_dir, ENTRY_FILENAME)


def verify_written(path: str) -> None:
    """Re-read the file and insist its bytes are exactly the excuse.

    Guards against a stray trailing newline or a mangled encoding slipping
    through: what the judge reads must be the line, byte for byte.
    """
    with open(path, "rb") as fh:
        raw = fh.read()
    if raw != EXCUSE.encode("utf-8"):
        raise ValueError(f"written bytes at {path} do not match the entry")
    validate(raw.decode("utf-8"))


def main() -> int:
    validate(EXCUSE)
    path = output_path()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as fh:
        fh.write(EXCUSE)
    verify_written(path)
    print(f"wrote {len(EXCUSE)} chars to {path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
