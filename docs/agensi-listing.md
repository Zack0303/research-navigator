# Agensi listing copy (v0.2)

Text for https://www.agensi.io/skills/research-navigator. The maintainer pastes it into the Agensi dashboard. Keep it in step with README.md.

---

## Short description

Keep your literature review and research plan on track. Six checks catch drift, unsupported novelty, overclaiming, the wrong appraisal yardstick and guessed workload. Built and used in a real systematic review. Free, experimental v0.2.0-alpha.

## About this skill

Research Navigator is a research-supervisor skill for master's and PhD students. Its strongest mode is **literature-review setup**.

**Built and used in a real review.** The author developed these checks while writing a systematic literature review (2026, in progress) and used them in it. Before the checks, that review drifted from the research group's aims one reasonable step at a time. It also judged studies on a single value ladder they were never designed for, and nearly claimed novelty for a grouping that other reviews already used. The author found this structure worked well for that review. It is one developer's experience, not an independent study.

**Five modes:** plan a project · review a proposal or paper · set up a literature review · brief a section before writing · evidence-linked notes on a scholar's methods (advanced).

**Six checks:**
- **C1 Anchor:** has the work drifted from what you and your supervisor need?
- **C2 Nearest neighbours:** what do the 3–5 closest works already do?
- **C3 Claim strength:** is any claim stronger than its evidence?
- **C4 Right yardstick:** are studies judged against their own aims, with describing kept apart from appraising?
- **C5 Feasibility from a pilot:** is the workload measured from a small pilot, or guessed?
- **C6 Unknown is not zero:** does every rule, count and status have a source?

**Outputs:** a one-page research brief, a review report (verdict, at most five priority issues, claim-strength table), a literature-review setup sheet, a paragraph brief (claim | evidence | must-not-say) and a where-we-are note.

**No MCP agent?** Paste WEB-START.txt from the GitHub repository into any web chat, such as ChatGPT, Gemini or DeepSeek: https://github.com/Zack0303/research-navigator

The student owns the research and the final wording. MIT licensed. Source: https://github.com/Zack0303/research-navigator

## Example session

Use this real agent-trial output in place of the hand-written example. It is abridged; the full record is in docs/v0.2-trial.md.

**Prompt (synthetic):**
> My topic started as how small manufacturers adopt AI scheduling tools. My supervisor wanted industry relevance. I narrowed to LLM scheduling, then to benchmarks for LLM scheduling, and now I'm comparing evaluation metrics across benchmark papers. Is this a good review topic? I'm an MSc student with 10 weeks left.

**Response (abridged):**
> Short answer: it can be a good review topic, but not in its current form. Your purpose has drifted, and your time is short.
>
> **C1, drift.** Steps 1–2 keep your purpose. Step 3 is a different purpose: you now study how researchers measure, not what manufacturers need. Has your supervisor seen the last two narrowings?
>
> **A possible bridge:** "Do the metrics used in LLM scheduling benchmarks measure what a small manufacturer cares about, such as lateness, changeover cost and robustness to disruptions?"
>
> **C2.** Find 3–5 existing surveys first. Until then, "no one has compared these metrics" is unknown, not proven.
>
> **C5.** Run a pilot this week: one database, screen about 50 records, time it, then estimate.
>
> **Next action:** write one paragraph, "who needs this and what they must learn", and send it to your supervisor.

Caption: Agent-trial output to a synthetic prompt (Claude Sonnet, web-chat edition, 2026-11-15). Not a real student outcome.

## Known limitations

Experimental alpha. The evidence so far is the author's own use in one real, ongoing review and a small agent-only trial. There has been no independent student pilot and no native-speaker review, and it has not been shown to beat ordinary prompting. The nine offline tests check structure and packaging, not scientific truth. Source verification depends on the host agent's browsing. There are no admission, grading, compliance or publication guarantees.

## FAQ: How does it differ from just asking a standard AI?

A strong model already spots obvious problems. In a small agent trial, the difference was in what happened next. With the skill, the agent proposed a timed pilot instead of a guessed plan and kept the supervisor in the loop. It did not plant an expected finding in a draft, and it asked about the institution's AI policy before writing. The author also used the structure in a real review and found it worked well. Neither of these is an independent test.
