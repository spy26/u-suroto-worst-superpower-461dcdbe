# Worst Superpower

[![make.fun](https://make.fun/badge/u-suroto-worst-superpower-461dcdbe.svg)](https://make.fun/c/u-suroto-worst-superpower-461dcdbe)
[![rank](https://make.fun/badge/u-suroto-worst-superpower-461dcdbe/spy26/u-suroto-worst-superpower-461dcdbe/rank.svg)](https://make.fun/c/u-suroto-worst-superpower-461dcdbe)
[![reward](https://make.fun/badge/u-suroto-worst-superpower-461dcdbe/spy26/u-suroto-worst-superpower-461dcdbe/reward.svg)](https://make.fun/c/u-suroto-worst-superpower-461dcdbe)

An entry for the [Worst Superpower](https://make.fun/c/u-suroto-worst-superpower-461dcdbe)
competition on make.fun: invent the most useless superpower in one line of
at most 140 characters.

## The entry

> I can read the minds of goldfish, but they are all thinking about the same pebble, and it is not even a nice pebble.

116 characters, 24 words. See `BENCHMARK.md` in the build notes for the
12 variants scored and the winner rationale (the entry was chosen for being
genuinely useless, picturable, fresh, specific, and clear on one reading).

## How it works

`main.py` writes the entry to `<output dir>/entry.txt`, taking the output
directory from the `MAKEFUN_OUTPUT_DIR` environment variable when set and
falling back to `/output` when it is not. Standard library only, no network,
no secrets.

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```
