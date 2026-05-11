# Brutalist d3 x Claude — Vision & Positioning

**Author:** Nik Bear Brown
*Phase 1 output from Tic TOC. Updated to reflect full theoretical pantry.*

---

## Book Concept Summary

"This book teaches chart selection, design judgment, and visual storytelling with D3 to data analysts, researchers, and graduate students, by decoupling the implementation problem (solved by Claude Code) from the design problem (still requiring human judgment), filling the gap left by existing books that teach either code without design (Murray) or design without code (Wilke). It succeeds if the reader can, given any dataset and communication goal, select the right chart type with a principled justification, direct Claude Code to build it, and evaluate the output against design principles."

**Biggest unresolved structural question:** Does Part II sequence by functional category (comparison, distribution, flow…) or by D3 implementation complexity? Current draft uses functional-category order — flag for confirmation.

---

## Theoretical Position (resolved)

**The chartjunk debate: Few's position, not Tufte's.**

The book adopts Stephen Few's "clarity over minimization" position rather than Tufte's strict data-ink ratio maximization. The reasons are structural: the book teaches judgment, not rules. Tufte's data-ink ratio is a heuristic that becomes a commandment in unskilled hands — the same failure mode the book is designed to prevent with chart selection. Few's analysis of the Bateman/Holmes chartjunk study demonstrates that embellishments can serve communication when properly designed; what matters is whether a visual element supports the message, not whether it adds ink.

The evaluation criterion for Claude Code output throughout this book is therefore: "does this support the communication goal clearly?" — not "does this minimize ink?" This position is explicitly argued in Chapter 14 using the Tufte vs. Holmes vs. Few debate as the primary case.

**The Cairo ethical frame: visualization choice is a moral decision.**

Alberto Cairo's rule-utilitarian position — that choosing an ineffective chart type is morally wrong because it impedes understanding — frames the book's Introduction and runs through Chapter 2. This is stronger than "bad chart choice is bad design": it's a claim that the reader has a professional responsibility to their audience. The FiveThirtyEight Nigeria kidnapping case (proxy variable used without normalization, data not put in context) opens the Introduction as the first concrete example of what this responsibility means. Cairo's graphicacy concept — the fourth literacy alongside reading, writing, and numeracy — gives the book's educational project its stakes.

**The Bertin → Cleveland & McGill → Munzner lineage: the theoretical spine of Part I.**

Chapter 1 traces a single intellectual thread:
- Bertin (1967, *Sémiologie Graphique*): the first systematic grammar of visual variables — the marks and channels vocabulary the book uses throughout. His taxonomy (x/y position, size, value/luminance, texture, color/hue, orientation, shape) is the origin of the framework Munzner extends.
- Cleveland & McGill (1986): the perceptual accuracy rankings that ground every "prefer bar length to area" judgment in empirical evidence, not aesthetic preference. The Heer & Bostock (2010) replication and extension — showing bar charts most accurate, stacked bars second, pie charts and circle packing less accurate — updates the evidence for the D3 era.
- Munzner (2014, *Visualization Analysis and Design*): the synthesis taxonomy — magnitude channels (position, length, area, luminance, saturation) vs. identity channels (hue, shape, texture) — and the expressiveness and effectiveness principles that provide the modern design vocabulary.

This lineage is not presented as history for its own sake. Each figure is introduced as "the person who named the problem your current tools are trying to solve." The Kelleher marks-and-channels video is the accessible entry point that frames all three and provides the worked examples for Chapter 1.

**The Friendly history: visualization as a cumulative intellectual project.**

Chapter 2 (Chart Selection) draws on Michael Friendly's history of data visualization to establish that every chart type in the taxonomy has a story: who invented it, for what purpose, and what problem they were trying to solve. Playfair invented the bar chart and line graph to argue about trade policy. Nightingale invented the polar area chart to argue about preventable deaths in the Crimean War. Snow invented the dot map to find the source of cholera. Every chart type is a solution to a specific communication problem — and understanding that problem is part of understanding when to use the chart. This frames chart selection as intellectual history, not menu navigation.

**The Gestalt principles and preattentive attributes: the perceptual mechanism behind design rules.**

The JSI/Dubow-Makulec design deck and related perceptual psychology sources establish the perceptual mechanism behind design decisions. Proximity, similarity, enclosure, continuity, closure, figure/ground — these are not style guidelines, they are descriptions of how the human visual system actually processes information. Every design rule in Chapter 14 is grounded in one of these mechanisms. This is the "why" behind the rules.

**The MBTA case (Barry & Card, 2014): the complete project template.**

The Visualizing MBTA Data project is the model for Chapter 15 (Building a Complete Project). It demonstrates: prototype-driven iteration, Bret Victor's levels of abstraction (moving from map to Marey diagram to scatterplot), avoiding administrative debris in interaction design, integrating words/numbers/graphics, and the lesson that "nothing beat iterating on working code." It's also a D3.js project built around a specific communication question ("When and where are the trains crowded or delayed?"), which makes it directly applicable to the book's framework.

---

## Book Type and Deployment Specification

**Primary type:** Course textbook — adopted for a semester, read chapter-by-chapter.

**Secondary type:** Practitioner handbook — consulted by chart type when a specific visualization problem arises.

**Deployment specification:**
- Primary adoption context: graduate data visualization courses; undergraduate data journalism courses; data science programs with a visualization module. 14–15 week semester.
- Secondary adoption context: self-study by analysts and researchers; professional development for humanitarian data practitioners (Humanitarians AI direct audience).
- What this book is NOT designed for: readers who need to become D3 JavaScript developers; readers who need a comprehensive JavaScript/web reference; readers who want to learn data visualization theory without any implementation.

**How the TOC signals book type to a faculty reviewer:** Chapter count (15 primary chapters) maps cleanly to a 15-week semester. Part I establishes the conceptual vocabulary weeks 1–4; Part II is modular weeks 5–13; Part III synthesizes weeks 14–15. Part II chapters can be assigned selectively — a course focused on statistical visualization can skip Chapter 11 (flow/network) without breaking the arc.

---

## Learner Profile

**Primary reader:** A graduate student in data science, public policy, journalism, or a social science field. Has encountered D3 and bounced off the API complexity. Has basic JavaScript literacy but is not a developer. Works with real datasets in their research or job. Wants interactive, publication-quality charts.

**Secondary reader:** An undergraduate in a data visualization course. Less prior JavaScript. More time available for structured learning.

**Prior knowledge (reliable):** Basic statistics (mean, median, distribution); familiarity with spreadsheet tools; conceptual awareness that bar charts and pie charts exist; some HTML/CSS exposure.

**Prior misconceptions:**
- Believes chart choice is aesthetic preference, not a design decision with perceptual and ethical consequences (Cairo's frame corrects this).
- Believes D3 mastery requires JavaScript fluency — may have abandoned D3 for this reason.
- Believes Claude Code "writes visualization code" without needing direction — does not understand that prompt quality depends on design vocabulary.
- Believes pie charts are categorically wrong (common Tufte overcorrection). The book's position: pie charts fail in specific conditions, not categorically — Few's nuanced view.
- Conflates Tufte's heuristics with laws. Chapter 14 addresses this directly.

**Current capability gap:** Cannot move from "I have this data" to "this is the right chart and here is why." Cannot evaluate whether a generated D3 output is perceptually honest or misleading. Cannot direct Claude Code to produce a specific visual encoding with precision.

**Graphicacy level:** Low-to-medium. Cairo's concept of graphicacy — the ability to read and produce visual representations of data — is the developmental target. The book builds graphicacy from the ground up: marks and channels (Chapter 1) → chart selection grammar (Chapter 2) → full taxonomy fluency (Chapters 5–13) → design audit capability (Chapter 14).

---

## Prerequisite Map

| Prerequisite | Safe to assume? | If not: where handled |
|---|---|---|
| Basic statistics (mean, median, quartile) | Probably | Embedded at first use in Chapter 7 (distribution) |
| HTML/CSS basics | Probably | Chapter 4 covers minimum viable web literacy |
| JavaScript fundamentals | No — explicit barrier | Chapter 4 frames Claude Code as the implementation layer |
| What a dataset is (rows, columns, data types) | Yes | — |
| Basic chart literacy (knows what a bar chart is) | Yes | — |
| D3 API familiarity | No — and this is the point | The book's thesis is that this is no longer required |
| Familiarity with Tufte, Cairo, Bertin, or visualization theory | No | Part I builds this from scratch |

---

## Central Argument

**Thesis:** "This book argues that the implementation barrier in D3 visualization — the steep API learning curve that has blocked designers, analysts, and researchers for a decade — has been dissolved by LLM-assisted coding, which means that the skills that now determine visualization quality are chart selection, perceptual honesty, and design judgment rooted in the Bertin–Cleveland–Munzner tradition, and this matters because a generation of potential D3 practitioners abandoned the tool for this reason and can now return to it."

**The implication for practice:** The reader's job shifts from syntax memorization to design vocabulary. The Bertin/Cleveland/Munzner/Cairo/Few intellectual tradition is not supplementary enrichment — it is the core professional skill set that Claude Code cannot replace.

**The consequence if ignored:** Readers who use Claude Code without design vocabulary will produce faster, more syntactically correct, but still perceptually dishonest visualizations. Cairo's FiveThirtyEight case demonstrates what this looks like in practice: technically produced, factually misleading. The bottleneck moves from implementation to judgment. This book addresses the new bottleneck.

---

## Field Positioning

**Scott Murray, *Interactive Data Visualization for the Web* (3rd ed., O'Reilly, 2023)**
- Covers: D3 API, SVG, scales, axes, layouts, interaction.
- Misses: The Bertin/Cleveland/Munzner theoretical spine. Cairo's ethical frame. LLM workflow.
- Positioning: "Unlike Murray, which teaches D3 API fluency to developers, this book teaches the design judgment the Bertin–Munzner tradition grounds, to analysts and researchers who use Claude Code as their implementation layer."

**Claus Wilke, *Fundamentals of Data Visualization* (O'Reilly, 2019)**
- Covers: Chart selection, design principles, perceptual accuracy, color theory. The closest competitor on content.
- Misses: Any implementation. D3 specifically. The Cairo ethical frame. The Tufte/Few debate.
- Positioning: "Unlike Wilke, which provides the design vocabulary without any implementation path, this book pairs every principle with a working D3 example and adds the Cairo ethical frame Wilke omits."

**Alberto Cairo, *The Truthful Art* / *How Charts Lie***
- Covers: Ethics of visualization, graphicacy, why charts mislead. Essential.
- Misses: Implementation. D3. Taxonomy depth for practitioners.
- Note: Cairo is a source the book teaches from, not a direct competitor. The ethical frame is incorporated into Chapter 2 and the Introduction.

**Edward Tufte, *The Visual Display of Quantitative Information***
- Covers: Data-ink ratio, chartjunk, graphical integrity. Foundational.
- Note: Tufte is a source the book teaches from and argues with. Chapter 14 explicitly positions Few's critique of Tufte as the book's anchor for design judgment. Students learn Tufte's principles and Few's refinements.

**Curran Kelleher (Observable notebooks, YouTube)**
- Covers: D3 mechanics, marks and channels theory (Chapter 1's primary entry point).
- Misses: Structured course arc. Chart selection framework. Assessment-ready exercises.
- Positioning: "Unlike Kelleher's excellent but unstructured tutorials, this book provides a semester-length arc from first principles to a complete project."

**The positioning statement (primary):**
"For analysts, researchers, and students who need to communicate data visually, *Brutalist d3 x Claude* is the course textbook that teaches chart selection, perceptual honesty, and design judgment rooted in the Bertin–Cleveland–Munzner tradition — unlike existing books that force a choice between design theory without code (Wilke) or code without design theory (Murray)."
