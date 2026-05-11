# Chapter 9 — Part-to-Whole Charts
*When the Pieces Have to Add Up to One.*

## Three suggested titles

- Part-to-Whole Charts: The Five-Slice Rule and What Comes After
- Pie Charts Earn Their Criticism, But Not Always
- Nightingale's Rose: When Distortion Earns Its Place

---

## Chapter overview

By the end of this chapter you will be able to build the family of part-to-whole charts — pie, donut, waffle, Marimekko, Nightingale rose — and you will know when each is honest and when each misleads. You will know the five-slice rule (and its perceptual mechanism), the angle-vs-length accuracy comparison from Cleveland & McGill that grounds the case for redesigning over-sliced pies as bar charts, and the conditions under which Florence Nightingale's polar area chart's known distortion can be defended in advocacy contexts and not in analytical ones.

---

## Learning objectives

1. **(Apply)** Build a pie chart that passes the five-slice rule; rebuild an over-sliced pie chart as a bar chart and justify the redesign using the Cleveland & McGill angle-vs-length accuracy comparison.
2. **(Analyze)** Explain the perceptual distortion produced by a Nightingale rose chart's outer-ring amplification, tracing the mechanism to the area-encoding problem Bertin's framework predicts.
3. **(Evaluate)** Select the most appropriate part-to-whole chart for a given dataset size and audience graphicacy level, using Few's clarity-first position rather than Tufte's minimalism-first position.

---

## Opening case — the HAI five-slice pie chart with rule enforcement

Open `pantry/visualization/illustration-diagram.html` (or whichever file in the pantry shows the HAI pie chart with the five-slice rule). Five sectors. Each slice is large enough to read its angle clearly. The chart's title or annotations document the rule: "Pie charts limited to five slices for perceptual accuracy. Categories beyond the top five aggregated into 'Other.'"

This is what a pie chart looks like when it has been *defended*. Most pie charts you encounter have not been defended. They have eight, ten, fourteen slices. The slices below 5% become indistinguishable. The reader cannot rank them by size. The chart shows part-to-whole structure but fails to communicate it.

The five-slice rule is not a stylistic preference. It traces to Cleveland & McGill (1986): humans perceive *angle* with substantially less accuracy than *length*. The pie chart's encoding channel is angle. Past five or six slices, angles are too small for reliable comparison. The rule is the perceptual threshold; the chart that ignores it produces predictable failures.

This is the territory of Chapter 9. Part-to-whole charts use angle (pies, donuts), area (waffles, treemaps in Chapter 10), or stacked length (single stacked bar) as their encoding channels. Each has perceptual costs. Each has an audience and a question for which it is right. The chapter walks them, applies Cleveland & McGill's accuracy ranking, and adopts Stephen Few's "clarity over minimization" stance: pie charts are not categorically wrong, but they fail in specific conditions and the conditions are predictable.

---

## Theoretical grounding — Cleveland & McGill on angle accuracy, Bertin on area encoding, Cairo on Nightingale, Few on chart selection

This chapter draws on four sources, each at the moment its specific contribution is needed.

**Cleveland & McGill (1986).** The accuracy ranking again: position > length > angle > area > luminance > hue. For part-to-whole comparison, the question is which channel encodes proportion best. A pie chart uses angle (rank 4); a stacked bar uses length-without-baseline (rank 3); a waffle chart uses count of equal-area cells (effectively position-along-aligned-scales for the count, rank 2); a treemap uses area (rank 5, with Stevens' sublinear perception). The ranking determines which form is most accurate when only the choice of part-to-whole form is considered. The accuracy hierarchy puts waffle charts and stacked bars above pie charts for proportion comparison. (The pantry's `Visualizing-Percentages-20-Ways-InfoNewt.txt` documents 20 forms; most outperform the pie chart.)

**Bertin on area encoding.** Pie charts and donuts encode magnitude as the *area* of the slice (or, equivalently, the angle of the slice — since angle and area are linearly related when the radius is constant). Stevens' power law on area perception applies (Chapter 1). Bertin's framework predicts the failure: area is a usable but limited magnitude channel; the eye underestimates area sublinearly. Pie chart slices' relative sizes are systematically misread.

**Cairo on the Nightingale rose chart.** Florence Nightingale's polar area chart (1858) showed British army deaths in the Crimean War, broken down by cause (preventable disease, wounds, other) across months. The chart's outer-ring amplification distortion is *known and documented*: a wedge twice as long as its neighbor has roughly four times the area, but the eye reads it as roughly twice as large in ways that are sometimes wrong. Nightingale used the form anyway because the rhetorical force was worth the perceptual cost — and because the comparison she most needed (preventable vs. inevitable deaths) is *between* wedges of the same radial distance, where the distortion partially cancels. Cairo's frame: this is defensible in advocacy contexts; it is not defensible in analytical contexts unless the distortion is explicitly disclosed.

**Few's clarity-first position.** From Chapter 5 and the chartjunk debate. Few rejects Tufte's strict minimalism: the question is "does this support the message?" not "is this strictly data ink?" Applied to part-to-whole: a five-slice pie chart can support a message efficiently when the audience is non-technical and the message is "X dominates the breakdown." A waffle chart for the same data is more accurate but less familiar. Few's position: choose by clarity for the audience, not by minimal-channel-error.

---

## Concept 1 — Pie charts and the five-slice rule

A pie chart represents proportional values as wedges of a circle. The encoding channel is angle (or equivalently, area if the radius is constant). Total values sum to 100% (or some defined total).

### The five-slice rule

Past five or six slices, pie charts fail. The mechanism is angular perception: humans can compare angles between roughly 30° and 150° with reasonable accuracy. Slices below 30° (about 8% of the pie) become hard to distinguish. With fourteen slices averaging around 7% each, the reader sees a wreath of small wedges that all look similar.

The five-slice rule formalizes this:

- **5 or fewer slices, with significant proportion differences** → pie chart can work.
- **6+ slices** → bar chart almost always wins.
- **5 slices that are roughly equal** → still problematic; consider a waffle chart for proportion accuracy or a stacked bar for total + proportion.

### When pie charts work

- Five or fewer slices.
- Significant proportion differences (the largest slice is at least 1.5× the smallest).
- Audience expects a pie chart (executive readers, general audiences with low statistical graphicacy, situations where the part-to-whole *story* matters more than precise comparison).
- The total is meaningful as a single value (a budget, a population breakdown, a revenue split).

### When pie charts fail

- More than five slices.
- Slices are similar in size (the comparison the reader needs to make is exactly the comparison the chart obscures).
- Precise reading of values matters.
- The audience has the graphicacy to read a more accurate form.

### Donut charts

A donut chart is a pie chart with the center removed. The encoding is the same (angle). The donut form has one advantage: the empty center can hold a summary statistic (the total, the average, a key annotation). For dashboard contexts where space is at a premium and a single supporting number adds value, donut charts win over pies. For analytical contexts, they share the pie's perceptual limitations.

The pantry's pie/donut implementations show both forms.

> ### ↳ Dig Deeper — Pie chart redesign as bar chart
>
> **Prompt:**
>
> > Take a published pie chart with 8+ slices (corporate reports, government statistical summaries, and educational publications all have many). Build the bar chart redesign with Claude Code. Compare reading time and accuracy. Apply Cairo's frame: was the original pie chart defensible, or was it a familiarity-bias failure? Cite the Cleveland & McGill ranking.
>
> **What to do with the output:** Save the comparison. Use it as the case study when a colleague defends an over-sliced pie chart.

---

## Concept 2 — Waffle charts and stacked bars

Two part-to-whole forms that outperform pies on perceptual accuracy.

### Waffle charts

A waffle chart represents a percentage (or proportion) as a count of equal-area cells. Typically a 10×10 grid of 100 cells; each cell is 1%. The cells are colored by category; the count of colored cells per category encodes the proportion.

Why waffle charts work:

- The encoding channel is *count of cells* — which the reader processes as position along an aligned grid (the highest-accuracy channel from Cleveland & McGill).
- The 100-cell grid makes percentages directly readable: a category with 23 colored cells is 23%.
- The discrete nature of the grid (cells, not continuous areas) avoids Stevens' power law area-perception issues.

Limitations:

- The form requires a defined total (typically 100%). Open-ended part-to-whole data doesn't work.
- The 10×10 grid is the conventional layout. Larger or smaller grids exist but the convention is so strong that deviation is jarring.
- The chart is less compact than a pie or stacked bar at the same data.

### Stacked bar charts (single bar)

A single stacked bar shows a total split into segments. The encoding channel is *length-without-baseline* for the segments above the bottom. This is one channel-rank below position-along-common-scale (used by individual bars in a multi-bar chart) but still better than angle.

Single stacked bars are particularly useful for showing how a budget, a population, a revenue split decomposes — the *total* is a single bar, and the proportions are visible as segment lengths.

The form's limitation: like stacked area charts (Chapter 6), the segments above the bottom don't share a baseline, so the eye cannot precisely compare segment sizes across bars. For single-bar use, this is fine; for multi-bar comparison, the limitation matters.

The pantry's `stacked-bar.html` shows the form.

---

## Concept 3 — Marimekko (mosaic) charts

A Marimekko chart shows two dimensions of part-to-whole simultaneously: the chart's total area is divided into rectangles where one dimension's width encodes one variable and the other dimension's height encodes another. The chart shows market share by region by product, for example, where region width × product height = combined market share.

### When Marimekko charts work

- Two part-to-whole variables that the reader needs to see jointly.
- The combined "market segments" matter more than either dimension alone.
- The audience has graphicacy to read 2D area encoding.

### When they fail

- More than ~5 categories per dimension. The chart becomes a tile mosaic with tiny rectangles.
- Audiences without graphicacy. The "birds-eye view" of two dimensions of part-to-whole is unfamiliar; readers default to misreading the rectangles as bar chart segments.
- Either dimension has highly skewed values. Some rectangles dominate visually; others vanish.

The Marimekko earns its complexity in specific contexts: business strategy presentations (market share × product line), corporate finance (revenue by product × geography). For audiences without these specific contexts, the form is harder than its alternatives.

---

## Concept 4 — Nightingale rose chart and the rhetorical-vs-analytical distinction

Florence Nightingale's polar area chart (1858) is the classical case for designing with known distortion when the rhetorical force justifies it.

### The form

Nightingale's chart had:

- Twelve wedges per ring, one per month of the year.
- Two rings for two years (April 1854–March 1855 and April 1855–March 1856).
- Each wedge's *radial length* encoded the count of British army deaths from a specific cause.
- Color hue distinguished cause (preventable disease, wounds from battle, other).

The chart showed dramatic seasonal swings in deaths from preventable disease, particularly in the first year before sanitary reforms. The visual force was the chart's argument: the deaths from preventable causes vastly exceeded deaths from battle, and the magnitude was so large it could not be ignored.

### The known distortion

Polar area charts encode magnitude through the *area* of the wedge. As radial length increases, area increases as the *square* (for a fixed angle). A wedge twice as long has roughly four times the area. The eye, reading area, perceives the difference as larger than the data alone would predict — Stevens' power law applies, but the squaring effect of polar geometry compounds it.

For Nightingale's chart, the comparison most readers make is between months *within the same ring* (preventable disease in January vs. August) where the radial distortion is consistent across compared wedges. The relative sizes are read accurately because both wedges share the same radial position.

The comparison that breaks: between months at very different radii, or between wedges in different rings. For Nightingale's specific advocacy purpose (showing dramatic monthly variation), the form was defensible. For an analytical context where the reader needs to compare absolute counts across years, the form fails.

### Cairo's frame applied

A designer using a Nightingale-style polar chart today is making a choice. Cairo's frame:

- **In advocacy contexts** (a humanitarian campaign showing the scale of preventable deaths; a public-health visualization meant to motivate action), the rhetorical force can justify the perceptual cost. Disclosure is good practice but not always required.
- **In analytical contexts** (a research paper, a decision-support dashboard, a peer-reviewed publication), the distortion is a moral failure unless explicitly disclosed.

The chart is a case study because Nightingale knew exactly what she was doing. Most contemporary designers using polar area charts do not. The form looks visually striking; the distortion is invisible to readers who have not studied perceptual mechanism. The result is a chart that overstates its data without the designer realizing they are doing so.

For Claude Code work: if you are using a Nightingale-style polar chart, document the choice. Add a callout: "Wedge area encodes value (area scales as length squared)." The disclosure is what makes the chart defensible.

---

## Concept 5 — When part-to-whole is the wrong family

Sometimes the data looks like part-to-whole but the question is comparison.

The HAI funding-allocation example from Chapter 2 is the canonical case. The data is part-to-whole (sectors summing to 100%). The question is comparison ("which sectors received the most?"). The right chart is a bar chart sorted by funding descending, not a pie chart. The bar chart uses position-from-baseline (highest-accuracy channel) and supports the ranking question directly. The pie chart uses angle (rank 4) and obscures the ranking past five categories.

The diagnostic: when the message is *ranking* the parts rather than *understanding the parts as part of a whole*, comparison wins over part-to-whole. Cairo's four-step framework (Chapter 2) catches this: step 1 (key message) names whether the message is comparative or compositional, and step 4 (specific form) follows from there.

For Claude Code work: the audit before the chart is what catches this. Ask "is this a comparison question disguised as part-to-whole?" before choosing pie or stacked bar.

---

## Mid-chapter checkpoint

Pick a part-to-whole context from your work. Apply the five-slice rule: how many categories does the data have? If 5 or fewer with significant differences, pie or donut works. If 6+, bar chart wins. If the message is ranking rather than composition, bar chart wins regardless.

Check the form against audience graphicacy. Pie charts are accessible to anyone who has seen one; waffle charts require a 30-second explanation; Marimekko charts require business-context familiarity.

---

## Extended worked example — the HAI funding pie redesign

Take the HAI fiscal year 2024 funding example. Five sectors with these proportions: Food Security 56%, Shelter 21%, Water 14%, Health 6%, Protection 3%.

### Should this be a pie chart?

- Five slices: passes the five-slice rule.
- Significant differences: yes (largest is 18× the smallest).
- Message: "Food Security dominates; Shelter is second; the other three are smaller."

The pie chart can work for this data. The largest two slices are easily distinguishable (56% vs. 21%); the third (14%) is also clearly different; the bottom two (6% and 3%) are small but visible against the larger context.

### Why a bar chart still wins

If the message is "the proportions" — which the message above is — a sorted bar chart shows them more accurately than a pie. Position-from-baseline beats angle. The bar chart also annotates the values directly, removing any need to estimate angles.

The pie chart works *if* the audience expects part-to-whole framing and the visual force of the proportions is the message. The bar chart is more accurate.

### What about a stacked bar?

A single stacked bar (one bar, segmented) is a valid alternative. It shows the same part-to-whole structure as the pie. Its primary channel (segment length, ranked above angle) is more accurate. Its limitation: cross-comparison of segments above the bottom is harder than the comparison in either the pie or the multi-bar chart.

For this data, the single stacked bar would work but adds little over the multi-bar chart.

### What about a waffle chart?

A waffle chart of these proportions: 56 cells colored Food Security, 21 cells Shelter, 14 cells Water, 6 cells Health, 3 cells Protection. The proportions are exactly readable.

For an audience comfortable with waffle charts, this is more accurate than any of the alternatives. For an audience unfamiliar with the form, the chart requires explanation. The trade-off depends on the audience.

### The four-move prompt

For the pie chart version:

```
**Show what I have:**
5 sectors with FY2024 funding percentages: Food Security 56%, Shelter
21%, Water 14%, Health 6%, Protection 3%.

**Say what I want:**
Pie chart in D3 v7. Single self-contained HTML file with inline CSS
and inline D3 (loaded via CDN). Responsive to window resize.

**Constrain it:**
- Marks: pie wedges, one per sector.
- Angle: proportional to percentage (sum of angles = 360°).
- Color hue: sector identity. Use HAI palette: Food Security #8B0000,
  Shelter #6B6B5E, Water #5C3317, Health #4A4A4A, Protection #9B957F.
- Sort order: descending by percentage (largest at 12 o'clock,
  proceeding clockwise).
- Labels: percentage and sector name on each slice (or in legend if
  slices are too small for inline labels).
- Subtitle: "FY2024 Humanitarian Funding by Sector".
- Margins: top 60, right 40, bottom 40, left 40.
- Five-slice rule: this dataset has exactly 5 slices, passing the rule.
  No additional logic needed.
- Dark mode support.

**Verify:**
Restate the channel decomposition. The chart uses angle (Cleveland &
McGill rank 4). For more accurate proportion comparison, a bar chart
or waffle chart would outperform. Confirm that the dataset (5 slices,
significant differences, audience expecting pie format) justifies the
pie choice.
```

For the bar chart redesign version (recommended in most contexts):

```
**Show what I have:** [same data]

**Say what I want:**
Horizontal bar chart in D3 v7. Single self-contained HTML file...

**Constrain it:**
- Marks: rectangles, one per sector.
- y-position: sector (categorical, sorted by percentage descending).
- x-position from zero baseline: percentage (range 0-100%).
- Color luminance: percentage (sequential pale-to-dark, redundant
  encoding).
- Subtitle: "FY2024 Humanitarian Funding by Sector".
- Percentage values labeled at the right end of each bar.
- ...
```

The bar chart is more accurate. Choose between the two based on audience expectation, not on chart-type preference.

---

## Chapter summary

You can now do four things you could not do before this chapter.

You can apply the five-slice rule to any pie chart request: 5 or fewer with significant differences supports a pie; 6+ requires redesign as a bar chart. The rule is grounded in Cleveland & McGill's angle-perception accuracy finding, not in stylistic preference.

You can build pie, donut, waffle, stacked bar, Marimekko, and Nightingale rose charts — choosing based on the channel each uses, the audience's graphicacy, and the rhetorical-vs-analytical context.

You can recognize the Nightingale rose chart's known distortion (radial polar area encoding produces sublinear area perception that is sometimes wrong) and apply Cairo's frame: defensible in advocacy contexts, requires explicit disclosure in analytical contexts.

You can adopt Few's clarity-first position on part-to-whole: pie charts are not categorically wrong, but they fail in specific conditions. The judgment is the design decision.

The thing to watch for, going forward, is the temptation to use a pie chart for any part-to-whole data. The five-slice rule is the threshold. Past it, a bar chart almost always communicates more accurately. The pie chart's familiarity is not the same as its appropriateness.

---

## Key terms

- **Pie chart.** Wedges of a circle, angles proportional to values. Channel: angle (rank 4 in Cleveland & McGill).
- **Donut chart.** Pie with center removed; same encoding, plus center space for summary.
- **Waffle chart.** 10×10 grid; cells colored by category; count encodes percentage.
- **Stacked bar (single).** One bar segmented into colored regions; channel: length-without-baseline.
- **Marimekko (mosaic) chart.** 2D part-to-whole; width and height each encode one variable.
- **Nightingale rose chart.** Polar area chart; radial length encodes value.
- **Five-slice rule.** Pie charts limited to ~5 slices for perceptual accuracy.
- **Rhetorical-vs-analytical distinction (Cairo).** Forms with known distortion are defensible in advocacy contexts; require explicit disclosure in analytical contexts.

---

## Discussion questions

1. The five-slice rule is grounded in Cleveland & McGill's perceptual evidence. Why do pie charts with 8+ slices nonetheless persist in published work?
2. Cairo's distinction between advocacy and analytical contexts blurs in practice. Where does it land for your professional work — are most of your charts one or the other?
3. Waffle charts outperform pie charts on perceptual accuracy but lag on familiarity. When does the accuracy gain justify the familiarity cost?
4. Marimekko charts are powerful when audiences have business context but unfamiliar otherwise. In your professional context, would you use them?
5. *Cross-chapter synthesis.* Chapter 10 (hierarchy charts) treats treemaps as area-encoded forms. Frame the relationship between treemaps and the Marimekko / Nightingale-class area-encoded forms.

---

## Exercises

### Warm-up

**Exercise 9.1** — *Five-slice rule diagnosis.* For each of the following, decide whether a pie chart works or whether redesign is needed:
- 5 product lines with shares 35%, 28%, 18%, 12%, 7%.
- 8 funding categories with shares ranging 1% to 25%.
- 3 demographic groups with shares 60%, 30%, 10%.
- 12 sub-regions with shares each between 4% and 12%.

**Exercise 9.2** — *Pie-to-bar redesign.* Take a published pie chart with 8+ slices. Build the bar chart redesign with Claude Code. Compare.

**Exercise 9.3** — *Waffle chart implementation.* Take five proportions summing to 100%. Build a waffle chart with Claude Code.

### Application

**Exercise 9.4** — *Audit a published part-to-whole chart.* Find a pie or donut chart in a recent publication. Apply the five-slice rule and Cairo's frame. Diagnose any failure.

**Exercise 9.5** — *Single stacked bar comparison.* Take five-category data. Build pie, single stacked bar, and waffle. Compare.

**Exercise 9.6** — *Nightingale-style with disclosure.* Build a polar area chart with explicit disclosure of the radial-area distortion. Justify the choice in Cairo's frame.

### Synthesis

**Exercise 9.7** — *Familiarity vs. accuracy.* Take a part-to-whole context where the audience expects a pie chart but a waffle chart would be more accurate. Build both. Decide which to publish, and document the reasoning.

**Exercise 9.8** — *Marimekko in your domain.* If your professional context supports two-dimensional part-to-whole (market share by region by product, etc.), build a Marimekko chart with Claude Code.

### Challenge

**Exercise 9.9** — *Pie chart redesign portfolio.* Find five published pie charts with 6+ slices. Redesign each. Document the trade-off in each case.

**Exercise 9.10** — *Cairo audit.* Take a part-to-whole chart where the message is comparison but the form is part-to-whole. Identify the misalignment. Apply the four-step framework from Chapter 2 to justify the redesign.

---

## LLM Exercise — Chapter 9: Part-to-Whole Charts

**The Prompt:**

```
I have a part-to-whole dataset of [DESCRIBE: categories, percentages,
total]. The audience is [DESCRIBE: graphicacy, context]. The communication
goal is [DESCRIBE].

Walk me through:
1. Confirm the family is part-to-whole vs. comparison disguised.
2. Apply the five-slice rule: count categories.
3. Choose the form: pie / donut / waffle / single stacked bar / Marimekko.
4. If the form has known distortion (Nightingale rose, Marimekko in
   some configurations), apply Cairo's rhetorical-vs-analytical frame
   and decide whether disclosure is needed.
5. Specify channels.
6. Write four-move Claude Code prompt.

Audit using Evergreen/Emery + part-to-whole-specific (slice count,
sort order, percentage labels, disclosure annotations).
```

**Connection to previous chapters:** Chapter 1 (Cleveland & McGill ranking on angle), Chapter 2 (selection — confirming part-to-whole vs. comparison), Chapter 4 (workflow), Chapter 5 (the comparison alternative).

**Preview of next chapter:** Chapter 10 covers hierarchy charts — treemaps, sunbursts, circle packing. Hierarchy is part-to-whole with depth structure; the chapter examines how the additional structural channel changes form selection.

---

## Visual suggestions

This chapter is about part-to-whole chart selection. Each chart family it discusses has a Part II reference; the focal figure here is the chapter's central worked example, plus a Nightingale rose figure that earns its keep through the chapter's rhetorical-vs-analytical discussion.

Part II references for part-to-whole charts: [Pie Chart](53-pie-chart.md), [Donut Chart](33-donut-chart.md), [Stacked Bar](67-stacked-bar.md), [Marimekko Chart](44-marimekko-chart.md), [Nightingale](48-nightingale.md), [Proportional Area](56-proportional-area.md), [Radial Bar](58-radial-bar.md). Each Part II chapter has its own prompt.

### Figure 9.1 — Five-slice pie vs. fourteen-slice pie

The chapter's central worked example. Two pie charts side by side: one with 5 slices (within Cleveland & McGill's angle-comparison limit, readable), one with 14 slices (well beyond it, fails). The figure makes the five-slice rule a perceptual demonstration.

See [Pie Chart](53-pie-chart.md) in Part II for the canonical reference.

```
Generate two side-by-side pie charts in D3 v7. Two files:

1. `chapter-09-fig-01.html` — full HTML with inline CSS and inline D3 v7. Two SVG panels in a flex layout. Page subtitle: "The five-slice rule — Cleveland & McGill's angle-comparison limit, illustrated."

2. `chapter-09-fig-01/data.json` — the dataset.

Data shape:
- Two slices arrays: `five_slice` (5 categories summing to 100) and `fourteen_slice` (14 categories summing to 100).

{DATA NEEDED} — Any humanitarian-data part-to-whole breakdown that supports both views. The 5-slice version is a high-level rollup (e.g., 5 macro-sector aggregates); the 14-slice version is the detailed breakdown.

Left panel — five-slice pie:
- Five slices, single-hue family with sequential luminance for ordering.
- Direct percentage labels on each slice.
- Readable at a glance.

Right panel — fourteen-slice pie:
- Fourteen slices, default rainbow palette.
- Detached legend with 14 entries.
- Intentionally hard to read; do not "fix" the encoding.

Caption beneath both: "The eye can compare angles between roughly 30° and 150°. Below 30° (slices under ~8% of the circle), comparison fails. Above five slices, multiple slices fall below this threshold."

Style: warm monochrome.

Provide both files as separate code blocks.
```

### Figure 9.2 — Nightingale rose with the rhetorical-vs-analytical toggle

A coxcomb chart of monthly humanitarian deliveries by category, with a toggle exposing the rhetorical-vs-analytical distinction the chapter draws. The rhetorical mode keeps Nightingale's original radius encoding (visually dramatic, perceptually distorted); the analytical mode applies the area correction (less dramatic, perceptually honest). Both modes labeled.

See [Nightingale](48-nightingale.md) in Part II for the canonical reference.

```
Generate a Nightingale-style rose chart in D3 v7 with a rhetorical/analytical toggle. Two files:

1. `chapter-09-fig-02.html` — full HTML with inline CSS and inline D3 v7. A polar area diagram with a toggle. Page subtitle: "Rhetorical vs. analytical — Nightingale's chart with the area correction made visible."

2. `chapter-09-fig-02/data.json` — the dataset.

Data shape:
- 12 months × 2–4 categories per month.
  - `months`: array of `{month, categories: {sector1: value, sector2: value, ...}}`.

{DATA NEEDED} — Monthly humanitarian deliveries broken down by 2–4 sectors (food, shelter, WASH, protection). UNHCR or WFP monthly delivery reports.

Encoding:
- Angular position: month (12 evenly spaced bands), January at 12 o'clock.
- Per category: a wedge from inner radius to outer radius.
- Toggle:
  - "Rhetorical (Nightingale's original)": outer radius scales linearly with value. Visually dramatic; the eye reads area, which scales as r². A doubled value produces a roughly 4× area on the page.
  - "Analytical (area-corrected)": outer radius = sqrt(value), so area scales linearly with value. Smaller, less dramatic, perceptually honest.
- Hue per category.

Caption beneath the toggle reads: "Both modes are valid in different contexts. The rhetorical mode is appropriate for advocacy where the seasonal pattern is the message. The analytical mode is required for technical comparison where exact values matter."

Style: warm monochrome.

Provide both files as separate code blocks.
```

---

## Further reading

- **Cairo, Alberto. (2019).** *How Charts Lie.* Chapter 4 develops the Nightingale case.
- **Cleveland, William S., and Robert McGill. (1986).** "Graphical Perception." Angle perception findings.
- **Wilke, Claus O. (2019).** *Fundamentals of Data Visualization.* Chapter 10 on proportions.
- **The book's pantry** — `Visualizing-Percentages-20-Ways-InfoNewt.txt` for 20 forms; `bar-chart.html` for the redesign target.

---

## Tags

part-to-whole, pie-chart, donut, waffle, stacked-bar, Marimekko, Nightingale-rose, five-slice-rule, Cleveland-McGill-angle, Bertin-area, Cairo-rhetorical-analytical, Few-clarity, D3, Claude-Code
