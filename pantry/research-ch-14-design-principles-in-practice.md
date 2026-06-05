# Research: Chapter 14 — Design Principles in Practice
## Brutalist d3 x Claude

**Chapter one-line:** The design audit resolves visual polish into testable questions about clarity, honesty, accessibility, and audience.
**Research date:** 2026-06-01

---

## 1. Primary Sources

1. Tufte, *The Visual Display of Quantitative Information*.
2. Stephen Few, chartjunk and dashboard design writing.
3. Cairo, *The Truthful Art* and "Ethical Infographics."
4. Bateman et al., memorability and embellished charts.
5. Evergreen and Emery, data visualization checklist.
6. Munzner, *Visualization Analysis and Design*.
7. Cleveland and McGill, "Graphical Perception," 1984.
8. Ware, visual thinking and Gestalt principles.
9. ColorBrewer and accessibility color guidance.
10. D3 docs for scales, axes, shapes, and accessibility-aware SVG/HTML output.

## 2. Core Concept — State of the Field

The mature position is not "remove everything" or "decorate freely." Visual elements should stay only when they support the communication goal, improve comprehension, support recall, or provide necessary context.

Claude output needs an explicit audit because polished code can still violate proportional ink, accessibility, uncertainty disclosure, or claim boundaries.

## 3. Application Domain Examples

1. Truncated bar chart audit.
2. Red/green color failure and color-blind simulation.
3. Overdecorated chart where ornament competes with data.
4. Under-annotated chart where the reader cannot find the claim.
5. Challenger O-ring display as evidence-design failure.

## 4. Book's Thesis Connection

The book's promise is not "Claude makes charts." It is "Claude can implement, while the human learns enough visual judgment to reject bad output."

## 5. AI Wayback Machine — Candidate Figures

1. Edward Tufte — data-ink ratio and evidence display.
2. Stephen Few — clarity over minimization.
3. Alberto Cairo — truthful and ethical visualization.
4. Stephanie Evergreen and Ann Emery — practical audit checklists.

## 6. Pedagogical Delivery Research

Use a flawed chart and run the audit out loud: proportional ink, scale, labels, accessibility, annotation, uncertainty, and audience.

## 7. Representation and Display Research

Checklist:

- Does each element support the question?
- Are encodings proportional and accessible?
- Is uncertainty shown or disclosed?
- Does annotation guide without overclaiming?
- Is the chart appropriate for the audience's graphicacy?
- Has Claude's output been independently checked?

## 8. Open Questions and Research Gaps

1. Pick one full flawed visualization for the chapter's redesign.
2. Decide how much Challenger material belongs in the main text.
3. Create a reusable Claude output audit prompt.
