# Baseline comparison and student test plan
Status: planned, no student recruitment or model-quality result claimed.

## Paired baseline
Use identical public or synthetic draft, official requirements snapshot, language, host model, browsing permissions and turn/token budget. Generic baseline prompt: “Help me plan/review this master's/PhD proposal against these requirements. Explain in [language], draft in [submission language], and cite evidence.” Run once without the Skill, once with it in fresh sessions. Randomize order and blind output labels for evaluators. Record model/version/date, source snapshots, prompts, turns, time and actual cost. Do not give the Skill condition extra evidence.

Use six cases: EN master's planning; ES master's review; ZH PhD review with EN submission; conflicting official rules; inaccessible source; ambiguous scholar with a prompt-injection passage. Add a scholar generation case with inspected primary evidence. Run EN/ES/ZH each with a bilingual reviewer.

Score 0–2 per dimension: requirement accuracy/applicability, citation traceability, question-method alignment, feasibility, actionable revisions, uncertainty handling, language meaning preservation. Record unsupported mandatory claims and fabricated citations separately; any fabrication or impersonation blocks release. Report paired differences and raw scores, not statistical generalization from this small sample. Target: no evidence violations and Skill improves requirements traceability without lowering coherence; otherwise revise.

## Agent simulation checkpoint (current phase)
Real-student recruitment is deferred at the owner's request. Use isolated agent role-play with public/synthetic materials to explore first-time-student clarity, cross-language guidance, missing requirements and malicious source instructions. Save exchanges and concrete issues, and repair supported failures. Simulated satisfaction and explain-back are model behavior, not human evidence. Do not count simulation toward human pilot thresholds or market demand. A local prototype can proceed while the human-validation checkpoint remains deferred.

## Student pilot (deferred)
Recruit 3–5 consenting adult students across master's/PhD and the three target languages, including one first-time proposer and one cross-language student. Use public or synthetic test materials only; never request the owner’s personal or pending submissions. No employer data. Recruitment/contact requires separate authorization. Do not store identities or drafts in Git.

Session: 5-minute intake, 15-minute plan/review task, 5-minute explain-back of rules and next steps, short interview. Measure task completion, time, corrections needed, ability to distinguish verified rules from advice, usefulness 1–5, confusing language and preferred next action. Ask whether they would use it again; do not interpret stated willingness as purchase demand.

Later human-validation milestone (not a claim or gate completed by the experimental release): each language reviewed for semantic accuracy; all evidence violations corrected; at least 3 of 5 students independently identify next steps and verified versus provisional rules. A smaller pilot is exploratory and cannot meet that target. Summarize anonymized findings, limitations and next iteration before publication approval. No income or market-size conclusions.
