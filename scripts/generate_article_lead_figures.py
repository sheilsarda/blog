#!/usr/bin/env python3
"""Original lead figures for posts that had no square-safe thumbnail.

These are schematic diagrams, not reproductions of paper figures.
The canvas is 5:4. Homepage thumbs are a square center crop, so every
label sits inside the center square (x from 1.0 to 9.0 on a 10 by 8 canvas).
"""

from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "assets" / "posts"

W, H = 10.0, 8.0
NAVY = "#022169"
INK = "#1c2430"
MUTED = "#5c6570"
PURPLE = "#7C3AED"

plt.rcParams.update(
    {
        "font.family": "Segoe UI",
        "font.size": 13,
        "text.color": INK,
    }
)


def new_ax():
    fig, ax = plt.subplots(figsize=(W, H), dpi=160)
    ax.set_xlim(0, W)
    ax.set_ylim(0, H)
    ax.set_aspect("equal")
    ax.axis("off")
    fig.subplots_adjust(0, 0, 1, 1)
    fig.patch.set_facecolor("white")
    ax.set_facecolor("white")
    return fig, ax


def card(ax, x, y, w, h, face, edge, lw=1.8):
    ax.add_patch(
        FancyBboxPatch(
            (x, y),
            w,
            h,
            boxstyle="round,pad=0.015,rounding_size=0.14",
            facecolor=face,
            edgecolor=edge,
            linewidth=lw,
            mutation_aspect=1,
            joinstyle="round",
        )
    )


def arrow(ax, x0, y0, x1, y1, color=NAVY):
    ax.add_patch(
        FancyArrowPatch(
            (x0, y0),
            (x1, y1),
            arrowstyle="-|>",
            mutation_scale=14,
            linewidth=1.6,
            color=color,
            shrinkA=0,
            shrinkB=0,
        )
    )


def title(ax, text, y=7.35):
    ax.text(5, y, text, ha="center", va="center", fontsize=20, color=NAVY, fontweight="bold")


def save(fig, path: Path):
    path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(path, dpi=160, facecolor="white")
    plt.close(fig)
    print(path.relative_to(ROOT))


def fig_four_properties(path: Path):
    fig, ax = new_ax()
    title(ax, "Four properties of the simulated data")
    cells = [
        (1.05, 3.62, "#EEF2FF", "#4338CA", "Selection", "TUCO", "which demonstrations you keep"),
        (5.15, 3.62, "#ECFEFF", "#0E7490", "Coverage", "SimVLA", "which states the data covers"),
        (1.05, 0.42, "#FFF7ED", "#C2410C", "Behavior", "OCBench", "how the demonstrations move"),
        (5.15, 0.42, "#F5F3FF", PURPLE, "Appearance", "Splat2Act", "what the cameras see"),
    ]
    for x, y, face, edge, name, paper, detail in cells:
        card(ax, x, y, 3.8, 2.9, face, edge)
        ax.text(x + 1.9, y + 1.95, name, ha="center", va="center", fontsize=22, color=edge, fontweight="bold")
        ax.text(x + 1.9, y + 1.25, paper, ha="center", va="center", fontsize=15, color=INK)
        ax.text(x + 1.9, y + 0.7, detail, ha="center", va="center", fontsize=13, color=MUTED)
    save(fig, path)


def fig_stereo(path: Path):
    fig, ax = new_ax()
    title(ax, "Measure on stereo. Apply to mono.")
    cols = [
        (1.05, "#FFF7ED", "#C2410C", "1,000 h", "Stereo + IMU", "depth, pose, hands"),
        (3.78, "#EEF2FF", "#4338CA", "RGB", "Student", "intrinsics only"),
        (6.51, "#ECFEFF", "#0E7490", "100,000 h", "Mono fleet", "scale still to check"),
    ]
    for x, face, edge, big, name, detail in cols:
        card(ax, x, 1.85, 2.44, 4.55, face, edge)
        ax.text(x + 1.22, 4.85, big, ha="center", va="center", fontsize=20, color=edge, fontweight="bold")
        ax.text(x + 1.22, 3.85, name, ha="center", va="center", fontsize=15, color=INK, fontweight="bold")
        ax.text(x + 1.22, 3.25, detail, ha="center", va="center", fontsize=12, color=MUTED)
    arrow(ax, 3.54, 4.15, 3.72, 4.15)
    arrow(ax, 6.27, 4.15, 6.45, 4.15)
    ax.text(3.63, 4.48, "labels", ha="center", va="center", fontsize=11, color=MUTED)
    ax.text(6.36, 4.48, "apply", ha="center", va="center", fontsize=11, color=MUTED)
    ax.text(
        5,
        0.95,
        "Held-out rig recordings test the student on RGB alone.",
        ha="center",
        va="center",
        fontsize=13,
        color=MUTED,
    )
    save(fig, path)


def fig_gap_clean(path: Path):
    fig, ax = new_ax()
    title(ax, "Where the compute is spent")
    steps = [
        (5.2, "#EEF2FF", "#4338CA", "01", "Author", "Agents wire a typed skill graph"),
        (3.2, "#FFF7ED", "#C2410C", "02", "Rehearse", "Thirty scenes, then edit the graph"),
        (1.2, "#F0FDFA", "#0F766E", "03", "Run", "Interpreter, no model in the loop"),
    ]
    for y, face, edge, num, name, detail in steps:
        card(ax, 1.2, y, 7.6, 1.65, face, edge)
        ax.text(1.9, y + 0.82, num, ha="center", va="center", fontsize=14, color=edge, fontweight="bold")
        ax.text(2.45, y + 1.08, name, ha="left", va="center", fontsize=20, color=edge, fontweight="bold")
        ax.text(2.45, y + 0.52, detail, ha="left", va="center", fontsize=14, color=INK)
    arrow(ax, 5.0, 5.12, 5.0, 4.95)
    arrow(ax, 5.0, 3.12, 5.0, 2.95)
    ax.text(
        5,
        0.58,
        "A VLA spends the same intelligence on every action.",
        ha="center",
        va="center",
        fontsize=13,
        color=MUTED,
    )
    save(fig, path)


def fig_sla(path: Path):
    fig, ax = new_ax()
    title(ax, "Who can sign the number")
    cols = [
        (1.05, "#F8FAFC", "#64748B", "Pitch", "Business development", "demos stand in"),
        (3.78, "#F5F3FF", PURPLE, "Contract", "Engineering", "sim, within 10%", 2.2),
        (6.51, "#F8FAFC", "#64748B", "Delivery", "Systems architect", "not the catalog system"),
    ]
    for item in cols:
        x, face, edge, name, who, detail = item[:6]
        lw = item[6] if len(item) > 6 else 1.8
        card(ax, x, 2.05, 2.44, 4.4, face, edge, lw=lw)
        ax.text(x + 1.22, 5.35, name, ha="center", va="center", fontsize=18, color=edge, fontweight="bold")
        ax.text(x + 1.22, 4.45, who, ha="center", va="center", fontsize=12, color=INK)
        ax.text(x + 1.22, 3.15, detail, ha="center", va="center", fontsize=12, color=MUTED)
    arrow(ax, 3.54, 4.25, 3.72, 4.25, color="#94A3B8")
    arrow(ax, 6.27, 4.25, 6.45, 4.25, color="#94A3B8")
    card(ax, 1.15, 0.4, 7.7, 1.25, "#FFF7ED", "#C2410C")
    ax.text(
        5,
        1.02,
        "The timing sim is upstream of the SLA.",
        ha="center",
        va="center",
        fontsize=15,
        color="#9A3412",
        fontweight="bold",
    )
    save(fig, path)


def fig_six(path: Path):
    fig, ax = new_ax()
    title(ax, "What each training method needs")
    cells = [
        (1.05, 3.7, "#EEF2FF", "#4338CA", "Behavior cloning", "demonstrations"),
        (3.78, 3.7, "#ECFEFF", "#0E7490", "RL in simulation", "reward and resets"),
        (6.51, 3.7, "#FFF7ED", "#C2410C", "Distill a teacher", "successful rollouts"),
        (1.05, 0.85, "#F0FDFA", "#0F766E", "RL on the robot", "time on hardware"),
        (3.78, 0.85, "#F5F3FF", PURPLE, "Generative data", "a model, seed demos"),
        (6.51, 0.85, "#F8FAFC", NAVY, "Edit the library", "agent, sim, toolbox"),
    ]
    for x, y, face, edge, name, need in cells:
        card(ax, x, y, 2.44, 2.45, face, edge)
        ax.text(x + 1.22, y + 1.45, name, ha="center", va="center", fontsize=13, color=edge, fontweight="bold")
        ax.text(x + 1.22, y + 0.8, need, ha="center", va="center", fontsize=11, color=MUTED)
    save(fig, path)


def fig_contact(path: Path):
    fig, ax = new_ax()
    title(ax, "Contact does not wait for the chunk")
    card(ax, 1.05, 3.15, 3.15, 3.15, "#EEF2FF", "#4338CA")
    card(ax, 5.8, 3.15, 3.15, 3.15, "#FEF2F2", "#BE123C")
    ax.text(2.62, 5.35, "5–50 Hz", ha="center", va="center", fontsize=24, color="#4338CA", fontweight="bold")
    ax.text(2.62, 4.45, "VLA chunk", ha="center", va="center", fontsize=16, color=INK, fontweight="bold")
    ax.text(2.62, 3.8, "committed plan", ha="center", va="center", fontsize=13, color=MUTED)
    ax.text(7.38, 5.35, "1–2 kHz", ha="center", va="center", fontsize=24, color="#BE123C", fontweight="bold")
    ax.text(7.38, 4.45, "Contact", ha="center", va="center", fontsize=16, color=INK, fontweight="bold")
    ax.text(7.38, 3.8, "force you cannot see", ha="center", va="center", fontsize=12, color=MUTED)
    ax.text(5, 4.85, "100–1000×", ha="center", va="center", fontsize=14, color=NAVY, fontweight="bold")
    chips = [
        (1.05, "Occlusion"),
        (3.78, "Blind chunk"),
        (6.51, "Wrong modality"),
    ]
    for x, label in chips:
        card(ax, x, 0.85, 2.44, 1.35, "#F8FAFC", "#94A3B8", lw=1.4)
        ax.text(x + 1.22, 1.52, label, ha="center", va="center", fontsize=13, color=NAVY, fontweight="bold")
    save(fig, path)


def main():
    fig_four_properties(ASSETS / "paper-review-tuco-simvla-ocbench-splat2act" / "four-properties-of-sim-data.png")
    fig_stereo(ASSETS / "distilling-a-thousand-stereo-hours-into-a-recipe-for-mono-video" / "stereo-teacher-mono-student.png")
    fig_gap_clean(ASSETS / "compute-into-working-policy" / "design-time-graph.png")
    fig_sla(ASSETS / "selling-and-gtm-in-robotics" / "who-signs-the-sla.png")
    fig_six(ASSETS / "six-ways-labs-train-manipulation-policies" / "what-each-method-needs.png")
    fig_contact(ASSETS / "vlas-in-contact" / "frequency-gap.png")


if __name__ == "__main__":
    main()
