# Deployment Runbook

This runbook describes a public-safe publication flow for the static site.

## Scope

The deployable surface is static:

- `index.html`
- `404.html`
- `procurement/index.html`
- `ai-control/index.html`
- `pt/index.html`
- `pt/procurement/index.html`
- `pt/ai-control/index.html`
- `styles.css`
- `assets/`

No build step, backend, package manager, analytics, forms, cookies, redirects, language-detection script, external JavaScript, external CSS, external fonts, or binary images are required. Visual assets are local SVGs only.

## Cloudflare Pages Package

This is a traditional static multi-page site, not a single-page application. Cloudflare Pages treats a project without a top-level `404.html` as an SPA and may serve the root homepage for unknown paths. That fallback is a deployment defect for this site. A root `404.html` is mandatory so unknown routes receive the branded not-found response.

Only the generated `dist/` directory is published. Repository documentation, validation scripts, README files, support records, Git metadata, and Codex handoffs must never be copied into `dist/`.

Cloudflare Pages configuration remains:

- Production branch: `main`
- Root directory: repository root
- Build output directory: `dist`
- Deployment source: existing Git integration

Use this exact build command:

```sh
set -eu; rm -rf dist; mkdir -p dist; cp index.html 404.html styles.css dist/; cp -R assets procurement ai-control pt dist/; test -f dist/index.html; test -f dist/404.html; test -f dist/styles.css; test -f dist/assets/favicon.svg; test -f dist/procurement/index.html; test -f dist/ai-control/index.html; test -f dist/pt/index.html; test -f dist/pt/procurement/index.html; test -f dist/pt/ai-control/index.html
```

## Local Review

Run the validator:

```sh
python3 scripts/validate_public_surface.py
```

Preview locally:

```sh
python3 -m http.server 8080 --bind 127.0.0.1
```

Open:

```text
http://localhost:8080
http://localhost:8080/procurement/
http://localhost:8080/ai-control/
http://localhost:8080/pt/
http://localhost:8080/pt/procurement/
http://localhost:8080/pt/ai-control/
http://localhost:8080/404.html
```

Review desktop and mobile widths. Check focus states, contrast, links, SVG readability, and wording.

Manual review focus:

- `/` and `/pt/`: in 10 seconds, both tracks should be clear and balanced.
- `/procurement/`: the page should feel Ireland-first, buyer-native, and Deal Hunter-only.
- `/pt/procurement/`: the page should feel Portugal-native, buyer-native, and Deal Hunter-only.
- `/procurement/`: "What is not claimed" must appear mid-page, not only in the footer.
- `/ai-control/` and `/pt/ai-control/`: TrustGate must lead with action clearance, receipt evidence, and protected-target verification; Certify must remain a secondary local technical proof slice.
- `/ai-control/` and `/pt/ai-control/`: verify the DORA and data-protection disclaimers, illustrative-stack boundary, controlled-disclosure section, and root-card alignment.
- Review EN/PT desktop, mobile, and print/PDF output before approval.
- all pages: Boundaries/Limites and Contact/Contacto navigation must work.
- all pages: EN/PT switchers must map only to equivalent pages.

## Post-Deployment Verification

Known public routes must return HTTP 200:

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

The 404 response body must render the branded `404.html`, not the homepage. Nested unknown paths must retain styling through root-relative references. `docs/`, `scripts/`, `README.md`, `.git/`, support-request files, and Codex handoffs must never become directly accessible.

Python's basic HTTP server does not reproduce Cloudflare's nearest-404 routing behavior exactly. Use it to review `/404.html` visually, not to claim production 404 status-code behavior.

## Publication Flow

1. Complete `docs/publication_checklist.md`.
2. Review `docs/public_claims_ledger.md`.
3. Confirm no private files or unsupported claims are present.
4. Run the exact Cloudflare package command above.
5. Confirm `dist/` contains only approved public files.
6. Deploy through the existing Cloudflare Pages Git integration.
7. Run every post-deployment 200/404 check above.
8. Open the deployed URLs and check all six pages, the branded 404, EN/PT switchers, contact links, LinkedIn links, and SVG assets.

## Rollback

Because this is a static site, rollback should be performed by reverting to the previous reviewed public-safe revision and redeploying through the existing Cloudflare Pages integration.

## Boundary

Publish only `dist/`. Never configure Cloudflare Pages to publish the repository root.
