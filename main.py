"""The Most Boring Object, Reviewed in One Line.

The rubber band is the dullest object in the drawer, and that is exactly
why it deserves five stars: it has done one unglamorous job, perfectly,
for years, without ever asking to be noticed. The review is funny because
every word of it is true.

Running this file writes the review to ``$MAKEFUN_OUTPUT_DIR/entry.txt``
(default ``/output``), with no trailing newline.
"""

import os

ENTRY = (
    "Five stars. This rubber band has held the same drawer shut since 2019, "
    "never asked for a raise, and will still be working long after we are all gone."
)


def get_entry() -> str:
    """Return the one-line review."""
    return ENTRY


def write_entry(output_dir: str | None = None) -> str:
    """Write the entry to entry.txt inside output_dir and return its path."""
    directory = output_dir or os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(directory, exist_ok=True)
    path = os.path.join(directory, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(get_entry())
    return path


def main() -> None:
    """Write the entry and print where it went."""
    print(write_entry())


if __name__ == "__main__":
    main()
