# Phase 3.0 - TrustGate Sovereign AI Control Page Rebuild

## Prompt Summary

- Rebuild `/ai-control/` as the public TrustGate Sovereign presence page.
- Rebuild `/pt/ai-control/` as the pt-PT TrustGate Sovereign localization.
- Preserve root/procurement/AI Control route structure, Portuguese localization, language switching, and track isolation.
- Keep Procurement pages materially unchanged.
- Lightly update root AI Control cards to point to TrustGate Sovereign positioning.
- Add original SVG assets only; no external assets, binaries, media, JavaScript, dependencies, cookies, redirects, or publication actions.
- Strengthen validation for TrustGate Sovereign content and claims boundaries.
- Update docs and repository run memory.
- Do not commit, tag, push, or publish.

## Files Added

- `assets/trustgate-sovereign-execution-firewall.svg`
- `assets/trustgate-sovereign-working-example.svg`
- `assets/tg360-evidence-cockpit.svg`
- `docs/codex_runs/20260627_phase_3_0_trustgate_sovereign_ai_control_rebuild_handoff.md`

## Files Modified

- `index.html`
- `pt/index.html`
- `ai-control/index.html`
- `pt/ai-control/index.html`
- `styles.css`
- `scripts/validate_public_surface.py`
- `README.md`
- `docs/site_content_model.md`
- `docs/public_claims_ledger.md`
- `docs/review_notes.md`
- `docs/publication_checklist.md`
- `docs/restrictions.md`
- `docs/translation_glossary.md`

## Public Positioning Summary

TrustGate Sovereign now leads the AI Control page as the execution firewall for agentic AI. The page distinguishes deployment governance, platform governance, and action clearance, then explains the Principal -> Control -> Proof model, the expanded control chain, TG360, TGSG surfaces, an illustrative watsonx Orchestrate / Manta / Db2 enterprise-stack scenario, executive value levers, private walkthrough scope, related systems, and public claims boundaries.

## English Page Summary

`/ai-control/` now leads with:

- TrustGate Sovereign
- The execution firewall for agentic AI
- the governed deployment/platform line
- the airport analogy
- Principal, Action, Context, Route, Admission, Telemetry, Proof, Held Gate
- TG360 evidence cockpit
- TGSG trust surfaces
- illustrative watsonx Orchestrate / Manta / Db2 scenario
- private walkthrough CTA
- Certify, Evidra, and FieldDelta as secondary related systems
- strengthened public boundaries

## PT-PT Page Summary

`/pt/ai-control/` mirrors the English meaning in European Portuguese, with product names preserved. It uses TrustGate Sovereign, IA agêntica, firewall de execução, implantação, âmbito, autorização, cockpit de evidência, Porta mantida, and the same illustrative scenario and claims boundaries.

## Visual Assets Added

- `assets/trustgate-sovereign-execution-firewall.svg`
- `assets/trustgate-sovereign-working-example.svg`
- `assets/tg360-evidence-cockpit.svg`

All are original SVGs, local-only, with no logos, screenshots, external assets, or media binaries.

## Validator Updates

- Added the three TrustGate Sovereign SVGs to required assets.
- Updated AI Control EN/PT required content checks for TrustGate Sovereign.
- Added public-page-only blocked phrases for production, customer, telemetry, connector, CP-7, IBM, ROI/savings, media metadata, and internal identifier claims.
- Preserved existing bilingual route, switcher, track isolation, safety, SVG, local link, and claim checks.

## Validation Commands Run

- `git rev-parse --is-inside-work-tree`
- `git branch --show-current`
- `git rev-parse HEAD`
- `git log -1 --oneline`
- `git status --short --untracked-files=all`
- `python3 scripts/validate_public_surface.py`
- `git diff --check`
- `git status --short --untracked-files=all`
- `ls docs/codex_runs`
- `find . -type f | grep -E '\.(mp4|mov|mkv|avi|wav|aiff|mp3|aac|png|jpg|jpeg|gif|webp|srt|vtt|woff|woff2|ttf|otf)$' || true`

## Validation Results

Preflight:

```text
git rev-parse --is-inside-work-tree
true

git branch --show-current
main

git rev-parse HEAD
ea0d80980e8824c46a35eee09a1f7e00ed057f82

git log -1 --oneline
ea0d809 Initial commit
```

Initial `git status --short --untracked-files=all` before editing:

```text
 M README.md
?? .gitignore
?? ai-control/index.html
?? assets/ai-action-control-gate.svg
?? assets/evidence-control-pattern.svg
?? assets/evidence-pack.svg
?? assets/favicon.svg
?? assets/mark.svg
?? assets/og-image.svg
?? assets/procurement-evidence-chain.svg
?? assets/simulation-review-pack.svg
?? docs/codex_runs/20260608_phase_2_1_hub_public_language_qa_handoff.md
?? docs/codex_runs/20260608_phase_2_2_homepage_public_language_correction_handoff.md
?? docs/codex_runs/20260608_phase_2_3_footer_label_cleanup_handoff.md
?? docs/codex_runs/20260608_phase_2_4_track_navigation_isolation_handoff.md
?? docs/codex_runs/20260608_phase_2_5_ai_control_sentence_removal_handoff.md
?? docs/codex_runs/20260608_phase_2_6_procurement_buyer_language_translation_handoff.md
?? docs/codex_runs/20260609_phase_2_7_portuguese_localization_handoff.md
?? docs/deployment_runbook.md
?? docs/public_claims_ledger.md
?? docs/publication_checklist.md
?? docs/restrictions.md
?? docs/review_notes.md
?? docs/site_content_model.md
?? docs/translation_glossary.md
?? index.html
?? procurement/index.html
?? pt/ai-control/index.html
?? pt/index.html
?? pt/procurement/index.html
?? scripts/validate_public_surface.py
?? styles.css
```

`python3 scripts/validate_public_surface.py`:

```text
Public surface validation: PASS
Required files checked: 18
HTML pages checked: 6
Bilingual route, SEO, language switcher, persona-specific nav, TrustGate Sovereign content, procurement language, Boundaries, Contact, safety, claim, SVG, and local link checks passed.
```

`git diff --check`:

```text
PASS - exit 0, no output.
```

Final `git status --short --untracked-files=all`:

```text
 M README.md
?? .gitignore
?? ai-control/index.html
?? assets/ai-action-control-gate.svg
?? assets/evidence-control-pattern.svg
?? assets/evidence-pack.svg
?? assets/favicon.svg
?? assets/mark.svg
?? assets/og-image.svg
?? assets/procurement-evidence-chain.svg
?? assets/simulation-review-pack.svg
?? assets/tg360-evidence-cockpit.svg
?? assets/trustgate-sovereign-execution-firewall.svg
?? assets/trustgate-sovereign-working-example.svg
?? docs/codex_runs/20260608_phase_2_1_hub_public_language_qa_handoff.md
?? docs/codex_runs/20260608_phase_2_2_homepage_public_language_correction_handoff.md
?? docs/codex_runs/20260608_phase_2_3_footer_label_cleanup_handoff.md
?? docs/codex_runs/20260608_phase_2_4_track_navigation_isolation_handoff.md
?? docs/codex_runs/20260608_phase_2_5_ai_control_sentence_removal_handoff.md
?? docs/codex_runs/20260608_phase_2_6_procurement_buyer_language_translation_handoff.md
?? docs/codex_runs/20260609_phase_2_7_portuguese_localization_handoff.md
?? docs/codex_runs/20260627_phase_3_0_trustgate_sovereign_ai_control_rebuild_handoff.md
?? docs/deployment_runbook.md
?? docs/public_claims_ledger.md
?? docs/publication_checklist.md
?? docs/restrictions.md
?? docs/review_notes.md
?? docs/site_content_model.md
?? docs/translation_glossary.md
?? index.html
?? procurement/index.html
?? pt/ai-control/index.html
?? pt/index.html
?? pt/procurement/index.html
?? scripts/validate_public_surface.py
?? styles.css
```

`ls docs/codex_runs`:

```text
20260608_phase_2_1_hub_public_language_qa_handoff.md
20260608_phase_2_2_homepage_public_language_correction_handoff.md
20260608_phase_2_3_footer_label_cleanup_handoff.md
20260608_phase_2_4_track_navigation_isolation_handoff.md
20260608_phase_2_5_ai_control_sentence_removal_handoff.md
20260608_phase_2_6_procurement_buyer_language_translation_handoff.md
20260609_phase_2_7_portuguese_localization_handoff.md
20260627_phase_3_0_trustgate_sovereign_ai_control_rebuild_handoff.md
```

Media guard:

```text
PASS - exit 0, no output.
```

## Known Issues

- No Phase 3.0 validation issues known.
- The broader worktree remains unstaged and mostly untracked from earlier local phases.
- Browser visual preview was not run through an in-app browser tool because no direct Browser navigation tool was exposed in this thread. Manual preview command is provided below.

## Next Recommended Step

- Manually preview `/ai-control/` and `/pt/ai-control/` at desktop, tablet, and mobile widths, with special attention to SVG readability, Portuguese wording, and claims-boundary clarity.

## Confirmation

- No commit.
- No tag.
- No push.
