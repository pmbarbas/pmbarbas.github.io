# Phase 2.1 - Hub Public-Language and QA Pass

## Prompt Summary

- Keep the two-track architecture: `/`, `/procurement/`, and `/ai-control/`.
- Make the homepage a balanced public hub with two equal route cards.
- Remove internal public-facing wording from the homepage and public HTML.
- Use "Ireland & Portugal" on the homepage procurement card.
- Preserve `/procurement/` Ireland first / Portugal next positioning.
- Preserve `/ai-control/` structure and content except tiny QA fixes.
- Confirm Boundaries and Contact navigation/anchors on all three pages.
- Update validation and local run memory.

## Files Added

- `docs/codex_runs/20260608_phase_2_1_hub_public_language_qa_handoff.md`

## Files Modified

- `README.md`
- `index.html`
- `procurement/index.html`
- `ai-control/index.html`
- `styles.css`
- `docs/site_content_model.md`
- `docs/public_claims_ledger.md`
- `docs/review_notes.md`
- `docs/publication_checklist.md`
- `docs/restrictions.md`
- `scripts/validate_public_surface.py`

## Validation Commands Run

- `python3 scripts/validate_public_surface.py`
- `git diff --check`
- `git status --short`
- `ls docs/codex_runs`
- Browser QA via local `python3 -m http.server 8080 --bind 127.0.0.1` preview at desktop `1280x900` and mobile `390x844`.

## Validation Results

`python3 scripts/validate_public_surface.py`:

```text
Public surface validation: PASS
Required files checked: 13
HTML pages checked: 3
Route, SEO, Boundaries, Contact, nav, safety, claim, SVG, and local link checks passed.
```

`git diff --check`:

```text
PASS - exit 0, no output.
```

`git status --short`:

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
```

Browser QA:

```text
PASS - desktop homepage route cards rendered at equal width and height; mobile cards stacked without horizontal overflow; visible nav labels were present on all three pages; Boundaries and Contact sections were present; SVG assets loaded; no console warnings or errors observed.
```

## Known Issues

- None known at draft handoff time.

## Next Recommended Step

- Run the final quality gates, then preview `/`, `/procurement/`, and `/ai-control/` locally at desktop and mobile widths before publication review.

## Confirmation

- No commit.
- No tag.
- No push.
