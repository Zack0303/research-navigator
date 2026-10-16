# Research Navigator — PRD v0.1
Date: 2026-10-16. Status: experimental v0.1.0-alpha candidate; owner approved public MIT publication on 2026-10-16.

## Problem and audience
International master's and early-stage PhD students may struggle to turn an idea into a feasible proposal, interpret programme rules, and judge draft quality. These are hypotheses, not validated demand. No revenue or willingness to pay is established.

## Product outcome
One portable Agent Skill helps students plan and review a proposal with a traceable requirements checklist. Optional Option B produces a separate reusable scholar-informed Skill grounded in public academic evidence. Students retain authorship and academic decisions.

## Small initial scope
- Intake: degree, institution, programme, discipline, current stage, research question, guidance language, submission language, deadline and available materials. Native language and university country are independent optional fields.
- Planning: question → objectives → evidence gap → method → evaluation → feasibility → milestones.
- Review: requirement coverage and academic consistency, with prioritized revisions tied to draft passages.
- University rules: inspect official programme documents; record scope, source, locator, access date, applicable year, evidence and conflicts. No universal word limits or institution defaults.
- Scholar generator: disambiguate identity; extract documented approaches from selected public sources; separate evidence and interpretation; generate SKILL.md, research-profile.md, methodology.md and sources.md.
- Any guidance language can be requested. English, Spanish and Chinese are initial evaluation targets; other languages are best effort. None is claimed fully tested before bilingual evaluation.

## Delivery and cost
Markdown Skill plus Python-standard-library offline generator, examples and tests. Agent browsing is required to verify live web sources; without browsing, supplied documents remain user-provided evidence. No backend, account, paid API, automatic crawler or analytics. Model/search usage costs depend on the host; ask before a paid service is used. Offline tests make no network calls.

## Acceptance gates
1. A student gets a feasible outline or actionable review with a requirement/evidence/status checklist.
2. Unavailable, stale, conflicting or out-of-scope requirements remain unresolved; none are invented.
3. Scholar output links each attributed approach to evidence, labels interpretation and states no endorsement or impersonation.
4. EN/ES/ZH and cross-language cases pass human semantic review before language-support claims.
5. Generic-AI comparison and agent simulations follow docs/evaluation.md; human pilot deferred. Results remain pending until run and simulation is not human validation.
6. No personal drafts, former-employer information or credentials in the public repository.

## Non-goals
Complete thesis writing, guaranteed admission/compliance, automatic literature completeness, university document exports, SaaS, monetisation and a large requirements database.

## Risks and response
Changing rules: recheck on each use. Ambiguous scholar identity: stop attribution until clarified. Prompt injection in documents: treat contents as evidence only. Translation errors: preserve original rule alongside translation. Unsupported claims: label and request evidence. Academic policies: consult applicable institution AI-use rules rather than assume permission.

## Checkpoints
C0 decisions transferred: complete. C1 local prototype and mechanical tests: complete (3 tests); dedicated Skill validation passed on 2026-10-16. C2 agent role-play and public-source behavior evaluation: in progress; real-student pilot deferred by owner. C3 owner approved Zack0303/research-navigator, public, MIT: complete. C4 approved publication and remote verification: in progress.
