---
name: aquasc-response-letter
description: Draft or revise reviewer response letters using the user's AquaSC conventions, with self-contained replies, gratitude in the opening acknowledgments, black response prose, exact blue manuscript excerpts, and verified section/page/figure/table locators. Use when syncing a letter to a revised manuscript.
---

# AquaSC Response Letter

Write a professional, readable response letter that accurately represents the latest manuscript. Discuss the work with the user in Vietnamese by default; keep the letter in its existing language and template.

## Work from current sources

Identify the active manuscript, letter, and original reviewer comments. Inspect the latest advisor/user edits before changing the letter. Preserve reviewer wording and advisor annotations unless the user explicitly requests otherwise.

For a narrow request, change specified responses and their affected excerpts/locators. For a full sync, review every reply against the current paper. Do not change the manuscript merely to make a letter statement true without authorization for that edit.

Read [response examples and locator handling](references/responses-and-locators.md) when drafting replies, using `\action`, or checking cross-document references.

## Tone and organization

- Keep gratitude in the cover letter and opening acknowledgments. The user's latest AquaSC preference is not to begin every comment response with thanks. A specific additional acknowledgment is appropriate when useful, but repetitive gratitude is not a requirement.
- Answer the reviewer's question directly, then give the relevant change and evidence. Vary openings with the substance of the reply, not with a catalogue of thank-you synonyms.
- Keep each reviewer's replies understandable independently. Repeat focused evidence when needed; do not send Reviewer 3 to a response written for Reviewer 2.
- Use normal black text for ordinary author responses. Preserve the existing template's colored labels/reviewer comments. Use blue for actual manuscript excerpts/revision markup, not for the entire response body.
- Describe corrections neutrally and concretely. Avoid a defensive debugging narrative and unnecessary admissions unrelated to the comment. Retain facts needed to interpret corrected results honestly.
- Use short, developed paragraphs. Avoid long tables of numbers when a representative contrast and its interpretation answer the point.
- Prefer current public terminology and model names. Do not expose internal experiment aliases when the manuscript presents them as the same model/configuration.

## Action statements and exact excerpts

When using `\action`, identify the actual manuscript change and reproduce a focused excerpt from the latest source. The quote must already exist in the manuscript. Do not write a smoother paraphrase and present it as a verbatim quotation.

Allow presentation-only transformations such as local blue markup, rendered citations, or expansion of a manuscript macro, but verify that words, numbers, formulas, and qualifications remain identical. Quote only text that supports the action statement, with a verified section and page locator.

If the change exists only in the letter, say so in the response. Do not invent a manuscript action or quote. If the main text needs another change, finish permitted letter work and explain the concrete missing manuscript edit to the user.

## Scientific consistency

Check every changed assertion against the current manuscript/evidence: metric aggregation, rate, SNR, dataset/split, channel protocol, model scope, uncertainty, and configuration. A conditional image-bootstrap interval is not a pooled-mAP interval, a training-seed study, or a cross-video guarantee.

Do not relabel an invalid diagnostic to preserve a favorable comparison. Do not omit privileged inputs or protocol differences while retaining conclusions that depend on them. If no public implementation was found, phrase that as the bounded outcome of an actual search; do not assert universal nonexistence without evidence.

When the paper narrows a claim, synchronize abstract/contribution quotations, summary of changes, individual replies, and closing summary that depend on it. Do not add redundant limitations to unrelated responses.

## Final pass

Compile the final manuscript first when possible, then verify all changed excerpt contents and manual locators against that version. Cross-document `\ref` commands can be unresolved on Overleaf; use explicit verified numbers when the project uses manual locators. Retain working local references unless the user asks to replace them.

Compile the letter and inspect changed pages for unresolved references/citations, overflow, and awkward page breaks. Distinguish source/content checks from compilation and visual checks in the report. If the user forbids prose edits, report a stale locator rather than silently changing it.

Return a concise summary of corrected responses, synchronization checks, and any concrete item still needing code or manuscript evidence. Push only when authorized by the user; stage only approved files.
