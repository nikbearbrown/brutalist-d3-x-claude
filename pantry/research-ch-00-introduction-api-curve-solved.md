# Research: Introduction — The API Curve Is Solved
## Brutalist d3 x Claude

**Chapter one-line:** Claude can reduce the D3 implementation burden, but the human still owns the visual argument.
**Research date:** 2026-06-01

---

## 1. Primary Sources

1. D3 by Observable, official documentation. Source: https://d3js.org/  
   D3 is the official implementation anchor: a JavaScript library for bespoke dynamic visualization, with modules for selections, scales, axes, shapes, layouts, interactions, maps, and data utilities.

2. D3, "What is D3?" Source: https://d3js.org/what-is-d3  
   This source explains that D3 is a low-level toolbox built on web standards rather than a charting library. That supports the book's thesis that Claude may help with API mechanics while humans must specify visual structure.

3. Bostock, Ogievetsky, and Heer, "D3: Data-Driven Documents," IEEE TVCG, 2011. Source: https://vis.stanford.edu/papers/d3  
   The original D3 paper anchors D3 historically as a system for binding data to documents using web standards.

4. Alberto Cairo, "Ethical Infographics" / data journalism ethics writing. Source: https://www.thefunctionalart.com/  
   Cairo's work supports the introduction's ethical frame: a technically competent visualization can still mislead if the data, framing, or visual argument is wrong.

5. William Cleveland and Robert McGill, "Graphical Perception," JASA, 1984. Source: https://lenagroeger.s3.amazonaws.com/newschool/ClevelandMcGill.pdf  
   This is the perception anchor for why visual argument cannot be delegated entirely to code generation.

6. Tamara Munzner, *Visualization Analysis and Design*, 2014. Source: https://www.taylorfrancis.com/books/mono/10.1201/b17511/visualization-analysis-design-tamara-munzner  
   Munzner provides the design framework: problem abstraction, data/task abstraction, encoding/interaction design, and validation.

7. Heer and Bostock, "Crowdsourcing Graphical Perception," CHI 2010. Source: https://idl.cs.washington.edu/files/2010-CrowdsourcingGraphicalPerception-CHI.pdf  
   This source updates graphical perception evidence for web-scale chart types and supports the book's perceptual honesty emphasis.

8. Edward Tufte, *The Visual Display of Quantitative Information*, 1983. Source: https://www.edwardtufte.com/tufte/books_vdqi  
   Tufte provides a classic "show the data" frame that remains useful for auditing D3 output.

9. Financial Times, "Visual Vocabulary." Source: https://github.com/Financial-Times/chart-doctor/tree/main/visual-vocabulary  
   FT Visual Vocabulary supports chart-selection categories as a navigation aid.

10. Observable Plot, official docs. Source: https://observablehq.com/plot/  
    Plot gives the chapter a comparison point: higher-level APIs can make quick charts, while D3 remains valuable for bespoke visual arguments.

## 2. Core Concept — State of the Field

Claude can help with D3 syntax, SVG structure, and iteration, but the visualization problem remains conceptual: what does the reader need to see, what comparison is honest, and what visual channel supports that task.

D3's low-level nature is both the obstacle and the power. It requires composing scales, axes, shapes, selections, layouts, and interactions. Claude can reduce the implementation load, but only if the human supplies a clear chart specification.

The field's stable center is graphicacy: knowing how data becomes visual evidence. The chapter should distinguish coding fluency from visual reasoning.

## 3. Application Domain Examples

1. A technically correct map built from a misleading dataset.
2. A polished bar chart with a truncated baseline.
3. A D3 chart that renders but encodes area when length is needed.
4. An interactive visualization whose interaction adds friction rather than insight.
5. A humanitarian dataset whose real question is "compared with what?"

## 4. Book's Thesis Connection

This introduction establishes the book's thesis: Claude can help write D3, but the reader must know what the visualization is supposed to argue. The implementation problem is increasingly delegable; the design, perceptual, and ethical problem is not.

## 5. AI Wayback Machine — Candidate Figures

1. Jacques Bertin — visual variables and graphic semiology.
2. William Cleveland — graphical perception as empirical science.
3. Alberto Cairo — visual ethics and graphicacy.
4. Mike Bostock — D3 as a web-native visualization grammar.

## 6. Pedagogical Delivery Research

Open with a visualization that is technically impressive and substantively wrong. The reader should feel the split between "the chart works" and "the chart is honest."

Common misconceptions:

- "If Claude can code the chart, I do not need visualization knowledge."
- "D3 is the hard part."
- "Interactivity makes a chart better."
- "A map makes data true."
- "Publication quality means visual polish."

## 7. Representation and Display Research

Recommended diagram:

```text
Dataset -> reader question -> chart choice -> marks/channels -> D3 specification -> rendered chart -> visual integrity audit
```

Recommended checklist:

- What is the claim?
- What data supports it?
- What comparison matters?
- What channel encodes the key value?
- What could mislead?
- What must Claude not decide?

## 8. Open Questions and Research Gaps

1. The chapter should verify the exact Cairo/FiveThirtyEight Nigeria case details before final publication.
2. D3 docs and version details should be checked before screenshots or code snippets are finalized.
3. The book should decide when to mention Observable Plot as an alternative without diluting the D3 focus.
4. The chapter should define "Brutalist" clearly as a workflow stance, not merely an aesthetic style.

