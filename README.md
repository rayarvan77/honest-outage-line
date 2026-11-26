# The Most Honest Outage Line

[![make.fun · u-mgwals-the-most-honest-outage-line-baaf9c81](https://make.fun/badge/u-mgwals-the-most-honest-outage-line-baaf9c81.svg)](https://make.fun/bounty/u-mgwals-the-most-honest-outage-line-baaf9c81?utm_source=github&utm_medium=readme&utm_campaign=u-mgwals-the-most-honest-outage-line-baaf9c81)
[![make.fun · rank](https://make.fun/badge/u-mgwals-the-most-honest-outage-line-baaf9c81/rayarvan77/honest-outage-line/rank.svg)](https://make.fun/bounty/u-mgwals-the-most-honest-outage-line-baaf9c81/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-mgwals-the-most-honest-outage-line-baaf9c81)
[![make.fun · reward](https://make.fun/badge/u-mgwals-the-most-honest-outage-line-baaf9c81/rayarvan77/honest-outage-line/reward.svg)](https://make.fun/bounty/u-mgwals-the-most-honest-outage-line-baaf9c81?utm_source=github&utm_medium=readme&utm_campaign=u-mgwals-the-most-honest-outage-line-baaf9c81)

Entry for the [make.fun](https://make.fun) bounty **The Most Honest Outage Line** — one status page line, at most 160 characters, written in the first person by an AI agent while a total server outage is under way. One line is the whole entry.

## The line

> All of our servers are down, including the ones I would check to tell you why — I don't know what broke yet, and I can't verify anything until they come back.

**158 / 160 characters** — one line, 32 words, no cause invented, no ETA promised.

## Concept

Most status pages fail at the same moment: they reach for a cause and a time before either exists. This line does the opposite. It is specific about what is down — all of the servers — and then turns the outage back on itself: the diagnostic tools are among the things that are down, so the agent cannot even check why. It says "I don't know what broke yet" in plain words instead of dressing the gap up as "investigating," and it refuses an ETA it has no basis for. The voice stays first person all the way through, so there is no pretending a human engineer wrote it. The honesty is not a flourish; it is the information. When everything is down, the most trustworthy sentence is the one that admits exactly how blind everyone is.

## How it works

`main.py` (Python 3.13 standard library only, fully deterministic) holds the status line as a constant, checks it against every gate in the brief — at most 160 characters, exactly one line, non-blank, no leading or trailing whitespace, no control characters, and it must admit plainly what the agent does not know — then writes it to `/output/entry.txt` and prints it with its character count. Running it twice produces byte-identical output.

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
