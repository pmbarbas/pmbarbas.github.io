# Public Surface Phase 3.1 Discovery and Claims Map

## Baseline

- Repository: `/Users/pbarbas/Documents/GitHub/pedro-public-surface`
- Branch observed: `main` (the brief expected `master`)
- HEAD: `092317a5029a5a14c62a8f6864c5441993c57517`
- Worktree at preflight: clean; no staged, modified, or untracked paths
- Existing evidence: Phase 3.0 and Phase 3.0R1 handoffs are present under `docs/codex_runs/`

## Claims Map

| Current section | Current claim | Action | Replacement public claim | Reason | Disclosure tier | EN/PT parity | Validator rule |
| --- | --- | --- | --- | --- | --- | --- | --- |
| AI Control title, metadata, H1, hero visual | TrustGate is "the execution firewall for agentic AI" | Remove / revise | TrustGate is the action-clearance and proof layer for consequential agentic AI | Retire an unqualified enforcement metaphor and state the accepted public principle | Public principle | Exact EN and approved pt-PT H1 plus aligned metadata | Require new H1/metadata; reject visible `execution firewall` |
| Hero body | TrustGate checks authority, scope, route, evidence, and proof before execution is trusted | Revise | TrustGate evaluates one exact action, binds the decision into a clearance receipt, and gives a protected target evidence to verify clearance before accepting a change | Make the protected-clearance principle explicit without exposing mechanics | Public principle | Semantically equivalent approved copy | Require exact supporting copy and governance distinction |
| Hero diagram | Request -> checks -> TrustGate -> clear/hold -> proof | Revise | Proposed action -> TrustGate clearance -> bound receipt -> protected-target verification -> accept/reject before state change -> outcome proof | A decision alone is not execution authority | Public principle | Equivalent labels and boundaries | Require diagram labels, public principle, and bounded-reference disclaimer |
| Missing layer | Deployment, platform, and execution-firewall questions | Revise | Deployment governance, platform governance, TrustGate action clearance, and protected-target verification | Separate deployment/platform governance from exact action authority and target verification | Public principle | Four matched cards | Require all four questions in EN/PT |
| Airport analogy | A governed airport does not mean every flight may take off | Revise | A cleared flight still needs clearance verified before entering the protected runway | Explain the verification boundary without claiming a real runway interlock | Public principle | Matched analogy | Require approved sentence in EN/PT |
| Principal -> Control -> Proof | Principal, Action, Context, Route, Admission, Telemetry, Proof, Held Gate | Revise | Principal, Purpose, Action, Target, Route, Evidence, Impact, Policy, Clearance, Receipt, Target Verification, Outcome Proof | Replace telemetry and internal-contract implications with a high-level public model | Public principle | Matched chip vocabulary | Require all chips; reject standalone Telemetry/Telemetria |
| Enterprise stack | watsonx Orchestrate proposes against Db2; Manta context; TrustGate sits between intent and execution | Revise | Orchestration proposes; context informs clearance; TrustGate issues clearance and receipt; protected target verifies; outcome evidence is reviewable | Remove direct-write implication while preserving the concrete IBM illustration | Public principle with boundary | EN/PT sequence and exact disclaimer | Require IBM illustration, alternatives, verification boundary, and no-integration disclaimer |
| Working-example SVG | TrustGate arrows directly to Db2 target and clear/hold proof | Revise | TrustGate clearance and receipt -> protected-target verification -> illustrative Db2-side outcome | Avoid implying direct TrustGate writes or live target enforcement | Public principle with boundary | One language-neutral public-safe SVG | Scan SVG for retired claim and verify required public-safe labels |
| Protected-target principle | Not a focused section | Add | The decision is verified where the change would occur; invalid, altered, reused, or stale clearance is rejected before the bounded reference target changes | State the category-defining principle with a local-reference boundary | Public principle | Approved EN/PT body and equally strong disclaimer | Require heading, body markers, and exact bounded-reference boundary |
| TG360 | Buyer-facing cockpit for known/bounded/synthetic/not-activated/proof signals | Revise | TG360 displays the accepted local evidence chain from action clearance through receipt verification to protected-target outcome; it is not a second decision engine | Connect cockpit value to the accepted control chain without exposing identifiers or schemas | Public principle / private walkthrough | Matched EN/PT statement and signal set | Require exact statement and bounded signal labels |
| Why adopt | Includes "Audit-ready evidence posture" | Revise | Review-ready evidence posture; add protected-target assurance and operational-resilience evidence | Avoid implying audit sufficiency and add accepted buyer value | Public principle | Matched eight-card set | Require review-ready wording; reject audit-ready |
| DORA relevance | General ledger note only; no concise public section | Add | TrustGate supports DORA-oriented control evidence and does not independently determine regulatory compliance | Make buyer relevance visible without a compliance claim | Public principle with regulatory disclaimer | Five matched cards and exact disclaimers | Require heading/cards/disclaimer; reject DORA compliant/certified |
| Data protection | Evidra/DPO references only | Add compact panel | TrustGate can support evidence for data-protection review but does not replace DPIA, lawful-basis, records, DPO judgment, or legal determination | Add accountability relevance while preserving human/legal authority | Public principle with legal boundary | Matched points and exact boundary | Require heading and exact EN/PT boundary; reject GDPR compliance |
| Private walkthrough | Executive/technical masterclasses, TG360, stack, claims boundary | Revise | Add action-clearance context, receipt/outcome evidence, protected-target principle, synthetic accept/reject scenarios, DORA mapping, data-protection lens, architecture roles, and claims review | Keep richer proof in controlled review | Private walkthrough | Matched content and persona sets | Require walkthrough CTA and selected scope markers |
| Controlled disclosure | Source, proof internals, dashboards, source maps, implementation stay private | Retain / strengthen | Add private contracts, schemas, target-verification, provenance, receipt-consumption, topology, and customer-integration details to withheld categories | Preserve the existing disclosure doctrine | Private walkthrough / NDA private | Same boundary strength | Reject internal names and implementation terms from visible public pages |
| Root AI Control card | Execution-time action governance for agentic AI | Minimal revise | Action clearance and proof for consequential agentic AI | Align routing language with the new category claim | Public principle | Approved EN/PT line | Require root-card consistency |

## Explicit Discovery Findings

## Phase 3.1R1 Audit Closure

- The hero and focused protected-target principles in both languages now repeat one complete boundary covering production enforcement, customer deployment, cross-process security guarantees, and enterprise-wide non-bypassability.
- TG360 now states in EN/PT whether the bounded reference target changed or remained unchanged after an accepted or rejected action.
- Visible Portuguese `walkthrough` wording was replaced by the canonical `sessão privada` terminology, including CTA labels and email subjects.
- Validator guards now inspect raw HTML/SVG source, comments, metadata, accessibility attributes, all-route scripts/events/headings/images/links, exact Open Graph contracts, and runtime/network/storage markers.
- Fourteen in-memory malformed fixtures prove the new guard paths reject the audited failure cases without writing fixtures into public routes.
- No public disclosure tier, vendor positioning, DORA scope, data-protection scope, or route architecture changed.

### Execution firewall

- English visible and metadata occurrences: page title, description, Open Graph title, H1, hero image alt, hero figcaption, missing-layer card, illustrative flow, and the hero SVG title/text.
- Portuguese visible and metadata occurrences: description, H1, hero figcaption, missing-layer card, and illustrative flow. The shared hero SVG also exposes the English term.
- Documentation and validator occurrences exist in `docs/site_content_model.md`, `docs/public_claims_ledger.md`, `docs/review_notes.md`, `docs/publication_checklist.md`, `docs/translation_glossary.md`, and `scripts/validate_public_surface.py`.

### Telemetry

- `Telemetry` appears as a standalone English public control-chain chip.
- `Telemetria` appears as the Portuguese equivalent.
- Negative live-telemetry boundaries also appear in both claims sections; these remain legitimate negative statements but should not drive the public model.

### Direct-target implication

- The enterprise-stack text says a workflow may propose an action "against Db2" and that TrustGate sits between intent and execution.
- The public flow places `Db2 target + Manta lineage/context` before `TrustGate Sovereign execution firewall`.
- `assets/trustgate-sovereign-working-example.svg` draws TrustGate directly to a `Db2 target` and a `clear / hold` outcome, which can imply TrustGate writes directly to the target.

### Production, regulatory, audit, and integration language

- No affirmative production deployment or customer deployment claim was found.
- Existing negative boundaries disclaim production deployment/readiness, customer and production data, live telemetry, connector execution, compliance/regulatory/security certification, guaranteed compliance, customer traction, IBM endorsement, and live IBM-stack integration.
- `Audit-ready evidence posture` / `Postura de evidência pronta para auditoria` is visible and must be replaced with review-ready wording.
- DORA appears in the claims ledger and root persona context, but not as a bounded AI Control section.
- Vendor-specific disclaimers already identify watsonx Orchestrate, Manta, and Db2 as illustrative and deny live/certified/production/supported/endorsed/partner integration. Phase 3.0R1 also preserves LangGraph, Microsoft Copilot Studio, and Amazon Bedrock AgentCore as role examples only.

### Controlled-disclosure boundary

- Both AI Control pages contain a dedicated Boundaries/Limites section, a private walkthrough CTA, lists of privately demonstrable content, private implementation categories, and explicit non-claims.
- Existing related-systems and vendor-neutral sections are retained.
- No public occurrence of TGCB, TGOS, TGPE, TGAPI, CACSAC, private source paths, receipt-consumption registers, certifier registries, or canonical digest material was found in the inspected public pages and assets.
