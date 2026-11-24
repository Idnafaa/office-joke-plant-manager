# SPDX-License-Identifier: MIT
"""Office joke entry for the make.fun 'Make the AI Judge Laugh' bounty.

Writes a single original one-line office joke to /output/entry.txt.
The joke must be 1-199 characters, UTF-8, and nothing else.
"""

import os

JOKE = (
    "Our office plant died, so we promoted it to middle management - "
    "it still just sits there, but now nobody dares question it."
)


def main() -> None:
    text = JOKE.strip()
    if not (1 <= len(text) <= 199):
        raise SystemExit(f"joke is {len(text)} chars, must be 1-199")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as fh:
        fh.write(text)


if __name__ == "__main__":
    main()
