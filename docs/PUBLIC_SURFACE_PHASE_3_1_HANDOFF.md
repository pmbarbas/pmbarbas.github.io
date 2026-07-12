# Public Surface Phase 3.1 Handoff

> R3R1 render closure: AI Control visuals now use versioned, structurally isomorphic EN/PT SVG pairs with browser-verified text fit. Fresh inspected A4 portrait PDFs are 14 pages for EN and 14 for PT. See `docs/PUBLIC_SURFACE_PHASE_3_1R3R1_HANDOFF.md`.

## Executive Result

`DELIVERED_PENDING_PEDRO_REVIEW`

Phase 3.1 rebases the bilingual TrustGate Sovereign public surface around exact-action clearance, a bound receipt, protected-target verification, reviewable outcome evidence, DORA-oriented control evidence, and data-protection accountability. The public principle is explicit while implementation mechanics remain private.

Phase 3.1R1 closes the final read-only audit findings without changing the public disclosure tier: both protected-target principles now carry the complete four-part boundary, TG360 explicitly reports whether the bounded reference target changed, Portuguese public copy uses `sessão privada`, and validator coverage now includes raw source, accessibility surfaces, exact Open Graph metadata, all six routes, and runtime/network/storage mechanisms.

Phase 3.1R2 closes the entity-encoding disclosure bypass identified during final validation review. Internal disclosure checks now cover literal source, bounded repeated HTML-entity decoding, Unicode-normalized values, HTML parser-decoded text/comments/metadata/accessibility/data attributes, and parsed SVG text/descriptions/attributes. No public HTML, SVG, CSS, metadata, route, translation, or visual content changed in R2.

Phase 3.1R3 aligns the visible diagrams and print output with the accepted narrative. The hero/control chain now exposes action context, clearance, receipt, separate protected-target verification, target-side accept/reject, and proof; Portuguese routes use dedicated localized hero, enterprise, and TG360 SVGs; enterprise connectors structurally enforce clearance -> verification -> outcome with no direct bypass; CTA contrast/focus are strengthened; and bounded print rules produce coherent EN/PT A4 output. No public claim or disclosure tier changed.

## Baseline

- Repository: `/Users/pbarbas/Documents/GitHub/pedro-public-surface`
- Branch observed at preflight: `main` (brief expected `master`)
- HEAD at preflight: `092317a5029a5a14c62a8f6864c5441993c57517`
- Worktree at preflight: clean
- Staged paths at preflight: none
- Existing Phase 3.0 and Phase 3.0R1 evidence: present under `docs/codex_runs/`

## Files Changed

Created:

- `docs/PUBLIC_SURFACE_PHASE_3_1_DISCOVERY_AND_CLAIMS_MAP.md`
- `docs/PUBLIC_SURFACE_PHASE_3_1_HANDOFF.md`

Modified:

- `ai-control/index.html`
- `pt/ai-control/index.html`
- `index.html`
- `pt/index.html`
- `styles.css`
- `assets/trustgate-sovereign-execution-firewall.svg`
- `assets/trustgate-sovereign-working-example.svg`
- `scripts/validate_public_surface.py`
- `README.md`
- `docs/site_content_model.md`
- `docs/public_claims_ledger.md`
- `docs/review_notes.md`
- `docs/publication_checklist.md`
- `docs/restrictions.md`
- `docs/translation_glossary.md`
- `docs/deployment_runbook.md`

Removed: none.

## Positioning Rebase

Old primary positioning:

- EN: `The execution firewall for agentic AI.`
- PT: `O firewall de execução para IA agêntica.`

New primary positioning:

- EN: `The action-clearance and proof layer for consequential agentic AI.`
- PT: `A camada de autorização da ação e prova para IA agêntica empresarial.`

Root route cards and AI Control metadata are aligned with the new category wording.

## Public Principle Disclosed

The page now states that TrustGate evaluates one exact consequential action, binds the decision into a clearance receipt, and enables a protected target to verify clearance before accepting a change. It distinguishes deployment governance, platform governance, action clearance, and protected-target verification. It also states that a decision alone is not execution authority.

The current rejection behavior is expressly bounded to a local reference demonstration. No production enforcement, customer deployment, cross-process security guarantee, or enterprise-wide non-bypassability is claimed.

## Implementation Detail Intentionally Withheld

Private contracts, receipt schemas, provenance and reuse mechanics, target-verification implementation, target synchronization, adapter contracts, evaluation ordering, reason catalogues, registries, deployment topology, credentials, and source code remain outside the public surface. Private walkthrough language stays at evidence-pattern and architectural-role level.

## TG360 Narrative

TG360 remains the buyer-facing evidence cockpit. It displays the bounded local chain from action clearance through receipt verification to the protected-target outcome, including whether the bounded reference target changed or remained unchanged, and does not become a second decision engine. Internal identifiers, reason codes, artifact names, full digests, and private request/response contracts remain private.

## DORA Relevance Boundary

The EN/PT pages include five DORA-relevant operational-resilience evidence questions. The exact boundary states that TrustGate supports DORA-oriented control evidence and does not independently determine regulatory compliance. No DORA compliance, certification, complete coverage, regulatory approval, supervisory acceptance, or programme-completion claim is made.

## Data-Protection Boundary

The compact EN/PT accountability lens covers purpose, authority, data/source context, target and route, residency/sovereignty constraints, and impact/outcome evidence. It states that TrustGate does not replace DPIA/AIPD, lawful-basis assessment, records of processing, DPO/EPD judgement, or legal determination. No GDPR compliance claim is made.

## EN/PT Parity

Both pages carry equivalent section structure, product principle, protected-target boundary, TG360 statement, vendor-neutral illustrative-stack doctrine, DORA disclaimer, data-protection disclaimer, buyer-value cards, walkthrough scope, and controlled-disclosure boundary. Portuguese uses the canonical pt-PT terminology recorded in `docs/translation_glossary.md`.

Visible Portuguese private-review terminology now uses `sessão privada`; no visible `walkthrough` remains on the Portuguese AI Control route.

## Validation Results

- `python3 scripts/validate_public_surface.py`: PASS
- `python3 -m py_compile scripts/validate_public_surface.py`: PASS
- `git diff --check`: PASS
- Targeted prohibited-claim scan: only required negative boundary matches; manually reviewed
- Internal-disclosure scan: no public disclosure matches
- Network/external-runtime scan: only local SVG namespace declarations matched; no external runtime dependency
- Media/font guard: no raster, media, subtitle, or font files found
- Validator regression probes: PASS for hidden internal terms, OG drift, scripts, event handlers, runtime APIs, storage, missing alt text, duplicate H1, Portuguese terminology, TG360 signal, complete boundary, and DORA overclaim
- Entity-decoded disclosure probes: PASS for decimal, hexadecimal, mixed literal/encoded, mixed-case, and double-encoded internal terms; encoded local paths; HTML attributes, metadata, hidden text, comments; and SVG title/description surfaces
- Safe-content probes: PASS for public clearance/receipt language and explicit negative production-enforcement wording
- Exact metadata contracts: PASS for title, description, Open Graph title, and Open Graph description on all six routes
- All-route integrity: PASS for scripts, event handlers, headings, image alternatives, links, raw disclosure, and local-path guards

## Visual Review Status

Implementation QA was performed through the local static preview at 1440 x 900 and 390 x 844 for both EN and PT AI Control pages. SVGs loaded, headings were present, and no horizontal overflow was detected. This is not Pedro's visual approval. Pedro must still review EN/PT desktop, mobile, and print/PDF output before publication.

## Change-Control Confirmation

No file was staged. No commit, tag, push, publish, or deploy was performed.

## Open Risks

- The active branch is `main`, while the brief named `master` as expected; no branch change was authorized or performed.
- The page is intentionally denser after adding protected-target, DORA, and data-protection content; Pedro should assess executive scan speed and print pagination.
- The protected-target principle must remain paired with its bounded local-reference disclaimer in future edits.
- R2 provides bounded protection for literal, up-to-three-pass HTML-entity-decoded, Unicode-normalized, and parser-decoded public-source surfaces. It does not claim resistance to every Unicode confusable or arbitrary obfuscation technique.

## Recommended Next Step

Pedro should review rendered EN/PT desktop, mobile, and print/PDF views, with particular attention to the hero claim, protected-target principle, DORA and data-protection disclaimers, illustrative-stack boundary, controlled-disclosure section, CTA, and root route cards. Keep all work uncommitted until that review is complete.

R3 render evidence: EN/PT desktop and mobile passed without overflow; A4 portrait produced 14 pages per language and is recommended; A4 landscape produced 18 pages per language and remained coherent but more fragmented. Pedro final visual approval remains required.
