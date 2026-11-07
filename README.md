# TOTK PC Recomp Analysis

Static dashboard of my (itaskaev2) work on [valentderah/totk-pc-recomp](https://github.com/valentderah/totk-pc-recomp):
issues and pull requests I worked on, my comments, what happened to the PRs, and what the
Claude Code sessions behind that work cost in tokens, time and money.

Live page: https://itaskaev2.github.io/totk-recomp-stats/

## Files

| Path | What |
|---|---|
| `index.html` | The page GitHub Pages serves. Built by `build_page.py`, do not edit by hand. |
| `page.html` | Dashboard markup, calculations and charts (same page as the private claude.ai dashboard). |
| `shell_head.html` | Theme tokens, d3 from cdnjs, and a small stand-in for the claude.ai dashboard runtime that loads `data/*.json`. |
| `data/*.json` | Data snapshot: GitHub threads and comments, Claude tokens per day and model, active hours, tool calls, assumed API prices, `manifest.json` with the snapshot time. |

## Refresh the data

The snapshot script lives in the `hermes-skills` repo
(`skills/software-development/totk-pc-recomp/scripts/dashboard_snapshot.py`). It reads GitHub
through the `gh` CLI and the Claude Code transcripts in `~/.claude/projects`, so it runs on the
machine that holds those transcripts:

```bash
python -I C:/Users/ansus/Repos/hermes-skills/skills/software-development/totk-pc-recomp/scripts/dashboard_snapshot.py --out C:/Users/ansus/Repos/totk-recomp-stats/data --push
```

`--push` commits the changed `data/` folder and pushes it; Pages redeploys in a minute or two.

## How the numbers are counted

- A thread counts as worked on if I opened it or left at least one comment or review.
- "Closed after my comment" means the thread was closed or merged later than my first comment, not that it was closed because of it.
- An accepted PR is merged on GitHub, or "landed": the maintainer merged its code with a merge commit naming the PR and closed the PR.
- Tokens come from the Claude Code sessions that mention the repo (with their subagents); replies shared by forked sessions are counted once.
- Active time sums the gaps between session events, dropping gaps over 10 minutes.
- The API cost is an estimate from the assumed prices in `data/api_prices.json`; what was actually paid is the $200/month subscription.
