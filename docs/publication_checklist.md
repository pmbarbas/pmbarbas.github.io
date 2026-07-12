# Publication Checklist

## Phase 3.1R3R1 Visual Evidence Gate

- [ ] Confirm both routes load only the versioned `*-en-v2.svg` / `*-pt-v2.svg` visual pairs.
- [ ] Compare the three EN/PT side-by-side renders for identical geometry and connector routing.
- [ ] Confirm every owned SVG label passes the documented browser bounds audit.
- [ ] Verify the exact PDF paths, SHA-256 values, timestamps, and 14/14 page counts in the R3R1 handoff.
- [ ] Confirm the primary CTA remains strong green with white text in screen and print output.
- [ ] Obtain Pedro's final visual approval before any commit or publication.

## Phase 3.1R3R2 Print Contrast Gate

- [ ] Confirm action-chain summaries use a light foreground on the dark panel in EN and PT.
- [ ] Confirm decision-authority statements use the same treatment and remain fully opaque.
- [ ] Confirm enterprise internal captions are readable while external disclaimer cards are unchanged.
- [ ] Verify computed screen and print contrast remains at least 4.5:1; measured R3R2 value is 16.62:1.
- [ ] Inspect pages 2 and 6 in both timestamped R3R2 PDFs.
- [ ] Confirm both R3R2 PDFs remain 14 pages and match the handoff hashes.

Use this checklist immediately before copying files into a fresh public repository or deploying to a static host.

- [ ] Repo contains only public-safe files.
- [ ] No draft private notes are present.
- [ ] No PDFs are present.
- [ ] No screenshots or raster images are present.
- [ ] No credentials, tokens, keys, `.env` files, or deployment secrets are present.
- [ ] No customer data, names, logos, testimonials, or unsupported traction claims are present.
- [ ] No source maps, scoring formulas, proof schemas, or implementation recipes are present.
- [ ] No product internals, protocol internals, or private dashboards are present.
- [ ] No unsupported claims are present.
- [ ] Claims ledger has been reviewed.
- [ ] Homepage can be reviewed in 10 seconds and both tracks are clear.
- [ ] Portuguese homepage can be reviewed in 10 seconds and both translated tracks are clear.
- [ ] Root homepage keeps full Home / Procurement / AI Control / Boundaries / Contact navigation.
- [ ] Portuguese root homepage keeps full Início / Procurement / Controlo IA / Limites / Contacto navigation.
- [ ] Root homepage contains no internal go-to-market shorthand.
- [ ] Homepage cards feel balanced / 50-50 in visual weight.
- [ ] Homepage procurement card says "Ireland & Portugal."
- [ ] EN/PT switcher works on all six pages and maps only to equivalent pages.
- [ ] Portuguese pages use European Portuguese (`pt-PT`) and no obvious Brazilian Portuguese terms.
- [ ] `/procurement/` feels Ireland-first and buyer-native.
- [ ] `/procurement/` reads like infrastructure market intelligence, not software architecture.
- [ ] `/procurement/` navigation is Procurement / Boundaries / Contact only.
- [ ] `/procurement/` does not visibly link to AI Control or Home.
- [ ] `/procurement/` includes the mid-page "What is not claimed" section.
- [ ] `/pt/procurement/` remains buyer-native and does not visibly link to Controlo IA or Início.
- [ ] `/ai-control/` leads with the approved action-clearance and proof-layer claim.
- [ ] `/ai-control/` explains the category gap between deployment governance, platform governance, and action clearance.
- [ ] `/ai-control/` includes Principal / Control / Proof, TG360, TGSG surfaces, and the illustrative enterprise-stack scenario.
- [ ] `/ai-control/` makes Certify, Evidra, and FieldDelta clearly secondary related systems.
- [ ] `/ai-control/` navigation is AI Control / Boundaries / Contact only.
- [ ] `/ai-control/` does not visibly link to Procurement or Home.
- [ ] `/ai-control/` does not imply IBM endorsement, live integration, live telemetry, connector execution, production deployment, customer data, production data, CP-7 authorization, ROI, or savings.
- [ ] EN desktop and PT desktop have been reviewed.
- [ ] EN mobile and PT mobile have been reviewed.
- [ ] EN/PT print or PDF output has been reviewed.
- [ ] EN hero SVG shows proposed action, action clearance, bound receipt, protected-target verification, target-side accept/reject, and outcome proof.
- [ ] PT hero SVG is fully localized and contains no English operational labels.
- [ ] EN enterprise SVG shows clearance -> verification -> target outcome with no direct bypass.
- [ ] PT enterprise SVG is localized and keeps the verification boundary distinct.
- [ ] PT TG360 SVG uses the approved Portuguese evidence-cockpit labels.
- [ ] Primary hero CTA appears active, readable, hoverable, and keyboard-focusable; secondary CTA remains secondary.
- [ ] AI Control SVGs remain legible and unclipped at 390 x 844.
- [ ] Print keeps each diagram with its immediate caption/disclaimer where avoidable.
- [ ] Final PDFs contain no nearly blank content page or orphan section heading.
- [ ] Final EN/PT A4 portrait PDFs have been reviewed by Pedro.
- [ ] Hero claim and root AI Control route card are aligned.
- [ ] Protected-target principle and bounded local-reference disclaimer are clear.
- [ ] The complete four-part boundary appears beside both protected-target principles in EN and PT.
- [ ] TG360 explicitly shows whether the bounded reference target changed or remained unchanged.
- [ ] Portuguese AI Control copy uses `sessão privada` and contains no visible `walkthrough`.
- [ ] Open Graph previews match the approved title and description contracts.
- [ ] Accessibility labels and alternatives contain no retired claim or private disclosure.
- [ ] Encoded internal-term validation passes for raw, entity-decoded, and parser-decoded public-source surfaces.
- [ ] Accessibility attributes, metadata, comments, and hidden text pass the decoded disclosure guard.
- [ ] SVG title, description, text, metadata, and descriptive attributes pass the decoded disclosure guard.
- [ ] DORA disclaimer and data-protection disclaimer are visible and equally strong in EN/PT.
- [ ] Illustrative-stack disclaimer, controlled-disclosure section, and private-walkthrough CTA are intact.
- [ ] `/pt/ai-control/` mirrors the TrustGate Sovereign meaning in pt-PT and does not visibly link to Procurement or Início.
- [ ] Portuguese AI Control copy does not claim compliance, legal effect, production maturity, or regulatory approval.
- [ ] Boundaries/Limites nav is visible and working on all six pages.
- [ ] Contact/Contacto nav is visible and working on all six pages.
- [ ] Controlled SVG visuals, including the three TrustGate Sovereign SVGs, have been checked for public-safe labels only.
- [ ] Email/contact links have been checked.
- [ ] LinkedIn link has been checked.
- [ ] Internal links have been checked across `/`, `/procurement/`, `/ai-control/`, `/pt/`, `/pt/procurement/`, and `/pt/ai-control/`.
- [ ] Local preview has been checked at desktop, tablet, and mobile widths.
- [ ] Validation script has passed.
- [ ] A fresh public repository is used for publication.
- [ ] The private staging repo is not simply flipped public if it has sensitive history.

Recommended pre-publication commands:

```sh
python3 scripts/validate_public_surface.py
python3 -m http.server 8080 --bind 127.0.0.1
```

Then open:

```text
http://localhost:8080
http://localhost:8080/procurement/
http://localhost:8080/ai-control/
```
