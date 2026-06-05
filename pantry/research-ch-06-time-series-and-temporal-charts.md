# Research: Chapter 06 — Time Series and Temporal Charts
## Brutalist d3 x Claude

**Chapter one-line:** Time charts must preserve temporal continuity and distinguish individual trends from cumulative area.
**Research date:** 2026-06-01

---

## 1. Primary Sources

1. Tufte, *The Visual Display of Quantitative Information*.
2. Cleveland, *Visualizing Data*.
3. Munzner, *Visualization Analysis and Design*.
4. D3 time scales and time-format docs. Source: https://d3js.org/what-is-d3
5. D3 shape docs for lines, areas, stacks.
6. Kelleher and Wagener data visualization guidelines.
7. Friendly, history of data visualization.
8. Etienne-Jules Marey historical movement diagrams.
9. Gantt chart history / Henry Gantt.
10. Cairo, *The Truthful Art*.

## 2. Core Concept — State of the Field

Time series charts encode continuity. Lines are strong for individual trends; area and stacked area encode volume but make non-baseline series harder to read.

Temporal charts can mislead through skipped intervals, uneven time bins, non-zero area baselines, excessive smoothing, and unreadable multi-series encodings.

## 3. Application Domain Examples

1. Line chart for trend.
2. Area chart for cumulative volume over time.
3. Stacked area for total and composition.
4. Stream graph for changing composition with aesthetic/interpretive cost.
5. Timeline/Gantt for events and durations.
6. Spiral plot for seasonality.

## 4. Book's Thesis Connection

Claude can implement temporal forms quickly, but the reader must specify whether the reader needs trend, volume, seasonality, duration, or event sequence.

## 5. AI Wayback Machine — Candidate Figures

1. William Playfair — time series line chart.
2. Etienne-Jules Marey — movement/time visualization.
3. Henry Gantt — duration planning.
4. Joseph Priestley — timelines.

## 6. Pedagogical Delivery Research

Compare line, area, and stacked area on the same dataset. Ask what each makes easy and what each hides.

## 7. Representation and Display Research

Checklist:

- Time axis continuous?
- Intervals honest?
- Baseline appropriate?
- Series count manageable?
- Smoothing disclosed?
- Missing data visible?

## 8. Open Questions and Research Gaps

1. Include examples of irregular time series.
2. Need D3 prompt template for time parsing.
3. Clarify stream graph tradeoffs.

