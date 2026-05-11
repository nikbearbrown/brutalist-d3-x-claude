# Part I — Concepts

The first part of this book is the curriculum: marks and channels, chart selection as a design decision, reading a dataset before writing a prompt, working with Claude Code as a labor partner, the chart-family chapters that follow, and the design-principles synthesis. Read these chapters in order. Each one builds vocabulary that the chapters after it use.

Part II — *Examples* — comes after, alphabetically arranged from `arc-diagram` to `word-cloud`. Part II is reference material. Read it in any order, take what you need, skip what you don't.

---

# Chapter 1 — Marks and Channels
*The Channels Your Eye Trusts and the Ones It Doesn't.*

## Three suggested titles

- Marks and Channels: The Grammar Beneath Every Chart
- Why Position Wins: The Bertin–Cleveland–Munzner Tradition
- The Alphabet of Visualization

---

## Chapter overview

By the end of this chapter you will know why some charts are immediately readable and others are not — and you will know it from the perceptual mechanism, not from a list of rules. You will be able to name the marks (points, lines, areas) and the channels (position, length, area, color hue, color luminance, shape, orientation) that every chart in this book is built from. You will know which channels humans can read accurately for which kinds of data, and you will be able to apply that knowledge to direct Claude Code with the precision that turns a one-shot vague prompt into a one-shot working chart.

---

## Learning objectives

1. **(Remember)** Identify the six primary visual channels in Munzner's taxonomy — position (x and y), size/area, color hue, color luminance, shape, orientation — and classify each as a magnitude or identity channel.
2. **(Understand)** Explain why position is the most perceptually accurate channel for quantitative data, citing the Cleveland & McGill (1986) accuracy ranking and the Heer & Bostock (2010) replication, and naming Stevens' power law as the mechanism behind the area-perception failure.
3. **(Apply)** Given a dataset with specified attribute types (categorical, ordered, quantitative), assign appropriate channels to each attribute and justify each choice using Munzner's expressiveness and effectiveness principles.
4. **(Analyze)** Diagnose a given visualization for channel-attribute mismatches — encoding a categorical variable with luminance, scaling a bubble chart by radius rather than area — and specify the correction with a perceptual mechanism that grounds it.

---

## Opening case — two scatterplots, one dataset, two readings

Look at two scatterplots side by side. Both encode the same data: 50 countries, two attributes per country, GDP per capita and life expectancy.

In the first chart, GDP per capita sits on the x-axis and life expectancy sits on the y-axis. Each country is a single point. The position of the point — its x-coordinate and y-coordinate — encodes the two values. You can read the chart in less than a second. The cluster of low-GDP, low-life-expectancy countries pulls toward the lower left. The high-GDP, high-life-expectancy countries pull toward the upper right. The relationship is visible at a glance.

In the second chart, GDP per capita sits on the x-axis. Life expectancy is encoded by *color luminance* — pale points for low values, dark points for high. The y-axis is unused; all points sit on a single horizontal line. To find a low-life-expectancy country, you scan along the line looking for a pale point. To compare two countries, you look at their two colors and try to estimate which is darker. The relationship is technically there. You cannot read it.

Same data. Different encoding. Different chart.

The first chart used **position** for both quantitative attributes — the highest-accuracy channel humans have for reading numerical magnitude. The second chart used **color luminance** for one of those attributes — a channel that humans can distinguish maybe seven to ten levels of, and that the eye reads slowly. The data is identical. The chart is wholly different in what it lets you see.

This chapter is about why. Specifically, it is about the grammar — the marks and channels — that decides whether a chart works or fails before any aesthetic question is asked. This grammar is not new. It has a tradition that runs from Jacques Bertin in 1967 through William Cleveland and Robert McGill in 1986 through Tamara Munzner in 2014. Every later chapter of this book uses the vocabulary you will learn here. So does Claude Code, when you specify a chart precisely enough for it to build what you actually want.

---

## Theoretical grounding — the Bertin → Cleveland → Munzner tradition

The grammar this book uses comes from a single intellectual lineage. Each figure in the lineage solved a specific problem; each solution rests on the one before. You do not need to read these works in their entirety. You do need to know the shape of the argument, because every design decision in this book traces back to it.

**Jacques Bertin, *Sémiologie Graphique* (1967, English ed. 1983).** The first systematic grammar of visual variables. Bertin distinguishes between the *informational invariant* (in modern statistical language, the dependent variable — the thing the chart is about) and *information components* (the independent variables). He then identifies the visual variables — *retinal variables*, in his term — that can encode these: the two planar dimensions (position x and y), and six others (size, value/luminance, texture, color, orientation, shape). Bertin's working examples — Napoleon's 1812 Russian campaign, John Snow's cholera dot map of London, Florence Nightingale's polar area chart — are themselves marks-and-channels analyses, executed before the framework had a name. Your author's own notes on Bertin (in `pantry/Semiology_of_Graphics_NBB.txt`) walk through these cases in detail.

**William Cleveland and Robert McGill, "Graphical Perception" (1986).** The empirical accuracy ranking. Cleveland and McGill ran controlled experiments asking subjects to make judgments from charts that differed only in how data was encoded — same numbers, different channels. The ranking they reported, from most accurate to least:

> position along a common scale → position along non-aligned scales → length → angle → area → volume → color luminance → color hue.

This is not a stylistic claim. It is the result of psychophysical experiments, and it has been replicated and refined. Jeffrey Heer and Michael Bostock's 2010 *CHI* paper reproduced the ranking using Mechanical Turk and extended it to chart types Cleveland and McGill had not tested (pie charts, treemaps, circle packing). Their replication confirmed: position dominates, area is consistently underestimated, color hue is an identity channel that fails for magnitude.

**The mechanism is Stevens' power law.** Stanley Smith Stevens (1957, 1961) showed that human perception of physical magnitudes follows a power function: perceived magnitude is proportional to actual magnitude raised to an exponent that varies by stimulus. For perceived length, the exponent is approximately 1.0 — perception is nearly linear with actual length. For perceived area, the exponent is approximately 0.7 — perception is *sublinear*, meaning a doubled area is perceived as somewhere between 1.5× and 1.7× larger, not 2×. For brightness (luminance), the exponent is around 0.33 — even more sublinear. This is why a bubble chart sized by radius (which doubles the area when the radius doubles, then doubles the area again when the radius doubles, producing a 4× area for a 2× value) is perceptually misleading. The chart shows 4× area; the data is 2×; the eye reads 2.5×. Three different numbers, none of which match.

**Tamara Munzner, *Visualization Analysis and Design* (2014).** The synthesis. Munzner's book is the canonical modern reference, and the framework she calls *expressiveness* and *effectiveness* is the practical version of Bertin's vocabulary plus Cleveland & McGill's ranking:

- **Expressiveness principle:** the channel must be capable of expressing the attribute type. Use a magnitude channel for quantitative attributes; use an identity channel for categorical attributes. Don't use hue for quantity.
- **Effectiveness principle:** encode the most important attribute on the highest-ranked channel that fits.

Munzner also formalizes the magnitude-vs-identity split. **Magnitude channels** (position, length, area, luminance, saturation) are good for quantitative or ordered attributes. **Identity channels** (hue, shape, texture) are good for categorical attributes. Mixing them — putting a categorical attribute on a magnitude channel, or a quantitative attribute on an identity channel — is the most common encoding error in undergraduate visualization work and in plenty of professional work.

**Curran Kelleher's marks-and-channels video** (transcribed in `pantry/markchennls.txt`) is the accessible entry point for all of this. If you watched only one piece of supplementary material for this chapter, watch that. The book's framework here is the Kelleher-Munzner synthesis with Bertin's specific cases as the worked examples.

---

## Concept 1 — Marks: the geometric primitives

A **mark** is a geometric element used to represent data: a point, a line, a region, a glyph. Every chart in this book is built from marks.

- **Point marks** — dots, circles, single symbols. Scatterplots, bubble charts, dot maps. Each point typically represents one observation.
- **Line marks** — connected sequences of points. Line charts, slope graphs, trend lines. The line implies that the values between points are interpolated; you should not use a line for categorical data because there is no meaningful "between" for categories.
- **Area marks** — filled regions. Bar charts, area charts, treemaps, choropleths, stacked compositions. The region's *area* can carry data (its size encodes magnitude) or merely contain other marks (a country shape contains a color encoding).
- **Glyph marks** — composite symbols. Candlestick bodies-with-wicks, bullet-graph bars-with-bands, stars, arrows. Glyphs let one mark encode multiple attributes at once, at the cost of requiring the reader to learn the symbol.

### The mark choice as a meaning choice

The mark you choose communicates something about the data even before any channel is assigned. A line mark says "these values are connected; they evolve continuously." A point mark says "these are individual observations, not a continuous trend." An area mark says "the size of this region carries meaning."

If you connect categorical observations with a line, you imply continuity that does not exist. This is why "connecting the dots" between unrelated categories is a textbook chart failure — the line itself is making a false claim about the data. The mark is asserting something its data does not support.

A scatterplot with 200 points lets the reader see the cloud and the outliers. A line through the same points smooths the cloud into a trend line — useful for some questions, misleading for others. Choosing the mark is choosing which feature of the data to make visible.

Bertin's working example here: Charles Joseph Minard's 1869 flow map of Napoleon's 1812 Russian campaign, which Edward Tufte later called "the best statistical graphic ever drawn." Minard uses one continuous *area mark* — a band whose width encodes the size of Napoleon's army — that flows from the Niemen River to Moscow and back. The mark choice is the argument: the army is a continuous, depleting mass, and the chart shows it depleting. If Minard had used point marks (one dot per army position), the same data would show troop locations at sample times — a different claim. The mark is the encoding before any channel is assigned.

> ### ↳ Dig Deeper — Marks across the pantry
>
> **Prompt:**
>
> > Look at three D3 chart examples — a bar chart (rectangles as area marks), a scatterplot (circles as point marks), and a line chart (a path as a line mark). For each, explain what claim the choice of mark is making about the data. Then specify what kind of dataset would be inappropriate to render with that mark, and why. Use the Bertin/Cleveland/Munzner framework to ground each answer in a perceptual mechanism, not just a stylistic preference.
>
> **What to do with the output:** Save it. You will use it in Chapter 5 (comparison charts) when the bar chart's area-mark choice is the load-bearing argument for the zero-baseline rule.

---

## Concept 2 — Channels: the visual variables that carry data

A **channel** is a visual variable that can encode a data attribute. The eight major channels in Munzner's taxonomy, ranked by perceptual accuracy for quantitative data (Cleveland & McGill 1986; Heer & Bostock 2010 replication):

1. **Position along a common scale.** A bar chart's bar height. A scatterplot's x and y. The most accurate channel by far.
2. **Position along non-aligned scales.** Small multiples where each panel has its own y-axis. Slightly less accurate than (1) because the reader must mentally align the scales.
3. **Length (without a shared baseline).** A Sankey flow's width. A bar that floats without an anchor. Reasonably accurate but worse than (1) because the eye cannot anchor against a common reference.
4. **Angle.** A pie chart's slice angle. The eye is moderately good at angles between 30° and 150° and substantially worse outside that range. This is why pie charts with many slices fail.
5. **Area.** The size of a circle or rectangle. **Stevens' power law** gives the mechanism: area perception has an exponent around 0.7, so a doubled area is perceived as roughly 1.5–1.7× larger, not 2×. The eye underestimates area, consistently.
6. **Color luminance.** Lightness or darkness. Useful for ordered or sequential data when position is already used. The eye can distinguish maybe 7–10 luminance levels reliably.
7. **Color hue.** Different colors. Excellent for categorical data (red/green/blue distinguish distinct categories at a glance). Useless for quantitative data — the reader cannot rank red, green, and blue without a legend.
8. **Shape.** Circle, square, triangle, star. Categorical only. The reader can distinguish maybe 5–7 shapes reliably before they start blurring.
9. **Orientation.** The angle of a line or glyph. Limited; useful primarily as a secondary identity channel (wind-direction arrows).
10. **Texture.** Hatching, stippling. Largely deprecated in modern visualization; legacy of monochrome printing.

### Magnitude channels and identity channels

Munzner's split:

- **Magnitude channels** are good for *quantitative* data (data with a meaningful order and magnitude): position, length, area, luminance, saturation.
- **Identity channels** are good for *categorical* data (data with distinct labels but no inherent order): hue, shape, texture.

The single most common encoding error in undergraduate visualization work — and in plenty of professional work — is using an identity channel (hue) for a magnitude attribute (a quantitative value). The opening case of this chapter is exactly this error: life expectancy encoded by color luminance instead of position. Luminance is a magnitude channel, but it is far down the ranking; using it when position is available violates the *effectiveness* principle. Worse is the version of this error that uses *hue* for quantity — a chart with eight blobs colored in a rainbow, where bigger numbers correspond to "more saturated" or "redder" hues. The reader cannot decode the ranking without a legend, and even with a legend the comparison is slow and unreliable.

The mirror error — using a magnitude channel for an identity attribute — is rarer but also wrong. A bar chart where bar position implies an order, when the categories have no inherent order, can mislead the reader into seeing a trend that does not exist. (This is why categorical bar charts are often *sorted by value*: the implied order is replaced by an actual one.)

### The expressiveness and effectiveness principles in practice

When you sit down to design a chart, the framework reduces to three steps:

1. Identify the *most important* attribute in your data — the one the reader needs to read first.
2. Encode it on the *highest-ranked channel that fits* its attribute type. Position, if quantitative. Hue, if categorical.
3. For each subsequent attribute, find the next-highest available channel that fits its type.

This is the *effectiveness* principle (encode important attributes with high-ranked channels) constrained by the *expressiveness* principle (the channel must be capable of expressing the attribute type). The constraint matters: the most accurate channel is position, but if position is already used for a more important attribute, you move down the ranking. Channel ranking is conditional, not absolute.

Bertin's worked example for this concept: John Snow's 1854 cholera dot map of London. Snow's communication question was "where in the Soho neighborhood are the cholera deaths concentrated?" The most important attribute was *location* (two-dimensional, continuous, geographic). Snow used the highest-ranked channel that could express it: position on a map. Each death is a point mark; its (x, y) position encodes the address. The clustering around the Broad Street pump is visible without any further channel work. Snow added a few annotations — the brewery whose workers had no cholera, the workhouse whose inmates were mysteriously unaffected — but the central encoding was just *position-of-point-on-map*. The most important attribute on the most accurate channel. The chart worked, the pump handle came off, the cholera outbreak ended. The framework Snow used implicitly is the framework Bertin named explicitly a century later.

> ### ↳ Dig Deeper — Cleveland & McGill, replicated and refined
>
> **Prompt:**
>
> > Walk me through the Cleveland & McGill (1986) experiment design and the perceptual ranking they produced. Then summarize how Heer & Bostock's 2010 *CHI* paper replicated the ranking using Mechanical Turk, and what their extension to pie charts, treemaps, and circle packing added. Where do the two studies agree? Where does the ranking depend on context (chart size, data range, reader expertise)? Cite the specific experimental conditions that produce each finding.
>
> **What to do with the output:** Save it. The ranking returns in Chapter 5 (bar charts as the highest-accuracy comparison form), Chapter 8 (Stevens' power law and the radius-not-area bubble chart failure), Chapter 9 (the angle-comparison limit that grounds the five-slice pie rule), and Chapter 13 (Few's argument that bullet graphs replace gauge charts because position beats angle).

---

## Concept 3 — The accuracy ranking, with Stevens' power law as the mechanism

The Cleveland & McGill ranking is the empirical result. Stevens' power law is the underlying mechanism. They are not redundant — the mechanism explains why the ranking takes the shape it takes.

Stevens published in *Psychological Review* in 1957 a finding that has held up across six decades of subsequent psychophysical research: human perception of physical magnitude is a power function of the actual magnitude. The form is:

> Ψ = k · I^a

where Ψ is perceived intensity, I is physical intensity, k is a scaling constant, and *a* is an exponent that varies by stimulus type.

The exponents matter:

- **Length:** *a* ≈ 1.0. Perception is approximately linear with actual length. Double a line, the eye sees a doubled line. This is why position-along-a-common-scale and length are at the top of the accuracy ranking.
- **Area:** *a* ≈ 0.7. Perception is sublinear. Double an area, the eye sees roughly 1.5–1.7× larger. The eye underestimates area, consistently and in a predictable way.
- **Brightness (luminance):** *a* ≈ 0.33. Strongly sublinear. Doubled luminance is perceived as much less than doubled.
- **Volume (3D shapes):** *a* ≈ 0.6. Even more sublinear than 2D area, which is one of the reasons 3D charts are perceptually worse than their 2D equivalents.

Stevens' law is the mechanism behind several of this book's later design rules:

- **Bubble charts must encode the third variable as area, not radius.** If you scale the bubble's *radius* with the value, the *area* scales with the value squared. A value that doubled produces a bubble whose visual area is 4×. The eye, applying Stevens' power law, perceives that 4× area as roughly 2.5×. The chart now shows three different things at once — the data (2×), the area (4×), the perceived area (2.5×) — and none of them matches another. The fix is to scale by area: doubled value, doubled area, perceived as roughly 1.5× — closer to the data than the radius scaling would produce, though still not perfect.

- **Bar charts beat pie charts for proportion.** Length perception is nearly linear; angle perception is moderate; area perception (which is what the eye is doing when comparing pie slice sizes) is sublinear. The proportion comparison the reader needs to make — "is this slice 30% or 40%?" — is mediated by the worst of the three channels. A bar chart of the same proportions uses position-along-a-common-scale, the most accurate channel. The bar chart wins not because of taste but because of perception.

- **Color luminance is a usable but limited magnitude channel.** Luminance perception is even more sublinear than area, and the eye distinguishes only a small number of luminance levels reliably. A choropleth map (color luminance as the magnitude channel) is therefore a *coarse* magnitude encoding; it shows quintiles or deciles, not exact values. This is fine for the question "where on this map are the high values?" and not fine for the question "what is the exact value here?"

You will encounter the law's consequences in Chapters 5 (proportional ink), 8 (bubble charts), 9 (pie charts), 12 (choropleths), and 14 (the design audit). Each consequence traces back to the same exponent.

### Common misconceptions

**"Color is the most important design choice."** Color is sixth or seventh on the channel ranking for quantitative data. Designers who lead with color produce charts that look polished and read poorly. Lead with position. Use color for the work the position cannot do — adding a categorical dimension, reinforcing a sequential ordering as a redundant encoding.

**"More channels = more information = better chart."** Each channel the reader has to decode is cognitive load. A scatterplot encoding x-position, y-position, point size, point color, and point shape simultaneously is asking a great deal. If your chart genuinely needs five channels, it probably wants to be redesigned as a small-multiples display where each panel encodes fewer dimensions.

**"You should always use the highest-ranked channel."** The ranking is conditional. The highest channel might already be used by a more important attribute. A scatterplot uses x and y for two quantitative variables; if you also have a categorical group attribute, position is taken. You move down the ranking to color hue, which is appropriate for categorical data. The framework tells you what is best when the channel is available; it does not tell you to ignore the structure of your data.

---

## Concept 4 — Bertin's specific cases as worked examples

Three Bertin-class examples (drawn from your author's pantry notes and the Bertin framework) make the marks-and-channels analysis concrete. Each one was created before the framework had a name, but each is best read as an explicit channel decomposition.

**Charles Joseph Minard's 1869 flow map of Napoleon's 1812 Russian campaign.**
- Mark: a single continuous area band representing the army.
- Channels:
  - x-position: longitude (geographic west-east axis).
  - y-position: latitude.
  - band width: number of soldiers — area-as-channel for quantitative magnitude.
  - color: army state (advance / retreat) — hue as identity channel.
  - secondary line below: temperature on a separate y-axis aligned to the geographic x.
- Reading: you see the army's path, the army's depletion, the geographic context, the temperature collapse, and the loss of life on the retreat. Five channels, all carrying data, none decorative. Tufte called it "the best statistical graphic ever drawn." Bertin would say: it uses the most appropriate channel for each attribute, and uses no channels that don't carry data.

**John Snow's 1854 cholera dot map.**
- Mark: point per death.
- Channels:
  - x-position and y-position: street address (geographic).
  - point count at a location: quantity of deaths (mark count, a degenerate channel).
- Reading: the cluster around the Broad Street pump is visible immediately. No legend, no axis labels, no further channels needed. The most important attribute (location) is encoded on the most accurate channel (position-on-map). Snow's chart worked because Snow chose his channels well.

**Florence Nightingale's 1858 polar area chart of British army deaths in the Crimean War.**
- Mark: wedge-shaped area per month.
- Channels:
  - angle around the circle: month (categorical-cyclic, with continuity from December to January).
  - area of the wedge: number of deaths from a specific cause (preventable disease, wounds, other).
  - color hue: cause of death (categorical).
- Reading: the dramatic seasonal swell of preventable disease deaths is visible at a glance. The chart succeeded politically — it convinced the British public and Parliament to fund sanitary reform.
- *But:* the area-as-channel for the radial form means the outer parts of each wedge are amplified relative to the inner parts. A wedge twice as long does not have twice the area; it has roughly four times. Nightingale was aware of this. She used the form anyway because the rhetorical force was worth the perceptual cost — and because the comparison she most needed the reader to make (preventable vs. inevitable deaths) was *between* wedges of the same radial distance, where the distortion cancels.

This last case matters for the book's stance on design rules. Nightingale's chart violates the area-perception accuracy rule that Cleveland & McGill would later codify. It also worked. The point is not that "rules can be broken" — the point is that *the rules describe perceptual mechanisms*, and a designer who understands the mechanism can decide when the rhetorical or political payoff justifies the perceptual cost. Cairo's frame: this is a defensible decision in advocacy contexts; it is not defensible in analytical contexts unless the distortion is explicitly disclosed. Nightingale knew what she was doing. Most designers using Nightingale-style polar charts today do not.

---

## Mid-chapter checkpoint

Pick a chart you have seen recently — in a newspaper, a dashboard, a research paper. Identify its mark (point, line, area, glyph). Identify the two channels it uses most prominently. For each channel, name what data attribute it encodes and whether the attribute is categorical, ordered, or quantitative. Note any channel-attribute mismatch. Note any redundant encoding (two channels carrying the same attribute) and decide whether the redundancy serves the reader or merely adds clutter.

You should be able to do this in 90 seconds. If you cannot, re-read Concept 2.

---

## Extended worked example — building the Humanitarians AI box plot with Claude Code

The Humanitarians AI box-and-whisker plot in `pantry/visualization/box-whisker.html` visualizes simulated AI capability scores across five cognitive domains: Causal Reasoning, Pattern Recognition, Moral Judgment, Creative Synthesis, Embodied Teaching. 80 observations per domain. Score range 10–100. Walk through every channel decision.

**Marks:**
- The box itself is a *rectangle* — an area mark.
- The whiskers are *lines*.
- Outliers are *points*.
- The median is a *horizontal line* inside the box.

**Channels:**
- **x-position:** cognitive domain — *categorical* attribute, 5 values. The expressiveness principle is satisfied: x-position can represent categorical separation. The categories have no inherent order; the chart sorts them by median value to give the reader a ranking the data does not impose.
- **y-position:** AI capability score — *quantitative* attribute, range 10–100. Encoded on the highest-accuracy channel for quantitative data. The y-axis is shared across all five boxes (positions are aligned), which is the most accurate possible encoding (rank 1 in Cleveland & McGill).
- **Box top edge (y-position of the top edge):** Q3, the 75th percentile of the distribution.
- **Box bottom edge:** Q1, the 25th percentile.
- **Box height (length):** the interquartile range — the middle 50% of the distribution.
- **Whisker top:** the maximum value within 1.5× IQR of Q3 (Tukey's rule, 1977).
- **Whisker bottom:** the minimum within 1.5× IQR of Q1.
- **Median line (y-position of the line inside the box):** the 50th percentile.
- **Outlier points:** observations beyond 1.5× IQR.
- **Color hue:** category identity — redundant with x-position (each category already has its own x-coordinate). The hue redundancy serves accessibility (a reader who has trouble distinguishing crowded x-axis labels can still use color to track which category is which) and legend support.

Every shape on the chart carries data. Nothing is decorative. This is the Bertin standard: each visual element is justified by the channel-to-attribute mapping it implements.

### What Claude Code would do without the specification

Submit a vague prompt to Claude Code: "Make a box plot of these AI capability scores."

Claude Code will produce something that looks like a box plot. It may or may not be *the* box plot. Common failure modes:

- The box shows the *full range* (min to max) rather than the IQR. The whiskers are absent or redundant. The chart looks like a box plot but communicates very different information — the visible "box" is now dominated by the most extreme value in each group, not by the bulk of the distribution.
- The y-axis is auto-fit to the data range (say, 30–95) rather than the meaningful range (0 or 10 to 100). Whether this is a problem depends on the reader's question; for cross-distribution comparison, the auto-fit is misleading.
- Outliers are drawn as small ticks rather than distinct points, hiding them.
- Color is applied to the boxes by *value* (a luminance gradient) rather than by *category identity* (hue) — using a magnitude channel for what should be an identity attribute.

Each of these is a channel-theory violation that the Chapter 1 vocabulary names. The reader who has worked through this chapter can diagnose them in seconds.

### The four-move prompt that gets it right

Submit this to Claude Code:

```
**Show what I have:**
Five categories — Causal Reasoning, Pattern Recognition, Moral Judgment,
Creative Synthesis, Embodied Teaching. 80 observations per category.
Each observation is a quantitative score in the range 10-100.

**Say what I want:**
A box and whisker plot in D3 v7. Single HTML file with inline CSS and
inline D3 (loaded via CDN). Responsive to window resize.

**Constrain it:**
- Marks: rectangle (box), line (median, whiskers), point (outliers).
- x-position: category (categorical, no inherent order — sort by median
  for ranking readability).
- y-position: score (quantitative, range 10-100, shared y-axis across
  all boxes for direct comparison).
- Box top edge: Q3 (75th percentile).
- Box bottom edge: Q1 (25th percentile).
- Whisker top: max value within Q3 + 1.5*IQR (Tukey's rule).
- Whisker bottom: min value within Q1 - 1.5*IQR.
- Median: horizontal line at the 50th percentile inside the box.
- Outliers: points beyond 1.5*IQR fences.
- Color hue: category identity, redundant with x-position. One distinct
  hue per category. Use a five-color palette that works in light and dark
  mode.
- Y-axis ticks at 0, 25, 50, 75, 100. Light grid lines at each tick.
- X-axis labels rotated -30 degrees with text-anchor "end" (the category
  names are 12-17 characters and would crowd if horizontal).
- Margins: top 60, right 40, bottom 60, left 60.
- Dark mode support via prefers-color-scheme media query.

**Verify:**
Before writing the code, restate the channel decomposition in your own
words to confirm you understand. Then write the D3 v7 code with comments
showing which line implements which channel. After the code, list any
decisions you made that are not specified above (font choice, exact
margin values, padding) so I can confirm or override them.
```

This prompt is roughly 400 words. Claude Code will produce a chart that matches the pantry's `box-whisker.html` to within minor styling differences. The chart is the right one on the first attempt because the channel decomposition is in the prompt, not in Claude Code's guess about what you wanted.

The pattern of this prompt — channel decomposition first, then design constraints, then verification — repeats in every chapter from this point forward. Each chapter introduces additional design considerations (zero baselines for bars, label-length heuristics, color scale types), but the core remains the same: name the marks, name the channel-to-attribute mappings, and let Claude Code handle the syntax.

---

## Chapter summary

You can now do four things you could not do before this chapter.

You can name the marks (point, line, area, glyph) and the channels (position, length, area, hue, luminance, shape, orientation) and use that vocabulary as the basis for every subsequent chapter.

You can rank the channels by perceptual accuracy for quantitative data, citing Cleveland & McGill (1986) for the empirical ranking, Heer & Bostock (2010) for the replication, and Stevens' power law as the underlying mechanism. You know that position dominates, that area is consistently underestimated, and that hue is an identity channel that misleads when used for magnitude.

You can apply Munzner's expressiveness and effectiveness principles — match channel type to attribute type, encode the most important attribute on the highest-ranked appropriate channel — to design a chart from scratch given only the data and the communication question. You can read a Bertin-class example (Minard, Snow, Nightingale) as a channel decomposition, not as a historical curiosity.

You can specify a chart precisely enough for Claude Code to build it on the first attempt — by naming the marks, the channel-to-attribute mappings, and the design constraints. When Claude Code produces something wrong, you can diagnose the channel-theory violation and fix it in one follow-up prompt.

The thing to watch for, going forward, is the temptation to skip the channel decomposition. "Make a bar chart" is a bad prompt. "Vertical bar chart, x-position for category, bar height for quantity with zero baseline, sequential luminance reinforcing the quantity, x-axis labels rotated -30°" is a good prompt. The difference is the chapter you just read.

---

## Key terms

- **Mark.** A geometric primitive (point, line, area, glyph) used to represent data.
- **Channel.** A visual variable (position, length, area, hue, luminance, shape) that can encode a data attribute.
- **Magnitude channel.** A channel suited for quantitative attributes — position, length, area, luminance.
- **Identity channel.** A channel suited for categorical attributes — hue, shape, texture.
- **Expressiveness principle (Munzner).** The channel must be capable of expressing the attribute type. Don't use hue for quantity.
- **Effectiveness principle (Munzner).** Encode the most important attribute on the highest-ranked appropriate channel.
- **Cleveland & McGill ranking (1986).** The empirical ranking of perceptual accuracy: position > length > angle > area > luminance > hue.
- **Heer & Bostock replication (2010).** Confirmed and extended the ranking to pie charts, treemaps, circle packing.
- **Stevens' power law (1957).** Perceived magnitude = k · (actual magnitude)^a, where the exponent *a* varies by stimulus. Length ≈ 1.0; area ≈ 0.7; luminance ≈ 0.33. The mechanism behind the channel ranking.
- **Redundant encoding.** Two channels encoding the same attribute. Useful for accessibility and emphasis; clutter when applied without purpose.
- **Bertin's *Sémiologie Graphique* (1967).** The original systematic grammar of visual variables.
- **Munzner's *Visualization Analysis and Design* (2014).** The modern synthesis of marks, channels, and the expressiveness/effectiveness principles.

---

## Discussion questions

1. The Cleveland & McGill ranking puts angle below length and far below position. Why, then, do pie charts persist? Identify two scenarios where a pie chart's perceptual cost is worth paying. Frame the answer in terms of the audience's question, not the chart's appearance.
2. A heatmap encodes a quantitative value on color luminance — a channel that is sixth on the magnitude ranking. Heatmaps are nonetheless useful. What does a heatmap let you do that a position-based chart of the same data cannot? When does the trade-off favor the heatmap?
3. Take a chart from a recent newspaper or dashboard. Diagnose every channel-attribute mapping. Identify any case where an identity channel encodes a magnitude attribute or vice versa. Specify the redesign and predict how much the perceptual accuracy improves.
4. The expressiveness principle says hue should not be used for quantitative attributes. Diverging color scales (red-white-blue for negative-zero-positive) appear to violate this. Are they an exception, or is something subtler going on? Reframe in terms of the magnitude/identity split.
5. *Cross-chapter synthesis.* Chapter 9 will argue that pie charts should generally be replaced with bar charts. Frame that argument in marks-and-channels terms — what channel does the pie chart use, what does the bar chart's channel offer, and what does Stevens' power law say about each?

---

## Exercises

### Warm-up

**Exercise 1.1** — *Channel identification.* For each of the following, identify the marks and the channel-attribute mappings. List any case where a magnitude attribute is encoded on an identity channel.
- A bubble chart where bubble x-position is GDP per capita, y-position is life expectancy, bubble area is population, and bubble color hue is continent.
- A choropleth where color luminance is unemployment rate.
- A scatterplot with point shape (square, triangle, circle) representing year (2020, 2021, 2022).

**Exercise 1.2** — *Specification practice.* Write a four-move Claude Code prompt for the box plot in the pantry's `box-whisker.html`. Use the show / say / constrain / verify structure. Specify all marks and channel-attribute mappings explicitly.

**Exercise 1.3** — *Failure-mode diagnosis.* You ask Claude Code: "Make a chart of these AI capability scores." Claude Code returns a scatterplot with circles colored by domain (categorical hue) and sized by score (area). Diagnose every channel-attribute mismatch. Specify the corrected encoding.

### Application

**Exercise 1.4** — *Channel choice for a real dataset.* You have a dataset of 50 countries with three attributes: country name (categorical), GDP per capita (quantitative), and continent (categorical, 6 values). Design a chart that shows GDP ranked across countries with continent as a secondary identifier. Specify the marks and the channel-attribute mappings. Justify the channel ranking using the expressiveness and effectiveness principles.

**Exercise 1.5** — *Build it with Claude Code.* Take your specification from Exercise 1.4. Submit the four-move prompt to Claude Code. Verify that the output uses the channels you specified. If it does not, write the follow-up prompt that corrects the mismatch and identifies the channel-theory violation it implements.

**Exercise 1.6** — *Audit a published chart.* Find a chart in a newspaper, a financial report, or a dashboard from the past month. Apply the channel framework. Identify any expressiveness or effectiveness violations. Specify the redesign with one-paragraph perceptual justification per change.

### Synthesis

**Exercise 1.7** — *The Minard analysis.* Look up Charles Joseph Minard's 1869 flow map of Napoleon's 1812 Russian campaign. List every mark and every channel-to-attribute mapping. Identify the most important attribute, the channel it uses, and the channel-ranking justification. Then write a Claude Code prompt that would produce a contemporary version using the same channel decomposition on a different dataset (the dataset is your choice — humanitarian flows, supply-chain logistics, immigration patterns).

**Exercise 1.8** — *The Nightingale defense.* Florence Nightingale's polar area chart violates the area-perception accuracy rule. It also worked. Read the chapter's Nightingale analysis. Make the case for and against using a polar area chart in a contemporary humanitarian-data context. Where does the rhetorical-vs-analytical distinction land you?

### Challenge

**Exercise 1.9** — *Replicate Cleveland & McGill on a small scale.* Design a 5-question survey: same dataset, different encodings (bar / pie / bubble / heatmap / radial bar). Ask three colleagues to estimate values from each. Report the results and compare them to the published ranking. What does the small-N replication add or fail to add?

**Exercise 1.10** — *Channel limits in your domain.* Identify a chart type common in your professional or research domain (medical reports, sports analytics, financial dashboards, climate science). Diagnose the chart's channel use. Identify whether the domain's conventions reflect the channel ranking or override it for domain-specific reasons. If the domain overrides the ranking, defend the override using the rhetorical-vs-analytical distinction from the Nightingale case.

---

## LLM Exercise — Chapter 1: Marks and Channels

**Project:** [TBD — selected after Chapter 00]

**What you're building this chapter:** A channel-mapping audit document for a real dataset, plus the Claude Code prompt that builds the corresponding chart.

**Tool:** Claude Code (for the build) + Claude chat (for the audit)

---

**The Prompt (channel audit):**

```
I have a dataset of [DESCRIBE: rows, columns, types — for example,
"5 cognitive domains and 80 simulated capability scores per domain,
score range 10-100"] and a communication goal: [DESCRIBE: what the
reader needs to know in 5 seconds].

Walk me through the marks-and-channels analysis using the
Bertin / Cleveland & McGill / Munzner framework:

1. Identify each data attribute and classify as categorical, ordered,
   or quantitative.

2. Identify the most important attribute given the communication goal.

3. Recommend a chart type by applying Munzner's expressiveness and
   effectiveness principles. Use the Cleveland & McGill ranking
   (replicated by Heer & Bostock 2010) as the scaffold.

4. Specify the marks (point, line, area, glyph) and the
   channel-to-attribute mappings precisely enough that the chart could
   be built from the specification alone.

5. Flag any channel that is being used redundantly. Justify the
   redundancy in terms of accessibility, emphasis, or legend support.

6. Cite Stevens' power law where it applies (bubble chart area-vs-radius;
   choropleth luminance accuracy; pie chart angle accuracy).

Then write a single Claude Code prompt that would produce the chart.
The prompt should follow the four-move structure (show, say, constrain,
verify) and should be precise enough that Claude Code produces a usable
output on the first attempt.
```

---

**What this produces:** A markdown document with the channel audit (six sections) and a copy-paste-ready Claude Code prompt. Save as `chapter-01-channel-audit.md`.

**How to adapt this prompt:**
- *For your own domain:* Replace the dataset description with your data. The structure works for any dataset.
- *For ChatGPT / Gemini:* Works as-is. Some LLMs default to "use any visually appealing chart" rather than the Cleveland & McGill ranking; the explicit instruction to use the ranking is the constraint that fixes this.
- *For Claude Code:* Submit the channel audit document as context, then ask Claude Code to build the chart. The two-step process (audit, then build) makes the encoding decisions explicit before the code runs.
- *For a Claude Project:* Save the channel framework as the system prompt; the audit prompt becomes the user message. The same Project can serve every chapter's LLM Exercise.

**Connection to previous chapters:** None — this is the first taxonomy chapter. Subsequent chapters' LLM Exercises will reference the channel audit as a prerequisite step.

**Preview of next chapter:** Chapter 2 takes the channel framework and applies it to chart selection — given the data attributes and the communication goal, which of the 60+ available chart types is the right one? Cairo's ethical frame ("a chart that fails its reader is a moral failure, not just a design one") joins the framework here.

---

## Visual suggestions

The figures this chapter discusses, with Claude Code prompts to generate them. Where a figure also appears in Part II as a stand-alone reference chapter, the link is provided; the prompt below is tuned to the channel pedagogy this chapter introduces. The chapter's extended box-plot worked example already contains a full prompt; see Concept 4 above.

For the broader chart-type references this chapter mentions in passing — heatmap, choropleth, treemap, circle packing, line graph, candlestick, bullet graph, sankey, pie chart — see their respective Part II chapters: [Heatmap](39-heatmap.md), [Choropleth](29-choropleth.md), [Treemap](75-treemap.md), [Circle Packing](30-circle-packing.md), [Line Graph](43-line-graph.md), [Candlestick Chart](27-candlestick-chart.md), [Bullet Graph](26-bullet-graph.md), [Sankey Diagram](62-sankey-diagram.md), [Pie Chart](53-pie-chart.md). Each Part II chapter has its own prompt.

### Figure 1.1 — Two scatterplots, one dataset

The opening case made literal. Same 50 countries; GDP per capita and life expectancy plotted twice. Left panel: x-position and y-position carry the two quantitative attributes. Right panel: x-position carries GDP, color luminance carries life expectancy. The reader sees the chapter's argument before the chapter makes it.

See [Scatterplot](36-scatterplot.md) in Part II for the canonical reference.

```
Generate a single HTML page in D3 v7 with two side-by-side scatterplots sharing one dataset. Two files:

1. `chapter-01-fig-01.html` — a full HTML page with inline CSS and inline D3 v7 (loaded from `https://cdnjs.cloudflare.com/ajax/libs/d3/7.8.5/d3.min.js`). Two SVG panels arranged side by side in a flex layout, responsive on resize. Each panel has an in-chart subtitle naming the encoding. Page-level subtitle: "Same data, different encoding — position vs. luminance."

2. `chapter-01-fig-01/data.json` — the dataset.

Data shape:
- 50 countries with three attributes each:
  - `country`: string — country name
  - `gdp`: number — GDP per capita in current USD, range roughly 1,000–100,000
  - `life_exp`: number — life expectancy at birth in years, range 50–85

{DATA NEEDED} — World Bank GDP per capita (current USD) and WHO life expectancy at birth, most recent year. Match the 50 countries to span the full range from low- to high-income.

Left panel — standard scatterplot:
- x-position: `gdp` on a log scale.
- y-position: `life_exp` on a linear scale.
- Each country is a single circle, radius 4, fill walnut.
- No color encoding by attribute.

Right panel — luminance-only scatterplot:
- x-position: `gdp` on the same log scale as the left panel.
- y is fixed at the panel's vertical center; all circles sit on a single horizontal line.
- Color luminance: `life_exp` on a sequential walnut palette (light = 50, dark = 85).
- All circles same radius 4.
- This panel is *intentionally* hard to read; do not "improve" the encoding.

Both panels share an x-axis range. Annotate each panel with the channel decomposition in a small caption box. Include accessibility `<title>` and `<desc>` inside each SVG.

Style: warm monochrome — black, dark walnut, blood-red accents only. Serif body, JetBrains Mono for labels. No gradients, no shadows.

Provide both files as separate code blocks. Do not explain — just produce the files.
```

### Figure 1.2 — Bubble chart with the radius-vs-area distortion toggle

A bubble chart of GDP per capita vs. life expectancy, with population as the third quantitative attribute encoded by bubble size. A toggle switches the size scale between *radius* (the common implementation error) and *area* (the perceptually honest encoding). The chart shows Stevens' power law making real numbers wrong on screen.

See [Bubble Chart](24-bubble-chart.md) in Part II for the canonical reference.

```
Generate a bubble chart in D3 v7 with a radius/area scaling toggle. Two files:

1. `chapter-01-fig-02.html` — a full HTML page with inline CSS and inline D3 v7. Responsive on resize. A toggle button switches the size encoding between `d3.scaleLinear` on radius (incorrect) and `d3.scaleSqrt` on radius (correct, equivalent to scaling area linearly with value). The page subtitle: "Stevens' power law on the page — radius scaling vs. area scaling."

2. `chapter-01-fig-02/data.json` — the dataset.

Data shape:
- 30–50 countries with four attributes:
  - `country`: string
  - `gdp`: number — GDP per capita in USD
  - `life_exp`: number — life expectancy in years
  - `population`: number — population, range roughly 1M–1.4B

{DATA NEEDED} — World Bank GDP per capita, WHO life expectancy, UN population estimate. Most recent year. Span the full population range from small (Iceland, ~400k) to large (China, ~1.4B).

Encoding:
- x-position: `gdp` on log scale
- y-position: `life_exp` on linear scale
- Bubble size: `population` — toggle between linear-on-radius (broken) and sqrt-on-radius (correct, area-linear). Default to broken so the reader sees the distortion first.
- Bubble fill: walnut at 0.4 opacity so overlaps are visible.
- Hover: tooltip with country, gdp, life_exp, population, and the apparent-vs-actual area ratio under each scaling.

The toggle is the teaching device. Label the two states clearly: "RADIUS-LINEAR (perceptually wrong, value-doubled = area-quadrupled)" and "AREA-LINEAR (correct, value-doubled = area-doubled)."

Style: warm monochrome. Serif body, JetBrains Mono for labels and the toggle.

Provide both files as separate code blocks.
```

### Figure 1.3 — Minard's 1869 flow map of Napoleon's 1812 Russian campaign, contemporary remake

A modern recreation of Minard's most-cited statistical graphic, using the same channel decomposition (geographic position, band-width-as-area-mark for army size, hue for advance/retreat, secondary line for temperature). The contemporary version uses humanitarian-convoy or supply-chain data so the chart can be read without the historical context.

The closest Part II reference is [Flow Map](37-flow-map.md), though Minard's chart is more specifically a *territorial-flow band map* than a standard origin-destination flow map. The prompt below produces the Minard variant.

```
Generate a Minard-style territorial flow map in D3 v7. Two files:

1. `chapter-01-fig-03.html` — a full HTML page with inline CSS and inline D3 v7. The page renders a continuous flow band over a base map. The page subtitle: "Five channels, one mark — the Minard analysis applied to a contemporary case."

2. `chapter-01-fig-03/data.json` — the dataset.

Data shape:
- A `route` array of waypoints, each with: `lat`, `lon`, `date` (ISO), `magnitude` (number — drives band width), `direction` ("outbound" or "return"), and optional `temperature` (number, in Celsius).
- A `cases` array of small annotation events along the route: `lat`, `lon`, `date`, `note` (string).

{DATA NEEDED} — Choose one of: (a) a humanitarian convoy route with daily tonnage delivered (UNHCR, WFP, ICRC published reports often have this); (b) a supply chain corridor with daily shipment volumes; (c) a re-rendered Minard dataset (the original is in `pantry/Tuftish_principles_NBB.txt` and on multiple D3 community repositories).

Marks and channels (Bertin's analysis applied to D3):
- Single continuous *area mark*: a `d3.line()`-derived path with variable stroke width or a `d3.area()` band whose width encodes `magnitude`. Render with a smooth curve (`d3.curveCatmullRom`) so the band reads as a single moving entity.
- x-position and y-position: longitude and latitude, projected with `d3.geoMercator()` or `d3.geoEquirectangular()` zoomed to the relevant region.
- Band width: `magnitude` — area-as-channel for quantity.
- Hue: `direction` — walnut for outbound, blood-red for return. Identity channel.
- Secondary line below the map: temperature, time-aligned with the route's date axis. Linked highlight: hovering on the route highlights the corresponding point on the temperature line.
- Annotation glyphs: `cases` events as small markers along the route with hover tooltips.

The chart should look like a single graphic with the temperature line as a subordinate panel below. No legend should be needed if the encodings are tight; if a legend is added, keep it within the same vertical column as the chart.

Style: warm monochrome — black, dark walnut, blood-red accents. Serif body, JetBrains Mono for labels. The base map should be quiet (light gray country outlines, no fill).

Provide both files as separate code blocks.
```

### Figure 1.4 — John Snow's 1854 cholera dot map, contemporary remake

A modern recreation of Snow's Soho cholera map, using a contemporary public-health or service-access dataset. The lesson the chart teaches is the same: position-on-map encodes location, mark-count encodes quantity, and a single channel decision (the most important attribute on the most accurate channel) is the whole chart.

See [Dot Map](34-dot-map.md) in Part II for the canonical reference.

```
Generate a Snow-style point map in D3 v7. Two files:

1. `chapter-01-fig-04.html` — a full HTML page with inline CSS and inline D3 v7. The page renders a base map of a city neighborhood with point markers showing event locations and a small set of annotated landmarks. Page subtitle: "Position on map — the most important attribute on the most accurate channel."

2. `chapter-01-fig-04/data.json` — the dataset.

Data shape:
- `events` array: each entry has `lat`, `lon`, `count` (default 1; use higher counts to indicate multiple events at one address).
- `landmarks` array: `lat`, `lon`, `label` (string), `type` (e.g., "pump", "brewery", "workhouse" — categorical, drives marker shape or an icon).
- `boundaries` (optional): GeoJSON polygons for neighborhood outlines.

{DATA NEEDED} — Choose one of: (a) the original Snow dataset (cholera deaths around the Broad Street pump, freely available in multiple D3 tutorials and GeoJSON archives); (b) a contemporary public-health point dataset (e.g., a city's reported infectious-disease cases by address, anonymized); (c) a service-access dataset (e.g., libraries, food pantries, EV chargers within a city).

Marks and channels:
- Point mark per event. x and y position by lat/lon, projected with `d3.geoMercator()` or `d3.geoTransverseMercator()`.
- Point radius: small (3–4 px) when `count` is 1; scale by `Math.sqrt(count)` for stacked locations.
- Landmarks rendered as larger annotated markers with text labels.
- No color encoding for events — Snow's original used a single mark type. (You may add a sequential luminance ramp by date if the dataset is time-stamped, but call it out as a redundant encoding, not a primary one.)

The clustering pattern should be visible on first glance; that is the design success criterion. Annotations on landmarks should be subtle but legible.

Style: warm monochrome — black, dark walnut, blood-red. The base map quiet (light gray streets, no fill). Serif body, JetBrains Mono for landmark labels.

Provide both files as separate code blocks.
```

### Figure 1.5 — Nightingale's 1858 polar area chart, contemporary remake

A modern recreation of Nightingale's coxcomb chart, applied to a contemporary cyclical dataset (monthly humanitarian deliveries, monthly mortality by cause, monthly hospital admissions). The chapter discusses the chart's perceptual cost (area-as-channel under polar coordinates) and rhetorical force (the seasonal pattern is preattentive); the figure makes both visible. A toggle exposes the area-correction so the reader can see the distortion's magnitude.

See [Nightingale](48-nightingale.md) in Part II for the canonical reference.

```
Generate a Nightingale-style polar area chart in D3 v7 with an area-correction toggle. Two files:

1. `chapter-01-fig-05.html` — a full HTML page with inline CSS and inline D3 v7. The chart is a polar area diagram with 12 angular bands (one per month) and stacked or split sectors per cause/category. A toggle switches between *radius-encoded* (Nightingale's original; perceptually distorted) and *area-encoded* (corrected; smaller, less rhetorical). Page subtitle: "Polar area — rhetorical force and perceptual cost in the same chart."

2. `chapter-01-fig-05/data.json` — the dataset.

Data shape:
- `months`: array of 12 entries; each has `month` (string, "Jan"–"Dec") and `categories` (object: category name → numeric value).

{DATA NEEDED} — A 12-month cyclical dataset broken down by 2–4 categorical causes. Examples: (a) UN humanitarian deliveries by sector (food, shelter, WASH, protection) by month; (b) cause-of-death by month for a chosen population; (c) hospital admissions by department by month.

Encoding:
- Angular position: month, evenly spaced around the circle, January at the top (12 o'clock).
- Per category: a wedge from inner radius to outer radius, with the outer radius driven by the category's monthly value.
- Two encoding modes (toggle):
  - "Radius-linear" (Nightingale's original): outer radius = innerRadius + scale(value). Visually larger.
  - "Area-corrected": outer radius such that the wedge's *area* scales linearly with value (use `Math.sqrt`). Visually less dramatic but perceptually honest.
- Hue: category — identity channel.

The toggle is the teaching device. Label the two states. The reader should be able to flip between them and see the distortion's magnitude.

Style: warm monochrome — black, dark walnut, blood-red. Serif body, JetBrains Mono for labels and the toggle.

Provide both files as separate code blocks.
```

---

## Further reading

- **Bertin, Jacques. (1967, English ed. 1983).** *Semiology of Graphics.* The original framework. The English edition has been reissued by ESRI Press. Read Chapters 1 and 6.
- **Cleveland, William S., and Robert McGill. (1984).** "Graphical Perception: Theory, Experimentation, and Application to the Development of Graphical Methods." *Journal of the American Statistical Association* 79(387). The foundational empirical ranking. The experimental design section is unusually clear.
- **Heer, Jeffrey, and Michael Bostock. (2010).** "Crowdsourcing Graphical Perception: Using Mechanical Turk to Assess Visualization Design." *CHI '10.* The replication that confirmed the ranking and extended it to pie charts, treemaps, circle packing.
- **Munzner, Tamara. (2014).** *Visualization Analysis and Design.* CRC Press. The canonical modern textbook. Chapter 5 is the comprehensive channel taxonomy. If you read one academic textbook on visualization, read this.
- **Stevens, S. S. (1957).** "On the Psychophysical Law." *Psychological Review* 64(3). The power-law mechanism behind the channel ranking. Read for the formulation; subsequent psychophysical work has refined the exponents.
- **Kelleher, Curran. (Observable notebooks and YouTube tutorials).** The marks-and-channels material is the accessible entry point. The transcript is in the book's pantry (`pantry/markchennls.txt`).
- **Tufte, Edward R. (1983, 2nd ed. 2001).** *The Visual Display of Quantitative Information.* Tufte's reading of Minard, Snow, and Nightingale is the most-cited treatment in the visualization literature. Chapter 1 in particular.

---

## Tags

marks, channels, Bertin, Cleveland-McGill, Heer-Bostock, Munzner, Stevens-power-law, expressiveness-principle, effectiveness-principle, position-as-channel, hue-as-identity, magnitude-channels, identity-channels, Minard, Snow, Nightingale, Kelleher, D3, Claude-Code-specification
