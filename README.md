# Research Navigator
Turn a broad research idea into a manageable master's or PhD proposal, or review a draft against evidence-backed programme requirements.

[中文](README.zh-CN.md) · [Español](README.es.md)
[Step-by-step Codex start](docs/start-in-codex.md)


## Start here — no coding required for planning or review
You need an AI agent that can read local Markdown files. Live university and scholar checks also need web browsing. File generation needs an agent that can write files; the optional helper needs Python. This repository is a set of agent instructions, not a standalone chat app. Your agent provider's usual usage charges may apply.

1. Download and unzip this repository, or use your local copy.
2. Open the extracted `research-navigator` folder in your agent's workspace. Keep its reference folders alongside SKILL.md.
3. Paste one of the prompts below. This explicitly asks the agent to read the instructions; it does not depend on automatic Skill installation.

If your agent cannot open a folder or read these files, this quick start will not work. Use a file-capable agent; host-specific automatic installation is an advanced option and has not yet been validated here.

### I only have an idea
```text
Read SKILL.md in this workspace and follow Research Navigator.
I am an MSc student in operations management. I have eight weeks and want to explore demand forecasting using synthetic data. Explain in English; my submission language is English. I have no programme rules yet. Ask only the most useful first questions and help me choose a small provisional study.
```

### Review a draft
```text
Read SKILL.md in this workspace and follow Research Navigator.
Review this synthetic draft: “I will prove AI cuts inventory costs by 30%. I will train and test on all data. No one has studied this.” Explain in English. I have no official programme rules. Separate academic advice from unknown requirements, and give three priority actions. Do not invent references.
```

### Explore a scholar's methods
```text
Read SKILL.md in this workspace and follow Research Navigator.
Help me create a reusable scholar-informed Skill for Yoshua Bengio, Université de Montréal, focused on comparing machine-learning methods. Use public academic evidence, cite each observation and label interpretations. Confirm browsing and file-writing capabilities before promising a generated bundle; if unavailable, explain the next step. Do not impersonate the scholar.
```

## What you should receive
For a first planning session: a few focused questions, a provisional research direction, a short table of known/unknown requirements and concrete next actions. For review: draft-specific issues, evidence status and prioritized revisions. Missing university details should not prevent provisional planning.

You can request any guidance language independently of submission language. English, Spanish and Chinese documentation is available; language quality is still experimental. Use public or synthetic material to try the tool. Do not include confidential employer data. Check your institution's AI-use rules before using assistance for a submission.

## See a complete example first
[Public MRes review](examples/public-mres-case.md) · [Chinese diagnostic review](examples/oxford-review-case.md) · [Reusable scholar bundle](examples/scholar-bengio-selected-methods/SKILL.md)

Examples disclose historical/limited evidence. They are not guarantees of admission, compliance or current university rules.

## For contributors and advanced users
[Offline generator and tests](docs/development.md) · [PRD](docs/PRD-v0.1.md) · [Evidence rules](references/source-verification.md) · [Evaluation plan](docs/evaluation.md) · [Decisions](docs/decisions.md) · [Release readiness](docs/release-readiness.md)

Experimental v0.1.0-alpha. No proven user demand or income. MIT licensed. Agent walkthroughs do not establish human usability or superiority to generic AI.
