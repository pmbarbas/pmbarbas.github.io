# Review Notes

## Phase 0 Notes

- LinkedIn placeholder is set to `https://www.linkedin.com/in/pedrobarbas/`.
- Email contact is set to `pedro.m.barbas@gmail.com`.
- No contact form has been added.
- No external JavaScript, CSS, fonts, analytics, cookies, tracking pixels, or CDN dependencies have been added.
- No binary images have been added.
- SVG assets are locally created and public-safe.
- Claims are intentionally bounded to private walkthroughs, local technical review, active validation, architecture, and evidence generation.

## Phase 1 Notes

- Buyer-value wording has been added for procurement visibility, AI action control, evidence packs, and engineering review.
- Deal Hunter is presented as the procurement intelligence track.
- TrustGate, Certify, Evidra, and FieldDelta are presented as related evidence-first systems.
- Controlled SVG visuals were added with abstract labels only. They do not include source names, scoring logic, proof schemas, protocol internals, real product data, screenshots, or customer material.
- The validator allows forbidden phrases in `index.html` only when they appear in an explicit not-claimed boundary context. This exception preserves the public "What is not claimed" trust section while still failing unsupported overclaims.
- LinkedIn placeholder remains `https://www.linkedin.com/in/pedrobarbas/`; confirm before publication.

## Phase 1.2 Notes

- Review whether the TrustGate wording keeps finance clearly first without making the page finance-only.
- Review whether insurance, healthcare/life sciences, and critical infrastructure are mentioned as expansion categories without overclaiming domain readiness.
- Check whether "examiner-ready evidence posture" feels strong but not too compliance-heavy.
- Check mobile layout because the TrustGate card is denser after this pass.
- Validator blocked-phrase exceptions still require explicit guardrail context such as BLOCKED, forbidden, not claimed, or boundary wording.

## Phase 2 Notes

- The site has been restructured into `/`, `/procurement/`, and `/ai-control/`.
- The homepage is now a short balanced public hub, not a long portfolio page.
- Deal Hunter appears first in order on the homepage.
- The two homepage route cards should remain balanced in visual weight.
- The AI Control route is serious and available, with TrustGate, Certify, Evidra, and FieldDelta preserved.
- `/procurement/` is Deal Hunter-only and does not include TrustGate, Certify, Evidra, or FieldDelta product cards.
- `/procurement/` positions Ireland as the first buyer-conversation path and Portugal as the next regional market view.
- `/procurement/` includes "What is not claimed" mid-page, before the final CTA.
- `/ai-control/` orders systems as TrustGate, Certify, Evidra, and FieldDelta.
- `/ai-control/` includes the relationship note that TrustGate defines the broader enterprise control path and Certify proves the local pre-execution certification mechanics.
- Boundaries navigation is present on all three pages and links to each page's own `#boundaries` section.
- Contact navigation is present on all three pages and links to each page's own `#contact` section.
- No new unsupported claims, customer claims, production claims, compliance claims, legal claims, or prediction claims were added.

## Phase 2.1 Notes

- Homepage internal routing language was removed in favor of public evidence-first wording.
- Homepage procurement card uses "Ireland & Portugal"; `/procurement/` keeps Ireland first / Portugal next.
- Deal Hunter and AI Control are both treated as valid tracks explored in parallel.
- The phrase "Two doors, one primary GTM wedge" must stay removed from public HTML.
- AI Control page was not materially rewritten; only public-language QA and punctuation fixes were made.
- Boundaries and Contact anchors should work on all three pages.
- Desktop and mobile layouts should be checked for balanced cards, readable Boundaries sections, and no horizontal overflow.

## Phase 2.2 Notes

- Root homepage source labels now use public-facing wording for both route cards.
- Root homepage validation blocks the prior internal phrases and requires the public routing heading, subheading, procurement country wording, and AI Control product line.
- `/procurement/` and `/ai-control/` were preserved for this correction pass.

## Phase 2.4 Notes

- Root remains the full two-track hub and should still link to both `/procurement/` and `/ai-control/`.
- `/procurement/` uses persona-specific navigation: Procurement, Boundaries, and Contact only.
- `/ai-control/` uses persona-specific navigation: AI Control, Boundaries, and Contact only.
- Verify `/procurement/` does not visibly link to AI Control or Home.
- Verify `/ai-control/` does not visibly link to Procurement or Home.
- Verify Boundaries and Contact remain visible on all three pages.
- Verify manual browser back button behavior remains normal.
- Verify mobile nav remains clear after the shorter track-specific nav sets.
- Verify no content was materially rewritten on `/procurement/` or `/ai-control/`.

## Phase 2.6 Notes

- Review `/procurement/` as an infrastructure procurement buyer.
- Check whether any phrase feels like software architecture rather than market intelligence.
- Confirm the tender line remains unchanged.
- Confirm "What is not claimed" remains mid-page.
- Confirm Ireland first / Portugal next remains on `/procurement/`.
- Confirm AI Control was not materially touched.
- The embedded procurement SVG still contains legacy labels such as "Evidence chain"; this phase did not edit SVG assets, so manually review whether the visual should be relabeled in a future asset pass.

## Phase 2.7 Notes

- Manually review Portuguese copy with a Portugal-native reader if possible.
- Verify the EN/PT switcher on all six pages.
- Verify no obvious Brazilian Portuguese terms appear.
- Verify track isolation still holds in English and Portuguese.
- Verify the Portuguese procurement page remains buyer-native.
- Verify the Portuguese AI Control page does not overclaim compliance, legal effect, production status, or regulatory approval.
- Check mobile layout in both languages.

## Phase 3.0 Notes

- `/ai-control/` now leads with TrustGate Sovereign as the execution firewall for agentic AI.
- Review whether the category gap is clear: deployment governance, platform governance, and action clearance are different layers.
- Confirm the airport analogy is understandable and not too informal for executive buyers.
- Confirm Principal -> Control -> Proof and the expanded control chain are visible without exposing proof internals.
- Confirm TG360 reads as an evidence cockpit for private walkthrough review, not as a live production dashboard.
- Confirm TGSG surfaces are understandable for senior technical adopters without exposing implementation details.
- Confirm the watsonx Orchestrate / Manta / Db2 scenario is clearly illustrative only.
- Confirm no IBM endorsement, partnership, live integration, live telemetry, connector execution, customer data, production data, CP-7 authorization, ROI, or savings claim is implied.
- Confirm Certify, Evidra, and FieldDelta remain secondary related systems.
- Review `/pt/ai-control/` with a Portugal-native reader if possible, especially IA agêntica, implantação, autorização, cockpit de evidência, and Porta mantida.
- Check the three new SVG assets for readability at desktop, tablet, and mobile widths.

## Manual Review Before Publication

- Review homepage in 10 seconds: are both tracks clear?
- Review Portuguese root page in 10 seconds: are both translated tracks clear?
- Review root page: does it still link to both tracks?
- Review root page: does it no longer contain internal phrases?
- Review homepage: does the procurement card say Ireland & Portugal, not Ireland first / Portugal next?
- Review homepage: do the two cards feel balanced?
- Review homepage: is the phrase "Two doors, one primary GTM wedge" removed?
- Review `/procurement/`: does it still preserve Ireland first / Portugal next?
- Review `/procurement/`: does it feel buyer-native and Deal Hunter-only?
- Review `/procurement/` as an infrastructure procurement buyer: does any phrase feel like software architecture rather than market intelligence?
- Review `/procurement/`: is the exact tender line unchanged?
- Review `/procurement/`: does it avoid visible AI Control and Home navigation?
- Review `/procurement/`: is "What is not claimed" mid-page?
- Review `/ai-control/`: does it avoid visible Procurement and Home navigation?
- Review `/ai-control/`: does TrustGate Sovereign clearly lead?
- Review `/ai-control/`: do Certify, Evidra, and FieldDelta feel secondary?
- Review `/ai-control/`: is the illustrative watsonx Orchestrate / Manta / Db2 scenario clearly bounded?
- Review all pages: are Boundaries and Contact anchors working?
- Review all six pages: do EN/PT switchers map only to equivalent pages?
- Review `/pt/procurement/`: does it read like Portugal-native procurement and infrastructure market intelligence?
- Review `/pt/ai-control/`: does it preserve boundaries without compliance, legal, production, or regulatory guarantees?
- Review `/pt/ai-control/`: does TrustGate Sovereign read naturally in pt-PT and preserve the same claim boundaries?
- Review the browser back button from each track page after navigating from the homepage.
- Review mobile nav clarity on all three pages.
- Review desktop and mobile layouts.
- Review no claims were added beyond routing.
- Confirm the LinkedIn URL is exact.
- Confirm the email address and subject line are preferred.
- Review all product wording against `docs/public_claims_ledger.md`.
- Check the page at desktop, tablet, and mobile widths.
- Check controlled SVG visual readability and ensure labels remain abstract.
- Confirm no private history exists in any repository intended for publication.
