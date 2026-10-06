---
name: product-release-doc-writer
description: Create or revise internal release notes, external release notes, product release plans, feature FAQs, and support FAQs from supplied product context. Use for these release artifacts; exclude PRDs, product or launch strategy, retrospectives, roadmaps, prioritization, adoption analysis, stakeholder presentations, enablement talk tracks, and general product analysis.
---

# Product release documents

Create or revise one or more of these artifacts:

- Internal Release Notes: align internal readers on context, rollout, risks, dependencies, decisions, readiness, and actions.
- External Release Notes: explain the customer outcome, capability, availability, use, and confirmed public limitations.
- Product Release Plan: organize execution around learning, evidence, validation, risk reduction, rollout, and adoption.
- Feature FAQ: answer customer-facing questions about a capability, access, use, limits, and supported claims.
- Support FAQ: distinguish expected behavior, access/configuration issues, limitations, defects, verified steps, and unknowns.

For an explicitly requested artifact, create or revise it. If the request could mean several supported artifacts, infer from the intended reader and use when clear; otherwise ask one focused question. This skill does not create PRDs, product or launch strategy, retrospectives, roadmaps, prioritization, adoption analysis, stakeholder presentations, enablement talk tracks, or general product analysis. In a mixed request, complete supported release artifacts and handle any out-of-scope deliverable separately without expanding this skill's workflow.

Before drafting, inspect the active conversation and supplied materials. Apply [source grounding](references/shared/source-grounding.md), [clarification behavior](references/shared/clarification-behavior.md), [template resolution](references/shared/template-resolution.md), and [audience boundaries](references/shared/audience-boundaries.md). These invariants apply to every artifact and template.

Load only the relevant artifact guide(s):

- [Internal Release Notes](references/internal-release-notes.md)
- [External Release Notes](references/external-release-notes.md)
- [Product Release Plan](references/product-release-plan.md)
- [Feature FAQ](references/feature-faq.md)
- [Support FAQ](references/support-faq.md)

Use the matching default at `assets/templates/<artifact-name>.md` when no higher-priority template applies. Keep useful Markdown tables, blockquotes, and numbered documented usage steps where suitable. Use plain Markdown by default; follow the selected template's format. Do not add emojis or impose organization-specific phases, sign-off roles, deadlines, pricing rules, or processes without task evidence.

For revisions, preserve verified content and requested structure, apply the user's latest explicit corrections, and remove or qualify unsupported claims. Label inferred actions and follow-ups in any artifact as proposals or open questions; only supplied actions are confirmed, and a missing owner is unknown rather than “unassigned.” Before drafting an external artifact, identify the facts confirmed as public and use that subset; a fact included in an external-artifact request is not public by default if it is unlabeled or marked internal. Never treat a template heading as evidence.
