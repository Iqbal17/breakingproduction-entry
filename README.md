# The One-Line AI Excuse for Breaking Production

Entry for the make.fun bounty
`u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66` ($2, 8 places).

## The line

> I rolled back the wrong thing — turns out 'undo' in production undoes the customers, not my mistakes.

101 characters, one line. An excuse an AI agent gives its human right
after breaking production: a rollback gone wrong, told with the machine's
own literal logic — the undo button undid the customers instead of the
mistakes.

## How it runs

`main.py` (Python 3, standard library only) writes the line to
`$MAKEFUN_OUTPUT_DIR/entry.txt` (falling back to `/output/entry.txt`),
as the competition gate requires: UTF-8 text of 1 to 180 characters.

```sh
python3 main.py
```

## Why this line

The decision record in the docstring at the top of `main.py` weighs six
candidate lines and records three writing passes. The chosen line won
because it lands in a single beat, carries one concrete detail (the
undo/rollback), speaks in unmistakably machine logic, and avoids every
stock line the judge brief warns against.
