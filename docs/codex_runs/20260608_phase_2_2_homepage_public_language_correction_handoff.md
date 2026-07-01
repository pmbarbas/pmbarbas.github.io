# Phase 2.2 - Homepage Public-Language Correction Pass

## Prompt Summary

- Correct root homepage public language only.
- Remove internal homepage shorthand and prior GTM phrases from `index.html`.
- Preserve balanced 50/50 homepage card treatment.
- Keep homepage procurement card language as "Ireland & Portugal."
- Keep `/procurement/` Ireland first / Portugal next positioning unchanged.
- Keep `/ai-control/` materially unchanged.
- Preserve Boundaries and Contact nav/anchors on all three pages.
- Strengthen validation for the Phase 2.2 homepage wording contract.

## Files Added

- `docs/codex_runs/20260608_phase_2_2_homepage_public_language_correction_handoff.md`

## Files Modified

- `index.html`
- `scripts/validate_public_surface.py`
- `docs/site_content_model.md`
- `docs/review_notes.md`
- `docs/publication_checklist.md`

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
Required files checked: 14
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
20260608_phase_2_2_homepage_public_language_correction_handoff.md
```

Browser QA:

```text
PASS - desktop homepage route cards measured at equal width and height: 582x701 each. Mobile cards stacked at equal width with no horizontal overflow. Nav count was 5, and Boundaries and Contact anchors were present.
```

## Known Issues

- None known at draft handoff time.

## Next Recommended Step

- Run final quality gates, then manually preview the homepage at desktop and mobile widths to confirm both route cards still feel balanced.

## Confirmation

- No commit.
- No tag.
- No push.
