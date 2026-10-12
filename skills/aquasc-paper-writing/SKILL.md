---
name: aquasc-paper-writing
description: Draft, revise, or proofread engineering and ML manuscripts using the user's AquaSC-derived writing conventions. Use for abstracts, introductions and contributions, methods, results discussion, and conclusions, including revisions limited to blue text and preservation of advisor edits.
---

# AquaSC Paper Writing

Write clear English academic prose with the structure, paragraph flow, and revision discipline established in AquaSC. Discuss edits with the user in Vietnamese unless they choose another language. AquaSC supplies editorial preferences, not experimental facts for a new paper.

## Establish the current task

- Identify the active manuscript and requested sections. Read the surrounding paragraphs before rewriting.
- Use the latest user-approved source. When asked to pull advisor changes, inspect the local/upstream diff and preserve local work before integrating it.
- Respect the edit boundary. A request to edit only blue text, captions, figures, or specified passages does not authorize rewriting other prose. Preserve advisor comments such as `%Phuc`, `%Dinh`, and `\Dinh{...}`.
- Derive factual statements from the user's current evidence. A plotting script is the numerical authority when the user designates it; do not silently replace its numbers with an older results record.
- For a structural change that the user asks to approve first, show the proposed arrangement before moving sections.

## Drafting and polishing

Read [the section and prose guide](references/section-and-prose-guide.md) for the sections being revised. Apply these shared preferences:

- Preserve the author's established voice. Favor concrete descriptions of the system, design choices, and measured behavior over promotional language or a wholesale stylistic rewrite.
- Give each paragraph a developed main point. Merge related one-sentence fragments; keep a short paragraph when its role genuinely needs one. Do not pad text to satisfy a sentence count.
- Introduce full terms before abbreviations. Treat the abstract and main text as separate first-use contexts. Contributions should be readable on their own, especially for the paper's proposed modules.
- In results discussion, explain the pattern through the design and evaluation conditions. Quote only the numbers needed for the argument; leave full sweeps in figures and tables.
- Separate an observed result from a proposed explanation. Use causal language only when the controlled evidence supports it.
- Keep terminology stable across the abstract, contributions, method, captions, conclusion, and response letter. Prefer meaningful operating-point names such as high rate over internal experiment labels such as headline.
- Avoid repeated staged openers, dramatic contrasts, inflated adjectives, and formulaic closing sentences. Vary sentence length and transitions while retaining precise technical language.
- Keep the abstract selective. It normally needs the problem, proposed approach, essential mechanism, and main supported outcome; competitor paper names and exhaustive protocol details belong elsewhere.
- Keep the conclusion compact, normally one synthesis paragraph and a short limitations/future-work paragraph. The target venue and user's length goal determine the actual length.

## Mathematical and presentation flow

- Introduce symbols before using them and connect a group of related equations with a coherent paragraph. Avoid a succession of indented one-line bridges between displays.
- Use `align` or a similarly appropriate environment for genuinely related expressions; preserve meaning and required equation labels.
- Apply the user's AquaSC convention of no trailing commas in displayed equations. Retain sentence-ending punctuation when appropriate to the surrounding grammar.
- Use concise captions that identify the comparison, metric, and essential setting. Move explanation of causes and secondary protocol details to nearby text.
- Tables use horizontal rules without vertical separators. Name the measured scope accurately, for example encoder parameters and encoder state rather than total transmitter cost when only the encoder was counted.
- For a figure/table formatting task, use `$aquasc-publication-figures` if available. Core defaults are subcaptions below panels, regular caption weight, matching axis fonts, and thinner curves.

## Evidence and final verification

Read [revision and evidence handling](references/revision-and-evidence.md) when editing a revision, reconciling results, changing layout, or synchronizing Overleaf.

Check changed text against the actual metric, denominator, rate, protocol, data split, and accounting scope. Keep an unresolved implementation question in the user-facing report; do not invent an answer in the paper. Necessary qualifications belong where they affect interpretation, without repeating unrelated limitations after every result.

Compile and inspect affected pages when source files and a compiler are available. Layout changes can invalidate manual figure/table/section numbers and response-letter page locators. Verify them from the final PDF; edit them only within the authorized scope.

## Delivery

For file work, write approved changes and give a short summary of what changed, what was checked, and any concrete issue still requiring code or evidence. For a passage rewrite, return proposed prose directly. Keep editorial notes and claim-evidence working notes outside the manuscript unless requested. A writing task alone does not authorize a Git push or submission.
