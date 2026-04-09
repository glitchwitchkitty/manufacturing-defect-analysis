# 🔩 Manufacturing Defect Analysis
**Capstone Project | DAT 475 | Southern New Hampshire University**

> *When a manufacturing facility's defect rates won't stop climbing, you stop guessing and start asking the data better questions.*

---

## The Problem

A manufacturing facility was seeing a high and persistent volume of welding and assembly defects concentrated in their Manual Finish Area. The question wasn't just *how many* defects — it was *which production models were driving them*, *where* they were occurring, and *whether those differences were statistically meaningful or just noise.*

Spoiler: they were not noise.

---

## What I Did

This project combined root cause analysis, statistical testing, and data visualization to turn a messy defect dataset into actionable recommendations.

**Tools used:** Python (pandas, scipy, matplotlib), Power BI, Jupyter Notebook

### Root Cause Analysis
Built a custom Python-generated **Ishikawa (Fishbone) Diagram** mapping contributing factors across six categories: Methods, Manpower, Measurement, Machines, Materials, and Environment. The diagram exports to SVG for clean, scalable rendering.

📄 [`fishbone.py`](fishbone.py)

### Statistical Analysis
Ran a **one-way ANOVA** in Python to test whether production model type had a statistically significant effect on weekly defect counts.

**Result:** F = 17.64, p < 0.001 — null hypothesis rejected. Production model type *significantly* influences defect variation. This wasn't a gut feeling anymore; it had math behind it.

📓 [`anova_test_project3.ipynb`](anova_test_project3.ipynb)

### Dashboard
Built an interactive **Power BI dashboard** visualizing:
- Defect volume by production area (Pareto-style)
- Weekly defect trends across the top 3 production models
- ANOVA results surfaced as KPI cards
- Multi-chart Pareto breakdown by defect type and area

📊 [`project3_dashboard_draft2.pbix`](project3_dashboard_draft2.pbix) *(requires Power BI Desktop)*
🖼️ [`dashboard_preview.pdf`](assets/dashboard_preview.pdf) *(no install needed — start here)*

---

## What I Found

- **Production Line 3** had the highest defect volume (544 total)
- **Model 595130-195** consistently showed the highest average weekly defect count
- Defects were statistically non-uniform across models — meaning targeted intervention is both justified and measurable
- Root cause analysis pointed to operator variability, inconsistent procedures, and machine calibration as the highest-leverage areas for improvement

---

## The Recommendation

Process improvement efforts should prioritize **Model 595130-195** and **Production Line 3** first. The ANOVA results mean you can measure whether interventions actually work — which is the whole point.

---

## Repo Structure

```
manufacturing-defect-analysis/
├── README.md
├── fishbone.py                      # Custom Python fishbone diagram generator
├── anova_test_project3.ipynb        # Statistical analysis notebook
├── anova_defects_per_week.csv       # Dataset
├── project3_dashboard_draft2.pbix   # Power BI dashboard file
└── assets/
    ├── fishbone_diagram.png         # Exported fishbone visual
    └── dashboard_preview.pdf        # Dashboard export (human-readable)
```

---

## About Me

I'm Kat — data analyst, creative coder, chaos gremlin. I like finding the signal in messy systems and building tools that make the answer obvious.

📎 [Portfolio](https://glitchwitchkitty.github.io/chaosgremlinhq-portfolio/) | [GitHub](https://github.com/glitchwitchkitty)