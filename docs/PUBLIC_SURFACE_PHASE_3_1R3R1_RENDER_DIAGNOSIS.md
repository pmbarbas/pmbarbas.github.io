# Public Surface Phase 3.1R3R1 Render Diagnosis

## Baseline

- Repository: `/Users/pbarbas/Documents/GitHub/pedro-public-surface`
- Branch: `main`
- HEAD: `092317a5029a5a14c62a8f6864c5441993c57517`
- Staged paths: none
- Diagnosis server: `http://127.0.0.1:8087/`
- Requests used `Cache-Control: no-cache, no-store, must-revalidate` and `Pragma: no-cache`.

## Source And Served Identity

| Route | Asset | Source SHA-256 | Served SHA-256 |
| --- | --- | --- | --- |
| EN hero/control | `assets/trustgate-sovereign-execution-firewall.svg` | `11479fe768548739989ed6dd25744be4861d23e33730e319ee5bb34b429b70df` | same |
| PT hero/control | `assets/trustgate-sovereign-execution-firewall-pt.svg` | `adae6b273087237fe713d28328d47b812da29a7c1037e00069e0e46cbeed9f3b` | same |
| EN enterprise | `assets/trustgate-sovereign-working-example.svg` | `6bbaa121978bdae6a17dc89a874466c3c9b2a9a0efd407de214c79046a68ce8f` | same |
| PT enterprise | `assets/trustgate-sovereign-working-example-pt.svg` | `3d0af2be119df990871f4cdd5a3049a2ff4d24597db953f95cbafc833e1bfc8e` | same |
| EN TG360 | `assets/tg360-evidence-cockpit.svg` | `891351d4b4d79e3119bb683e8486603338d8133cff35e69bf84092321b0ec526` | same |
| PT TG360 | `assets/tg360-evidence-cockpit-pt.svg` | `ea585541197b1c063fe1730fac473512428087b9e43d7be42f7bc765fae0ee22` | same |

The fresh server served repository bytes exactly. There is no source-versus-server divergence.

## Browser Rendering

The fresh browser loaded these exact URLs:

- `http://127.0.0.1:8087/assets/trustgate-sovereign-execution-firewall.svg`
- `http://127.0.0.1:8087/assets/trustgate-sovereign-working-example.svg`
- `http://127.0.0.1:8087/assets/tg360-evidence-cockpit.svg`
- `http://127.0.0.1:8087/assets/trustgate-sovereign-execution-firewall-pt.svg`
- `http://127.0.0.1:8087/assets/trustgate-sovereign-working-example-pt.svg`
- `http://127.0.0.1:8087/assets/tg360-evidence-cockpit-pt.svg`

All images completed with non-zero natural dimensions. Browser cache provenance for Pedro's attached PDFs is not observable retroactively. The stale English result is consistent with cache reuse because materially changed English visuals retained legacy filenames. R3R1 will use new deterministic paired filenames instead of query-string cache busting.

## SVG Metadata And Structural Diagnosis

All six assets use `viewBox="0 0 620 360"`. Each has localized `<title>` and `<desc>`. The hero pair shares principal IDs, but the PT verification node is 132 units high while EN is 124. The enterprise pair differs in verification, outcome, and evidence node heights. TG360 geometry is visually similar but lacks deterministic node/text ownership markers needed for structural proof.

The enterprise IDs are `orchestration-input`, `lineage-context`, `identity-authority-context`, `trustgate-clearance`, `protected-target-verification`, `target-outcome`, and `outcome-evidence`. The current PT enterprise asset has objectively crowded text in compact nodes, especially vendor, identity/authority, TrustGate, and outcome-evidence labels.

## Finding

R3 source-level semantics are present, but the assets are not one deterministic bilingual geometry system. New cache-safe EN/PT pairs, explicit text ownership, browser `getBBox()` auditing, and fresh PDF evidence are required. No product claim, disclosure tier, DORA statement, privacy statement, or positioning change is required.
