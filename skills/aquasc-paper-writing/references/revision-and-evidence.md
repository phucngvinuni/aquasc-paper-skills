# Revision scope and evidence handling

## Revision discipline

Inspect the current source, not a remembered filename or old PDF. Response-letter filenames and section numbering may change after advisor edits.

Preserve advisor annotations and settled text. When blue text only is permitted, modify approved blue spans. Note an important issue outside that scope separately and continue permitted work. If a particular black-text correction is authorized, apply it and mark it using the agreed convention.

Keep clean/marked variants derived from the same substantive text. Color should not introduce a second version of the argument. Green review markup becomes blue only when requested.

Figure-only edits preserve prose bytes, numeric data, figure selection, and scientific configuration. Keep unused plots untouched unless the user asks to regenerate or archive them.

## Numerical authority

Use the source explicitly designated by the user. This may be the active plotting script, not a results-record Markdown file. Establish authority for the task and resolve conflicts before changing dependent claims.

Synchronize affected figure arrays, tables, discussion, abstract/conclusion claims, and letter excerpts. Keep measured precision internally, then round consistently. Never interpolate a missing point and present it as measured. Preserve a missing point, request its source, or label an estimate when that is agreed.

Do not embed AquaSC numerical results, checkpoint names, or rates as defaults for another paper.

## Quantities needing exact definitions

- Source bits, packed bytes, coded bits, complex symbols, and channel uses differ. Packed byte counts normally require a ceiling for a partial byte.
- A complex symbol has two real components. Serialized I/Q bytes follow the actual dtype/packing, not the size of one component.
- Encoder-only parameters/state differ from complete-transmitter parameters/state. Codebooks and auxiliary modules follow the declared counting scope.
- Pooled mAP, mean per-image AP, and retention ratios have different aggregation/reference denominators.
- Evaluation seeds, router/mask seeds, training seeds, and source-video replication describe different uncertainty.
- Simulated-channel accuracy and measured Wi-Fi/hardware latency are separate measurements. Do not imply that a latency test validated fading-channel accuracy.
- Close rates can be approximately matched while coding/modulation/transport protocols still differ. Do not infer a pure model-design advantage from mismatched protocols.

A code-dependent ambiguity should become a concrete check for the user: file/function to inspect, quantity to print, and evidence resolving it. Do not add training or broaden experiments just to polish a passage.

## Honest but concise correction language

State what changed and what the corrected evaluation establishes. Avoid dramatic confessions or unnecessary debugging narrative. Preserve information materially changing interpretation, including invalidated results, data-dependent selection, privileged diagnostic inputs, and protocol differences.

An implementation correction does not justify silently relabeling an old measurement. A router measuring activation magnitude cannot retain a gradient-importance label. Removing an invalid comparison also requires removing its dependent claims/stale references.

## LaTeX and layout checks

Check changed prose for acronym first use, notation consistency, citation support, brace/environment balance, and active figure/table/section references.

Compile the final approved source when available, then inspect affected pages for spacing, floats, clipping, and readability. Report a missing compiler rather than claiming successful compilation.

Resolve manual numbers from the final PDF/label map. Avoid unresolved external `\ref` commands in a response letter. Recheck copied excerpts and page/section locators after layout changes. Keep functional intra-document references unless manual numbers are requested.

Do not repair letter locators or manuscript wording during a figure-only task forbidding prose edits. Verify unchanged locators when canvas dimensions preserve layout; otherwise identify the follow-up needed.

## Overleaf synchronization, only when authorized

Inspect status/remote, fetch, and compare upstream changes before integrating. Back up local work and inspect advisor edits. Fast-forward a clean checkout when possible; reconcile overlaps deliberately instead of overwriting.

On Windows, use per-command `git -c safe.directory=...` when needed. Do not change global Git settings or put credentials into source, remote URLs, logs, skill files, or packages.

Stage only approved files. Run `git diff --check` and checks relevant to the change, then push normally. Verify the final remote commit and clean status. Do not force-push advisor changes away. This skill supplies no credential or permission to publish a paper.
