# Figure and table specification

These are AquaSC editorial defaults, not a claim that IEEE mandates exact dimensions/font sizes. The target template and actual inclusion width take precedence.

## Typography

Prefer Times New Roman, with the same resolved font file for both axis labels. Use one serif fallback such as Liberation Serif if unavailable and disclose it. Mathematical expressions can use compatible STIX math; ordinary words/units remain in the chosen roman text face.

At the intended printed size, use approximately:

- General text: 9.5 pt.
- Axis labels: 10 pt, regular weight/style on x and y.
- Tick labels: 8.5 pt, regular.
- Legend: 8 pt, regular.
- Subcaption: 9-10 pt, regular, below the panel.

An existing six-panel figure may need smaller labels, but x/y styles and sizes should match. Avoid fixing density by repeatedly shrinking fonts. Inspect actual included size, not just a large preview.

## Lines, markers, and colors

Use 1.0-1.25 pt curves, approximately 0.8 pt reference/dashed lines, and light dotted grids around 0.5-0.6 pt. Existing AquaSC styling used a 0.65 reduction of older heavy curves, capped at 1.25 pt; apply that reduction once. Markers around 4.5-5.5 pt are usually readable without dominating curves.

Keep colors/markers stable for each model across figures. Combine color with shape and line style so close/monochrome curves remain distinguishable. Avoid pale colors for an important baseline.

The reusable palette, adaptable to another paper:

- Primary system: dark blue `#08519C`, circle.
- System variants: blue `#3182BD` or teal `#008C95`, square/diamond.
- Baseline: green `#238B45`, triangle.
- Baseline: orange `#D94801`, square/cross.
- Baseline: purple `#756BB1`, diamond.
- Additional L1/reference variant: magenta `#C2185B`, cross.
- Codec/reference: gray `#4D4D4D`, inverted triangle/dashed line.

These map appearance, not a prescribed ranking or set of model names.

## Panel captions and spacing

Place `(a)`, `(b)`, and descriptions below each plot, after visible ticks and the x label. Keep about 6-8 pt clearance. Do not leave a bold title at the top and add a duplicate below.

For vertical stacks, allow room for the upper panel's x label/caption. A shared legend can sit above all panels without overlap. For two-row grids, row-one captions sit in the inter-row gap and row-two captions below lower x labels.

Wrap a long subcaption instead of extending it over its neighbor. Adjust layout/wording only within authorized scope. Scatter annotations need individual offsets; verify them after changing the evaluated SNR.

Qualitative grids may keep model-name column headers and letters below images. Both should be regular weight. Preserve exact image pixels and detection overlays during styling.

## Size and export

AquaSC defaults were approximately 3.5 inches for one column and 7.16 inches for full width. Use actual template widths for another venue.

A single-column pair is often clearer stacked; full-width comparisons can use horizontal panels or a grid. Do not change an approved orientation unnecessarily.

Export vector PDF with embedded TrueType fonts (`pdf.fonttype=42`) and 300-DPI PNG. Do not make a numerical plot screenshot-only. For stable pagination, retain `figsize` and `bbox_inches=None`; tight bounding-box export changes the PDF media box.

## Content labels and captions

Use only model names when adaptation/configuration are shared and documented in text. Keep suffixes when configurations would otherwise be ambiguous. Remove matched/configured labels when redundant, while retaining conditions needed to interpret unequal comparisons.

Label units/aggregation: pooled mAP versus mean per-image AP, PSNR in dB, complex channel uses per pixel, and the CI's actual resampling unit. Keep related SNR axes consistent when evaluated grids permit it; preserve negative-SNR points unless a narrower display is requested.

Keep main captions short, for example:

> Rate-performance at 5 dB: (a) pooled mAP@0.50 and (b) reconstruction PSNR.

Use that wording only for that setting. Discuss curve crossings, protocol differences, and reconstruction/task gaps in surrounding text.

## Tables

Use `booktabs` or existing compatible horizontal rules. Remove `|` from `tabular` specifications and avoid vertical-rule multicolumns/`\vline`. Preserve precision, groups, footnotes, and meaningful uncertainty labels.

Illustrative skeleton:

```latex
\begin{table}[t]
\centering
\caption{Encoder parameter and memory footprints.}
\begin{tabular}{lrr}
\toprule
Model & Encoder params (M) & Encoder state (MB) \\
\midrule
% Insert actual verified values here.
\bottomrule
\end{tabular}
\end{table}
```

Captions name what is counted. An encoder-only table cannot be called total transmitter complexity. Put reduction ratios in discussion or a meaningful column, not as decorative suffixes in model names. Keep protocol footnotes concise and substantial discussion outside the caption.
