# Chapter 14 — Design Principles in Practice
*From Principle to Audit Checklist.*

## Three suggested titles

- Design Principles in Practice: The Tufte/Few/Cairo Synthesis
- The Evergreen/Emery Audit Applied
- Resolving the Chartjunk Debate, Once and For All

---

## Chapter overview

By the end of this chapter you will have a single audit framework that synthesizes Tufte (data-ink ratio, proportional ink, chartjunk), Few (clarity over minimization), Cairo (graphicacy, ethical responsibility, "compared with what?"), and Gestalt principles (proximity, similarity, enclosure, continuity, figure-ground) into a single 22-point checklist (Evergreen/Emery) you can apply to any visualization. You will resolve the chartjunk debate explicitly, with the book's Few-position conclusion. You will be able to redesign a flawed visualization documenting each change with the principle and perceptual mechanism it serves.

---

## Learning objectives

1. **(Apply)** Audit a completed visualization using the Evergreen/Emery checklist (text, arrangement, color, lines, overall) and the Tufte data-ink ratio heuristic; produce a written critique with specific corrections.
2. **(Evaluate)** Apply Few's critique of Tufte to determine whether a specific visual element is genuine chartjunk or a functional embellishment that serves the communication goal.
3. **(Create)** Redesign a flawed visualization applying all four principles (proportional ink, data-ink ratio, color accessibility, annotation strategy); document each change with the perceptual mechanism it serves.

---

## Opening case — auditing a flawed published chart

A published quarterly report contains the following chart. Take a moment to imagine it (the elements recur in many real charts):

- A bar chart of Q4 sales by region.
- The y-axis starts at $400K instead of $0.
- The bars are 3D rectangles with perspective shading.
- Five regions, with bars colored in five different gradients (red-orange-yellow-green-blue).
- Heavy gridlines at every dollar increment.
- Small text labels rotated 45° at the bottom.
- A title in 8pt italic at the top: "Q4 Performance Highlights."

Walk through the failures one at a time.

**Proportional ink violation (Tufte, grounded in Stevens' power law).** The truncated y-axis means bar lengths do not encode the actual values. A region at $480K and a region at $440K look like a 4× difference; the data shows a 9% difference. The visual claim exceeds the empirical reality.

**Data-ink ratio failure (Tufte heuristic, refined by Few).** The 3D perspective and shading add ink without adding data. Few's resolution: are the 3D effects supporting the message? No — they distort the bar lengths and add visual noise. Cut them. Are the heavy gridlines supporting the message? No — they crowd the data and serve no comprehension goal. Lighten or remove. Color gradients across regions encode nothing meaningful (the regions have no inherent order); replace with a single hue or a single sequential luminance.

**Accessibility failure (Cairo's responsibility frame).** The five-color rainbow palette does not survive color-blind simulation. The title is 8pt italic — small and hard to read. The rotated labels add cognitive load.

**"Compared with what?" failure (Cairo).** The chart shows Q4 by region. Compared to what? Q3? The same quarter last year? The annual target? The chart makes a claim ("Q4 performance highlights") that the data alone cannot support; it needs a comparison reference.

**Gestalt violation.** The crowded gridlines and 3D effects violate proximity (data labels not near their data) and continuity (visual flow disrupted by the gradient). The chart fights its reader.

The redesign is a single chart that fixes all five failures: horizontal bar chart, sorted by Q4 sales descending, zero baseline, no 3D, single muted color, light gridlines at axis ticks only, 16pt sans-serif title, value annotations on the bars, "Compared with Q3" or "vs. Q4 last year" added as a subtitle making the comparison explicit. The redesigned chart is more accurate, more accessible, more readable, and uses less ink — and every change is grounded in a specific principle from the synthesis.

This chapter is about that synthesis: Tufte, Few, Cairo, Gestalt, and Evergreen/Emery applied as a single working framework. By the end of the chapter you will have the audit instrument that operates across every chart in this book.

---

## Theoretical grounding — Tufte, Few, Cairo, Gestalt, Evergreen/Emery

This chapter brings together sources introduced throughout Part I and Part II, now treated as a unified framework.

**Tufte's principles (1983).** Data-ink ratio (maximize the proportion of ink that encodes data; minimize the rest). Proportional ink (visual area of an element must be proportional to the data value it represents). Chartjunk (decorative ink that does not encode data; should be removed). These are the heuristics. They are not commandments.

**Few's clarity-over-minimization position.** From the chartjunk-debate analysis (`pantry/the_chartjunk_debate.txt`). The Bateman et al. (2010) study showed that embellishments which support the message do not reduce comprehension and may aid recall. Few's resolution: the criterion is "does this support the message?" not "is this strictly data ink?" Functional redundancy stays. Decoration goes. The book adopts this position throughout.

**Cairo's ethical frame.** Choosing an ineffective chart is morally significant — not just stylistically suboptimal — when a more appropriate alternative is available. Graphicacy as the audience capacity that constrains chart-form choice. The "compared with what?" check as the mandatory test before any chart is finalized.

**Gestalt principles.** Proximity (related elements grouped together), similarity (similar visual properties group), enclosure (bordered regions perceived as units), continuity (smooth flows perceived as connected), figure-ground (foreground vs. background). These are not stylistic rules — they are descriptions of how the visual system processes information. Every effective chart works *with* these principles; every chart that violates them creates cognitive friction.

**Evergreen/Emery 22-point checklist.** A practical synthesis instrument from Stephanie Evergreen and Ann Emery (`pantry/EvergreenDataVizChecklist.txt`). Five categories — text, arrangement, color, lines, overall — with concrete yes-or-no items. The checklist operationalizes the synthesis. This chapter walks the full checklist; per-chart subsets appeared in Chapters 5–13.

---

## Concept 1 — Proportional ink: the foundation

Proportional ink is the most concrete of Tufte's principles. The visual area of any chart element must be proportional to the data value it represents.

### The mechanism

Stevens' power law on area perception (Chapter 1) gives the perceptual mechanism: the eye perceives area sublinearly. When the visual area of a chart element doesn't match the data value (because the y-axis is truncated, or radius rather than area is encoded, or 3D perspective distorts), the reader's perception diverges from the underlying value in ways predictable from the math.

### The recurring violations

Throughout Part II, you encountered specific proportional-ink violations. Cataloged:

- **Truncated y-axis on bar charts** (Chapter 5). The bar's length encodes (value − baseline), not value. The visual proportion misrepresents.
- **Non-zero baseline on area charts** (Chapter 6). The shaded area encodes (value − baseline) integrated over time, not the actual cumulative magnitude.
- **Radius scaling on bubble charts** (Chapter 8). Doubled value → doubled radius → 4× area, perceived as 2.5×.
- **Radial bars and polar area charts** (Chapters 5, 9, 13). Radial-area encodings have outer-ring distortion that further skews perceived magnitude.
- **3D perspective effects** on any chart. Bars in 3D are read as different magnitudes depending on viewing angle.

The fix in every case is the same: encode the data value as the visual area, with a zero baseline where applicable, using `d3.scaleSqrt` for radius scaling where area is the channel.

### Where proportional ink is *not* required

Line charts (Chapter 6) use point position as the magnitude channel, not area. The y-axis can be non-zero without violating proportional ink. The exception is a real one — the rule is contingent on the chart's channel.

Scatterplots use position too. Heatmaps use color luminance. Each chart's channel determines whether the proportional ink rule applies, in what form.

### The audit checklist item

For any chart with area as a channel: is the area proportional to the value? If a bar chart, zero baseline. If a bubble chart, area encoding (`d3.scaleSqrt`). If an area chart, zero baseline. If a polar/radial form, document the distortion.

---

## Concept 2 — Data-ink ratio: Tufte's heuristic, Few's refinement

Tufte's data-ink ratio is the proportion of total ink that encodes data, divided by the total ink used. Maximize the ratio. Remove non-data ink.

### Tufte's strict version

Tufte's strict reading: every visual element that doesn't encode data is candidate for removal. Heavy gridlines? Remove. Decorative borders? Remove. Tick marks beyond what the data needs? Remove. The chart should consist of as little ink as possible while still showing the data.

### Few's refinement

Few argues this is too strict. Some non-data ink supports the reader. Light gridlines help readers read precise values from a chart. Subtle decorative elements (a banner, a brand color) help the chart fit a publication's visual language. The criterion is whether the element supports the message — not whether it strictly encodes data.

The Bateman et al. chartjunk study supports Few's position: embellishments that supported the message did not reduce comprehension, and aided recall. Tufte's strict reading was too strict.

### The book's position

The book adopts Few's resolution: clarity over minimization. The Tufte heuristics remain useful; they are guides, not commandments. Apply them with judgment. Functional redundancy (color luminance reinforcing position; light gridlines aiding precise reading) stays. Decoration that does not serve the message goes.

### Common decoration to remove

- 3D effects on bars or pies.
- Drop shadows.
- Gradient backgrounds.
- Excessive tick marks.
- Decorative borders.
- "Cosmetic" colors that do not encode data.

### Common functional redundancy to keep

- Light gridlines at axis ticks (aid precise reading).
- Color luminance reinforcing position-encoded magnitude (aid scanning).
- Value annotations on bars (aid precise reading without crowding).
- Subtle separators between chart and surrounding text (aid figure-ground).
- A single neutral-color background tile for the chart area (aid figure-ground).

The audit question for any visual element: does this support the message?

> ### ↳ Dig Deeper — Few-resolved audit applied
>
> **Prompt:**
>
> > Take a published chart from your domain. Walk through every visual element. For each, apply Few's "does this support the message?" test. Categorize as: data ink (encodes a value); functional redundancy (supports the message without encoding); chartjunk (does not support the message). Specify which to keep and which to cut.
>
> **What to do with the output:** Save the audit. The Few-resolved standard is the working criterion for this chapter and the rest of the book.

---

## Concept 3 — Color: categorical, sequential, diverging

Color encoding has three primary use cases. Each has a recommended palette type.

### Categorical color (hue)

- For categorical attributes (different categories, no inherent order).
- Use distinct hues, ideally with similar luminance.
- 5–7 colors maximum (the eye's reliable distinction limit).
- Color-blind safe palettes: ColorBrewer's qualitative palettes; viridis-family; or designed palettes that maintain distinguishability for color-blindness simulators.
- Avoid: red and green together (color-blindness friendly only with luminance variation); excessive saturation (visual fatigue).

### Sequential color (luminance)

- For ordered or quantitative attributes.
- Single hue (or hue gradient through closely-related hues), varying luminance.
- 5–7 luminance levels.
- Pale at the low end, dark at the high end (or reverse if culturally appropriate; this is a convention, but a strong one).
- Examples: viridis, magma, blues, purples, greys.

### Diverging color (two-hue around midpoint)

- For data with a meaningful midpoint (zero, target, baseline).
- Two hues, one for negative direction, one for positive.
- Pale around the midpoint, darker as values diverge.
- Common combinations: red-blue (positive=red), purple-orange, brown-blue.
- Use diverging only when the midpoint is meaningful. For unipolar data, sequential is correct.

### Color in dark mode

The light-mode palette often does not work in dark mode. Specifically:

- Dark backgrounds inversed: light text on dark backgrounds; light bar fills.
- Sequential luminance: light shades for low values become dark shades; dark shades for high become light.
- Categorical hues remain (with adjustments for visibility).
- White and black swap roles (with appropriate luminance adjustments).

For Claude Code work: use `prefers-color-scheme` media query to handle both modes. Specify the dark-mode palette explicitly in the prompt.

### Accessibility check

Test every chart with a color-blindness simulator (Sim Daltonism for macOS, Coblis online). Particularly:

- Red-green confusion (deuteranopia, protanopia) — the most common types.
- Blue-yellow confusion (tritanopia) — less common but real.
- Total absence of color (achromatopsia) — rare but ensure that even without color, the chart conveys information through other channels (position, length, etc.).

A chart that fails the color-blindness test is failing 8% of male readers (and a smaller percentage of female readers). Cairo's frame applies: the failure is not stylistic; it is excluding a specific audience from comprehension.

---

## Concept 4 — Annotation strategy

Annotations are text or graphical elements that explain, label, or highlight specific parts of a chart.

### When to annotate

- A specific data point that matters (an outlier, a turning point, a notable case).
- The "compared with what?" answer that the chart's primary encoding doesn't make explicit.
- Information that the audience needs but the visual encoding doesn't convey (units, source, methodological notes).
- Brand or publication metadata (logo, date, attribution).

### Direct labeling vs. legends

- **Direct labeling.** Label the chart element directly (a name on a bar, a value above a column, a callout pointing to an outlier). Reduces the need for the reader to look back at a separate legend; supports faster reading.
- **Legend.** Separate region of the chart explaining the encoding (color = category, line type = year, etc.). Necessary when many elements share an encoding; can reduce density.

The trade-off: direct labels save reading time but compete with the data for visual prominence. Use direct labels for ≤7 categories; switch to a legend for more.

### Cairo's "the chart must answer the question" criterion

Every annotation should answer a question the reader might have. If it doesn't, it's chartjunk. The questions to anticipate:

- "What does this chart show?" → title and subtitle.
- "What unit is this measured in?" → axis labels with units.
- "What's the comparison?" → "compared with X" annotation.
- "Why is this bar so much higher than the others?" → callout on the outlier.
- "Where does this data come from?" → source citation.

Each question gets an annotation. Each annotation answers a question. Annotations that answer no question are decoration.

---

## Concept 5 — The Evergreen/Emery 22-point checklist

The full instrument. Five categories, with items per category.

### Text (5 items)

1. Title is clear, concise, and informative.
2. Axes are labeled and units are clear.
3. Data labels are visible at deployment size.
4. Annotations support understanding.
5. Body text is legible at deployment size.

### Arrangement (4 items)

6. Sort order is meaningful (when applicable).
7. Layout uses space efficiently.
8. Related elements grouped (Gestalt proximity).
9. Visual flow matches reading order.

### Color (5 items)

10. Color is used purposefully.
11. Sequential / categorical / diverging matched to data type.
12. Color-blind safe.
13. Sufficient contrast with background.
14. Dark-mode behavior verified.

### Lines (4 items)

15. Gridlines support reading without distracting.
16. Axis lines visible but unobtrusive.
17. Stroke widths consistent.
18. No 3D effects or perspective.

### Overall (4 items)

19. No chartjunk that doesn't support the message (Few's criterion).
20. Proportional ink (zero baselines where required; area encoding where required).
21. Data shown without distortion.
22. Accessibility metadata present (ARIA, color-blind safety, sufficient contrast).

### Applying the checklist

Walk every chart through all 22 items. For every "no" answer, write the follow-up prompt that fixes it. The checklist works as both a design discipline (apply during creation) and an audit instrument (apply after creation).

The full checklist is in the pantry: `pantry/EvergreenDataVizChecklist.txt`. Use it.

---

## Mid-chapter checkpoint

Pick a chart from your work. Walk it through all 22 items. Note the items that pass and the items that fail. For each failure, write the corresponding follow-up Claude Code prompt.

Then resolve the chartjunk debate for one specific element. Take a "decorative" element you've seen on a chart and apply Few's "does this support the message?" test. Where does it land?

---

## Extended worked example — full audit and redesign

The opening case's flawed chart (truncated y-axis, 3D, gradient colors, heavy gridlines, small italic title). Walk the audit through the 22 items.

Failed items: 1 (title not informative), 4 (annotations missing), 6 (sort order missing), 8 (related elements not grouped), 10 (color not purposeful), 11 (categorical color used for sequential data), 12 (palette likely fails color-blind), 13 (contrast insufficient), 15 (heavy gridlines distract), 18 (3D effects present), 19 (chartjunk that does not support the message), 20 (truncated y-axis), 21 (data distorted by 3D + truncation), 22 (accessibility not addressed).

That's 14 of 22 failures. The chart is more failure than success. The redesign:

```
**Show what I have:**
Q4 sales by region: 5 regions with quantitative values.
[paste data]

**Say what I want:**
Horizontal bar chart in D3 v7. Single self-contained HTML file with
inline CSS and inline D3 (loaded via CDN). Responsive to window
resize. Light and dark mode support.

**Constrain it:**
- Marks: rectangles, one per region.
- y-position: region (categorical, sorted by Q4 sales descending).
- x-position from zero baseline: Q4 sales (quantitative). Zero baseline
  non-negotiable.
- Color: single muted hue (#9B957F), no gradient, no rainbow.
- y-axis: region labels, no rotation, left-aligned.
- x-axis: ticks at $0, $200K, $400K, $600K. Format as currency.
- Gridlines: light (opacity 0.07), at x-tick positions only.
- Annotations: dollar values labeled at the right end of each bar.
- Title: "Q4 Sales by Region" (16pt, sans-serif, regular).
- Subtitle: "Compared with Q4 2023, regions sorted by Q4 2024 sales".
- Margins: top 60, right 80, bottom 40, left 160.
- ARIA: role="img", aria-label describing the chart; per-bar <title>
  for screen readers.
- Color-blind safe: single hue with sufficient contrast.

**Verify:**
Restate the channel decomposition. Then write D3 v7 code with comments
on which line implements which channel. Confirm zero baseline, no
gradients, no 3D, light gridlines only.
```

The redesigned chart passes all 22 items. The redesign is grounded in specific principles: Tufte's proportional ink (zero baseline), Few's clarity (single color, light gridlines), Cairo's responsibility frame (color-blind safety, comparison made explicit), Gestalt proximity (labels next to bars), and the Evergreen/Emery checklist as the audit instrument.

---

## Chapter summary

You can now do four things you could not do before this chapter.

You can audit any visualization using the Evergreen/Emery 22-point checklist (text, arrangement, color, lines, overall) and produce a written critique with specific corrections.

You can apply Few's clarity-over-minimization resolution to the chartjunk debate: the criterion is "does this support the message?" not "is this strictly data ink?" Functional redundancy stays; decoration goes.

You can apply the unified Tufte/Few/Cairo synthesis: Tufte's heuristics as guides, Few's refinements as the working criterion, Cairo's ethical frame as the responsibility, Gestalt as the perceptual mechanism, Evergreen/Emery as the audit instrument.

You can redesign a flawed visualization, documenting each change with the principle and perceptual mechanism it serves. The redesign is not improvisational; it is grounded in specific frameworks from Part I of this book.

The thing to watch for, going forward, is the temptation to apply the audit only after charts are built. The most useful application is *during* design: writing the four-move prompt with the 22 items in mind, then auditing the output to catch what slipped through.

---

## Key terms

- **Data-ink ratio (Tufte).** Proportion of total ink that encodes data. Tufte's heuristic: maximize.
- **Proportional ink (Tufte, Stevens).** Visual area of element must be proportional to data value. Grounded in Stevens' power law.
- **Chartjunk (Tufte).** Decorative ink that does not encode data. Tufte: remove. Few: depends on whether it supports the message.
- **Few's clarity-over-minimization.** The criterion is "does this support the message?" not "is this strictly data ink?"
- **Cairo's ethical frame.** Chart choice is morally significant; the designer has professional responsibility to the reader.
- **Graphicacy (Cairo).** Audience capacity to read visual representations of data.
- **Gestalt principles.** Proximity, similarity, enclosure, continuity, figure-ground. The perceptual mechanisms behind design rules.
- **Evergreen/Emery 22-point checklist.** Five categories (text, arrangement, color, lines, overall); 22 items. The audit instrument.
- **Functional redundancy.** Visual elements that support the message without strictly encoding data. Few-resolved: keep.
- **Decoration.** Visual elements that do not support the message. Few-resolved: cut.

---

## Discussion questions

1. The chartjunk debate has been ongoing since the early 1980s. Few's resolution is the book's position. Where does it land for your professional work — what kinds of "embellishments" survive Few's test in your domain?
2. The Evergreen/Emery 22 items are a working checklist. Which 5 are the highest-leverage items for the kind of charts you produce?
3. Tufte's strict minimalism has a moral force in some readings (the responsibility to the reader to remove distractions). Few's resolution preserves the force without the strict rules. Where does the reading land for you?
4. Color-blind safety is a Cairo-class accessibility issue. What does failing this test look like in your professional context, and what would the cost of correction be?
5. *Cross-chapter synthesis.* Chapter 15 will produce a complete project. Frame the relationship: how does this chapter's audit framework operate during Chapter 15's project, and how does it operate after?

---

## Exercises

### Warm-up

**Exercise 14.1** — *22-point audit on a published chart.* Find a chart in a recent publication. Walk through all 22 items. Note each pass and fail.

**Exercise 14.2** — *Few-test on three elements.* Take three "decorative" elements (gradient backgrounds, 3D bar effects, drop shadows). For each, apply Few's "does this support the message?" test. Where does each land?

**Exercise 14.3** — *Color-blind audit.* Take five recent charts from your work. Test each with a color-blindness simulator. How many fail?

### Application

**Exercise 14.4** — *Full redesign.* Take a chart with multiple failures. Walk through the 22-point audit. Specify the redesign with Claude Code. Build it.

**Exercise 14.5** — *Build dark-mode versions.* Take three of your previous charts. Add dark-mode support via prefers-color-scheme media query. Test in both modes.

**Exercise 14.6** — *Annotation audit.* Take a chart you produced. List every annotation. For each, identify which question it answers. Cut any that answer no question.

### Synthesis

**Exercise 14.7** — *Pre-flight audit.* Build the 22-item checklist as a one-page reference document. Use it before publishing the next 5 charts you produce. Refine the checklist from experience.

**Exercise 14.8** — *Cairo-class moral failure.* Find a chart in published work that you would categorize as a Cairo-class moral failure (impedes understanding when a more appropriate choice was available). Walk the analysis.

### Challenge

**Exercise 14.9** — *Three-perspective redesign.* Take a flawed chart. Redesign it three times: once with Tufte's strict minimalism, once with Few's clarity-over-minimization, once with the book's Few-resolved synthesis. Compare.

**Exercise 14.10** — *Build your team's checklist.* If you work with a team, draft a customized version of the Evergreen/Emery checklist for your domain. Test it on five real charts from your team's recent work.

---

## LLM Exercise — Chapter 14: Design Audit

```
I have a visualization to audit and redesign: [DESCRIBE OR PASTE CHART
SPECIFICATION/IMAGE].

Walk me through:
1. Apply the Evergreen/Emery 22-point checklist:
   - Text (5 items)
   - Arrangement (4 items)
   - Color (5 items)
   - Lines (4 items)
   - Overall (4 items)
2. For each failure, name the principle violated (Tufte proportional
   ink? Few clarity? Cairo responsibility? Gestalt proximity? etc.).
3. Specify the redesign: a four-move Claude Code prompt that addresses
   all failures.
4. Document each change with the principle and perceptual mechanism
   it serves.
```

**Connection to previous chapters:** Synthesizes Chapter 1 (Cleveland & McGill, Stevens), Chapter 2 (Cairo's frame), Chapters 5-13 (chart-family-specific design rules). The audit framework operates across all of Part II.

**Preview of next chapter:** Chapter 15 builds a complete project from raw data to published output, using this chapter's audit framework throughout. The project is the final exam: walking the entire pipeline and producing a publishable artifact.

---

## Visual suggestions

The figures this chapter discusses, with Claude Code prompts to generate them. The chapter is about audit and redesign, so the focal figures are before/after pairs — flawed published charts and their corrections, with the audit point named.

For chart-type references the chapter mentions in passing, see Part II directly: [Bar Chart](20-bar-chart.md), [Bubble Chart](24-bubble-chart.md), [Area Graph](19-area-graph.md), [Scatterplot](36-scatterplot.md), [Line Graph](43-line-graph.md), [Heatmap](39-heatmap.md). Each Part II chapter has its own prompt.

### Figure 14.1 — Before/after audit of a flawed bar chart

The chapter's central worked example. A bar chart with multiple Evergreen/Emery audit failures (truncated y-axis, rainbow palette, ambient grid lines, no zero baseline highlighted, decorative gradients) followed by the same data redrawn with each failure corrected. Each correction is labeled.

```
Generate a 6-panel audit/redesign sequence in D3 v7. Two files:

1. `chapter-14-fig-01.html` — full HTML with inline CSS and inline D3 v7. A 2×3 grid: top row is the flawed original chart with 5 audit-failure annotations; bottom row is the same data through 5 sequential corrections to a final clean chart. Page subtitle: "From flawed to clean — five Evergreen/Emery checklist items applied."

2. `chapter-14-fig-01/data.json` — the dataset.

Data shape:
- 8–10 categories with one quantitative value, plus a target value for context.
  - `category`: string
  - `value`: number
  - `target`: number (optional reference)

{DATA NEEDED} — Any humanitarian-program metric by category where multiple-axis problems can be illustrated. Sectoral funding-vs-need ratios, agency response-time-vs-target by region, etc.

Top row, 3 panels — flawed and annotated:
- Panel 1: the original flawed chart (truncated y-axis starting at the data minimum, rainbow palette, ambient grid, 3D bars, no zero indicator).
- Panel 2: same chart with arrows pointing at each failure, labeled (truncation, palette, grid, 3D, etc.).
- Panel 3: the audit checklist with checkboxes — 5 items, each marked failed.

Bottom row, 3 panels — sequential corrections:
- Panel 4: zero baseline established, y-axis range fixed.
- Panel 5: palette reduced to single hue with sequential luminance for ordering; grid simplified.
- Panel 6: final cleaned chart with direct labels, no ambient elements, subtitle naming the chart's claim.

Caption beneath: each panel labeled with the specific Evergreen/Emery checklist item it addresses.

Style: warm monochrome — except the "before" charts which intentionally show the failures (do not fix them).

Provide both files as separate code blocks.
```

### Figure 14.2 — Color scale family: categorical, sequential, diverging

A reference figure showing the three color scale types side by side, each applied to a small dataset of the appropriate type. The reader sees the expressiveness principle (categorical scale for categorical data, sequential for ordered, diverging for centered) made visible.

```
Generate a 3-panel color-scale demonstration in D3 v7. Two files:

1. `chapter-14-fig-02.html` — full HTML with inline CSS and inline D3 v7. Three small panels in a row, each rendering a small chart with one of the three color scale types applied. Page subtitle: "Three scale types, three data types — categorical, sequential, diverging."

2. `chapter-14-fig-02/data.json` — three small datasets.

Data shape:
- `categorical`: 5 categories (programs, regions) for a categorical-bar example.
- `sequential`: 8 ordered values (low to high) for a sequential heatmap.
- `diverging`: 10 values centered on zero (positive and negative deviations) for a diverging-bar example.

{DATA NEEDED} — Any three small datasets of the appropriate types. The chapter's worked-example dataset works for the categorical and sequential cases; the diverging case wants a deviation-from-target dataset.

Panel 1 — categorical:
- 5-category bar chart.
- Hue encodes category identity; 5 distinct hues with similar luminance (so no category reads as more important).

Panel 2 — sequential:
- 8-cell heatmap row.
- Single-hue palette with sequential luminance from light to dark.

Panel 3 — diverging:
- 10-bar deviation chart with positive bars right of zero, negative bars left.
- Two-hue diverging palette (e.g., walnut for negative, blood-red for positive) with white at zero.

Caption beneath each panel names the scale type and the data type it serves.

Style: warm monochrome — except where the scale demonstration requires the named hues (e.g., the diverging panel must show two hues).

Provide both files as separate code blocks.
```

### Figure 14.3 — Annotation strategy: the same chart at three annotation levels

A 3-panel comparison showing one chart at three annotation levels: under-annotated (no labels, no subtitle, no in-chart context), well-annotated (subtitle, direct labels, one in-chart highlight), and over-annotated (every detail labeled, multiple subtitles, callouts everywhere). The figure is the annotation Goldilocks principle made visible.

```
Generate a 3-panel annotation comparison in D3 v7. Two files:

1. `chapter-14-fig-03.html` — full HTML with inline CSS and inline D3 v7. Three small panels in a row, each rendering the same chart with different annotation density. Page subtitle: "Annotation Goldilocks — too little, just right, too much."

2. `chapter-14-fig-03/data.json` — the dataset.

Data shape:
- A 12-month time series with 3 series, plus a few notable events to annotate.
  - `series`: 3 lines of monthly values.
  - `events`: 3–5 dated events with `month` and `note`.

{DATA NEEDED} — Any time-series with annotatable events: humanitarian funding by month with major appeal launches; refugee arrivals with policy-change events; agency response times with operational-incident dates.

Panel 1 — under-annotated:
- Three lines, default colors.
- No subtitle, no axis labels, no series labels, no event markers.
- Reader cannot tell what they are looking at.

Panel 2 — well-annotated:
- Three lines with direct labels at endpoints.
- Subtitle naming the chart's claim.
- 2–3 dated events highlighted with vertical reference lines and one-line notes.
- Y-axis at meaningful round numbers.

Panel 3 — over-annotated:
- Same chart with every monthly value labeled, every series with multiple labels at different points, every event with multi-line callouts, an excessive subtitle, multiple axis annotations.
- Reader cannot find anything because everything is labeled.

Caption beneath: "Annotation should make the reader's primary question answerable in under three seconds. Under-annotation forces guessing; over-annotation forces filtering."

Style: warm monochrome.

Provide both files as separate code blocks.
```

---

## Further reading

- **Tufte, Edward R. (1983).** *The Visual Display of Quantitative Information.* The foundational text. Read Chapters 4-5 for data-ink ratio and chartjunk.
- **Few, Stephen. (2011).** "The Chartjunk Debate." In the book's pantry. The Few-resolved position.
- **Cairo, Alberto. (2016).** *The Truthful Art.* The ethical frame.
- **Cairo, Alberto. (2019).** *How Charts Lie.* The accessible companion.
- **Evergreen, Stephanie. (2019).** *Effective Data Visualization.* The 22-point checklist with examples.
- **The book's pantry** — the Evergreen checklist (`pantry/EvergreenDataVizChecklist.txt`), Tuftish principles, the chartjunk debate.

---

## Tags

design-principles, audit, Tufte, Few, Cairo, chartjunk-debate, data-ink-ratio, proportional-ink, Stevens-power-law, Gestalt, Evergreen-Emery, 22-point-checklist, accessibility, color-blind, dark-mode, annotation-strategy, D3, Claude-Code
