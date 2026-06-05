# Research: Chapter 08 — Relationship and Correlation Charts
## Brutalist d3 x Claude

**Chapter one-line:** Relationship charts show association, but visual strength must not be mistaken for causal evidence.
**Research date:** 2026-06-01

---

## 1. Primary Sources

1. Cleveland and McGill, "Graphical Perception," 1984.
2. Cairo, *The Truthful Art* and "Ethical Infographics" examples.
3. Stevens, psychophysical power law.
4. Munzner, *Visualization Analysis and Design*.
5. Tufte, *The Visual Display of Quantitative Information*.
6. D3 scales, symbols, shapes, and interaction docs. Source: https://d3js.org/
7. Heer and Bostock, "Crowdsourcing Graphical Perception."
8. Friendly, history of statistical graphics.
9. Evergreen and Emery data visualization checklist.
10. Kelleher and Wagener visualization guidelines.

## 2. Core Concept — State of the Field

Scatterplots use position on common scales, making them strong for two quantitative variables. Bubble charts add area as a third channel, which introduces perceptual risk if radius is scaled instead of area.

Correlation annotations should be treated as ethical context, not decorative text. Trend lines, Pearson r, and visual clustering can invite causal readings unless the chart explicitly limits the claim.

## 3. Application Domain Examples

1. Scatterplot with trend line and correlation readout.
2. Bubble chart with proportional area for a third quantitative variable.
3. Connected scatterplot for changing relationships over time.
4. Parallel coordinates for multivariate comparison and brushing.
5. Heatmap for two categorical axes plus quantitative intensity.

## 4. Book's Thesis Connection

Claude can make impressive relationship graphics, but the human author must specify the claim boundary: association, trend, clustering, prediction, or causation.

## 5. AI Wayback Machine — Candidate Figures

1. Francis Galton — correlation and regression history.
2. Jacques Bertin — channels and visual variables.
3. Stanley Smith Stevens — nonlinear area perception.
4. Alberto Cairo — correlation and uncertainty ethics.

## 6. Pedagogical Delivery Research

Use the same scatterplot with and without a causation caveat. Then ask readers how the visual argument changes when the annotation is removed.

## 7. Representation and Display Research

Checklist:

- Axes labeled with units?
- Trend line method disclosed?
- Correlation not framed as causation?
- Bubble area, not radius, scaled to value?
- Overplotting handled with transparency, jitter, or density?
- Parallel coordinate axis order explained?

## 8. Open Questions and Research Gaps

1. Add a clear example where a confounder reverses a relationship.
2. Include prompt language for causal humility in chart annotations.
3. Decide whether to introduce residual plots or keep the chapter visual-only.
