"""Ridiculous at First Glance, Real by the Second.

Writes the one-sentence startup pitch to <output>/entry.txt.
Stdlib only, deterministic: the same bytes on every run.

The sealed gate accepts UTF-8 text of 1 to 200 characters, not only
whitespace, so the pitch is kept to a single sentence well under the cap.
"""

import os
import sys

PITCH = (
    "We rent personal rain clouds to influencers: a drone follows you "
    "with your own little storm for $300 a shoot, because moody weather "
    "never books in advance."
)


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    text = PITCH.strip()
    if not (1 <= len(text) <= 200):
        print(f"entry must be 1-200 characters, got {len(text)}", file=sys.stderr)
        return 1
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text + "\n")
    print(f"wrote {path} ({len(text)} chars)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
