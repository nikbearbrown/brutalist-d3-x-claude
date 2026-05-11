# Brutalist d3 x Claude — Scope, Market & Risks

**Author:** Nik Bear Brown
*Phase 4 output from Tic TOC. Updated to reflect full theoretical pantry.*

---

## Comparable Texts Analysis

**Scott Murray, *Interactive Data Visualization for the Web* (3rd ed., O'Reilly, 2023)**
- Target reader: Web developer or developer-adjacent who wants D3 fluency.
- Strongest: API coverage, SVG fundamentals, scales, axes, layouts, interaction.
- Weakest: The Bertin/Cleveland/Munzner theoretical spine is absent. Cairo's ethical frame is absent. LLM workflow is absent (predates the current context).
- Why choose Murray: Students need to become D3 developers. Not the same reader.
- Positioning: "Unlike Murray, which teaches D3 API fluency to developers, this book teaches the design judgment the Bertin–Munzner tradition grounds, to analysts and researchers who use Claude Code as their implementation layer."

**Claus Wilke, *Fundamentals of Data Visualization* (O'Reilly, 2019)**
- Target reader: Anyone who wants to understand visualization principles. No implementation assumed.
- Strongest: Chart selection, design principles, perceptual accuracy, color theory. The closest competitor on content. Covers much of the Bertin/Cleveland territory.
- Weakest: Zero implementation. The Cairo ethical frame is largely absent. The Tufte/Few debate is not engaged. No LLM context.
- Why choose Wilke: Pure design theory course, students have a separate implementation environment.
- Positioning: "Unlike Wilke, which provides the design vocabulary without any implementation path and omits Cairo's ethical frame, this book pairs every principle with a working D3 example and makes the moral stakes of chart choice explicit."

**Alberto Cairo, *The Truthful Art* / *How Charts Lie* (New Riders / Norton)**
- Target reader: Journalists, communicators, general audiences for data literacy.
- Strongest: The ethical frame for visualization (rule utilitarianism). Graphicacy as a concept. The FiveThirtyEight case studies. Uncertainty visualization.
- Weakest: Implementation-free. D3-specific content absent. The Bertin/Cleveland/Munzner taxonomy is not the organizing framework.
- Note: Cairo is a source the book teaches from, not a competitor. The ethical frame is incorporated into Chapter 2 and the Introduction. Students who want to go deeper on Cairo's argument are directed to *The Truthful Art*.

**Edward Tufte, *The Visual Display of Quantitative Information***
- Covers: Data-ink ratio, chartjunk, graphical integrity, proportional ink. Foundational.
- Note: Tufte is a source the book teaches from and argues with. Chapter 14 presents Few's critique of Tufte as the book's design-judgment anchor. Students leave understanding Tufte's heuristics and their limits — a more sophisticated position than either "Tufte is law" or "Tufte is wrong."

**Stephen Few, *Show Me the Numbers* / *Now You See It***
- Covers: Practical data visualization design, dashboard design, the chartjunk critique.
- Note: Few is the book's primary authority on the Tufte/Holmes debate resolution. Chapter 14 draws heavily on Few's analysis of the Bateman/Holmes chartjunk study. Few is not a competitor — he's a source.

**Michael Friendly (history of visualization)**
- Note: Friendly's chapter "A Brief History of Data Visualization" is the primary source for the origin-story framing in Chapter 2. Every chart type has an inventor and a problem it was designed to solve — Friendly's history provides these stories.

**Curran Kelleher (Observable notebooks, YouTube)**
- Covers: D3 mechanics, marks and channels theory (the Chapter 1 entry point).
- Misses: Structured course arc. Chart selection framework. Assessment-ready exercises. The Cairo/Tufte/Few theoretical apparatus.
- Positioning: "Unlike Kelleher's excellent but unstructured tutorials, this book provides a semester-length arc from first principles (Bertin → Munzner) to a complete project (the MBTA model)."

---

## Adoption Decision Tree

**Syllabus fit:** 15 chapters map to a 15-week semester. Part II chapters (5–13) are modular — instructors can assign 6 of 9 chart-family chapters without breaking the arc. Chapter 4 (Claude Code workflow) is the only non-negotiable post-Part I chapter.

**Prerequisite fit:** Assumes basic data literacy and minimal web awareness. Does not assume JavaScript or D3 fluency. Does not assume prior exposure to Bertin, Cairo, Tufte, or Cleveland — Part I builds this from scratch. This is a broader prerequisite profile than any current D3 textbook.

**Exercise fit:** Every chapter has 3–5 exercises, at least one requiring production via Claude Code and evaluation using the Evergreen/Emery checklist. Faculty who assign weekly labs have direct material.

**Ideological fit:** Risk area (see below). Faculty who believe the Bertin/Cleveland/Munzner tradition is the right foundation for a visualization course will find this book aligned. Faculty who believe students must learn D3 syntax directly will not adopt it. Faculty who use Tufte as a primary text may resist the Few-mediated position — this requires careful framing in the proposal.

**Practical fit:** KDP pricing for a self-published EPUB/print puts this at $25–35 student cost, well below O'Reilly pricing ($60–80). Significant adoption advantage for courses where textbook cost is a friction point.

---

## Market Size Estimate

- Graduate data visualization courses (data science, journalism, public policy, information science): ~500–800 adoptable courses in US alone.
- Undergraduate data visualization or data communication courses: ~1,000+ courses.
- Professional development / certificate programs: Large and growing.
- At 30 students per adoption: even 50 course adoptions = 1,500 copies/semester.
- Primary textbook in courses that want the design-theory-plus-implementation combination. Supplementary for courses that use Murray for implementation + this book for design layer.

---

## Feature List with Priority Tags

| Feature | Priority | Learning outcome served | Production effort | Owner |
|---|---|---|---|---|
| Working D3 examples for every chapter (from HAI pantry) | ESSENTIAL | All implementation outcomes | Low (already built) | Author |
| Claude Code prompt templates per chapter, annotated with channel-theory reasoning | ESSENTIAL | Chapter 4 + all Ch. 5–15 production outcomes | Medium | Author |
| Chapter exercises with answer key | ESSENTIAL | All Bloom's Apply/Create outcomes | High | Author + contributor |
| Chart type reference (one-page decision guide mapping functional category → channel theory → form) | IMPORTANT | Chapter 2 selection framework | Low | Author |
| Instructor guide (suggested syllabi, discussion facilitation, Tufte/Few/Cairo debate facilitation notes) | IMPORTANT | Faculty adoption | Medium | Author |
| The Evergreen/Emery checklist formatted as a student worksheet for Chapter 14 | IMPORTANT | Chapter 14 design audit | Low | Author |
| Bertin/Cleveland/Munzner lineage summary (one-page reference for Chapter 1) | IMPORTANT | Chapter 1 theoretical foundation | Low | Author |
| Observable notebook versions of all examples | VALUABLE | Students who prefer live environment | Medium | Contributor |
| Video walkthrough of Chapter 15 MBTA-model project | VALUABLE | Chapter 15 synthesis | High | Author |
| Second dataset set (non-humanitarian for instructors who need domain variety) | VALUABLE | Chapters 5–15 adaptability | Medium | Contributor |
| Companion website with updated examples | ASPIRATIONAL | All chapters as D3 versions evolve | High | Author + volunteer |

**Minimum Viable Textbook:** Working D3 examples + Claude Code prompt templates (with channel-theory annotation) + chapter exercises. An instructor can run a semester course with only these three features. The book is adoptable at the MVT level.

---

## Out of Scope

**D3 API syntax instruction**
REASON: Explicitly excluded by the book's thesis. Claude Code handles implementation. Teaching D3 syntax would produce a different book — Murray exists for that book.
ACKNOWLEDGMENT IN PREFACE: Yes — the preface explicitly names this exclusion and its rationale, and names Murray as the right book for readers who need it.

**JavaScript fundamentals**
REASON: Outside the book's learner profile.
PERMANENTLY EXCLUDED.

**Python/R visualization (matplotlib, ggplot2, Plotly)**
REASON: Out of scope — this is a D3 book. Wilke's book uses ggplot2 examples; Plotly is mentioned as context but not taught.
REOPEN CONDITION: A second edition could add a "D3 vs. ggplot2 decision" chapter.

**Advanced D3 (custom layouts, WebGL, canvas rendering)**
REASON: Requires JS fluency this book explicitly does not assume.
REOPEN CONDITION: Companion advanced volume.

**Uncertainty visualization (error bars, confidence intervals, probability)**
REASON: Cairo covers this in depth (*The Truthful Art* chapters on uncertainty). This book acknowledges the obligation (Chapter 8, Chapter 3) but defers to Cairo for the full treatment. The Chapter 8 scatterplot annotation includes the correlation-is-not-causation note but not a full treatment of statistical uncertainty.
ACKNOWLEDGMENT: Chapter 8 directs readers to Cairo for the full uncertainty treatment.

**Data cleaning and ETL**
REASON: Chapter 15 acknowledges the step but does not teach it. This is a data engineering topic.

**Statistical analysis (regression, inference, hypothesis testing)**
REASON: The book uses statistical outputs (regression lines, confidence intervals, KDE) as visual encodings. It does not teach the statistics.
ACKNOWLEDGMENT: Chapters 7 and 8 note where statistical literacy is assumed and point to appropriate resources.

**Coherence check:** The excluded topics describe three adjacent books: (1) D3 for Developers (Murray), (2) Data Engineering for Analysts, and (3) Statistical Visualization (Wilke, extended). None of these is this book. A clearly scoped first book with three visible adjacent books is publishable.

---

## Adoption Risk Register

**RISK 1: The Thesis Risk**
CATEGORY: Content / Ideological fit
LIKELIHOOD: Medium
IMPACT: High
DESCRIPTION: Faculty who believe D3 mastery requires direct syntax knowledge will not adopt a book that argues otherwise. The book's differentiation is also its adoption barrier with the developer-education segment. Faculty who use Tufte as a primary text may resist the Few-mediated position in Chapter 14.
TRIGGER: Proposal reviews where the "Claude Code replaces syntax learning" framing generates pushback from technical faculty; or where the Few-vs-Tufte position generates pushback from faculty who treat Tufte as law.
MITIGATION 1 (thesis framing): Chapter 4 must be the strongest chapter in the book — the worked example must be undeniable. The preface explicitly names Murray as the right book for readers who need D3 syntax.
MITIGATION 2 (Tufte framing): Chapter 14 presents Tufte's heuristics respectfully before introducing Few's critique. The position is "Few refines Tufte" not "Few replaces Tufte." Faculty who love Tufte should find Chapter 14 gives Tufte his full due.
CONTINGENCY: If the thesis framing causes systematic rejection, reframe as "Claude Code accelerates D3 development" rather than "replaces syntax learning." Less true to the argument but adoptable by a wider faculty group.

**RISK 2: The Chapter 4 Aging Risk**
CATEGORY: Content / Timing
LIKELIHOOD: High (over a 3-year edition cycle)
IMPACT: Medium
DESCRIPTION: Chapter 4 (Claude Code workflow) is the highest-aging-risk chapter. Claude Code's interface, capabilities, and prompt conventions will change.
MITIGATION: Frame Chapter 4 around the MBTA iteration model and the Evergreen/Emery evaluation criteria — both of which are Claude Code-independent. The specific channel-theory vocabulary for prompts (from Chapter 1) is also stable. Separate the stable framework from the current-state interface screenshots.
CONTINGENCY: Companion website with updated Chapter 4 examples, free, updated each major Claude Code version.

**RISK 3: The Pantry Dependency Risk**
CATEGORY: Production
LIKELIHOOD: Low-Medium
IMPACT: Medium
DESCRIPTION: The book's worked examples depend entirely on the HAI D3 pantry (60+ working examples). If these examples break (D3 version changes, CDN changes), the worked examples in every chapter fail.
MITIGATION: Document the D3 version used for all examples. Pin examples to a stable CDN version. Use the existing Kindle/EPUB build pipeline to capture static outputs alongside live examples.
CONTINGENCY: If live examples break, fall back to the static EPUB captures. The Bertin/Cleveland/Cairo/Few theoretical content survives even if the live examples require updating.

**RISK 4: The Tufte/Few Positioning Risk (new)**
CATEGORY: Market / Ideological fit
LIKELIHOOD: Low-Medium
IMPACT: Medium
DESCRIPTION: Some faculty and readers will resist the Few-mediated position on chartjunk. Tufte's *The Visual Display of Quantitative Information* is treated as authoritative in many programs. A book that explicitly argues Tufte's data-ink ratio is a heuristic rather than a law may face resistance from faculty who assign Tufte.
MITIGATION: Chapter 14 presents Tufte respectfully and at length before introducing Few's critique. The framing is "Few refines Tufte for complex real-world charts" not "Few replaces Tufte." The Bateman/Holmes study is presented as empirical evidence, not as a philosophical argument. Faculty who use Tufte can assign this book as a complement.
CONTINGENCY: If this positioning generates systematic resistance, soften to "Tufte's heuristics apply in specific contexts; Few identifies the boundaries of those contexts" — which is accurate and less confrontational.

---

## Top 3 Adoption Risks Summary

**Risk 1 — The Thesis Risk** is the most consequential. The book's differentiation from Murray depends entirely on faculty accepting that Claude Code has changed what D3 learning requires, and its differentiation from Wilke depends on faculty wanting the implementation layer Wilke lacks. Faculty who disagree with the first premise won't assign it; faculty who only want theory will use Wilke. The target adopter is the faculty member who wants both — and that faculty member needs to exist in sufficient numbers. The Bertin/Cleveland/Munzner theoretical spine gives the book credibility with theory-oriented faculty; the HAI D3 pantry gives it credibility with implementation-oriented faculty. The proposal must reach both audiences simultaneously.

**Risk 2 — The Chapter 4 Aging Risk** is likely to materialize within one edition cycle. The MBTA iteration model and Evergreen/Emery evaluation criteria are the stable elements; the Claude Code interface is the perishable element. Separating them in the chapter structure is the mitigation.

**Risk 3 — The Pantry Dependency Risk** is low-probability but high-effort-to-fix if it hits. Pinning D3 versions and maintaining the EPUB build pipeline are the mitigations. The theoretical content (Bertin, Cleveland, Cairo, Few, Gestalt) is entirely independent of the pantry and survives any D3 version change.
