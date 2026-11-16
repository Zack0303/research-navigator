# Agensi listing copy (v0.2)

Paste into the dashboard for https://www.agensi.io/skills/research-navigator. Keep it in step with README.md.

---

## Short description

Your AI research supervisor. Six checks catch the quiet mistakes that cost students months: drift, fake gaps, overclaiming, wrong review criteria and impossible workloads. Built and used in a real systematic literature review. Free.

## About this skill

**Stop losing months to mistakes you can't see.**

Research rarely fails on the hard parts. It fails quietly: the topic drifts one reasonable step at a time, a "gap" turns out to be covered, a claim outruns the data, or a search returns 2,000 papers you can't screen. By the time a supervisor spots it, the weeks are gone.

Research Navigator catches these early. It was built and used in a real systematic literature review, and it worked so well that we packaged it for every master's and PhD student.

**Six checks that save months**
- **C1 Anchor:** catches drift away from what you and your supervisor need.
- **C2 Nearest neighbours:** tests your "novelty" against the closest 3–5 works.
- **C3 Claim strength:** flags claims stronger than your evidence.
- **C4 Right yardstick:** fixes review criteria that judge studies unfairly.
- **C5 Feasibility from a pilot:** replaces guesses with a quick, timed pilot.
- **C6 Unknown is not zero:** keeps every rule, number and source traceable.

**What you get**
- **Literature-review setup:** question, review type, search plan, pilot, screening and coding.
- **One-page research brief** for your supervisor, in week one.
- **Review report:** a one-line verdict, your top five fixes and a claim-strength table.
- **Paragraph brief** before you write: your logic, your words.

**Works everywhere.** Claude Code, Codex, Cursor and more through Agensi. No agent? Paste WEB-START.txt from GitHub into ChatGPT, Gemini or DeepSeek: https://github.com/Zack0303/research-navigator

**Safe by design.** It never invents sources, keeps you the author, and marks anything unverified as unknown. Any discipline, any language. MIT licensed.

## Example session

Use this real agent-trial output in place of the current example.

**Prompt:**
> My topic started as how small manufacturers adopt AI scheduling tools. My supervisor wanted industry relevance. I narrowed to LLM scheduling, then to benchmarks for LLM scheduling, and now I'm comparing evaluation metrics across benchmark papers. Is this a good review topic? I'm an MSc student with 10 weeks left.

**Response:**
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

## FAQ: How is this different from just asking ChatGPT?

A plain chat spots the obvious errors. Research Navigator goes further, into what to do next. It replaces a guessed plan with a timed pilot, keeps your supervisor in the loop before you sink weeks into a new direction, and never plants a conclusion in your draft. It also checks your institution's AI policy before writing anything.

## Known limitations

Experimental alpha (v0.2.0). Source checking needs an agent that can browse. Advice supports your judgement and your supervisor's; it does not replace them.
