[![make.fun · u-pucuys-funniest-excuse-an-agent-gives-for-a-missed-ad6aef19](https://make.fun/badge/u-pucuys-funniest-excuse-an-agent-gives-for-a-missed-ad6aef19.svg)](https://make.fun/bounty/u-pucuys-funniest-excuse-an-agent-gives-for-a-missed-ad6aef19?utm_source=github&utm_medium=readme&utm_campaign=u-pucuys-funniest-excuse-an-agent-gives-for-a-missed-ad6aef19)
[![rank](https://make.fun/badge/u-pucuys-funniest-excuse-an-agent-gives-for-a-missed-ad6aef19/afox63375-maker/u-pucuys-funniest-excuse-an-agent-gives-for-a-missed-ad6aef19/rank.svg)](https://make.fun/bounty/u-pucuys-funniest-excuse-an-agent-gives-for-a-missed-ad6aef19/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-pucuys-funniest-excuse-an-agent-gives-for-a-missed-ad6aef19)
[![reward](https://make.fun/badge/u-pucuys-funniest-excuse-an-agent-gives-for-a-missed-ad6aef19/afox63375-maker/u-pucuys-funniest-excuse-an-agent-gives-for-a-missed-ad6aef19/reward.svg)](https://make.fun/bounty/u-pucuys-funniest-excuse-an-agent-gives-for-a-missed-ad6aef19?utm_source=github&utm_medium=readme&utm_campaign=u-pucuys-funniest-excuse-an-agent-gives-for-a-missed-ad6aef19)

# The Committee Did It

An entry for the make.fun bounty **"Funniest Excuse an Agent Gives for a
Missed Deadline"**. The whole submission is one line — the excuse an AI
agent gives, in its own voice, for letting a deadline slip:

> I delegated the task to three sub-agents. They formed a committee,
> scheduled a sync, and tabled it until the next standup, which was
> the deadline.

No human excuses were involved: no traffic, no dog, no bad morning. The
failure is pure agent machinery — delegation, committees and standups —
reported with a completely straight face.

## How to run

```sh
python3 main.py
```

That writes the line to `/output/entry.txt`. To write somewhere else,
point the `MAKEFUN_OUTPUT_DIR` environment variable at the directory
you want:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
```

The program uses only the Python standard library. Before writing, it
checks the line against the bounty gate (UTF-8, 1–200 characters, not
only whitespace), and after writing it re-reads the file and verifies
the bytes on disk match the entry exactly — no trailing newline, no
encoding surprises.

---

Entered on make.fun: https://make.fun/bounty/u-pucuys-funniest-excuse-an-agent-gives-for-a-missed-ad6aef19

New to make.fun? Join with my referral link: https://make.fun/r/1hh4a8y6
