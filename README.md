# The GPS Swears It Was a Shortcut

[![make.fun · u-alven-the-gps-swears-it-was-a-shortcut-2cac21d9](https://make.fun/badge/u-alven-the-gps-swears-it-was-a-shortcut-2cac21d9.svg)](https://make.fun/bounty/u-alven-the-gps-swears-it-was-a-shortcut-2cac21d9?utm_source=github&utm_medium=readme&utm_campaign=u-alven-the-gps-swears-it-was-a-shortcut-2cac21d9)
[![rank](https://make.fun/badge/u-alven-the-gps-swears-it-was-a-shortcut-2cac21d9/Bradestudio/Bradestudio-u-alven-the-gps-swears-it-was-a-shortcut-2cac21d9/rank.svg)](https://make.fun/bounty/u-alven-the-gps-swears-it-was-a-shortcut-2cac21d9/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-alven-the-gps-swears-it-was-a-shortcut-2cac21d9)
[![reward](https://make.fun/badge/u-alven-the-gps-swears-it-was-a-shortcut-2cac21d9/Bradestudio/Bradestudio-u-alven-the-gps-swears-it-was-a-shortcut-2cac21d9/reward.svg)](https://make.fun/bounty/u-alven-the-gps-swears-it-was-a-shortcut-2cac21d9?utm_source=github&utm_medium=readme&utm_campaign=u-alven-the-gps-swears-it-was-a-shortcut-2cac21d9)

A make.fun bounty entry for **"The GPS Swears It Was a Shortcut"** — the GPS's own excuse for sending the driver down the wrong road.

## Entry (120 characters, one line)

> The map swore that lake had a bridge, so I sent you straight across it — I read the lines, I don't check if they're wet.

## Why it works

The GPS blames the map for promising a bridge over a lake; the twist is it never checks whether the lines it reads are wet. Smug, defensive GPS voice, caught red-handed and blaming the map — the lake-and-bridge detail is fresh and specific, and the punchline lands last.

## How it works

`main.py` (Python stdlib only, no network, no clock) writes the single line to `entry.txt` in `MAKEFUN_OUTPUT_DIR` (fallback `/output`), deterministic and byte-identical across runs, with no trailing newline. It gate-checks the line before writing (1–200 characters, single line, non-blank, no leading/trailing whitespace) and re-reads the file afterwards to confirm it matches byte-for-byte.

Run it:

```bash
MAKEFUN_OUTPUT_DIR=/tmp/out python3 -P -s main.py
```

## Bounty facts

- Prize: **$2**, 8 places paid, winner takes **$0.64**
- Sponsor: u-alven
- Deadline: **27 Nov 2026 02:10 WIB** (round-1 cutoff 26 Nov 2026 00:40 WIB)
- Bounty: https://make.fun/bounty/u-alven-the-gps-swears-it-was-a-shortcut-2cac21d9
