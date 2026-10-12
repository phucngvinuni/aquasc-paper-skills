---
name: aquasc-publication-figures
description: Create or restyle manuscript figures and tables using the user's AquaSC advisor-approved conventions. Use for Matplotlib publication plots, subplot captions below panels, regular caption weight, matching x/y-axis fonts, thinner curves, readable single-column layouts, and tables without vertical rules.
---

# AquaSC Publication Figures

Produce exportable, readable paper figures with the presentation conventions approved during the AquaSC revision. Use the current plotting/vector source where available; do not use image generation for numerical plots or edit chart pixels to change results.

## Scope and evidence

Identify active manuscript figures from its includes/labels and locate their plotting sources. Do not regenerate an unused scatter plot or every figure in an old script when only active manuscript figures are requested.

For a style-only task, preserve numerical arrays, error intervals, images, marker coordinates, axis limits/scales, model definitions, and scientific configuration. Preserve current PDF canvas dimensions when manuscript layout must stay stable. Do not edit prose, main captions, or letter locators outside approved scope.

For a result update, use the numerical source designated by the user and synchronize only affected outputs. Preserve missing measurements; do not turn interpolation into a reported baseline result.

## Styling defaults

Read [the figure and table specification](references/figure-and-table-spec.md). Distinctive defaults are:

- Subcaptions such as `(a)` and `(b)` go below each panel's ticks and axis label, with visible clearance. Use regular weight, not bold.
- Use the same resolved font face, normal text style, and label size for x and y. Times New Roman is preferred; use one consistent serif fallback when unavailable and report it.
- Use moderately thin curves, typically 1.0-1.25 pt, rather than older heavy lines. Keep markers distinguishable, legends legible, and grids light.
- Keep legends/model names concise. Put adaptation/configuration/rate explanations in nearby text or caption when needed; distinguish configurations in labels when the comparison would otherwise be ambiguous.
- Use vertically stacked panels for a multi-panel single-column figure when side-by-side panels make text too small. Use a wider arrangement for a genuine full-width figure. Respect an explicitly requested layout.
- Main captions identify the comparison, metrics, and indispensable setting. Put discussion and extensive protocol details in surrounding text. Follow the venue's caption style, with regular caption text as the AquaSC default.
- Tables have horizontal rules and no vertical separators. Use accurate scope labels and model names without decorative size-reduction claims.

## Reusable plotting helper

Use [scripts/aquasc_figure_style.py](scripts/aquasc_figure_style.py) for Matplotlib typography, subcaption placement, curve widths, and PDF/PNG export. Read its API when integrating it into an existing generator. It contains no AquaSC experiment data and does not force numeric limits or canvas size.

- Call `configure_style()` before creating new charts.
- After adding all artists/legends, call `finalize_figure(fig)`. Use `thin_existing=True` when reducing thick curves from an existing plot.
- Export through `save_figure(fig, output_stem)`; it retains the figure canvas and writes vector PDF plus 300-DPI PNG by default.
- Do not call another automatic layout pass after finalization without rechecking caption clearance.
- The finalizer is idempotent for an already finalized figure. Finalize after data and annotations are complete.

[scripts/demo_export.py](scripts/demo_export.py) demonstrates vertical, horizontal, and grid layouts using synthetic data. Its previews are formatting examples, not paper results. Run it with `--output-dir` pointing to a temporary/output directory.

For a hand-drawn/vector architecture figure, edit its native source. Apply the same caption-weight and below-panel convention manually; distinguish data flow from shared/frozen-module connections, and avoid text-marker/arrow overlap. Do not redraw an author's architecture as a different method.

## Verification and delivery

Verify data equality before/after a style-only change, including error-bar endpoints, scatter coordinates, and qualitative image arrays. Check PDF canvas dimensions when preserving layout. Inspect exported images and affected compiled manuscript pages at actual single/full-column size for clipped labels and collisions.

Confirm that the exact resolved font matches on both axes and that subcaptions are regular and below their panels. Compilation alone does not establish plot readability or scientific correctness.

After a layout change, compare final figure/table/page locators. If editing the letter is allowed, update affected locators from the final PDF; if prose edits are forbidden, preserve them and report any mismatch. For an Overleaf push, fetch/inspect upstream first and stage only authorized outputs.

Deliver revised figure sources and final exports, plus a concise summary of style changes and validation. State any font fallback or remaining collision. A figure task does not authorize changing results or publishing to a remote without user authorization.
