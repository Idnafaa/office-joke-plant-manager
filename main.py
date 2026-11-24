# SPDX-License-Identifier: MIT
"""Office joke entry for the make.fun 'Make the AI Judge Laugh' bounty.

Writes a single original one-line office joke to /output/entry.txt.
The joke must be 1-199 characters of UTF-8 text, and nothing else.
"""

import os

# One original office joke: the office plant gets promoted because
# doing nothing loudly is, apparently, a management skill.
JOKES = [
    "Our office plant died, so we promoted it to middle management - "
    "it still just sits there, but now nobody dares question it.",
]


def pick_joke() -> str:
    """Return the entry's joke, stripped of surrounding whitespace."""
    return JOKES[0].strip()


def validate(text: str) -> str:
    """Keep only a single-line joke of 1-199 characters."""
    if not text or text != text.strip() or "\n" in text:
        raise SystemExit("joke must be one non-blank line")
    if not 1 <= len(text) <= 199:
        raise SystemExit(f"joke is {len(text)} chars, must be 1-199")
    return text


def main() -> None:
    text = validate(pick_joke())
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as fh:
        fh.write(text)


if __name__ == "__main__":
    main()
