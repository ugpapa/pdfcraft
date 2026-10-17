"""Resolve an ATTRIBUTION.toml merge conflict between upstream and the fork, one [[asset]] at a time.

Usage: merge-attribution.py BASE OURS THEIRS OUT

Upstream's file wins, then the fork's own changes are replayed onto it: assets the fork removed
(present in BASE, gone from OURS, e.g. docs/brand/*) are dropped again, and assets the fork added
(in OURS, not in BASE, e.g. the Korean catalog) are re-inserted after the asset they followed in
OURS, or at the end when that one is gone.
"""

import re
import sys

HEADER = "[[asset]]\n"


def split(text):
    """The text before the first [[asset]], then each [[asset]] block keyed by its path."""
    parts = re.split(r"(?m)^(?=\[\[asset\]\]\n)", text)
    head, blocks = parts[0], []
    for block in parts[1:]:
        m = re.search(r'(?m)^path = "([^"]*)"', block)
        blocks.append((m.group(1) if m else None, block))
    return head, blocks


def paths(blocks):
    return {p for p, _ in blocks if p is not None}


def main():
    base, ours, theirs = (open(p, encoding="utf-8").read() for p in sys.argv[1:4])
    out = sys.argv[4]
    _, base_blocks = split(base)
    _, our_blocks = split(ours)
    head, result = split(theirs)

    removed = paths(base_blocks) - paths(our_blocks)
    result = [(p, b) for p, b in result if p not in removed]

    base_paths = paths(base_blocks)
    for i, (path, block) in enumerate(our_blocks):
        if path is None or path in base_paths or path in paths(result):
            continue
        if not block.endswith("\n\n"):
            block = block.rstrip("\n") + "\n\n"
        prev = next((our_blocks[j][0] for j in range(i - 1, -1, -1) if our_blocks[j][0] in paths(result)), None)
        at = next((k + 1 for k, (p, _) in enumerate(result) if p == prev), len(result))
        result.insert(at, (path, block))

    text = head + "".join(b for _, b in result)
    text = text.rstrip("\n") + "\n"
    with open(out, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)


if __name__ == "__main__":
    main()
