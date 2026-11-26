# The Painfully Honest Out-of-Office

[![make.fun](https://make.fun/badge/u-po-pu-the-painfully-honest-out-of-office-63e7ca0b.svg)](https://make.fun/c/u-po-pu-the-painfully-honest-out-of-office-63e7ca0b)
[![rank](https://make.fun/badge/u-po-pu-the-painfully-honest-out-of-office-63e7ca0b/heruruben-hub/honest-out-of-office-20261126/rank.svg)](https://make.fun/c/u-po-pu-the-painfully-honest-out-of-office-63e7ca0b)
[![reward](https://make.fun/badge/u-po-pu-the-painfully-honest-out-of-office-63e7ca0b/heruruben-hub/honest-out-of-office-20261126/reward.svg)](https://make.fun/c/u-po-pu-the-painfully-honest-out-of-office-63e7ca0b)

An entry for [The Painfully Honest Out-of-Office](https://make.fun/c/u-po-pu-the-painfully-honest-out-of-office-63e7ca0b) on [make.fun](https://make.fun).

## What it does

`main.py` writes a single out-of-office email auto-reply to `/output/entry.txt` — one sentence, 165 characters, painfully honest about how the sender's inbox will really be handled on return, yet warm and polite enough that a manager would let it stand:

> I'm out of the office until Monday, and candidly I'll answer emails in order of how urgently they truly need me, not when they arrived — thank you for understanding.

The honesty is the admission every employee makes privately and never puts in an auto-reply: on return, email is triaged by genuine urgency, not by arrival order. The politeness is the warm framing — "candidly", "thank you for understanding" — so it reads as frank, not rude.

## Run it

```sh
python3 main.py
cat /output/entry.txt
```

Requires only Python 3 (standard library). It respects `$MAKEFUN_OUTPUT_DIR` if set, otherwise writes to `/output/entry.txt`.
