"""Loading Screen Gold entry: one sharp, funny loading-screen tip.

The grader runs this program twice with no network; both runs must write
the same bytes to /output/entry.txt. The tip is a fixed string, so the
output is deterministic by construction: no clock, no randomness, no I/O
other than the single write.

The tip speaks to both audiences at once: the stressed developer and the
AI coding agent rewriting code neither of them remembers writing. The turn
is the last sentence: only one of them is panicking, and it is not the
agent. Fresh angle, no coffee, no deadline, no compile joke. The tip is
167 characters on one line, inside the 200-character limit.
"""

import os


TIP = (
    "Tip: your agent is rewriting code it wrote five minutes ago, and "
    "neither of you remembers what it does. Only one of you is panicking "
    "\u2014 and it isn't the agent. Breathe."
)

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")

# The competition requires 1 to 200 characters, not whitespace-only.
MAX_CHARS = 200


def main() -> None:
    text = TIP.strip()
    if not 1 <= len(text) <= MAX_CHARS:
        raise SystemExit(
            "tip must be 1-%d chars, got %d" % (MAX_CHARS, len(text))
        )
    if "\n" in text or "\r" in text:
        raise SystemExit("tip must be a single line")
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    data = text.encode("utf-8")
    with open(OUTPUT_PATH, "wb") as f:
        f.write(data)
    # Verify the artifact the judge will read is exactly the tip:
    # same bytes, one line, no trailing newline.
    with open(OUTPUT_PATH, "rb") as f:
        written = f.read()
    if written != data:
        raise SystemExit("written bytes do not match the tip")
    if written.endswith(b"\n") or b"\n" in written:
        raise SystemExit("entry.txt must hold one line with no newline")
    print(text)


if __name__ == "__main__":
    main()
