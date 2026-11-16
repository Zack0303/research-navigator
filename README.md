# Research Navigator

**A research-supervisor prompt for master's and PhD students.** Paste it into any AI chat. It helps you plan a project, review a draft, set up a literature review or plan a section, and it checks for the mistakes that usually cost students months.

[中文](README.zh-CN.md) · [Español](README.es.md)

## Start in one minute (no coding)

1. Open **[WEB-START.txt](WEB-START.txt)** ([plain text for copying](https://raw.githubusercontent.com/Zack0303/research-navigator/main/WEB-START.txt)).
2. Copy all of it into a new chat in ChatGPT, Claude, Gemini, DeepSeek or similar. Upload it instead if your chat accepts files. A link alone is not enough.
3. Say what you need, in any language. For example:

> I'm an MSc student in education. I want to study how teachers use AI feedback tools, but the topic is too broad. I have four months. Explain in English.

You should get two or three focused questions, a provisional direction and one clear next step. You do not need your university's rules to start. Unknown rules stay marked as *unknown*.

## What makes it different from just asking an AI

A plain chat already spots obvious problems, such as a missing method or train/test leakage. Research Navigator adds **six checks** for problems that are easy to miss, because each step looks reasonable on its own:

| Check | The question it asks |
|---|---|
| **C1 Anchor** | Has the project drifted from what you and your supervisor actually need? |
| **C2 Nearest neighbours** | What do the 3–5 closest works already do, and what is really new? |
| **C3 Claim strength** | Is any claim stronger than its evidence? |
| **C4 Right yardstick** | Are studies judged against their own aims, or against one ladder that does not fit? |
| **C5 Feasibility from a pilot** | Is your workload measured from a small pilot, or guessed? |
| **C6 Unknown is not zero** | Does every rule, number and status have a source? Is "planned" kept apart from "done"? |

**Used in a real literature review.** The author built these checks while writing a systematic literature review (2026, still in progress) and then used them in that review. Before the checks, the review had three problems:
- it drifted away from the research group's aims, one reasonable step at a time;
- it used one value ladder that judged studies against goals they never had;
- it nearly claimed novelty for a grouping that other reviews already used.

After the author switched to this structure, it worked well for that review. The structure is: anchor and nearest-neighbour checks, search planning from a pilot, coding that describes before it appraises, and a paragraph brief before each section. This is one developer's own experience, not an independent study.

It also gives you short, standard outputs you can share:
- a **one-page research brief** to show your supervisor early;
- a **review report**: one-sentence verdict, at most five priority issues, a claim-strength table and next actions;
- a **literature-review setup sheet** with a pilot-based workload estimate;
- a **paragraph brief** (claim, evidence, what must not be said) *before* you write, so the logic is yours.

## Try these

**Idea → plan**
> I'm a PhD student in operations management. I'm interested in using large language models for production scheduling. Help me find a manageable first study. Explain in Chinese; I submit in English.

**Review a draft**
> Review this paragraph from my proposal: "This study will prove that AI reduces inventory costs by 30%. I will train and test the model on all available data. No one has studied this before." I have no programme rules yet.

**Literature review**
> I need to do a systematic literature review on digital twins in hospitals for my master's thesis. I have ten weeks. Where do I start?

**Plan a section**
> Help me plan the Discussion section of my paper before I write it. My main finding is that the new method was faster but not more accurate.

## What it will not do

- Invent papers, citations, page numbers, counts or university rules.
- Call a source "verified" unless it actually read it in this chat.
- Write text for you to submit when your institution's AI policy is unknown or forbids it. It gives structure and feedback instead.
- Claim novelty without a search.

Use public or made-up material when you try it. Do not paste confidential employer data. Check your institution's AI-use rules before using any AI help for assessed work.

## For agent users (Codex, Claude Code and others)

Open this folder in your agent and say: `Read SKILL.md and follow Research Navigator.` Then describe your task. See [step-by-step Codex start](docs/start-in-codex.md). The agent version reads the detailed [checks](references/checks.md), [templates](references/templates.md) and [literature-review guide](references/lit-review.md).

An advanced option builds evidence-linked notes on a scholar's documented methods: [scholar guide](references/scholar-generator.md) · [example](examples/scholar-bengio-selected-methods/SKILL.md).

## Status and honesty

Version **v0.2.0-alpha**, experimental. Agent-only trials are recorded in [docs/v0.2-trial.md](docs/v0.2-trial.md). They show what the instructions make a model do. They do not show that real students find it useful. The author has used the structure in one real, ongoing literature review (see above). No independent student pilot has been run yet. Web interfaces have not each been tested. MIT licence.

[Evaluation plan](docs/evaluation.md) · [Decisions](docs/decisions.md) · [Release notes](docs/release-notes.md) · [Development and tests](docs/development.md) · [Public review example](examples/public-mres-case.md)

**Feedback wanted.** If you try it, please open an issue: what you asked, what helped, what confused you. Use made-up details only.
