# Section and prose guide

These are the user's AquaSC-derived defaults. Adapt them to the current contribution and venue; do not force every paper into the AquaSC architecture or a fixed number of sections.

## Abstract

Start with the application need and technical bottleneck. Introduce the proposed system and mechanisms addressing that bottleneck. End with the main supported result or qualitative finding and a restrained statement of its relevance.

Keep the abstract closer to a readable research summary than an experimental checklist. Include a representative number when it anchors the contribution; put full rate/SNR sweeps, payload decompositions, selection histories, and baseline configurations in later sections. Avoid naming competitor papers/models unless the user or venue needs them. Do not claim superiority beyond measured settings.

Explain an abbreviation on first use or write the term out when used only once. Define it again on first use in the main text if the abstract is read separately.

## Introduction and contributions

Develop the application need, mismatch in existing approaches, and specific gap addressed by this work. Connect the gap to the design choices so the contribution list follows naturally.

Cite the overview figure in the introduction or contributions when it orients the reader, and again in the system-model discussion where its components are explained.

Contribution bullets state an actual technical contribution and its supporting evidence. Avoid lists of experiment filenames, section summaries, or optimistic deployment promises. Spell out proposed module names before their abbreviations, even when a contribution may be read independently.

Illustrative contribution wording, to adapt only when it matches the actual method:

> We introduce a Feature Importance Module (FIM) and a Bounding-Box-Weighted (BBW) reconstruction loss. FIM selects patches for higher-rate quantization, while BBW gives target regions greater influence during training. Controlled component and routing comparisons evaluate their contributions under a common transmission budget.

Use a dataset contribution only when collection/annotation work supports it. Distinguish a dataset release, benchmark, and additional evaluation split.

## Related work

Group work by the problem or mechanism relevant to the contribution. Explain what each group establishes and what remains unresolved. Avoid an author-by-author catalogue and unsupported claims that an entire area ignores the problem.

A suggested citation should serve a specific argument. Verify its content before adding it; do not cite a title alone as evidence. Describe the relationship to the current paper without borrowing its claims.

## System model and proposed method

When background and innovations are interleaved, separate the common system model from the proposed method:

- The common model establishes the scenario, transmitter/receiver roles, channel assumptions, available information, task metric, and resource definitions.
- The proposed method explains the learned architecture, task-alignment mechanisms, representation/packet construction, receiver behavior, training objective, and any lightweight variant.

Keep the boundary substantive: generic assumptions precede innovations, while details supporting an innovation remain with it. A new arrangement is not permission to change the mathematical method.

Each mechanism needs a reason for its design and a clear account of inputs, outputs, and optimization. For a frozen/trainable arrangement, state which modules are shared, which outputs supervise the loss, and which parameters are updated. A loss consumes outputs; it is not a data input to a downstream frozen module.

Use the actual implementation as the authority for a formula. Branch-specific weights and normalization must not be simplified into a different objective. Report hyperparameters as defaults when that is how they were used; do not invent a tuning study.

Keep methodology separate from a chronology of debugging. If a correction materially changes evaluation, explain the corrected method and implications accurately in the paper and reviewer response.

## Dataset and experimental setup

Develop collection, annotation, image subsets, and split construction in coherent paragraphs. Avoid splitting a related fact, such as exclusion of an auxiliary subset, into an isolated one-sentence paragraph.

Provide information needed to interpret or reproduce the experiment: data unit, split independence, model/configuration scope, training/evaluation protocol, metric definitions, and resource accounting. Keep interpretation of results in Results.

Distinguish image counts from source-video counts and training randomness from evaluation randomness. Define pooled metrics and per-image means separately. If a reference detector differs across sites, label each denominator correctly.

## Results and discussion

Build discussion around a finding answering the experiment's question. Explain why the design would produce the pattern, then connect that interpretation to the task or resource constraint. Add a qualification when it changes interpretation. This is a paragraph strategy, not a mandatory three-sentence formula.

A task-weighted loss can prioritize small target regions while global PSNR remains dominated by the background. A shorter representation can lose context or spatial coverage. A coded transport can reject a frame, whereas a continuous-valued baseline can yield a distorted representation. Use these explanations only when they match the actual pipeline/evidence.

Illustrative mechanism-focused wording:

> The gap between reconstruction fidelity and detection performance is consistent with the allocation objective. Target regions receive more representation capacity and greater reconstruction weight during training, while the background contributes most of the pixel-level error. Detection performance therefore provides the more direct measure of the intended task benefit.

Do not call an explanation demonstrated when it is only consistent with the observation. Mention a rank reversal or exception when it invalidates a general claim. Avoid restating all table entries or ending each subsection with the same summary sentence.

For ablations, say what changes and what remains controlled. Four component configurations plus five routers on one reference checkpoint is not a complete component-by-router factorial experiment.

For sensitivity, distinguish evaluation-time changes on a fixed checkpoint from retraining each configuration. Keep a default choice separate from a validation optimum. A test-set sweep cannot establish a selection decision made before testing.

## Conclusion

Summarize the problem solved, design responsible, and strongest supported outcome. Use a few representative results if useful, not a recap of every table. Combine related summary paragraphs when fragmented.

Integrate material limitations and future work into a short closing paragraph. Do not introduce new evidence, rankings, or unmeasured energy/deployment/latency claims. A 15-page target is project-specific, not a universal skill requirement.
