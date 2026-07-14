# Phase 3.2 Cloudflare 404 Hardening Handoff

## Phase Name

Phase 3.2 - Cloudflare Pages 404 and Unknown-Route Hardening

## Prompt Summary

Add a concise, branded root `404.html`; preserve the six approved static routes; package only approved public files into `dist/`; harden validation for root-relative 404 dependencies and private-path exclusion; and document Cloudflare Pages build and post-deployment checks.

## Accepted Baseline

- Branch: `main`
- HEAD: `5ca78ce11b65bd0c5e551e32e30008578f161b19`
- Working tree and index were clean before implementation.

## Root Cause

Cloudflare Pages treats a static project without a top-level `404.html` as an SPA and may return the root homepage body for unknown paths. This site is a traditional static multi-page site. A root `404.html` is required so Cloudflare can return a branded not-found response instead of the homepage fallback.

## Files Added

- `404.html`
- `docs/codex_runs/20260714_phase_3_2_cloudflare_404_hardening_handoff.md`

## Files Modified

- `.gitignore`
- `README.md`
- `scripts/validate_public_surface.py`
- `docs/deployment_runbook.md`
- `docs/publication_checklist.md`

No approved content-page HTML, product copy, route structure, language switcher, or SVG asset was modified.

## Exact Cloudflare Build Command

```sh
set -eu; rm -rf dist; mkdir -p dist; cp index.html 404.html styles.css dist/; cp -R assets procurement ai-control pt dist/; test -f dist/index.html; test -f dist/404.html; test -f dist/styles.css; test -f dist/assets/favicon.svg; test -f dist/procurement/index.html; test -f dist/ai-control/index.html; test -f dist/pt/index.html; test -f dist/pt/procurement/index.html; test -f dist/pt/ai-control/index.html
```

## Validation Commands Run

```sh
python3 scripts/validate_public_surface.py
git diff --check
git status --short --untracked-files=all
tree -L 3 dist
```

The exact Cloudflare build command and all nine package file assertions were also run locally. The final validation result was PASS, `git diff --check` was clean, all six approved pages and `dist/404.html` existed, and `dist/` contained no `docs/`, `scripts/`, `README.md`, `.git/`, support record, or Codex handoff.

## Local Visual-Review Status

PASS. The packaged page was reviewed at `http://127.0.0.1:8081/404.html` on desktop and at a `390 x 844` mobile viewport. The title, noindex directive, stylesheet, favicon, brand mark, primary homepage CTA, and optional route links rendered correctly. There was no horizontal overflow. A fresh Chromium mobile screenshot is stored outside the repository at `/tmp/pedro-public-surface-phase-3-2-404-mobile.png`.

Python's basic HTTP server was used only for visual review. It does not reproduce Cloudflare's nearest-404 status-code behavior, so no local Cloudflare HTTP-status claim is made.

## Post-Deployment Verification Commands

Known routes must return HTTP 200:

```sh
curl -I https://pedro-public-surface.pages.dev/
curl -I https://pedro-public-surface.pages.dev/procurement/
curl -I https://pedro-public-surface.pages.dev/ai-control/
curl -I https://pedro-public-surface.pages.dev/pt/
```

Unknown and private-looking routes must return HTTP 404:

```sh
curl -I https://pedro-public-surface.pages.dev/docs/codex_runs/
curl -I https://pedro-public-surface.pages.dev/scripts/
curl -I https://pedro-public-surface.pages.dev/README.md
curl -I https://pedro-public-surface.pages.dev/definitely-not-a-page/
```

The 404 body must be the branded page, not the homepage. `docs/`, `scripts/`, `README.md`, `.git/`, support records, and Codex handoffs must remain inaccessible.

## Known Issues

- Production HTTP 404 behavior cannot be verified until Pedro commits and pushes the reviewed change and Cloudflare completes deployment.
- The in-app browser's mobile screenshot capture was distorted despite correct 390px DOM measurements. A separate fresh HeadlessChrome context produced the correct 390px render used for visual approval.

## Next Recommended Step

Pedro should review `404.html` and the local `dist/` package, commit and push when approved, wait for Cloudflare deployment, then run every documented 200/404 command and inspect an unknown nested route in a browser.

## Git And Cloudflare Confirmation

- No commit performed.
- No tag created.
- No push performed.
- No Cloudflare settings changed.
