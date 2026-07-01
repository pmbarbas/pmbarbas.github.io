# Deployment Runbook

This runbook describes a public-safe publication flow for the static site.

## Scope

The deployable surface is static:

- `index.html`
- `procurement/index.html`
- `ai-control/index.html`
- `pt/index.html`
- `pt/procurement/index.html`
- `pt/ai-control/index.html`
- `styles.css`
- `assets/`
- `docs/`
- `README.md`

No build step, backend, package manager, analytics, forms, cookies, redirects, language-detection script, external JavaScript, external CSS, external fonts, or binary images are required. Visual assets are local SVGs only.

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
```

Review desktop and mobile widths. Check focus states, contrast, links, SVG readability, and wording.

Manual review focus:

- `/` and `/pt/`: in 10 seconds, both tracks should be clear and balanced.
- `/procurement/`: the page should feel Ireland-first, buyer-native, and Deal Hunter-only.
- `/pt/procurement/`: the page should feel Portugal-native, buyer-native, and Deal Hunter-only.
- `/procurement/`: "What is not claimed" must appear mid-page, not only in the footer.
- `/ai-control/` and `/pt/ai-control/`: TrustGate must lead, and Certify must read as the local technical proof slice.
- all pages: Boundaries/Limites and Contact/Contacto navigation must work.
- all pages: EN/PT switchers must map only to equivalent pages.

## Publication Flow

1. Complete `docs/publication_checklist.md`.
2. Review `docs/public_claims_ledger.md`.
3. Confirm no private files or unsupported claims are present.
4. Create a fresh public repository, such as `pedrobarbas/pedrobarbas.github.io`.
5. Copy only reviewed public-safe files into the fresh public repository.
6. Enable the chosen static host.
7. Re-run the validator in the public repository.
8. Open the deployed URLs and check all six pages, EN/PT switchers, contact links, LinkedIn links, SVG assets, and claims ledger link.

## Rollback

Because this is a static site, rollback should be performed by reverting the public repository to the previous reviewed public-safe revision and redeploying from the static host.

## Boundary

Do not publish this private staging repository directly if it has ever contained sensitive history. Use a fresh public repository for publication.
