# Brutalist d3 x Claude

**Author:** Nik Bear Brown

---

## One-Sentence Pitch

Learn to build publication-quality D3 visualizations by mastering chart selection, design principles, and visual storytelling — Claude Code handles the syntax, you handle the thinking.

---

## The Argument

D3.js has always been two things: a visualization library and a programming challenge. For most learners, the programming challenge consumed everything — weeks spent on scales, joins, and transitions that could have been spent understanding *why* a violin plot reveals what a box plot hides, or *when* a Sankey diagram serves the reader better than a stacked bar.

That trade-off is over. Claude Code can generate conformant D3 faster than any developer can write it. The steep API curve is a solved problem.

What remains — what has always been the harder and more valuable skill — is the design layer: reading a dataset and knowing which of 60 chart types actually answers the question; understanding marks and channels well enough to justify every encoding decision; knowing when a radial bar chart is the right call and when it's just decorative noise. These skills cannot be delegated to Claude Code. They require a mental model of how humans perceive visual information, a working taxonomy of visualization forms, and judgment about when a chart is doing work versus performing effort.

This book teaches that layer. It uses the Humanitarians AI D3 example set — over 60 working visualizations covering the full chart taxonomy — as its laboratory. Each chapter pairs the conceptual framework with a working example students can inspect, modify, and rebuild. Claude Code writes the D3; the student directs it.

---

## The Gap

**Curran Kelleher / Observable Plot tutorials:** Excellent on D3 mechanics and marks-and-channels theory, but not a structured course. No chapter-by-chapter pedagogical arc. No chart selection framework. Reader learns syntax; may not learn decision-making.

**Scott Murray, *Interactive Data Visualization for the Web*:** The canonical D3 textbook. Strong on syntax and web fundamentals. Predates LLM-assisted coding entirely. Does not address chart selection as a teachable decision framework. Third edition still requires fluency in D3 API.

**Claus Wilke, *Fundamentals of Data Visualization*:** Outstanding on design principles and chart selection. No code at all. Students who finish it still cannot build anything.

**This book:** Teaches the decision layer Wilke covers but adds a complete working implementation layer via Claude Code + D3. Structured as a semester course. Every concept has a working example. The student's job is never to memorize D3 syntax — it is to develop the visual judgment that makes Claude Code useful.

---

## The Reader

**Primary:** A graduate student, data journalist, researcher, or analyst who works with data and needs to communicate it visually. Has basic familiarity with web concepts (HTML, CSS, some JavaScript) but has bounced off D3's API complexity before. Wants to produce interactive, publication-quality visualizations. Does not want to become a JavaScript developer.

**Secondary:** An undergraduate taking a data visualization course who will use Claude Code as the implementation environment throughout.

**What they can do after:** Given a dataset and a communication goal, select the appropriate chart type with a principled justification; direct Claude Code to build a D3 implementation; evaluate the output against design principles; and iterate. Produce 60-chart-type literacy — knowing what each form is for and when it fails.

---

## High-Level Outline

**Part I — The Decision Layer**
Why chart selection is a design decision, not a lookup. Marks and channels as the underlying grammar of all visualization. How to read a dataset and ask the right question before touching D3. The FT Visual Vocabulary and Data Visualisation Catalogue as navigational tools.

**Part II — The Chart Taxonomy (by functional category)**
A structured tour of all major chart families — comparison, distribution, relationship, part-to-whole, hierarchy, flow, spatial, temporal — with working D3 examples for each. Each chapter: the concept, the failure modes, the design rules, the implementation.

**Part III — Integration and Production**
Building a complete visualization project from raw data to published output. Accessibility, color, annotation, responsiveness. Using Claude Code for the full pipeline: data → chart → embed.

---

## Voice — Brutalist Posture (Required Reading Before Every Chapter)

The tone of every chapter in this book reflects **Brutalist**: a system for human–AI collaborative production whose guiding principle is *maximally informed and minimally autonomous by design*. The voice anchor is **`style/brutalist-voice.md`** — read it before drafting any chapter. The source manifesto is preserved in **`style/brutalist-manifesto-source.md`**.

Carry the six principles in the prose:

1. **Intent before code.** Each chapter specifies in plain English what the visualization is supposed to do before any D3 appears.
2. **Schema, not improvisation.** When code appears, it is generated against named conventions, not vibes.
3. **Phase discipline.** Audit → Schema → Generate → Verify → Handoff. Chapters move in order. Mid-chapter exercises mirror the same gate.
4. **Labor separation.** Each chapter names what Claude Code does and what the human does. The boundary is made explicit.
5. **Refusal behavior.** When a chart, default, or pattern is wrong for the task, the chapter says so. Plainly. No softening.
6. **Surface, defer action.** When the chapter touches anything that drifts (D3 version, accessibility standard, paper findings), it names the date of the reading and frames updates as the reader's decision, not the chapter's assumption.

**Forbidden:** tool-cheerleading, reader-flattery, frictionless framing, "magical/seamless/effortless," "AI-powered" as a modifier, any sentence that could appear on a SaaS landing page.

**Required:** load-bearing sentences, named boundaries, plain refusals where defaults are wrong, a closing line that could survive being printed on a wall.

The full markers, vocabulary, and per-principle prose mappings live in `style/brutalist-voice.md`. That file overrides root `style/` on conflict.

---

## Open Questions

- [ ] Should Part II chapters be organized strictly by FT Visual Vocabulary category, or by D3 implementation complexity (so prerequisites build)?
- [ ] How many examples per chapter — one deep or several shallow?
- [ ] Does the book need a Chapter 0 on setting up Claude Code + D3 environment?
- [ ] Is the target a KDP/EPUB release (matching the existing build pipeline) or a web-first course?
