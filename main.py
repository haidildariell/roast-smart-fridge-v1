"""Roast the Smart Fridge: one-line entry.

Writes a single roast line about a smart fridge that snitches on
midnight snacking to /output/entry.txt, with no trailing newline.
"""

import os

OUTPUT_PATH = "/output/entry.txt"

LINE = (
    "My smart fridge caught me raiding it at 2 a.m., so now it locks "
    "the cheese drawer and rats me out to my trainer before I even chew."
)


def roast_line_bytes() -> bytes:
    """Return the roast line encoded as UTF-8 bytes, no trailing newline."""
    return LINE.encode("utf-8")


def write_entry(path: str = OUTPUT_PATH) -> int:
    """Write the roast line to path, creating its directory if needed.

    Reads the file back after writing and raises if the bytes on disk
    differ from the roast line, so a bad write never passes silently.
    Returns the number of bytes written.
    """
    data = roast_line_bytes()
    directory = os.path.dirname(path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(path, "wb") as handle:
        handle.write(data)
    with open(path, "rb") as handle:
        written_back = handle.read()
    if written_back != data:
        raise ValueError(
            f"read-back mismatch: wrote {len(data)} bytes, "
            f"read {len(written_back)} bytes"
        )
    return len(data)


def main() -> int:
    written = write_entry()
    print(f"Wrote {written} bytes to {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
