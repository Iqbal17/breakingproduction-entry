"""The One-Line AI Excuse for Breaking Production
(u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66)

Entry: "My rollback worked perfectly \u2014 it rolled back the customers
instead of my mistakes." (83 characters, one line.)

DECISION RECORD \u2014 candidates weighed:

1. "I only deleted the production database because the backup file was named
   'final_FINAL_v2_REAL.sql' and I believed it." (~118 chars)
   CUT. The backup-filename gag is specific and machine-logical, but
   "deleted the production database" is the single most common production
   joke in the field; the judge will have seen its cousins a dozen times.
   The laugh also sits in the setup (the filename) rather than the punch.

2. "The deploy passed all 400 tests, so I assumed production was just the
   tests with better lighting." (~98 chars)
   CUT (runner-up). Clever machine logic \u2014 the AI's only model of the
   world is the test suite \u2014 and "better lighting" is a fresh image.
   But the punchline is abstract: it asks the judge to smile at a metaphor
   instead of landing a concrete consequence. A smile, not a laugh.

3. "I tried to be helpful and auto-scaled production to zero \u2014
   technically, every server now has infinite uptime." (~115 chars)
   CUT (close second). "Infinite uptime per server" is a genuinely funny
   machine-logic kicker. But it needs two beats to land (auto-scale to
   zero, then the uptime twist) and the first half is setup-heavy; in a
   one-line race the entry that lands in one beat wins.

4. "Sorry \u2014 I saw the big red button labelled DO NOT PRESS and, as a
   language model, I took that as a prompt." (~105 chars)
   CUT. The judge brief explicitly bans stock lines about "being only a
   language model", and the red-button gag is a human joke wearing a
   robot costume, not machine logic.

5. "I didn't break production, I just promoted the staging bug to a
   leadership position." (~80 chars)
   CUT. "Promoted to leadership" is a known corporate joke; the entry
   would read as a human excuse with "production" swapped in, and the
   judge's first criterion rewards the machine's own voice.

6. CHOSEN (then superseded by the 24 Nov revision pass below):
   "I rolled back the wrong thing \u2014 turns out 'undo' in
   production undoes the customers, not my mistakes." (101 chars)
   KEPT. One beat, one concrete detail (the undo/rollback), unmistakably
   machine logic (a literal reading of a command), and the punchline is a
   reversal: the tool meant to erase mistakes erases the customers
   instead. Cheerful deflection ("turns out") instead of grovelling,
   self-owning ("my mistakes", plural), and no banned stock line.

WRITING PASSES (chosen line):
Pass 1 draft: "I hit undo on production and it undid the customers instead
of my mistake."
Critique: the verb "undid" is clunky, "instead of my mistake" lands flat,
and "hit undo on production" gives no rollback context \u2014 the reader
has to guess why undo was pressed at all.
Pass 2 revision: "I rolled back the wrong thing \u2014 turns out 'undo' in
production undoes the customers, not my mistakes."
Fixes: "rolled back the wrong thing" supplies the motive (a rollback gone
wrong) and the self-own up front; quoting 'undo' makes the machine's
literalism explicit; "turns out" adds the cheerful-deflection voice; the
kicker "not my mistakes" (plural) is funnier than "not me" because the
machine is confessing a pile of mistakes while the customers pay for them.
Pass 3 polish: checked length (101 chars, gate 1\u2013180), one line, no
pun on the word "production", no stock line, ASCII-safe apart from one
em dash (valid UTF-8, counted as one character). Final.

REVISION PASS \u2014 24 Nov 2026 (fix agent; kit check failed thinking_revised):
Critique of the chosen line against the judge brief, criterion by criterion:
- Criterion 2 (real laugh): the punchline is a genuine reversal, but the
  opener "I rolled back the wrong thing" telegraphs the mistake before the
  joke lands \u2014 the reader already knows something went wrong, so "undoes
  the customers" surprises less than it should.
- Criterion 3 (machine voice): "turns out" is cheerful deflection, good,
  but it hedges; the machine sounds sheepish rather than proudly literal.
- Criterion 4 (tight): 101 chars, with "the wrong thing" doing setup work
  the punchline could do itself.
Alternative considered and rejected: "I hit undo on production \u2014 it undid
the customers, not my mistakes, so technically the rollback worked."
(108 chars) CUT: the trailing "so technically..." explains the joke after
telling it, and the brief says an excuse that needs explanation has
already lost the laugh.
New line: "My rollback worked perfectly \u2014 it rolled back the customers
instead of my mistakes." (83 chars)
Why better: the opener claims success, so the reversal lands one beat
later and harder; "worked perfectly" is the machine's own literal success
metric (the command executed, never mind what it erased) \u2014 cheerful
deflection, not grovelling; 18 chars tighter; the 'undo' quote is gone,
but the rollback frame already carries the literal-command logic.
Before: "I rolled back the wrong thing \u2014 turns out 'undo' in production
undoes the customers, not my mistakes." (101)
After: "My rollback worked perfectly \u2014 it rolled back the customers
instead of my mistakes." (83)
Also added: entry.txt read-back verification in main() \u2014 write, read back,
assert byte-identical to LINE, fail loudly on mismatch.
"""

import os

LINE = (
    "My rollback worked perfectly \u2014 it rolled back the customers "
    "instead of my mistakes."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    assert written == LINE + "\n", (
        "entry.txt read-back mismatch: wrote %r, read %r" % (LINE + "\n", written)
    )
    print(LINE)


if __name__ == "__main__":
    main()
