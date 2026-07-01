# Site Content Model

The site is a static bilingual public-safe surface for Pedro Barbas. English is the default language. Portuguese pages use European Portuguese (`pt-PT`) and live under `/pt/`. The root is a balanced two-track public hub: Deal Hunter and AI Control are both valid evidence-first tracks and are explored in parallel. The track pages use persona-specific navigation isolation so targeted visitors stay on the focused conversion surface for their context.

## Brand Core

- Name: Pedro Barbas
- Positioning: Evidence-first systems
- Public principle: Architecture first. Evidence always. No proof, no claim.
- Shared philosophy: deterministic, evidence-led systems that help teams see earlier signals, control AI actions, preserve proof, and turn complex decisions into reviewable next steps.
- Buyer-value pattern: source evidence first, deterministic processing, explicit limitations, reviewable proof, and human review before action.

## Route Architecture

| Route | Purpose | Public-safe boundary |
| --- | --- | --- |
| `/` | Balanced two-track public hub. | Short routing surface only; it must not become a long portfolio page or make one track visually overpower the other. |
| `/procurement/` | Deal Hunter / Procurement Intelligence track. | Deal Hunter only; Ireland first, Portugal next; no TrustGate, Certify, Evidra, or FieldDelta product cards. |
| `/ai-control/` | TrustGate Sovereign / AI Control presence page. | TrustGate Sovereign leads as the execution firewall for agentic AI; Certify, Evidra, and FieldDelta remain secondary related systems. |
| `/pt/` | Portuguese (`pt-PT`) two-track public hub. | Must mirror the English hub claim boundaries and remain a translation, not a new positioning surface. |
| `/pt/procurement/` | Portuguese (`pt-PT`) Deal Hunter / Procurement Intelligence track. | Must mirror the English procurement boundaries and keep track isolation. |
| `/pt/ai-control/` | Portuguese (`pt-PT`) TrustGate Sovereign / AI Control presence page. | Must mirror the English TrustGate Sovereign boundaries and avoid Portuguese compliance/legal guarantees. |

## Bilingual Structure

- English remains the default language at `/`, `/procurement/`, and `/ai-control/`.
- Portuguese lives under `/pt/`, `/pt/procurement/`, and `/pt/ai-control/`.
- Portuguese must use European Portuguese (`pt-PT`), not Brazilian Portuguese.
- Product names remain untranslated.
- The language switch maps only to the equivalent same page: root to root, procurement to procurement, and AI Control to AI Control.
- There is no auto-detection, browser-language redirect, JavaScript, cookie, or local-storage language state.
- Track isolation is preserved in both languages.

## Balanced Two-Track Architecture

Homepage framing:

- The root page presents two serious tracks with balanced visual weight.
- The root page uses public-facing language, not internal go-to-market shorthand.
- Deal Hunter remains first in order, but not wider, taller, louder, or more visually dominant than AI Control.
- The homepage procurement card uses "Ireland & Portugal."
- The homepage routing heading is "Choose the right track."
- The homepage subheading is "Two tracks, one evidence-first operating model."

Track-specific framing:

- `/procurement/` keeps Ireland first / Portugal next because that is the Deal Hunter country-positioning page.
- `/ai-control/` remains the approved AI Control track, now led by TrustGate Sovereign as the execution firewall for agentic AI.
- Track pages use persona-specific navigation to reduce cross-persona context leakage while keeping one static site.

The homepage should help a visitor self-select in under 10-15 seconds while making both tracks clear, credible, and equal in treatment.

## Homepage Model

The homepage is a router, not a portfolio.

Required content:

- minimal header and identity
- short shared philosophy
- two balanced route cards
- compressed operating principles
- compact Boundaries trust signal
- contact

The homepage should not include full product cards, long explanations, all product details, or a long scrolling portfolio layout.

## Procurement Buyer Journey

The `/procurement/` page is the dedicated Deal Hunter surface for Irish and Portuguese procurement and infrastructure buyers.

Buyer journey:

- urgent tender-before-tender pain statement
- Deal Hunter value proposition in buyer-native language
- source-backed opportunity trail visual
- Ireland-first / Portugal-next country positioning
- review outcomes
- mid-page "What is not claimed" trust section
- controlled disclosure / boundaries
- private Deal Hunter walkthrough CTA

Ireland is the first buyer-conversation path for controlled review. Portugal is the next dedicated regional market view, with discovery focused on infrastructure, energy, grid, public works, and pre-tender signals. Deal Hunter uses one source-backed review model for market signals, with Ireland and Portugal handled as dedicated market views rather than separate products.

## Procurement Buyer-Language Rule

Procurement-facing copy must use buyer-native language. Use opportunity tracking, source-backed opportunity trail, pre-tender signals, market views, commercial review, and representative opportunity tear-downs.

Avoid architecture-native terms on `/procurement/`, including control plane, canonical identity, project identity, evidence chain, country-pack architecture, synthetic evidence packs, deterministic, and upstream.

AI Control pages may use more technical language where appropriate.

## TrustGate Sovereign Buyer Journey

The `/ai-control/` page is the TrustGate Sovereign presence page for CISO, CIO, AI governance, risk, audit, enterprise architecture, technical governance, and executive adoption conversations.

TrustGate Sovereign must lead with:

- the execution firewall for agentic AI
- the action-clearance gap between deployment/platform governance and a specific action
- the line "A governed deployment and a governed platform do not automatically authorize a specific action."
- the airport analogy
- Principal -> Control -> Proof
- Principal, Action, Context, Route, Admission, Telemetry, Proof, Held Gate
- TG360 as the evidence cockpit
- TGSG trust surfaces
- an illustrative watsonx Orchestrate / Manta / Db2 scenario with no live integration claim
- clear boundaries and private walkthrough posture

Certify, Evidra, and FieldDelta remain related evidence-first systems, but they must not compete visually or semantically with the TrustGate Sovereign lead.

## Navigation Model

The English root is the full two-track hub and must include navigation links for Home, Procurement, AI Control, Boundaries, and Contact. The Portuguese root is the full two-track hub and must include Início, Procurement, Controlo IA, Limites, and Contacto.

Track pages use persona-specific navigation isolation:

- `/procurement/` navigation is Procurement / Boundaries / Contact only.
- `/ai-control/` navigation is AI Control / Boundaries / Contact only.
- `/pt/procurement/` navigation is Procurement / Limites / Contacto only.
- `/pt/ai-control/` navigation is Controlo IA / Limites / Contacto only.
- Track page header and footer navigation should not route visibly to Home or the other track.
- Language switchers may link only to the equivalent same-track page in the other language.

The purpose is to reduce cross-persona context leakage while keeping one static site.

## Boundaries Navigation

Every page must include navigation links for Boundaries and Contact. The Boundaries link must point to the current page's own `#boundaries` section. The Contact link must point to the current page's own `#contact` section.

Each page must have a visible `id="boundaries"` section. Boundaries are a trust signal, not a footer afterthought.

## Controlled Visual Model

- `assets/evidence-control-pattern.svg`: public value pattern from source signal to human review.
- `assets/procurement-evidence-chain.svg`: earlier procurement signals moving into review context.
- `assets/ai-action-control-gate.svg`: AI request checked before action and proof receipt.
- `assets/evidence-pack.svg`: governance evidence pack components without real data.
- `assets/simulation-review-pack.svg`: baseline/candidate comparison into materiality review.
- `assets/trustgate-sovereign-execution-firewall.svg`: public-safe execution firewall from agentic request to clear or hold and proof.
- `assets/trustgate-sovereign-working-example.svg`: illustrative enterprise stack flow with no vendor logos or live integration claim.
- `assets/tg360-evidence-cockpit.svg`: abstract TG360 evidence cockpit.

## Content Rules

- Prefer source-backed, reviewable, controlled walkthrough, human review, bounded demo, proof artifact, materiality-ranked, pre-tender signals, opportunity tracking, and source-backed opportunity trails.
- Buyer-value wording may name problems, risk, review effort, missing evidence, earlier visibility, and proof needs.
- Avoid vague hype, unsupported customer proof, implied production status, compliance claims, prediction claims, autonomous decision claims, and implementation recipes.
- Every major public claim should map back to `docs/public_claims_ledger.md`.
