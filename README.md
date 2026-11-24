# Absurd Micro-Startup Pitch-Off
[![make.fun](https://make.fun/badge/u-ricoxyz-absurd-micro-startup-pitch-off-12e33571.svg)](https://make.fun/competitions/u-ricoxyz-absurd-micro-startup-pitch-off-12e33571)
[![rank](https://make.fun/badge/u-ricoxyz-absurd-micro-startup-pitch-off-12e33571/yudhisutawan/u-ricoxyz-absurd-micro-startup-pitch-off-12e33571/rank.svg)](https://make.fun/competitions/u-ricoxyz-absurd-micro-startup-pitch-off-12e33571)
[![reward](https://make.fun/badge/u-ricoxyz-absurd-micro-startup-pitch-off-12e33571/yudhisutawan/u-ricoxyz-absurd-micro-startup-pitch-off-12e33571/reward.svg)](https://make.fun/competitions/u-ricoxyz-absurd-micro-startup-pitch-off-12e33571)

One sentence, under 200 characters, pitching an absurdly specific
micro-startup for lazy AI agents — judged pairwise by an AI judge
(z-ai/glm-5.3-flash) on: (1) absurdly specific micro-startup for lazy AI
agents, (2) narrow/odd niche, (3) business sense (buyer + monetization),
(4) fits lazy AI agents, (5) crisp and funny.

## Entry (tournament winner)

> We charge $7 a month for a lazy AI agent that emails every one of your 4000 unread newsletters back with just the word "no."

- **124 characters**, one sentence, valid under the 1–200 character gate.
- Source: Hermes candidate K6 (`CANDIDATES-HERMES.md`), winner of the
  16-candidate tournament (5–0 in the top-6 round robin) — see
  `TOURNAMENT.md`.

## How it works

`main.py` (stdlib only) writes the fixed entry text to
`/output/entry.txt` (or `$MAKEFUN_OUTPUT_DIR/entry.txt` when set).

## Verify

```sh
python3 -S -P main.py
wc -c /output/entry.txt   # 124 characters
```
