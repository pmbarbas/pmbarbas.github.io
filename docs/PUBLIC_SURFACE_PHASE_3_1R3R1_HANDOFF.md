# Public Surface Phase 3.1R3R1 Handoff

Status: `DELIVERED_PENDING_PEDRO_FINAL_VISUAL_REVIEW`

## Scope And Diagnosis

R3R1 closes deterministic bilingual SVG parity, Portuguese text fit, cache-safe asset identity, CTA print state, and fresh render evidence. The no-cache diagnosis found source and served bytes identical. Pedro's stale English output is consistent with browser/PDF cache reuse of materially changed legacy filenames, but cache provenance cannot be proven retroactively. See `docs/PUBLIC_SURFACE_PHASE_3_1R3R1_RENDER_DIAGNOSIS.md`.

## Cache-Safe Asset Migration

| Visual | Retired route asset | New EN asset | New PT asset |
| --- | --- | --- | --- |
| Hero/control | `trustgate-sovereign-execution-firewall*.svg` | `trustgate-action-clearance-chain-en-v2.svg` | `trustgate-action-clearance-chain-pt-v2.svg` |
| Enterprise | `trustgate-sovereign-working-example*.svg` | `trustgate-enterprise-verification-chain-en-v2.svg` | `trustgate-enterprise-verification-chain-pt-v2.svg` |
| TG360 | `tg360-evidence-cockpit*.svg` | `tg360-evidence-cockpit-en-v2.svg` | `tg360-evidence-cockpit-pt-v2.svg` |

Legacy assets remain present but are unreferenced. The validator rejects any legacy AI Control visual reference.

Fresh-server source/served SHA-256 values matched exactly:

- Hero EN: `81b22793f8f9f6c65ceb1e9b2bd2fad9782a5f3fc80e9f934d45fd47cbacb003`
- Hero PT: `b60d22f00707ba3dc39be624aa0251b31927867377e44c2ac08c5a1a032ebb69`
- Enterprise EN: `1d83f6d30a15b1c315943f57b15461dc6144ca3e34417db593b4c5e294de4250`
- Enterprise PT: `98a1f4f639adeb9436c0dc2025f3107737a482c6d3d0255351b1b71fc41c2390`
- TG360 EN: `183f6812b2613ec913f4f6bbdfa6510c1a3d25b2ec8bc95f7e777fbd4caf1653`
- TG360 PT: `b3562c2da9aadc3ab6961102575b0826230d5e8e08052ae7a615a03241096348`

## Structural Parity

| EN asset | PT asset | Same viewBox | Same IDs | Same geometry | Same connectors | Same order | Localization only |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `trustgate-action-clearance-chain-en-v2.svg` | `trustgate-action-clearance-chain-pt-v2.svg` | yes | yes | yes | yes | yes | yes |
| `trustgate-enterprise-verification-chain-en-v2.svg` | `trustgate-enterprise-verification-chain-pt-v2.svg` | yes | yes | yes | yes | yes | yes |
| `tg360-evidence-cockpit-en-v2.svg` | `tg360-evidence-cockpit-pt-v2.svg` | yes | yes | yes | yes | yes | yes |

The validator compares `viewBox`, node rectangles, connector order/routes, structural IDs, and semantic role sequence. Enterprise flow is inputs/context -> clearance and bound receipt -> protected-target verification -> target-side outcome -> reviewable evidence. No direct clearance-to-outcome connector exists.

## Browser Text-Bounding Audit

Every owned label group uses `data-label-for`, `data-role`, and a deterministic owner rect with `data-node-id`. Direct SVG inspection through the in-app browser exposed browser-rendered client bounds; the read-only browser proxy did not expose `getBBox()`, so equivalent scaled `getBoundingClientRect()` comparisons were used against the SVG viewBox. Required padding was 18 horizontal and 14 vertical viewBox units.

- Hero EN: 13 groups, 0 failures
- Hero PT: 13 groups, 0 failures
- Enterprise EN: 12 groups, 0 failures
- Enterprise PT: 12 groups, 0 failures
- TG360 EN: 12 groups, 0 failures
- TG360 PT: 12 groups, 0 failures

Corrected Portuguese overflow risks: `watsonx Orchestrate`, `identidade e autoridade`, `TrustGate Sovereign`, and `Evidência do resultado passível de análise`. Each now has explicit lines and safe node padding.

## Side-By-Side Evidence

Temporary matched-dimension comparisons were inspected at:

- `/tmp/pedro-public-surface-phase-3-1r3r1/trustgate-action-clearance-chain-pair.png`
- `/tmp/pedro-public-surface-phase-3-1r3r1/trustgate-enterprise-verification-chain-pair.png`
- `/tmp/pedro-public-surface-phase-3-1r3r1/tg360-evidence-cockpit-pair.png`

All pairs have identical geometry, ordering, arrow routing, node count, and visual weight. No clipping, collisions, or unexpected whitespace were observed.

## CTA Result

The primary CTA has explicit white text, strong green background and border, opacity 1, preserved visited color, and explicit print styling. It has no disabled attribute or `aria-disabled="true"`. Wording, mailto payload, focus behavior, and target behavior are unchanged. The fresh PDFs render it visibly stronger than the secondary CTA.

## EN PDF Evidence
- Path: `/tmp/pedro-public-surface-phase-3-1r3r1/ai-control-en-a4-portrait-20260711T205817+0100.pdf`
- SHA-256: `aea4c786b36fcf15d19b8e267e3c01eebdcd286381f885f457e166a69dbafc5f`
- Generated: `2026-07-11T20:58:17+01:00`
- Engine: `HeadlessChrome 150.0.0.0 / Skia PDF m150`
- Page size: `A4 (594.96 x 841.92 pt)`
- Orientation: `portrait`
- Margins: `12 mm`
- Background graphics: `enabled by print rendering and exact-color contract`
- Headers/footers: `disabled`
- Page count: `14`

## PT PDF Evidence
- Path: `/tmp/pedro-public-surface-phase-3-1r3r1/ai-control-pt-a4-portrait-20260711T205817+0100.pdf`
- SHA-256: `60b9c6adf500765140098dcfc05c93dafff387d27791c9fc095b3280a931ecde`
- Generated: `2026-07-11T20:58:17+01:00`
- Engine: `HeadlessChrome 150.0.0.0 / Skia PDF m150`
- Page size: `A4 (594.96 x 841.92 pt)`
- Orientation: `portrait`
- Margins: `12 mm`
- Background graphics: `enabled by print rendering and exact-color contract`
- Headers/footers: `disabled`
- Page count: `14`

All 28 PDF pages were rendered to PNG and inspected. There are no nearly blank pages, stale diagrams, clipped nodes, label overflows, orphaned diagram disclaimers, hero-boundary splits, pale primary CTAs, or English operational labels in Portuguese diagrams.

## Contract Continuity

No product semantics, strategic positioning, DORA/privacy claim, disclosure tier, or public claim changed. No dependency or public runtime script was added.

## Git And Approval Status

No commit, tag, push, publish, deploy, or staging operation was performed. Pedro's final visual approval remains pending.

## R3R2 Dark-Panel Print Contrast Closure

R3R2 corrects inherited dark print foregrounds on three existing dark-panel surfaces without changing wording, layout, pagination, routes, SVGs, claims, or asset parity. The action-chain summary, decision-authority statement, and enterprise internal caption now use the existing `#edf4f7` light neutral on `#101419`, with opacity 1 and explicit print color adjustment.

Fresh browser computation for all six EN/PT affected elements:

- Screen foreground/background: `rgb(237, 244, 247)` / `rgb(16, 20, 25)`
- Print foreground/background: `rgb(237, 244, 247)` / `rgb(16, 20, 25)`
- Screen contrast ratio: `16.62:1`
- Print contrast ratio: `16.62:1`
- Opacity: `1`
- Print color adjustment: `exact`

R3R2 EN evidence:

- Path: `/tmp/pedro-public-surface-phase-3-1r3r2/ai-control-en-a4-portrait-20260711T211634+0100.pdf`
- SHA-256: `96719cffeff1e209b5f033bd017a4552d349e44584df34fa0516af1f80e0c24b`
- Generated: `2026-07-11T21:16:34+01:00`
- Engine: `HeadlessChrome 150.0.0.0 / Skia PDF m150`
- Settings: `A4 portrait, 12 mm margins, backgrounds enabled, headers/footers disabled`
- Page count: `14`

R3R2 PT evidence:

- Path: `/tmp/pedro-public-surface-phase-3-1r3r2/ai-control-pt-a4-portrait-20260711T211634+0100.pdf`
- SHA-256: `80fbe44e923104ac5e2cb697b9ce86129a09832c6e62e2357219dae811aeb0c2`
- Generated: `2026-07-11T21:16:34+01:00`
- Engine: `HeadlessChrome 150.0.0.0 / Skia PDF m150`
- Settings: `A4 portrait, 12 mm margins, backgrounds enabled, headers/footers disabled`
- Page count: `14`

All 28 pages were rendered to PNG. Pages 2 and 6 were inspected at full resolution in both languages; corrected text is clearly readable, limitation cards remain unchanged, the CTA remains active, and no new blank page or layout shift was introduced. No commit, tag, push, publish, deploy, or staging operation was performed. Pedro's final visual approval remains pending.
