# Brutalist d3 x Claude

**Nik Bear Brown**

---

## Copyright

Copyright © 2026 Nik Bear Brown. All rights reserved.

Published by Bear Brown, LLC.

No part of this publication may be reproduced, distributed, or transmitted in any form or by any means without the prior written permission of the publisher, except in the case of brief quotations in critical reviews and certain other noncommercial uses permitted by copyright law.

The visualizations referenced in this book are drawn from the Humanitarians AI D3 example set, used with permission. The pantry of working examples is available alongside the book as a companion repository.

ISBN: [pending]

First edition: 2026

---

## Dedication

For the analyst who tried to learn D3 in 2018, ran into `d3.scaleLinear`, and quietly closed the tab. You can come back now.

---

## Preface — The Brutalist System Applied to D3

This book is the D3 renderer module of a system called **Brutalist**. The system, the series, and the working documentation live at [brutalist.art](https://www.brutalist.art/).

Brutalist began as a design conversation framework for After Effects. A senior motion graphics designer working with Claude Code needs to maintain a specific kind of separation: Claude Code can write ExtendScript faster than any motion designer; what Claude Code cannot do is decide whether a generated keyframe matches the rhythmic intent of a scene, hear when the wrong easing breaks the relationship between two layers, or know which solid is a video placeholder and which is just a background. Those judgments belong to the designer. Brutalist is the architecture that holds the separation: a phase model, a labor separation principle, a set of supervisory capacities, and a small set of governing files. The original convention names two — `CLAUDE.md` for coding rules and `PROJECT.md` for project state. This volume introduces a third, `DESIGN.md`, for visual rules — palette, typography, spacing, dark-mode behavior, responsive breakpoints — which are loaded only when visual decisions are in scope. The split is a consequence of the LLM instruction budget. Chapter 00 explains the reasoning; the rest of the book uses the three files as the persistent context for every chart.

The system was always renderer-agnostic. The After Effects plumbing — ExtendScript, undo groups, layer naming conventions — was the first instantiation, but the underlying architecture works for any technology stack where an AI assistant generates code that produces a deterministic visual artifact. The series treats each renderer as its own book:

- *Brutalist After Effects x Claude* — motion graphics; ExtendScript; the original module.
- *Brutalist d3 x Claude* — this book; data visualization in the browser.
- *Brutalist Blender x Claude* — 3D modeling, materials, and rendering through Blender's Python API.
- *Brutalist Remotion x Claude* — programmatic video composition in React.
- Additional modules — SVG/GSAP, Rough.js, Three.js, p5.js — published as the framework matures.

Each module shares the same spine: phase model, labor separation, supervisory capacities, two governing files. What changes is the renderer, the syntax Claude Code is asked to produce, and the genre-specific failure modes the designer must learn to audit. Cross-references between books are deliberate: a reader who has worked through the After Effects module will recognize the phase structure here immediately and only need to learn the D3-specific failure modes (chart-type mismatch, channel-attribute mismatch, API hallucination at the d3 v7 level). A reader new to the series learns the architecture as it is taught against D3, then can move to any other module without relearning the spine.

This book is what Brutalist looks like when D3 is the active renderer.

The architecture maps almost cleanly. A few components shift names because the medium is static rather than time-based, but the spine is the same.

### The same architecture, different medium

The Brutalist phase model — Audit, Schema, Generate, Verify, Handoff — translates directly:

**Phase A — AUDIT.** In motion graphics: dump the project, build the map, understand what exists before generating anything. In data visualization: read the dataset, identify the data attributes, build the channel map. *Chapter 3 is the audit phase.* You do not write a Claude Code prompt for a chart you have not yet read the data for. The marks-and-channels analysis (Chapter 1) is the vocabulary the audit produces.

**Phase B — SCHEMA.** In motion graphics: write `CLAUDE.md` (coding constitution) and `PROJECT.md` (project state, with both designer-intent and technical layers). In data visualization: write three files. `CLAUDE.md` (coding rules — D3 version, naming conventions, accessibility standards, the four-move prompt template) loads at the start of every Claude Code session. `DESIGN.md` (visual rules — palette, typography, spacing, dark-mode behavior, responsive breakpoints, component conventions) loads on demand when visual decisions are in scope. `PROJECT.md` (per-chart audit — chart type, data structure, channel-attribute mappings, design constraints, sort order, accessibility decisions) is produced by each LLM Exercise. The book itself functions as the persistent reference behind all three: channel ranking, chart selection grammar, design audit framework. Chapter 00 explains the instruction-budget reasoning behind the `CLAUDE.md`/`DESIGN.md` split.

**Phase C — GENERATE.** In motion graphics: Claude Code writes `.jsx` scripts against the schema. In data visualization: Claude Code writes D3 against the schema. Strictly bounded: one chart per prompt, one concern per iteration, the human runs and reviews every output before the next prompt is issued. Chapter 4 is the generation phase; Chapters 5 through 13 are the genres of generation that the schema (channel framework + chart taxonomy) enables.

**Phase D — VERIFY.** In motion graphics: run the composition, watch it at full frame rate, check naming conventions, check easing, check expressions. In data visualization: run the chart, audit it against the Evergreen/Emery checklist (or a chart-family-specific subset), check accessibility, check color encoding, check that the channel decomposition the prompt specified is actually what was rendered. Chapter 14 is the verification framework. Every chapter from Chapter 5 onward applies the chart-specific subset.

**Phase E — HANDOFF.** In motion graphics: lock the composition, export `.mogrt`, prepare the editorial package with placeholder solids labeled. In data visualization: publish the chart with the data-source documentation, the encoding decisions documented, the accessibility considerations stated, and the responsive behavior specified. Chapter 15 walks the complete handoff for one project.

### Labor separation, applied to D3

The labor separation principle translates with equal directness.

**Claude Code is the right labor for** writing D3 v7 syntax, building scales (`d3.scaleLinear`, `d3.scaleBand`, `d3.scaleSequential`), generating axis configurations, computing layout primitives (Sankey diagrams, treemap squarification, force-directed layouts), applying transitions and easing curves, generating accessibility metadata (ARIA labels, focus states), creating responsive resize handlers, and producing complete HTML files with inline CSS and inline D3 against a precise channel specification. Claude Code is fast, accurate, and reliable in this lane — every time.

**The human (you) is the right labor for** deciding what chart type the data wants (Chapter 2), formulating the communication question that the chart must answer (Chapter 3), specifying the channel-to-attribute mappings before any code runs (Chapter 1), running and visually evaluating every chart Claude Code produces, deciding whether the chart's encoding actually answers the question, owning the publishing and editorial decisions, and exercising the moral judgment Cairo names: that an ineffective chart is not just an aesthetic failure but a failure of professional responsibility to the reader.

**The dangerous middle** — operations that require explicit handoff conditions before either party touches them — includes Claude Code modifying an existing chart's encoding without knowing whether the encoding decision was deliberate, Claude Code applying a "design improvement" without reading the design intent, Claude Code generating accessibility metadata that contradicts the chart's actual structure, and the human accepting Claude Code output without running the chart. Each of these has a specific failure mode. The book names them at the moments they are most likely to occur.

### The five supervisory capacities, applied to chart design

Brutalist's five supervisory capacities translate to the work of the chart designer working with Claude Code:

**1. Plausibility Auditing (PA).** Looking at a generated chart and seeing whether the encoding works. Not "is the chart pretty" but "does the chart let me read what it claims to show?" Bar charts truncated below zero look fine until you read them; scatterplots with hue-encoded magnitude look colorful until you try to rank the points; choropleths colored by absolute count look informative until you notice that geographic area is dominating perception. Plausibility auditing is the muscle this book builds.

**2. Problem Formulation (PF).** Deciding what the chart IS before Claude Code sees it. Cairo's "compared with what?" question (Chapter 3). The communication question must be specific enough that Claude Code can build *a* chart against it, not *any* chart. "Visualize sales" is not problem formulation; "show how Q4 revenue per region compares to the same quarter last year, ranked by total revenue" is.

**3. Tool Orchestration (TO).** Choosing which Claude Code task, in what order, with what context. Building a complete project (Chapter 15) is not one prompt; it is six or seven prompts in sequence, each with the previous output as context, each producing a checkpoint the human verifies before the next is issued. The MBTA project model (Barry & Card, 2014) is the canonical template.

**4. Interpretive Judgment (IJ).** Supplying the visual and creative meaning that no automated audit can detect. The Nightingale rose chart violates the area-perception accuracy rule and was nonetheless the right chart for its rhetorical context. A choropleth of US health outcomes that puts the worst-performing states in red is not making a neutral encoding choice; it is making a political one. Interpretive judgment names what the choices mean.

**5. Executive Integration (EI).** Holding a project's visual language consistent across charts. A dashboard with twelve charts in twelve color palettes is not twelve charts — it is twelve unrelated documents pretending to be a dashboard. Chapter 14 (design principles in practice) and Chapter 15 (the complete project) build this capacity explicitly.

### The two governing files in this book

The Brutalist structure has two governing files. They both exist in this book.

**`CLAUDE.md` — the coding constitution for D3 work.** This is what every chapter from 1 onward implicitly builds on the coding side. By the end of the book, the reader has a complete D3 `CLAUDE.md`: the channel ranking and the expressiveness/effectiveness principles applied to code, the chart selection grammar as it informs prompt structure, the per-chart-family encoding rules, the accessibility standards, and the four-move prompt template. The book is a course in writing the `CLAUDE.md`.

**`DESIGN.md` — the visual constitution for D3 work.** The companion file, introduced in Chapter 00 as a consequence of the LLM instruction budget. The reader who builds a serious D3 practice produces this file alongside `CLAUDE.md`: color palette with semantic roles, typography stack, spacing scale, dark-mode behavior, responsive breakpoints, component rules. `DESIGN.md` is loaded when a session involves visual decisions and stays out of the way otherwise. Keeping it separate from `CLAUDE.md` is what keeps both files within the budget Claude Code can reliably hold in active attention.

**`PROJECT.md` — the per-chart specification.** Each chapter's LLM Exercise produces one. The format is consistent: data structure description, communication question, channel-to-attribute mappings, design constraints, color palette, sort order, accessibility decisions, the Claude Code prompt that produces the chart, the audit checklist applied to the output, the iteration log for any follow-up corrections. By Chapter 15, the reader has a portfolio of `PROJECT.md` documents — one per major chart they have built — that demonstrates the practice the book teaches.

A chart built without a `PROJECT.md` is a chart built on hope. The hope sometimes pays off. More often, it produces the chart you didn't know you didn't want. The audit document is the discipline that prevents the second outcome.

### Why D3 specifically

What makes D3 the right renderer for this book is not D3's expressive range, though that is real. It is the longest-standing combination of accessibility (D3 runs in the browser, the most universal rendering target available), generative power (every chart in the standard taxonomy is buildable in D3), and Claude-Code compatibility (Claude Code knows D3 v7 well; the syntax is stable; the API is well-documented). D3 is also the technology that locked thousands of would-be visualization practitioners out of the field for a decade because of its API complexity. The Brutalist pattern — designer judgment, AI execution — is exactly the unlock that lets those practitioners come back.

This book is therefore two things at once: a course in chart design judgment grounded in the Bertin–Cleveland–Munzner tradition, and a manual for the D3 renderer module of Brutalist. If you have used Brutalist for After Effects or for SVG/GSAP, the architecture here will be familiar. If you have not, the book teaches the architecture as it teaches the chart taxonomy. Either way: the renderer is configured. The designer conversation begins now.

### What this book is not

This book is not a D3 API reference. Scott Murray's *Interactive Data Visualization for the Web* (3rd ed., O'Reilly) is the canonical D3 textbook for that purpose; if you want to become a D3 developer, that is the book.

This book is not a comprehensive tour of all visualization theory. Claus Wilke's *Fundamentals of Data Visualization* (O'Reilly) and Tamara Munzner's *Visualization Analysis and Design* (CRC Press) are the comprehensive references on the theory side; this book teaches the parts of the theory you need to direct Claude Code.

This book is not Brutalist. Brutalist is the system architecture; this is the D3 module of it. Other modules exist for other renderers — *Brutalist After Effects x Claude*, *Brutalist Blender x Claude*, *Brutalist Remotion x Claude*, and additional renderers in development. The designer-conversation core is shared across all of them. The framework, the current list of modules, and the source documentation are at [brutalist.art](https://www.brutalist.art/).

This book is not a substitute for visual judgment. It is a scaffold for it. Reading the book without building anything will not develop the muscle the book is trying to build. Every chapter has working exercises and every chapter ends with a Claude Code task. The exercises are the book.

### How to use this book

**Read Part I before doing anything.** Chapters 1 through 4 build the vocabulary and the workflow. Skipping to a specific taxonomy chapter is possible but the chapter will read as a list of rules without justification. Part I supplies the justification.

**Read Part II modularly.** Chapters 5 through 13 are independent within Part II's structure. A course focused on statistical visualization can skip Chapter 11 (flow/network) without breaking anything. A practitioner who needs to build a Sankey diagram tomorrow can read Chapter 11 directly. The chapters cross-reference each other (bar charts return as the alternative form in pie chart redesigns; line charts return as the comparison case for area charts) but the cross-references are explicit.

**Read Part III as the synthesis.** Chapters 14 and 15 bring everything together. Chapter 14 is the design audit framework; Chapter 15 is a complete project from raw data to published output. Doing the Chapter 15 exercise — actually building a complete project — is the test the book asks you to pass.

**Use the pantry.** The book repeatedly references working examples in the pantry directory. Open them in a browser. Read the source. The Humanitarians AI D3 example set is the laboratory.

**Use Claude Code.** Every chapter ends with an LLM Exercise that produces a real, runnable D3 chart. Skipping the exercises means skipping the practice. The reading is the scaffold; the practice is the building.

The argument of this book is that the design layer of data visualization — the part that decides whether a chart works or fails — has not been delegated to Claude Code, and cannot be. Claude Code writes the D3. You write the specification. The book is a course in writing the specification.

---

*Nik Bear Brown*
*Boston, 2026*
