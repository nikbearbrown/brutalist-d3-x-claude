# Research: Chapter 03 — Reading a Dataset
## Brutalist d3 x Claude

**Chapter one-line:** Before touching D3, identify the data types and the reader question.
**Research date:** 2026-06-01

---

## 1. Primary Sources

1. Munzner, *Visualization Analysis and Design*. Source: https://www.taylorfrancis.com/books/mono/10.1201/b17511/visualization-analysis-design-tamara-munzner
2. Cairo, *The Truthful Art*. Source: https://www.thefunctionalart.com/p/the-truthful-art.html
3. Wickham, "Tidy Data," Journal of Statistical Software, 2014. Source: https://www.jstatsoft.org/article/view/v059i10
4. Friendly, "A Brief History of Data Visualization." Source: https://www.datavis.ca/papers/hbook.pdf
5. D3 dsv/fetch/array docs. Source: https://d3js.org/what-is-d3
6. Observable Plot docs. Source: https://observablehq.com/plot/
7. Kandel et al., "Enterprise Data Analysis and Visualization," IEEE VAST, 2012. Source: https://idl.cs.washington.edu/files/2012-Profiler-AVI.pdf
8. Heer and Shneiderman, "Interactive Dynamics for Visual Analysis," 2012. Source: https://queue.acm.org/detail.cfm?id=2146416
9. Tufte, *Visual Display*. Source: https://www.edwardtufte.com/tufte/books_vdqi
10. NIST/SEMATECH e-Handbook of Statistical Methods, EDA. Source: https://www.itl.nist.gov/div898/handbook/eda/eda.htm

## 2. Core Concept — State of the Field

Reading a dataset means identifying attribute types, units, granularity, missingness, comparators, and the question the reader needs answered. This precedes chart selection.

The analyst's question is often not the reader's question. The chart must encode the relationship the reader actually needs to inspect.

## 3. Application Domain Examples

1. Refugee flows: origin-destination, time trend, or per-capita rate?
2. GDP per capita: absolute, rank, regional comparison, or change?
3. Funding data: totals, proportions, or gaps?
4. Event logs: count, duration, sequence, or milestone?
5. Survey data: distribution, relationship, or subgroup comparison?

## 4. Book's Thesis Connection

Claude should not choose from a vague dataset. The reader must provide field meanings, data types, and the comparison question before implementation.

## 5. AI Wayback Machine — Candidate Figures

1. John Tukey — exploratory data analysis.
2. Hadley Wickham — tidy data.
3. John Snow — data mapped to a causal question.
4. Florence Nightingale — data prepared for public action.

## 6. Pedagogical Delivery Research

Start with "visualize refugee flows" and unpack the hidden ambiguity. Ask readers to write the reader question before chart type.

## 7. Representation and Display Research

Dataset reading checklist:

- Unit of observation
- Fields and types
- Missing values
- Aggregation level
- Time/geography
- Reader question
- Needed comparison
- What dataset cannot answer

## 8. Open Questions and Research Gaps

1. Include an annotated real CSV example.
2. Need careful treatment of rates versus counts for humanitarian examples.
3. Connect directly to Chapter 4 prompt anatomy.

