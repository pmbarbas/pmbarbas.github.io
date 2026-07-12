# Public Surface Phase 3.1R3 Visual Discovery

## Baseline

- Repository: `/Users/pbarbas/Documents/GitHub/pedro-public-surface`
- Branch: `main`
- HEAD: `092317a5029a5a14c62a8f6864c5441993c57517`
- Staged paths: none
- Existing worktree changes: approved Phase 3.1 / R1 / R2 scope only

## Visual Inventory

| Page section | Current asset path | Current EN labels | Current PT labels | Semantic defect | Localization defect | Proposed asset strategy | Validator requirement | Manual visual gate |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Hero and public control chain | `assets/trustgate-sovereign-execution-firewall.svg` | Proposed action; TrustGate clearance; Bound receipt; Protected-target verification; Accept/reject; Outcome proof | None; Portuguese route reuses English labels | Primary sequence is correct and the SVG no longer contains the retired claim, but authority/purpose/target/route/evidence context is not visible and nodes lack deterministic semantic roles | Entire visible SVG, title, and description are English on `/pt/ai-control/` | Revise the existing EN SVG with concise context and semantic IDs/data roles; create `assets/trustgate-sovereign-execution-firewall-pt.svg` with localized title, description, labels, and the same sequence | Reject retired visible/descriptive claim; require EN/PT concepts; verify EN and PT routing; require title/desc; reject English operational labels in PT | Desktop/mobile/print legibility; distinct clearance, receipt, verification, outcome; no clipping or tiny text |
| Illustrative enterprise stack | `assets/trustgate-sovereign-working-example.svg` | watsonx proposed action; Manta lineage/context; TrustGate clearance + receipt; Protected target verification; Db2-side outcome + evidence; illustrative disclaimer | None; Portuguese route reuses English labels | A verification node exists, but connector intent is not structurally declared and outcome evidence is merged into the target node | Entire visible SVG, title, and description are English on `/pt/ai-control/` | Revise EN SVG with `trustgate-clearance`, `protected-target-verification`, `target-outcome`, and directional connector roles; create `assets/trustgate-sovereign-working-example-pt.svg` with localized operational labels | Parse groups/connectors; require clearance -> verification -> outcome; reject direct bypass; require localized PT labels and title/desc | Verification gate visually unmistakable; no TrustGate-to-Db2 write implication; disclaimer remains attached in print |
| TG360 evidence cockpit | `assets/tg360-evidence-cockpit.svg` | known context; bounded scope; synthetic demo; not activated; proof visibility; walkthrough/private evidence | None; Portuguese route reuses English labels | Existing EN visual remains buyer-safe and static | Entire visible SVG, title, description, and walkthrough label are English on `/pt/ai-control/` | Retain EN asset; create `assets/tg360-evidence-cockpit-pt.svg` with canonical pt-PT labels and no public internals | Require six PT concepts; reject English operational labels; require localized title/desc and PT route reference | PT text fits at desktop/mobile/print; cockpit stays simple and does not imply telemetry |

## CTA Discovery

- `.button.primary` uses `background: var(--accent)` with `color: #ffffff`.
- In the light palette, the accent is relatively light for normal-size white button text and can read as disabled.
- R3 strategy: retain the current palette and button structure, use the stronger existing accent token for primary normal state, preserve a restrained hover state, and add an explicit focus-visible outline.

## Responsive Discovery

- The current `@media (max-width: 680px)` rule hides `.hero-visual` globally.
- This removes all three AI Control diagrams on mobile, contrary to the R3 semantic-review requirement.
- R3 strategy: keep unrelated mobile visual behavior intact while restoring AI Control hero, chain, enterprise, and TG360 figures through scoped overrides.

## Print Discovery

- `styles.css` currently has no `@media print`, `@page`, `break-inside`, `page-break-inside`, or heading keep-with-next contract.
- R3 strategy: add orientation-agnostic A4-friendly print rules; protect compact cards, figures, CTA groups, short panels, and disclosure columns; keep headings with following content; reduce print spacing conservatively; never hide substantive content.
- Manual authority: rendered A4 portrait and landscape inspection for EN/PT, including page counts and split/orphan review.
