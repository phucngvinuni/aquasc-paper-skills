"""Generate formatting previews with synthetic data; never paper evidence."""

import argparse
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

from aquasc_figure_style import (
    FULL_WIDTH_IN, SINGLE_COLUMN_IN, PALETTE, configure_style, save_figure,
)


def vertical_preview():
    fig, axes = plt.subplots(2, 1, figsize=(SINGLE_COLUMN_IN, 4.6))
    x = np.array([0, 5, 10, 15, 20])
    series = [
        ("System", [0.22, 0.39, 0.51, 0.58, 0.61], "primary", "o", "-"),
        ("Baseline A", [0.15, 0.30, 0.42, 0.50, 0.55], "green", "^", "-."),
        ("Baseline B", [0.13, 0.24, 0.32, 0.38, 0.41], "purple", "D", ":"),
    ]
    for label, y, color, marker, line in series:
        axes[0].plot(x, y, label=label, color=PALETTE[color], marker=marker, ls=line)
        axes[1].plot(x, 18 + 26 * np.asarray(y), color=PALETTE[color], marker=marker, ls=line)
    for ax in axes:
        ax.set_xlabel("Channel SNR (dB)")
        ax.set_xlim(-1, 21)
    axes[0].set_ylabel("Detection mAP@0.50")
    axes[0].set_ylim(0, 0.75)
    axes[1].set_ylabel("Reconstruction PSNR (dB)")
    axes[1].set_ylim(18, 36)
    axes[0].set_title("(a) Task performance (synthetic)")
    axes[1].set_title("(b) Reconstruction quality (synthetic)")
    handles, labels = axes[0].get_legend_handles_labels()
    fig.legend(handles, labels, loc="upper center", ncol=2,
               bbox_to_anchor=(0.55, 0.997), frameon=True)
    return fig


def horizontal_preview():
    fig, axes = plt.subplots(1, 2, figsize=(FULL_WIDTH_IN, 3.25))
    x = np.arange(3)
    axes[0].bar(x - 0.16, [0.30, 0.48, 0.62], width=0.32,
                color=PALETTE["variant"], label="Setting A")
    axes[0].bar(x + 0.16, [0.36, 0.53, 0.66], width=0.32,
                color=PALETTE["primary"], label="Setting B")
    axes[0].errorbar(x + 0.16, [0.36, 0.53, 0.66], yerr=[0.02, 0.025, 0.018],
                      fmt="none", color="black", capsize=3)
    axes[0].set_xticks(x, ["Base", "Component", "Full"])
    axes[0].set_ylabel("Mean AP@0.50 (±95% CI)")
    axes[0].set_ylim(0, 0.75)
    axes[0].set_title("(a) Component comparison (synthetic)")
    axes[0].legend(loc="upper left")
    sizes = [0.9, 6.0, 24.0]
    scores = [0.54, 0.60, 0.63]
    axes[1].plot(sizes, scores, "o-", color=PALETTE["primary"], lw=2.4)
    for name, xx, yy, offset in zip(
        ["Tiny", "Small", "Large"], sizes, scores, [(8, 12), (-8, 16), (-15, 14)]
    ):
        axes[1].annotate(name, (xx, yy), xytext=offset,
                         textcoords="offset points", ha="center", fontsize=8)
    axes[1].set_xscale("log")
    axes[1].set_xlim(0.5, 50)
    axes[1].set_ylim(0.50, 0.70)
    axes[1].set_xlabel("Encoder parameters (M, log scale)")
    axes[1].set_ylabel("Detection mAP@0.50")
    axes[1].set_title("(b) Complexity versus task performance (synthetic)")
    return fig


def grid_preview():
    fig, axes = plt.subplots(2, 3, figsize=(FULL_WIDTH_IN, 4.6), sharex=True)
    snr = np.array([-5, 0, 5, 10, 15, 20])
    for column in range(3):
        performance = np.array([0.14, 0.29, 0.44, 0.56, 0.63, 0.65]) - column * 0.045
        for row in range(2):
            ax = axes[row, column]
            values = performance if row == 0 else 16 + performance * 34
            ax.plot(snr, values, "o-", color=PALETTE["primary"], label="System")
            ax.plot(snr, values * 0.87, "^--", color=PALETTE["green"], label="Baseline")
            ax.set_xlim(-6, 21)
            ax.set_title(f"({chr(97 + row * 3 + column)}) Synthetic setting {column + 1}",
                         fontsize=8.4)
            if row == 1:
                ax.set_xlabel("Channel SNR (dB)", fontsize=8.5)
            if column == 0:
                ax.set_ylabel("mAP@0.50" if row == 0 else "PSNR (dB)", fontsize=8.5)
    handles, labels = axes[0, 0].get_legend_handles_labels()
    fig.legend(handles, labels, loc="upper center", ncol=2,
               bbox_to_anchor=(0.52, 0.995))
    return fig


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-dir", type=Path, required=True)
    args = parser.parse_args()
    font = configure_style()
    for name, make in [
        ("synthetic_vertical", vertical_preview),
        ("synthetic_horizontal", horizontal_preview),
        ("synthetic_grid", grid_preview),
    ]:
        fig = make()
        outputs = save_figure(fig, args.output_dir / name, thin_existing=True)
        print(f"{name}: {font}; " + ", ".join(str(path) for path in outputs))
        plt.close(fig)


if __name__ == "__main__":
    main()
