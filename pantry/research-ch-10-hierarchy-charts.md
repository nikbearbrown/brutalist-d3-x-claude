# Research: Chapter 10 — Hierarchy Charts
## Brutalist d3 x Claude

**Chapter one-line:** Hierarchy charts choose between proportion, depth, and exact structure.
**Research date:** 2026-06-01

---

## 1. Primary Sources

1. Shneiderman, treemap work, 1991.
2. Bruls, Huizing, and van Wijk, "Squarified Treemaps," 1999.
3. Bertin, *Semiology of Graphics*.
4. Munzner, *Visualization Analysis and Design*.
5. Tufte, *The Visual Display of Quantitative Information*.
6. D3 hierarchy docs for tree, cluster, treemap, pack, and partition. Source: https://d3js.org/
7. Friendly, history of data visualization.
8. Ware, visual thinking and Gestalt principles.
9. Cairo, *The Truthful Art*.
10. FT Visual Vocabulary.

## 2. Core Concept — State of the Field

Hierarchical charts expose nested structure, but they emphasize different questions. Treemaps emphasize proportion; sunbursts emphasize depth; circle packing handles irregular hierarchy visually but uses space less efficiently; node-link trees preserve exact parent-child structure.

## 3. Application Domain Examples

1. Treemap for nested proportions such as budgets or disk usage.
2. Sunburst for path and depth.
3. Circle packing for irregular nested domains.
4. Tree diagram for exact structure and navigation.
5. Dendrogram for clustering and similarity structure.

## 4. Book's Thesis Connection

Claude can infer a hierarchy layout from JSON, but the author must specify whether the reader should compare sizes, follow branches, or inspect exact structure.

## 5. AI Wayback Machine — Candidate Figures

1. Ben Shneiderman — treemaps.
2. Bruls, Huizing, van Wijk — squarified treemap algorithm.
3. Jacques Bertin — area encoding.
4. Tamara Munzner — task/data abstraction.

## 6. Pedagogical Delivery Research

Show the same hierarchy as a treemap, sunburst, circle packing chart, and tree. Have students name what each makes easy and what each suppresses.

## 7. Representation and Display Research

Checklist:

- Hierarchy depth manageable?
- Values sum correctly through parent nodes?
- Layout choice matches task?
- Labels legible at small nodes?
- Interaction supports drill-down where depth is high?
- Area comparisons not overclaimed?

## 8. Open Questions and Research Gaps

1. Add a rule of thumb for depth limits by chart type.
2. Include accessibility guidance for interactive hierarchy charts.
3. Source examples from filesystem, budgets, biology, or organizational charts.
