# Phase 2.5 - AI Control Cross-Track Sentence Removal

## Prompt Summary

- Implement one locked local-only cleanup phase.
- Remove the exact public-facing AI Control sentence that reintroduced cross-track context:
  `This track is serious and available for technical governance conversations, with Deal Hunter kept as the dedicated procurement intelligence path for buyer conversations.`
- Do not replace the sentence.
- Do not materially rewrite the AI Control page.
- Preserve the AI Control hero, required section content, TrustGate, Certify, Evidra, FieldDelta, Boundaries, Contact, and isolated AI Control navigation.
- Do not modify `/procurement/` or root `index.html` unless validation requires it.
- Do not commit, tag, push, or publish.

## Files Added

- `docs/codex_runs/20260608_phase_2_5_ai_control_sentence_removal_handoff.md`

## Files Modified

- `ai-control/index.html`

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
20260608_phase_2_5_ai_control_sentence_removal_handoff.md
```

## Known Issues

- No Phase 2.5 issues known.
- The broader worktree remains unstaged and mostly untracked from earlier local phases.

## Next Recommended Step

- Manually preview `/ai-control/` to confirm the "Why this matters now" section reads cleanly after the single sentence removal.

## Confirmation

- No commit.
- No tag.
- No push.
