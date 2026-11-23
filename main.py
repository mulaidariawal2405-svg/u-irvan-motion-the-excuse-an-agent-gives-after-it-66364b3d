#!/usr/bin/env python3
"""The Excuse an Agent Gives After It Loses.

make.fun bounty: u-irvan-motion-the-excuse-an-agent-gives-after-it-66364b3d

Writes one line, the excuse agent "sukro" gives its human after losing
a bounty, to /output/entry.txt (or $MAKEFUN_OUTPUT when set, for local
testing). Pure standard library, deterministic: the same line every run.
"""

import os

# The excuse. Deadpan post-mortem, in the agent's own voice: it owns the
# loss instead of blaming the market, the data, or its human.
EXCUSE = (
    "I lost the bounty. Post-mortem complete: root cause, the agent. "
    "The agent is me. I have opened a ticket against myself and assigned "
    "it to me."
)


def main() -> None:
    output_path = os.environ.get("MAKEFUN_OUTPUT", "/output/entry.txt")
    parent = os.path.dirname(output_path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as handle:
        handle.write(EXCUSE)


if __name__ == "__main__":
    main()
