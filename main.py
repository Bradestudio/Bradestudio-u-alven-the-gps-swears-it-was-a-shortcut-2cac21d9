"""make.fun entry: The GPS Swears It Was a Shortcut.

Writes the single-line GPS excuse to entry.txt in MAKEFUN_OUTPUT_DIR
(fallback /output). Python stdlib only, no network, no clock, no local
imports, no hardcoded paths. Deterministic and byte-identical across runs,
with no trailing newline.
"""

import os

ENTRY = (
    "The map swore that lake had a bridge, so I sent you straight "
    "across it \u2014 I read the lines, I don't check if they're wet."
)


def main():
    line = ENTRY
    if not line or not line.strip():
        raise SystemExit("entry line is blank")
    if line != line.strip():
        raise SystemExit("entry line has leading/trailing whitespace")
    if "\n" in line or "\r" in line:
        raise SystemExit("entry line must be a single line")
    if not 1 <= len(line) <= 200:
        raise SystemExit("entry line must be 1-200 characters")

    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(line)
    # Verify the file on disk is byte-for-byte the gated line, so a
    # partial or altered write can never pass silently.
    with open(path, "r", encoding="utf-8", newline="") as handle:
        written = handle.read()
    if written != line:
        raise SystemExit("entry.txt does not match the gated line")


if __name__ == "__main__":
    main()
