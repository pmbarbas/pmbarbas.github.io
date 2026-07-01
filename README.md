# Pedro Public Surface

Private staging repo for Pedro Barbas' public evidence-first systems website.

This repository is a static public-surface website for a future public hosting target such as GitHub Pages, Cloudflare Pages, or Netlify. It is not a product repository and should not contain product source code, implementation internals, source maps, scoring logic, proof schemas, private strategy, customer data, confidential material, credentials, private screenshots, or source research files.

The public site is allowed to describe buyer pain, risk reduction, review value, and controlled private walkthroughs. It must not expose implementation recipes or imply production maturity, compliance, legal outcomes, customer traction, guaranteed prediction, or autonomous decisions.

The site is designed so selected public-safe files can later be copied into a clean public repository, for example `pedrobarbas/pedrobarbas.github.io`.

## Static Structure

- `/` - balanced two-track public hub.
- `/procurement/` - Deal Hunter / Procurement Intelligence track for Ireland-first, Portugal-next buyer conversations.
- `/ai-control/` - TrustGate Sovereign presence page for execution-time action governance and related evidence-first systems.
- `/pt/` - Portuguese (`pt-PT`) balanced public hub.
- `/pt/procurement/` - Portuguese (`pt-PT`) Deal Hunter / Procurement Intelligence track.
- `/pt/ai-control/` - Portuguese (`pt-PT`) TrustGate Sovereign presence page.

English is the default language. Portuguese pages live under `/pt/`. Language switching is static same-page linking only: no auto-detection, redirects, JavaScript, cookies, or local storage.

The root pages keep full hub navigation. Track pages use persona-specific navigation isolation: `/procurement/` and `/pt/procurement/` show Procurement, Boundaries/Limites, and Contact/Contacto only; `/ai-control/` and `/pt/ai-control/` show AI Control/Controlo IA, Boundaries/Limites, and Contact/Contacto only.

No build step is required. The site uses static HTML, shared CSS, local SVGs, Markdown documentation, and a Python standard-library validation script.

## Local Preview

Run:

```sh
python3 -m http.server 8080 --bind 127.0.0.1
```

Then open:

```text
http://localhost:8080
http://localhost:8080/procurement/
http://localhost:8080/ai-control/
http://localhost:8080/pt/
http://localhost:8080/pt/procurement/
http://localhost:8080/pt/ai-control/
```

The site has no package manager, backend, analytics, cookies, forms, external JavaScript, external CSS, CDN dependency, or external font dependency.

## Validation

Run:

```sh
python3 scripts/validate_public_surface.py
```

The validation script checks required files, the bilingual routing structure, static language switching, persona-specific track navigation, TrustGate Sovereign page requirements, public-safe asset boundaries, SVG hygiene, missing required docs, obvious secret files, committed PDFs, committed binary images, external JavaScript or CSS references, external font references, analytics keywords, form/cookie usage, unsupported English and Portuguese public claims, internal links, Boundaries/Limites anchors, and Contact/Contacto anchors.

## Publication Flow

1. Review `docs/public_claims_ledger.md`.
2. Complete `docs/publication_checklist.md`.
3. Run the validation script.
4. Preview all three pages locally.
5. Copy only public-safe files into a fresh public repository.
6. Publish from the clean public repository.

Do not simply flip this private staging repo to public if it has ever contained rejected drafts, private notes, PDFs, raw research exports, secrets, screenshots, product code, customer material, or other sensitive history.

## Publication Boundary

Files that may be copied for publication after review:

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

Files that do not belong in this repository:

- product source code
- PDFs or raw source research exports
- private screenshots
- source maps, scoring formulas, proof schemas, or country-source implementation recipes
- credentials, tokens, keys, or `.env` files
- customer data, names, logos, or testimonials
- IBM, client, or employer confidential material
- private go-to-market notes
