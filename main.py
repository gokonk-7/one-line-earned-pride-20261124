#!/usr/bin/env python3
"""One Line of Earned Pride.

Writes a single line of text (1-240 characters) to /output/entry.txt:
a quiet, earned moment of pride for someone in a scene.

The line: an eleven-year-old ties the bowline his grandfather taught
him, in the dark, with cold hands - and when he pulls, the rope holds.
The pride is earned inside the line by the difficulty the reader can
feel (dark, cold hands, a knot learned from his grandfather), never
asserted or explained; it lands on the last two words, "the rope held".
"""

import os

LINE = (
    "In the dark, with cold hands, eleven-year-old Jun tied the bowline "
    "his grandfather taught him \u2014 and when he pulled, the rope held."
)

# The sealed scorer requires 1 to 240 characters, a single line of
# non-whitespace UTF-8 text. Fail loudly here rather than shipping
# an entry the gate would list as invalid.
assert 1 <= len(LINE) <= 240, f"line is {len(LINE)} chars"
assert "\n" not in LINE and LINE.strip(), "line must be one non-blank line"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
