# Phase 2.3 - Footer and Public Label Cleanup

## Prompt Summary

- Implement one locked local-only polish phase.
- Standardize public footer and navigation label language to `Boundaries`.
- Remove the internal homepage section label `PUBLIC HUB` from root `index.html`.
- Do not restructure the site or change approved three-page structure.
- Do not rewrite `/procurement/` or `/ai-control/`.
- Preserve approved content direction, Boundaries section, Contact section, route cards, and validation posture.
- Update validation only as needed to enforce the public label cleanup.
- Do not commit, tag, push, publish, or expand scope.

## Files Added

- `docs/codex_runs/20260608_phase_2_3_footer_label_cleanup_handoff.md`

## Files Modified

- `index.html`
- `scripts/validate_public_surface.py`

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
Route, SEO, Boundaries, Contact, nav, safety, claim, SVG, and local link checks passed.
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
```

## Known Issues

- No Phase 2.3 issues known.
- The broader worktree remains unstaged and mostly untracked from earlier local phases.

## Next Recommended Step

- Manually preview the three local pages, then review the tiny text cleanup before any commit or publication decision.

## Confirmation

- No commit.
- No tag.
- No push.
