# Research: Chapter 11 — Flow and Network Charts
## Brutalist d3 x Claude

**Chapter one-line:** Flow and network charts must distinguish quantity, direction, and mere connection.
**Research date:** 2026-06-01

---

## 1. Primary Sources

1. Bertin, *Semiology of Graphics*.
2. Munzner, *Visualization Analysis and Design*.
3. Tufte, *The Visual Display of Quantitative Information*.
4. Cairo, *The Truthful Art*.
5. D3 sankey, force, chord, and shape docs. Source: https://d3js.org/
6. D3 Sankey plugin documentation.
7. Friendly, history of flow maps and statistical graphics.
8. Ware, Gestalt connection and visual thinking.
9. Heer and Bostock, graphical perception research.
10. FT Visual Vocabulary for flow and networks.

## 2. Core Concept — State of the Field

Flow charts encode quantity through width when width is proportional to value. Network charts encode relationships and topology; they often do not encode amount unless edge width or color is explicitly mapped.

The core failure is using a network-looking chart when the reader needs quantities, or a flow chart when the reader only needs topology.

## 3. Application Domain Examples

1. Sankey for energy, money, or funnel flows.
2. Alluvial for categorical shifts over time.
3. Chord for reciprocal inter-entity flows.
4. Arc diagram for ordered relationships.
5. Force-directed graph for clusters, bridges, and outliers.

## 4. Book's Thesis Connection

Claude can create network spectacle faster than humans can evaluate it. The reader must specify whether edges mean existence, amount, direction, sequence, or category transition.

## 5. AI Wayback Machine — Candidate Figures

1. Captain Matthew Sankey — energy flow diagrams.
2. Jacques Bertin — line and width channels.
3. Tamara Munzner — network task abstraction.
4. Alberto Cairo — chart selection by question.

## 6. Pedagogical Delivery Research

Use one dataset twice: as an unweighted network and as a weighted Sankey. Ask which question each chart can answer.

## 7. Representation and Display Research

Checklist:

- Does edge width encode quantity?
- Direction shown when direction matters?
- Layout stable enough to interpret?
- Hairball risk mitigated?
- Labels and tooltips support exact reading?
- Network not used when a table or matrix is clearer?

## 8. Open Questions and Research Gaps

1. Decide when adjacency matrices should appear as a counterexample.
2. Add prompt constraints for force simulations and reproducible layouts.
3. Source a humanitarian coordination network example.
