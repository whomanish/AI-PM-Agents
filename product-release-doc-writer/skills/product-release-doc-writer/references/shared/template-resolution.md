# Template resolution

Choose the first available template in this order:

1. A template explicitly supplied for the current task.
2. A user or organization template available in the active context.
3. The bundled default at `assets/templates/<artifact-name>.md`.

The selected template controls headings, section names and order, optional sections, formatting, and terminology. Preserve its requested structure when creating or revising the artifact. Apply only the relevant default when no higher-priority template is available. Treat authoring notes, bracketed instructions, example values, and drafting scaffolding as instructions for preparing the artifact, not as reader-facing content. Remove them or replace them with grounded content or a specific placeholder before delivery, unless the user explicitly requests that scaffolding in the artifact. Preserve requested headings and structure while removing those instructions.

Templates do not establish facts or override the behavioral rules in this skill. A requested heading such as “Competitive Advantage,” “Pricing,” or “Known Issues” is not evidence that content exists. Do not fill unsupported sections with invented claims. Omit optional unsupported material or mark a material gap clearly; ask only if it blocks a useful and accurate draft.

If a template requests a format that conflicts with an invariant, retain the template's structure where possible while leaving unsupported content out, qualifying it, or asking a focused question. An absent value means it was not supplied or confirmed; do not turn that absence into claims such as “none,” “not assessed,” “not set,” or “unassigned.” For an essential gap in a useful draft, use a specific placeholder such as `[Availability not confirmed]` rather than an unsupported conclusion.

When adapting supplied material, distinguish substantive information, required wording or structure, and authoring context. Preserve wording exactly where the task requires it or accuracy depends on it, such as quoted text, error messages, or specified headings. Reframe substantive information for the artifact's audience while preserving its meaning, constraints, uncertainty, and attribution where relevant. Omit drafting instructions, source-management labels, and other authoring context that does not belong in the finished artifact. If omitting a qualification would materially change the reader's understanding, retain it or ask a focused question.
