import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Polygon
import textwrap



def wrap(s, width=26):
    return "\n".join(textwrap.wrap(s, width=width))

def draw_fishbone(problem, categories, outpath="fishbone.png"):
    """
    categories: list of dicts like:
      {"name": "People", "causes": ["a","b","c"]}
      {"name": "Process", "causes": ["a","b","c"]}
    """

    fig, ax = plt.subplots(figsize=(14, 6))
    ax.set_xlim(0, 14)
    ax.set_ylim(-4, 4)
    ax.axis("off")

    # Spine
    spine_y = 0
    ax.plot([1, 11.2], [spine_y, spine_y], linewidth=2)

    # Head (problem box)
    head_w, head_h = 2.5, 2.2
    head_x, head_y = 11.4, -head_h/2
    ax.add_patch(Rectangle((head_x, head_y), head_w, head_h, fill=False, linewidth=2))
    ax.text(head_x + head_w/2, 0, wrap(problem, 24),
            ha="center", va="center", fontsize=12, fontweight="bold")

    # Tail (optional small line)
    #ax.plot([0.6, 1], [0, 0], linewidth=2)
    # Tail (triangle)
    tail = Polygon(
        [
            (1.0, 0),     # tip of the tail (leftmost)
            (0.6, 0.8),   # top back
            (0.6, -0.8),  # bottom back
        ],
        closed=True,
        fill=False,
        linewidth=2
    )
    ax.add_patch(tail)


    # Layout controls
    # x positions where ribs connect to spine (spread evenly)
    rib_attach_x = [4.8, 4.8, 8, 8, 11.0, 11.0]  # supports up to 4 categories 
    # Angles: top ribs go up-left, bottom ribs go down-left
    rib_dx = 2.5     # how far left the rib extends
    rib_dy = 2.9      # how far up/down the rib extends
    cause_dx = 0.5    # small cause tick length
    cause_text_pad = 0.15

    # If you have 3 categories, we’ll use first 3 slots
    slots = rib_attach_x[:len(categories)]

    for slot_x, cat in zip(slots, categories):
        side = cat["side"].lower()
        is_top = (list(categories).index(cat) % 2 == 0)

        # Main rib end point (left end of the diagonal rib)
        end_x = slot_x - rib_dx
        end_y = rib_dy if is_top else -rib_dy

        # Draw diagonal rib
        ax.plot([slot_x, end_x], [0, end_y], linewidth=2)

        # Category label near the rib end
        label_x = end_x - 0.2
        label_y = end_y + (0.35 if is_top else -0.35)
        ax.text(label_x, label_y, cat["name"],
                ha="right", va="center", fontsize=11, fontweight="bold")

        # Causes: place along the rib, stacked outward from the spine
        causes = cat.get("causes", [])
        n = len(causes)

        # Choose y offsets for cause ticks so they’re evenly spaced
        # place them around the rib’s midsection rather than at the very end.
        # For top: ticks above the rib; for bottom: ticks below.
        if n > 0:
            # positions along the rib from near spine to near end
            t_values = [0.25 + i*(0.55/(max(n-1, 1))) for i in range(n)]  # 0..1 along rib
            for t, cause in zip(t_values, causes):
                # point on rib
                px = slot_x + (end_x - slot_x) * t
                py = 0 + (end_y - 0) * t

                # cause tick direction: roughly perpendicular-ish
                # draw a short horizontal tick for clean readability
                tick_dir = -1 if is_top else 1
                ax.plot([px, px - cause_dx], [py, py + 0], linewidth=1.8)

                # text aligned with tick
                ax.text(px - cause_dx - cause_text_pad, py,
                        wrap(f"- {cause}", 28),
                        ha="right", va="center", fontsize=9)

    # Title (optional)
    ax.text(0.6, 3.5, "Fishbone Diagram (Ishikawa) by Kat M.\n", fontsize=12, fontweight="bold")

    plt.tight_layout()
    plt.savefig('fishbone_diagram.svg', format='svg', bbox_inches='tight')
    plt.show()

# ---- content (assignment) ----
problem = "High Frequency of Welding and Assembly Defects in Manual Finish Area"

categories = [
    {"name": "Methods", "side": "top", "causes": [
        "Inconsistent assembly procedures",
        "Improper soldering techniques",
        "Lack of standardized work instructions",
        "Insufficient process controls",
        "Poor handling methods during transfer"
    ]},
    {"name": "Manpower", "side": "bottom", "causes": [
        "Inadequate operator training", 
        "High operator variablility",
        "Fatigue due to increased demand",
        "Inattention during manual assembly",
        "Skill mismatch across shifts"
    ]},
    {"name": "Measurement", "side": "top", "causes": [
        "Infrequent inspection checks", 
        "Subjective visual quality assessments",
        "Inconsistent defect classification",
        "Limited process performance metrics"
    ]},
    {"name": "Machines", "side": "bottom", "causes": [
        "Wave solder machine variability",
        "Fixture misalignment",
        "Inadequate machine calibration",
        "Equipment wear"
    ]},
    {"name": "Materials", "side": "bottom", "causes": [
        "Poor solder quality",
        "Defective components",
        "Inconsistent component specifications",
        "Damaged pins or pads",
        "Wetting conditions"
    ]},
    {"name": "Environment", "side": "bottom", "causes": [
        "Poor lighting",
        "Workspace congestion",
        "Temperature variations",
        "Distractions/noise",
        "Time pressure"
    ]},
]


draw_fishbone(problem, categories, outpath="fishbone.png")
