# v0.2.0-alpha — Research checks

Repositions Research Navigator as a research-supervisor prompt.

- **Six checks** for easily missed mistakes: C1 Anchor (drift), C2 Nearest neighbours (novelty), C3 Claim strength, C4 Right yardstick (appraisal fit), C5 Feasibility from a pilot, C6 Unknown is not zero. Plus an "own words" rule for borrowed logic. See references/checks.md.
- **Two new modes:** literature-review setup (references/lit-review.md) and section brief before writing.
- **Templates T1–T5:** one-page research brief, review report, paragraph brief, literature-review setup sheet, where-we-are note.
- **WEB-START.txt rewritten** (about 1,700 words, self-contained) with the checks, outputs and four entry choices.
- **SKILL.md rewritten** with clear structure and reply style (conclusion first, at most five issues, one next action).
- **READMEs (EN/ZH/ES) rewritten**: one-minute start, what is added beyond a plain chat, example prompts, limits.
- **Tests:** six new structural tests (check consistency, self-contained web file, link resolution, templates); the three generator tests are unchanged.
- **Agent trial** of the web edition against a no-prompt baseline on three check cases: docs/v0.2-trial.md.

Limitations unchanged: no human student pilot, no native-speaker language review, web platforms not individually tested.

# v0.1.1-alpha — Web chat access
Adds WEB-START.txt, a single self-contained instruction file for pasting/uploading in ordinary web chats. EN/ES/ZH README pages now put this route first, with humanities examples and no coding prerequisite. Browsing and downloadable files are optional capabilities; supplied sources remain unverified without inspection. Exact Gemini/DeepSeek interfaces have not been tested. The automated generator is unchanged. See web-chat-trial.md for agent-only checks.

# v0.1.0-alpha — 2026-10-16
First experimental release, approved for public MIT distribution.

Includes proposal planning/review instructions, programme evidence rules, independent guidance/submission languages, English/Spanish/Chinese onboarding, an offline evidence-to-Skill generator, synthetic examples, public-source walkthroughs and a limited real-scholar bundle.

Validation: three generator tests on Python 3.12.14; main and example Skills pass dedicated structural validation. Agent onboarding and one generic/Skill comparison are recorded separately from constructed role-play. Release behavior checks cover multilingual cases; see release-behavior-checks.md. GitHub CI passed on Python 3.10 and 3.12; see https://github.com/Zack0303/research-navigator/actions/runs/38894848854.

Limitations: no human student or bilingual validation, no comprehensive requirements library, no automatic factual verification, abstract-only scholar observations, historical institutional examples, no guaranteed admissions/compliance outcome, no established demand or income. Desktop menu instructions are documentation-backed, not a completed UI installation test. Browsing and file-writing capabilities depend on the host. This is a Skill repository, not a standalone application.

Report problems using public/synthetic reproductions. See development.md for contribution instructions. Do not submit confidential drafts, credentials or employer information in issues or pull requests.
