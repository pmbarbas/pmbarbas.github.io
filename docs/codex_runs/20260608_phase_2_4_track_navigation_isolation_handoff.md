# Phase 2.4 - Track-Specific Navigation Isolation

## Prompt Summary

- Implement one locked local-only refinement phase.
- Keep root `/` as the full public hub with Home, Procurement, AI Control, Boundaries, and Contact navigation.
- Isolate `/procurement/` navigation and footer to Procurement, Boundaries, and Contact only.
- Isolate `/ai-control/` navigation and footer to AI Control, Boundaries, and Contact only.
- Remove visible cross-track and Home navigation from the track pages.
- Remove cross-track CTA links from the track pages.
- Preserve approved body content, Boundaries, Contact, validation safety checks, and the three-page structure.
- Update validation and relevant docs for track-specific navigation isolation.
- Do not commit, tag, push, publish, restructure, add products, add claims, or add visuals.

## Files Added

- `docs/codex_runs/20260608_phase_2_4_track_navigation_isolation_handoff.md`

## Files Modified

- `index.html`
- `procurement/index.html`
- `ai-control/index.html`
- `scripts/validate_public_surface.py`
- `README.md`
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
Route, SEO, persona-specific nav, Boundaries, Contact, safety, claim, SVG, and local link checks passed.
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
```

## Known Issues

- No Phase 2.4 issues known.
- The broader worktree remains unstaged and mostly untracked from earlier local phases.

## Next Recommended Step

- Manually preview the root and both track pages on desktop and mobile, then review the isolated navigation before any commit or publication decision.

## Confirmation

- No commit.
- No tag.
- No push.
