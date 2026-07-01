# Phase 2.6 - Procurement Buyer-Language Translation Pass

## Prompt Summary

- Implement one locked local-only refinement phase focused only on procurement-facing language.
- Translate `/procurement/` copy from architecture-native vocabulary into buyer-native procurement, infrastructure, construction, market-intelligence, and pre-tender opportunity review language.
- Preserve the approved Deal Hunter strategy, exact tender hero line, Ireland first / Portugal next positioning, "What is not claimed", controlled disclosure, 30-minute walkthrough CTA, and stage/boundary honesty.
- Do not materially touch AI Control.
- Update validation so procurement-specific architecture terms are blocked only on `procurement/index.html`.
- Update repository memory docs for the procurement buyer-language rule.
- Do not commit, tag, push, publish, add visuals, add products, or add strategic claims.

## Files Added

- `docs/codex_runs/20260608_phase_2_6_procurement_buyer_language_translation_handoff.md`

## Files Modified

- `procurement/index.html`
- `index.html`
- `scripts/validate_public_surface.py`
- `docs/site_content_model.md`
- `docs/public_claims_ledger.md`
- `docs/review_notes.md`
- `docs/publication_checklist.md`

## Validation Commands Run

- `git status --short`
- `python3 scripts/validate_public_surface.py`
- `git diff --check`
- `git status --short`
- `ls docs/codex_runs`

## Validation Results

Initial `git status --short` before editing:

```text
 M README.md
?? .gitignore
?? ai-control/
?? assets/
?? docs/
?? index.html
?? procurement/
?? scripts/
?? styles.css
```

`python3 scripts/validate_public_surface.py`:

```text
Public surface validation: PASS
Required files checked: 14
HTML pages checked: 3
Route, SEO, persona-specific nav, procurement language, Boundaries, Contact, safety, claim, SVG, and local link checks passed.
```

`git diff --check`:

```text
PASS - exit 0, no output.
```

Final `git status --short`:

```text
 M README.md
?? .gitignore
?? ai-control/
?? assets/
?? docs/
?? index.html
?? procurement/
?? scripts/
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
```

## Known Issues

- No Phase 2.6 issues known.
- The broader worktree remains unstaged and mostly untracked from earlier local phases.
- The SVG file name `procurement-evidence-chain.svg` remains unchanged; validation intentionally checks public HTML language, not the asset filename.
- The embedded procurement SVG still contains legacy labels such as "Evidence chain"; this phase did not edit SVG assets, so it is recorded for manual review rather than blocking validation.

## Next Recommended Step

- Manually preview `/procurement/` as an infrastructure procurement buyer and confirm the page reads like market intelligence rather than software architecture.

## Confirmation

- No commit.
- No tag.
- No push.
