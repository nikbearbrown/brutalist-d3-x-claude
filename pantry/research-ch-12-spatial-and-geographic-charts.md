# Research: Chapter 12 — Spatial and Geographic Charts
## Brutalist d3 x Claude

**Chapter one-line:** Geographic charts make place visible, but area distortion and aggregation can overpower the data.
**Research date:** 2026-06-01

---

## 1. Primary Sources

1. Friendly, history of thematic cartography and statistical graphics.
2. John Snow's 1854 cholera map.
3. Tufte, analysis of Snow's map.
4. Cairo, *The Truthful Art*.
5. Bertin, *Semiology of Graphics*.
6. D3 geo docs and projections. Source: https://d3js.org/
7. Natural Earth map data documentation.
8. ColorBrewer guidance for map color schemes.
9. Munzner, *Visualization Analysis and Design*.
10. FT Visual Vocabulary for maps.

## 2. Core Concept — State of the Field

Maps answer geographic questions, not every question that happens to contain place. Choropleths should generally show rates or ratios because geographic area competes with the encoded value.

Dot maps, proportional symbols, and flow maps each solve different problems while introducing their own distortion risks.

## 3. Application Domain Examples

1. Choropleth for normalized rates.
2. Dot density map for spatial concentration.
3. Bubble/proportional symbol map for absolute values.
4. Connection map for routes or relationships.
5. Flow map for volume moving between places.

## 4. Book's Thesis Connection

Claude can wire D3 projections and TopoJSON, but the author must decide whether the map clarifies a spatial pattern or merely gives geography undue authority.

## 5. AI Wayback Machine — Candidate Figures

1. Charles Dupin — early choropleth mapping.
2. John Snow — dot map and epidemiological reasoning.
3. Charles Joseph Minard — flow map.
4. Cynthia Brewer — ColorBrewer and cartographic color.

## 6. Pedagogical Delivery Research

Use an absolute-count choropleth failure, then rebuild it as a rate choropleth and a proportional symbol map.

## 7. Representation and Display Research

Checklist:

- Rate or ratio for choropleth?
- Projection appropriate and disclosed?
- Geographic area not mistaken for data magnitude?
- Color scale sequential/diverging/categorical as needed?
- Missing data shown distinctly?
- Legend supports exact enough interpretation?

## 8. Open Questions and Research Gaps

1. Add a sourced example of choropleth area bias.
2. Include map projection selection guidance.
3. Write Claude prompts for GeoJSON/TopoJSON validation.
