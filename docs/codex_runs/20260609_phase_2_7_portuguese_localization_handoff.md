# Phase 2.7 - Portuguese Localization and Static Language Switcher

## Prompt Summary

- Implement one locked local-only refinement phase.
- Add Portuguese (`pt-PT`) static pages under `/pt/` while keeping English as the default language.
- Add static EN/PT language switchers to all six pages with no JavaScript, cookies, local storage, redirects, or browser-language detection.
- Preserve English strategic copy except for language-switcher and `hreflang` metadata.
- Preserve track-specific navigation isolation in English and Portuguese.
- Keep product names untranslated.
- Add a translation glossary and update validation/docs for bilingual structure and Portuguese claim safety.
- Do not commit, tag, push, publish, add products, add strategic claims, or overclaim in Portuguese.

## Files Added

- `pt/index.html`
- `pt/procurement/index.html`
- `pt/ai-control/index.html`
- `docs/translation_glossary.md`
- `docs/codex_runs/20260609_phase_2_7_portuguese_localization_handoff.md`

## Files Modified

- `index.html`
- `procurement/index.html`
- `ai-control/index.html`
- `styles.css`
- `scripts/validate_public_surface.py`
- `README.md`
- `docs/site_content_model.md`
- `docs/public_claims_ledger.md`
- `docs/review_notes.md`
- `docs/publication_checklist.md`
- `docs/deployment_runbook.md`
- `docs/restrictions.md`

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
Required files checked: 18
HTML pages checked: 6
Bilingual route, SEO, language switcher, persona-specific nav, procurement language, Boundaries, Contact, safety, claim, SVG, and local link checks passed.
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
?? pt/
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
20260609_phase_2_7_portuguese_localization_handoff.md
```

## Known Issues

- No Phase 2.7 validation issues known.
- The broader worktree remains unstaged and mostly untracked from earlier local phases.
- Portuguese pages reuse the existing local SVG assets; the procurement SVG still contains legacy English labels inside the asset from the earlier review note.

## Next Recommended Step

- Manually preview all six pages, especially Portuguese mobile navigation and pt-PT wording with a Portugal-native reader if possible.

## Confirmation

- No commit.
- No tag.
- No push.
