# Reusable Scholar Skill workflow
1. Resolve scholar name, institution and field from public academic evidence; ask if multiple identities fit.
2. Inspect a small relevant selection of primary academic materials (normally 2–3). Record URLs, titles, access dates and evidence locators. Explicitly state selection limits; do not imply a complete profile.
3. Extract only source-supported methodological observations. A practice observed in one paper is a practice in that paper, not a lifelong preference. Label application to the student's project as interpretation.
4. Prepare the JSON shape in examples/scholar-input.json, with identity_confirmed=true only after identity checks and per-source inspected=true only after actual inspection. This file is synthetic and must never be used as real academic evidence.
5. Run `python3 scripts/generate_scholar.py INPUT.json OUTPUT_DIRECTORY`. The helper validates structure and creates four reusable files. It does not browse, authenticate evidence, or verify factual claims. Review its output against original sources before reuse.
6. If browsing is unavailable, produce a provisional outline or request materials; do not generate a supposedly verified profile from a name alone.
