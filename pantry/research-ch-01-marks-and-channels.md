# Research: Chapter 01 — Marks and Channels
## Brutalist d3 x Claude

**Chapter one-line:** Marks and channels are the grammar beneath every chart.
**Research date:** 2026-06-01

---

## 1. Primary Sources

1. Jacques Bertin, *Semiology of Graphics*, 1967/1983. Source: https://monoskop.org/images/2/2b/Bertin_Jacques_Semiology_of_Graphics_Diagrams_Networks_Maps.pdf
2. Cleveland and McGill, "Graphical Perception," JASA, 1984. Source: https://lenagroeger.s3.amazonaws.com/newschool/ClevelandMcGill.pdf
3. Cleveland and McGill, "Graphical Perception and Graphical Methods for Analyzing Scientific Data," Science, 1985. Source: https://ils.unc.edu/courses/2015_spring/inls541_001/Readings/Cleveland%20and%20McGill%201985%20-%20Graphical%20Perception%20and%20Cleveland1985-Graphical%20Methods%20for%20Analyzing%20Scientific%20Data.pdf
4. Heer and Bostock, "Crowdsourcing Graphical Perception," CHI 2010. Source: https://idl.cs.washington.edu/files/2010-CrowdsourcingGraphicalPerception-CHI.pdf
5. Munzner, *Visualization Analysis and Design*, 2014. Source: https://www.taylorfrancis.com/books/mono/10.1201/b17511/visualization-analysis-design-tamara-munzner
6. Stevens, "On the psychophysical law," Psychological Review, 1957. Source: https://psycnet.apa.org/record/1958-01753-001
7. Colin Ware, *Information Visualization: Perception for Design*. Source: https://www.sciencedirect.com/book/9780123814647/information-visualization
8. D3 docs: scales, axes, shapes. Source: https://d3js.org/what-is-d3
9. Kelleher and Wagener, "Ten guidelines for effective data visualization in scientific publications," 2011. Source: https://pubmed.ncbi.nlm.nih.gov/21357710/
10. Cairo, *The Truthful Art*. Source: https://www.thefunctionalart.com/p/the-truthful-art.html

## 2. Core Concept — State of the Field

Marks are graphical objects; channels are visual properties used to encode data. The key design problem is matching data attributes to channels that humans can decode accurately.

Cleveland and McGill's empirical ranking makes position along a common scale the safest quantitative channel. Munzner translates this into expressiveness and effectiveness principles: use channels that can express the data type and prioritize important data with perceptually stronger channels.

## 3. Application Domain Examples

1. Scatterplot: point marks and x/y position.
2. Bar chart: rectangular marks and length/position.
3. Bubble chart: point/circle area, with area perception risk.
4. Heatmap: area tiles plus color luminance.
5. Network diagram: nodes, links, position, hue, and size.

## 4. Book's Thesis Connection

This chapter gives readers the vocabulary they must supply to Claude. Without marks and channels, prompts collapse into chart names; with marks and channels, D3 output becomes inspectable.

## 5. AI Wayback Machine — Candidate Figures

1. Jacques Bertin — visual variables.
2. William Cleveland — perception ranking.
3. Tamara Munzner — modern visualization design synthesis.
4. Leland Wilkinson — grammar of graphics.

## 6. Pedagogical Delivery Research

Start with two charts of the same data where one uses position and the other uses color luminance for magnitude. The reader should experience the perceptual difference before receiving terminology.

## 7. Representation and Display Research

Recommended table:

| Data type | Good channels | Risky channels |
|---|---|---|
| Quantitative | position, length | hue, area, angle |
| Ordered | position, luminance | unordered hue |
| Categorical | hue, shape, position grouping | luminance as magnitude |

## 8. Open Questions and Research Gaps

1. Need exact treatment of Bertin terminology to avoid mistranslation.
2. Include visual examples for each channel.
3. Avoid implying rankings are universal regardless of task and context.

