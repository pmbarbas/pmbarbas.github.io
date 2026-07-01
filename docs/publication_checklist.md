# Publication Checklist

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
- [ ] `/ai-control/` leads with TrustGate Sovereign as the execution firewall for agentic AI.
- [ ] `/ai-control/` explains the category gap between deployment governance, platform governance, and action clearance.
- [ ] `/ai-control/` includes Principal / Control / Proof, TG360, TGSG surfaces, and the illustrative enterprise-stack scenario.
- [ ] `/ai-control/` makes Certify, Evidra, and FieldDelta clearly secondary related systems.
- [ ] `/ai-control/` navigation is AI Control / Boundaries / Contact only.
- [ ] `/ai-control/` does not visibly link to Procurement or Home.
- [ ] `/ai-control/` does not imply IBM endorsement, live integration, live telemetry, connector execution, production deployment, customer data, production data, CP-7 authorization, ROI, or savings.
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
