"""Portable AquaSC plotting style. Requires matplotlib; contains no experiment data.

Call configure_style() before new plots. Finalize after all artists/legends exist,
then save_figure(fig, output_stem). For older thick curves, thin_existing=True
applies the advisor's reduction once. Existing limits and canvas size are kept.
"""

from functools import lru_cache
from pathlib import Path
import re
import warnings

import matplotlib as mpl
from matplotlib import font_manager


SINGLE_COLUMN_IN = 3.5
FULL_WIDTH_IN = 7.16
PALETTE = {
    "primary": "#08519C",
    "variant": "#3182BD",
    "teal": "#008C95",
    "green": "#238B45",
    "orange": "#D94801",
    "purple": "#756BB1",
    "magenta": "#C2185B",
    "reference": "#4D4D4D",
}


@lru_cache(maxsize=8)
def resolve_font(preferred="Times New Roman"):
    """Resolve one regular font file for both axes; return (path, family)."""
    candidates = dict.fromkeys(
        [preferred, "Liberation Serif", "Times", "Nimbus Roman", "DejaVu Serif"]
    )
    for family in candidates:
        props = font_manager.FontProperties(
            family=family, style="normal", weight="normal"
        )
        try:
            path = font_manager.findfont(props, fallback_to_default=False)
        except ValueError:
            continue
        return path, font_manager.FontProperties(fname=path).get_name()
    raise RuntimeError("No usable serif font found. Install a serif font first.")


def configure_style(font_family="Times New Roman"):
    """Set defaults for new charts; return the actual chosen font family."""
    _, resolved = resolve_font(font_family)
    if resolved != font_family:
        warnings.warn(
            f"{font_family} unavailable; using {resolved} consistently.",
            stacklevel=2,
        )
    mpl.rcParams.update({
        "font.family": "serif",
        "font.serif": [resolved],
        "mathtext.fontset": "stix",
        "font.size": 9.5,
        "axes.labelsize": 10,
        "axes.labelweight": "normal",
        "axes.titlesize": 9.5,
        "axes.titleweight": "normal",
        "xtick.labelsize": 8.5,
        "ytick.labelsize": 8.5,
        "legend.fontsize": 8,
        "lines.linewidth": 1.15,
        "lines.markersize": 5,
        "grid.color": "#E0E0E0",
        "grid.linestyle": ":",
        "grid.linewidth": 0.55,
        "axes.grid": True,
        "axes.axisbelow": True,
        "pdf.fonttype": 42,
        "ps.fonttype": 42,
        "figure.facecolor": "white",
        "savefig.facecolor": "white",
        "savefig.bbox": None,
    })
    return resolved


def _font(path, size):
    return font_manager.FontProperties(
        fname=path, size=size, weight="normal", style="normal"
    )


def _plain_label(text):
    # Keep arbitrary mathematical expressions intact; these text symbols need
    # not switch an entire label to a different font face.
    return (text.replace(r"$\pm 95\%$", "±95%")
                .replace(r"$\\pm 95\\%$", "±95%")
                .replace(r"$\Delta$", "Δ"))


def _wrap_caption(text, font, renderer, width):
    lines = []
    for paragraph in text.splitlines():
        current = ""
        for word in paragraph.split():
            candidate = (current + " " + word).strip()
            measured = renderer.get_text_width_height_descent(
                candidate, font, ismath=False
            )[0]
            if current and measured > width:
                lines.append(current)
                current = word
            else:
                current = candidate
        lines.append(current)
    return "\n".join(lines)


def _style_line(line, reduction):
    old = line.get_linewidth()
    if old > 0:
        line.set_linewidth(max(0.75, min(1.25, old * reduction)))
    line.set_markeredgewidth(min(1.0, line.get_markeredgewidth()))


def finalize_figure(fig, *, thin_existing=False, font_family="Times New Roman"):
    """Style artists and place panel captions below axes, without editing data.

    Titles beginning '(a)', '(b)', etc. become subcaptions. Other titles such as
    qualitative model-column headers remain at the top, in regular weight.
    Existing letter-only x labels are retained below qualitative images.
    This function is idempotent; do not add new artists after finalization.
    """
    previous = getattr(fig, "_aquasc_style_result", None)
    if previous is not None:
        return previous
    font_path, resolved = resolve_font(font_family)
    x_sizes = [ax.xaxis.label.get_fontsize() for ax in fig.axes
               if ax.get_xlabel() and not re.fullmatch(r"\([a-z]\)", ax.get_xlabel())]
    y_sizes = [ax.yaxis.label.get_fontsize() for ax in fig.axes if ax.get_ylabel()]
    label_size = min(x_sizes or y_sizes or [mpl.rcParams["axes.labelsize"]])
    reduction = 0.65 if thin_existing else 1.0
    captions = []
    for ax in fig.axes:
        ax.set_xlabel(_plain_label(ax.get_xlabel()))
        ax.set_ylabel(_plain_label(ax.get_ylabel()))
        for label in (ax.xaxis.label, ax.yaxis.label):
            label.set_fontproperties(_font(font_path, label_size))
        for text in ax.get_xticklabels() + ax.get_yticklabels():
            text.set_fontproperties(_font(font_path, text.get_fontsize()))
        for text in (ax.xaxis.get_offset_text(), ax.yaxis.get_offset_text()):
            text.set_fontproperties(_font(font_path, text.get_fontsize()))
        title = ax.get_title()
        if re.match(r"^\([a-z]\)", title):
            size = ax.title.get_fontsize()
            ax.set_title("")
            caption = ax.annotate(
                title, xy=(0.5, 0), xycoords="axes fraction",
                xytext=(0, -30), textcoords="offset points",
                ha="center", va="top", annotation_clip=False,
                fontproperties=_font(font_path, size),
            )
            caption.set_in_layout(True)
            ax._aquasc_panel_caption = caption
            captions.append((ax, caption, title))
        elif title:
            ax.title.set_fontproperties(_font(font_path, ax.title.get_fontsize()))
        for line in ax.lines:
            _style_line(line, reduction)
        for collection in ax.collections:
            if hasattr(collection, "get_linewidths"):
                collection.set_linewidths([
                    max(0.65, min(1.2, width * reduction)) if width > 0 else 0
                    for width in collection.get_linewidths()
                ])
        legend = ax.get_legend()
        if legend:
            for line in legend.get_lines():
                _style_line(line, reduction)
            for text in legend.get_texts():
                text.set_fontproperties(_font(font_path, text.get_fontsize()))
    for legend in fig.legends:
        for line in legend.get_lines():
            _style_line(line, reduction)
        for text in legend.get_texts():
            text.set_fontproperties(_font(font_path, text.get_fontsize()))

    if captions:
        # A second pass accommodates wrapping after panel widths change.
        for _ in range(2):
            fig.canvas.draw()
            renderer = fig.canvas.get_renderer()
            for ax, caption, title in captions:
                caption.set_text(_wrap_caption(
                    title, caption.get_fontproperties(), renderer, ax.bbox.width * 0.98
                ))
                decorations = [ax.xaxis.label] + ax.get_xticklabels()
                boxes = [text.get_window_extent(renderer) for text in decorations
                         if text.get_visible() and text.get_text()]
                clearance = max(
                    [(ax.bbox.y0 - box.y0) * 72 / fig.dpi for box in boxes] or [5]
                ) + 8
                caption.set_position((0, -clearance))
            legend_top = min([
                legend.get_window_extent(renderer).y0 / fig.bbox.height - 0.025
                for legend in fig.legends
            ] or [0.98])
            fig.tight_layout(
                pad=0.6, h_pad=1.4, w_pad=0.7,
                rect=(0.005, 0.005, 0.995, legend_top),
            )
    fig.canvas.draw()
    result = {"font_family": resolved, "font_path": font_path,
              "axis_label_size": label_size, "subcaptions": len(captions)}
    fig._aquasc_style_result = result
    return result


def save_figure(fig, output_stem, *, formats=("pdf", "png"), dpi=300,
                thin_existing=False, font_family="Times New Roman"):
    """Write final exports with the original canvas size; return their paths."""
    formats = tuple(fmt.lower() for fmt in formats)
    if not formats or any(fmt not in {"pdf", "png"} for fmt in formats):
        raise ValueError("Supported output formats are pdf and png.")
    finalize_figure(fig, thin_existing=thin_existing, font_family=font_family)
    stem = Path(output_stem)
    if stem.suffix.lower() in {".pdf", ".png"}:
        stem = stem.with_suffix("")
    stem.parent.mkdir(parents=True, exist_ok=True)
    outputs = []
    for fmt in formats:
        path = stem.parent / (stem.name + "." + fmt)
        fig.savefig(path, format=fmt, dpi=dpi, bbox_inches=None)
        outputs.append(path)
    return outputs
