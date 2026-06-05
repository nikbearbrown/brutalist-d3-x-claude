# Research: Chapter 04 — Working with Claude Code
## Brutalist d3 x Claude

**Chapter one-line:** Turn a chart specification into working D3, then iterate against visual integrity checks.
**Research date:** 2026-06-01

---

## 1. Primary Sources

1. Anthropic Claude Code overview. Source: https://code.claude.com/docs
2. Anthropic Claude Code permissions. Source: https://code.claude.com/docs/en/permissions
3. D3 official docs. Source: https://d3js.org/
4. D3 "What is D3?" Source: https://d3js.org/what-is-d3
5. Bostock, Ogievetsky, Heer, "D3: Data-Driven Documents." Source: https://vis.stanford.edu/papers/d3
6. Stephen Few, *Show Me the Numbers*. Source: https://www.perceptualedge.com/library.php
7. Evergreen and Emery visualization checklist materials. Source: https://stephanieevergreen.com/
8. Bret Victor, "Drawing Dynamic Visualizations." Source: http://worrydream.com/DrawingDynamicVisualizationsTalkAddendum/
9. Microsoft HAI Guidelines. Source: https://www.microsoft.com/en-us/research/project/guidelines-for-human-ai-interaction/publications/
10. HumanEval / code evaluation. Source: https://arxiv.org/abs/2107.03374

## 2. Core Concept — State of the Field

Claude Code can accelerate the D3 build loop when the user supplies a precise visual specification and verifies the rendered output. The loop is: specify, generate, render, inspect, correct one concern, repeat.

Generated D3 failure modes often come from visualization misunderstanding, not JavaScript syntax: missing zero baseline, wrong scale, area/radius confusion, bad labels, inaccessible color, or interaction without purpose.

## 3. Application Domain Examples

1. Bar chart with explicit scale and labels.
2. Multi-series line chart with legend and hover.
3. Choropleth with rate, not count.
4. Bubble chart with area-correct radius.
5. Full pipeline from CSV to HTML.

## 4. Book's Thesis Connection

This chapter is where implementation delegation becomes real. Claude Code writes the code; the reader checks the chart against the visual argument.

## 5. AI Wayback Machine — Candidate Figures

1. Mike Bostock — D3 implementation.
2. Bret Victor — live visual thinking.
3. Margaret Hamilton — code verification.
4. Stephen Few — practical chart audit.

## 6. Pedagogical Delivery Research

Teach through one chart done twice: vague prompt and specification prompt. Then run an audit and one focused correction.

## 7. Representation and Display Research

Recommended workflow:

```text
Read data -> choose chart -> specify channels -> Claude Code builds -> render -> audit -> revise
```

## 8. Open Questions and Research Gaps

1. Decide local HTML versus Observable for final examples.
2. Re-check current Claude Code setup before publication.
3. Include accessibility checks in every generated chart audit.

