# Advanced use and development
Planning and review use the agent conversation described in the README; Python is only needed for the offline packaging helper and tests.

## Offline demonstration
Python 3.10+ is the declared target; local tests passed on Python 3.9 and 3.12.14; the 3.10 minimum remains to be checked by CI. No third-party runtime dependencies.

From the repository folder, choose a new output directory:
```sh
python3 scripts/generate_scholar.py examples/scholar-input.json /tmp/scholar-demo-review
python3 -m unittest discover -s tests -v
```
The fixture is fictional. The helper packages evidence fields and checks citation relationships; it does not browse, confirm identity or authenticate sources. Existing output directories are rejected. For real sources follow references/scholar-generator.md first.

## Contribute
Use public/synthetic fixtures only. Describe the problem, reproduction steps, expected versus observed behavior and host/model details when known. Never include private drafts, credentials or employer data. Run offline tests for generator changes. For instruction changes record actual agent transcripts separately from constructed walkthroughs; no performance claims from expected answers. Submit changes through a pull request once a remote is published.
