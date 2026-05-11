# Chapter 6 — Time Series and Temporal Charts
*What Changes, in What Direction, How Fast.*

## Three suggested titles

- Time Series and Temporal Charts: Lines, Areas, and the Don't-Skip-Intervals Rule
- Why the Non-Zero Area Baseline Is Always Wrong
- Trends, Cycles, and the Channels That Show Them

---

## Chapter overview

By the end of this chapter you will be able to build the family of temporal charts — line, area, stacked area, stream graph, spiral, Gantt, timeline — and you will know when each is right. You will know why the zero-baseline rule applies to area charts (where area is a magnitude channel) but not to line charts (where point position is the channel), why time should always run left-to-right (Gestalt continuity) and why skipping intervals violates the channel, and how to specify a temporal chart for Claude Code that produces a perceptually honest output on the first attempt.

---

## Learning objectives

1. **(Apply)** Select and build a line chart, area chart, or stream graph for a specified temporal dataset, justifying the choice using the marks-and-channels framework from Chapter 1.
2. **(Analyze)** Identify the design failure in an area chart with a non-zero baseline, explaining the perceptual distortion in terms of area as a channel (Kelleher's worked example: the temperature area chart with non-zero baseline).
3. **(Evaluate)** Assess whether a spiral plot is more or less effective than a standard line chart for a given cyclic dataset, citing the perceptual trade-off between trend visibility and seasonal pattern visibility.

---

## Opening case — the AI capability gap line chart from HAI

Open `pantry/visualization/line-graph.html` in a browser. Three lines diverge across a horizontal time axis from 2016 to 2024. Each line traces a metric of AI capability — accuracy on a benchmark, training compute, model size. The y-axis covers a range that captures all three trajectories (with appropriate scaling); the x-axis covers the full eight years. The lines tell a clear story: the metrics rise together for several years, then diverge after 2020 with one accelerating sharply.

Walk every design decision the chart makes.

**Line marks, not bars.** The temporal dimension is continuous — every month between January 2016 and December 2024 has a meaningful position. Bars would impose discrete categories on what is fundamentally a continuous flow. Lines connect the points, signaling continuity. The reader's eye traces the trajectory as a single shape rather than reading independent bars.

**Time on the x-axis, running left to right.** This is Gestalt continuity at work. Western readers process time as a horizontal flow with the past on the left and the future on the right. Charts that violate this convention (time on the y-axis, time running right to left) impose extra cognitive load. The convention is so strong that it earns its own rule: time goes on x, time runs left to right.

**Y-axis does not need a zero baseline.** Line charts use *point position* as the magnitude channel, not length-from-axis. Stevens' power law (Chapter 1) on length perception applies to bar charts because the bar's length encodes the value; in a line chart, the channel is where the point sits, not how long anything is. A y-axis that starts at, say, the lower bound of the actual data range is not a proportional ink violation. (Bar charts: zero baseline non-negotiable. Line charts: zero baseline often misleading.) This is the channel-theory distinction that separates the two families.

**Continuous x-axis, no skipped intervals.** Every year from 2016 to 2024 is present on the axis at uniform spacing. If the dataset had gaps (no data for 2018), the right move is to mark the gap explicitly — not to compress the axis so 2017 sits next to 2019. Skipping an interval is a Gestalt continuity violation: the eye reads continuous spacing as continuous time.

**Multi-series legibility.** Three lines are a manageable number. Five would be at the upper limit; ten would be a hairball where the eye loses individual trajectories. The chart uses three distinct color hues (categorical encoding) plus distinct line weights to separate the series. Beyond five lines, small multiples (a panel per series, all sharing the y-axis) outperform the single multi-line chart.

This chapter is about building this kind of chart — and several variants — with Claude Code in a way that respects the channel theory the design depends on.

---

## Theoretical grounding — Kelleher's area-chart lesson, MBTA's Marey diagram, Gestalt continuity

This chapter draws on three sources, each at the moment its specific contribution is needed.

**Kelleher's area-chart-with-non-zero-baseline lesson.** In the Kelleher marks-and-channels video (transcript in `pantry/markchennls.txt`), Kelleher walks through a temperature-over-time area chart and identifies a specific failure: the area chart's y-axis does not start at zero, so the shaded area below the line does not encode the actual values. The reader sees an "area" that does not correspond to what the data shows. The line on top of the area is fine — point position carries the magnitude — but the moment area is added as a channel, the zero baseline becomes required. This chapter inherits Kelleher's framing: the rule depends on the channel, and area is the channel that triggers it.

**The MBTA project's Marey diagram (Barry & Card, 2014).** A Marey diagram is a time-distance graph: stations on one axis (typically y), time on the other (typically x), and a single line per train showing its journey through space and time. The MBTA project used Marey diagrams as the primary interface for exploring transit data. The team's framing: a Marey diagram is "an information-rich interface for controlling the visualization" — the chart is both the display and the navigation. The diagram works because position-on-x (time) and position-on-y (station) are both quantitative-magnitude channels, the highest-accuracy combination available. Multi-train density emerges as a Gestalt perception: where many lines cluster, there is congestion; where the lines diverge, there is variance. The diagram is in the temporal-chart family but does work that ordinary time-series charts cannot.

**Gestalt continuity.** The principle that elements arranged along a smooth curve or line are perceived as belonging together. Time naturally has continuity (one second flows into the next), and chart conventions exploit this: a continuous x-axis with smooth line marks reads as continuous flow. Skipping intervals on the x-axis breaks the Gestalt principle and produces a visual claim of continuity that the underlying data does not support. The principle is not a stylistic rule. It is a perceptual mechanism: the eye reads continuity from spacing whether the data justifies it or not.

---

## Concept 1 — Line charts: the workhorse of time series

A line chart is a path connecting data points, where x-position encodes time and y-position encodes a quantitative variable. The mark is a line; the channel is point position; the implication is continuity.

### When line charts work

- The data is continuous over time (or nearly so — data points at regular intervals are usually fine).
- The reader needs to see *trajectory* — the shape of change over time, the moments of inflection, the comparison between trends.
- There are between 1 and 5 series. Beyond 5, multi-series legibility breaks down.
- The y-axis range matters less than the trajectory shape (a non-zero y-axis is acceptable because point position is the channel, not bar length).

### When line charts don't work

- The temporal dimension is *discrete* without meaningful "between" points (annual data, where the line implies a 6-month value that doesn't exist). Bar charts work better here.
- The data is sparse (3-4 data points across decades). A line connecting them implies trajectory the data doesn't support; consider a slope graph or annotated points.
- The reader needs precise values rather than trajectory. Add value annotations or switch to a column chart.

### Design decisions

**Multi-series with too many lines.** Beyond 5 series, the chart becomes hard to read. Options:

- **Small multiples.** One panel per series, sharing the y-axis. The reader compares trajectories across panels.
- **Highlight one series.** Use color to emphasize the focal series; gray-out the others as context.
- **Sparkline grid.** Mini line charts in a grid layout, one per series, often used in dashboards.

**Y-axis range.** No zero baseline required. Use a range that shows the variation clearly. If the range is very narrow (a 5% change at the high end), consider whether the chart is showing the right comparison ("compared with what?" from Chapter 3).

**Smoothing.** D3 offers `d3.curveLinear` (straight segments) and several smoothing options (`d3.curveMonotoneX`, `d3.curveCardinal`, `d3.curveBasis`). For most data, `d3.curveLinear` or `d3.curveMonotoneX` is right. Aggressive smoothing (`d3.curveBasis`) can introduce visual artifacts where the smoothed curve passes "around" data points rather than through them, distorting the data.

**Annotations.** Mark the moments that matter: a peak, a turning point, a notable event. The line shows the trajectory; annotations name what the trajectory means.

> ### ↳ Dig Deeper — Multi-series strategies in your domain
>
> **Prompt:**
>
> > Pick a multi-series time-series problem in my professional domain (sales by region over time, performance metrics across products, indicators across countries). Walk me through three multi-series strategies: single multi-line chart, small multiples, and highlight-one-with-context. For each, name the perceptual mechanism (Gestalt similarity, position-along-aligned-scales, figure-ground) that makes it work, and the conditions where each strategy is the right choice. Cite the Cleveland & McGill ranking.
>
> **What to do with the output:** Save the analysis. Use it as the decision template the next time you face a multi-series time-series problem.

---

## Concept 2 — Area charts: the zero-baseline rule returns

An area chart is a line chart with the area below the line filled. The fill turns the chart from a trajectory display into an area-as-channel display: the visual area below the line communicates magnitude, not just trajectory.

### When area charts work

- The data is non-negative and the cumulative magnitude (the integral of the trajectory) is itself meaningful — total visits over time, cumulative cost, accumulated rainfall.
- A single series where the magnitude under the line is the answer to the communication question.
- Stacked composition (stacked area chart): multiple series combining into a total, and both the total trajectory and the composition are what the reader needs.

### The zero-baseline rule applied to areas

Area charts use **area as a channel**. The visual area below the line encodes magnitude. Stevens' power law on area perception — the perception of area is sublinear, exponent ≈ 0.7 (Chapter 1) — applies. Tufte's proportional ink principle therefore applies: the area must be proportional to the value.

If the y-axis does not start at zero, the area below the line does not represent the value. It represents the value minus the y-axis minimum. The reader's perception of magnitude (what the area looks like) does not match the data. This is the same proportional-ink violation as the truncated bar chart, but with area instead of length as the channel.

Kelleher's worked example: a temperature-over-time area chart with the y-axis starting at 50°F (where the data minimum sits). The shaded area looks dramatic — a large surface representing the temperature. But the area corresponds to (temperature - 50), not temperature. The shape and apparent magnitude are wrong. The fix: zero-baseline the area, or remove the area encoding (use a line chart, where point position is the channel and zero baseline is not required).

Some practitioners argue for non-zero-baseline area charts on aesthetic grounds. The argument fails at the perceptual mechanism: area-as-channel only works when the area corresponds to the value, and the area only corresponds when the baseline is zero. The exception is *centered* area charts (stream graphs; see below) where the baseline is variable by design and the chart's claim is about composition rather than absolute magnitude.

### Stacked area charts

A stacked area chart layers multiple series, with each series' area stacked on top of the previous one. The total area at any point is the sum of all series. The chart shows two things:

- **The total trajectory** — the upper edge of the topmost layer encodes the cumulative sum.
- **The composition** — each layer's area encodes the contribution of one series.

The total trajectory is read accurately (position of the topmost edge, the highest-accuracy channel). The composition is read less accurately — the layers below the topmost don't share a baseline, so the eye cannot precisely compare layer thicknesses across time. Layer ordering matters: put the most stable or most important series at the bottom (where it has a fixed baseline at zero); put the more variable series in the middle.

When to use stacked area:

- The total is the primary question and the composition is secondary.
- You have 2–5 series. Beyond 5, the layers become indistinguishable.

When to use small multiples instead:

- The composition is the primary question.
- You need cross-series comparison at specific time points.

### Stream graphs

A stream graph is a stacked area chart with a *centered* baseline — instead of starting at zero, the baseline is calculated to minimize the variation in series layer thicknesses. The visual effect is an organic flowing shape, often used for showing the rise and fall of categories over time.

Stream graphs have aesthetic appeal — the flowing shape is visually engaging — but they sacrifice precision. Without a zero baseline, individual layer values are harder to read. Use them when the rhetorical force of the shape is the point and precise values are not needed; consider a stacked area chart instead when values matter.

The pantry's `stream-graph.html` shows the form. Open it. Compare to `stacked-area.html`. The trade-off is visible: stream graph is more visually striking; stacked area is more precise.

> ### ↳ Dig Deeper — When stream graphs earn their organic shape
>
> **Prompt:**
>
> > Walk me through three published examples of stream graphs (NYT, Bloomberg, academic papers). For each, identify whether the stream graph form earned its complexity over a stacked area chart with a zero baseline. Apply Cairo's frame: where does the rhetorical force of the organic shape compensate for the precision loss, and where does the precision loss matter more than the rhetorical force?
>
> **What to do with the output:** Save the analysis. Stream graphs are easy to over-use; the discipline is recognizing the small set of contexts where they are the right form.

---

## Concept 3 — Spiral plots and cyclic data

A spiral plot wraps a time series around an Archimedean spiral, with the radial position encoding time and the angular position encoding the cyclic structure (months of the year, days of the week, hours of the day). Each "rotation" of the spiral represents one cycle.

### When spiral plots work

- The data has a strong cyclic structure that linear time hides — seasonal patterns, weekly cycles, daily rhythms.
- The cyclic pattern is the primary question, not the long-term trend.
- The cycle length is roughly constant (annual cycles work better than approximately-quarterly cycles).

### When they don't work

- The cyclic structure is weak or absent. The spiral form imposes a cycle the data doesn't have.
- Precise reading is required. The radial-angular layout is harder to read than a linear time axis.
- The reader is unfamiliar with the form. Spiral plots have a learning curve; for general audiences, a small-multiples line chart (one panel per cycle) often works better.

### The trade-off

Spiral plots accept the perceptual cost of curved layout in exchange for visual emphasis on the cycle. A linear line chart with monthly aid delivery would show the trend; a spiral plot of the same data shows the seasonal cycle as a clock-face pattern.

Cleveland & McGill's ranking applies: position along a curve is less accurate than position along a straight line. Spiral plots win their cost in two specific cases: (1) the cyclic pattern is the answer to the question, and the linear chart would obscure it; (2) the audience values the rhetorical force of the cyclic visual representation.

The pantry's `spiral-plot.html` shows the form. Open it. Compare what the spiral makes visible (the seasonal cycle) and what it makes harder (precise comparison of values across years).

---

## Concept 4 — Gantt charts and timelines

Gantt charts and timelines are a different shape of temporal chart: they show *intervals* on the time axis rather than continuous values.

### Gantt charts

A Gantt chart shows tasks as horizontal bars across time. Each bar's *position* on the time axis shows when the task starts and ends. Each bar's *length* shows the duration. The y-axis is categorical (tasks), and tasks may be grouped or ordered.

Gantt charts are the canonical project-management chart. They work because two channels carry data:

- **x-position (start, end):** when the task happens.
- **bar length (duration):** how long the task takes.

Both channels are position-along-a-common-scale (the time axis), the highest-accuracy channel. The reader can read both start time and duration accurately.

When to use Gantt charts:

- Project planning and tracking, where task durations and dependencies matter.
- Any context where multiple time-extended events overlap and the overlap is part of the question.

When not to use them:

- Discrete events without meaningful duration (a Gantt chart of "events that happened" with all bars one day long is just a categorical strip plot).
- More than ~30 tasks. The chart becomes a wall of bars; consider grouping or filtering.

### Timelines

A timeline is a single horizontal axis with discrete events marked at their dates. Each event is a point or short bar at its position. Annotations describe the event. Timelines work for "story" presentations: a sequence of events with time-spacing as the structure.

Timelines have less channel work than Gantt charts: the only channel is x-position (when). Annotations carry the rest. The chart is closer to a textual structure than a quantitative one.

The pantry's `gantt-chart.html` shows the Gantt form. The MBTA project's published timeline of train schedules is the Gantt-meets-Marey hybrid worth studying; see Barry & Card (2014).

---

## Mid-chapter checkpoint

Pick a temporal dataset you have on hand. Identify which form is most appropriate: line chart, area chart, stacked area, stream graph, spiral, Gantt, timeline. Apply the channel-theory criterion for each: does the form's primary channel match the magnitude perception you need?

Then check for two specific failures: (1) does the chart's primary channel justify a non-zero y-axis, or does the chart use area-as-channel and require zero baseline? (2) does the x-axis skip intervals or maintain Gestalt continuity?

You should be able to do this in 60 seconds.

---

## Extended worked example — the HAI stacked area chart

The Humanitarians AI stacked area chart in `pantry/visualization/stacked-area.html` shows humanitarian funding across five sectors from 2022 to 2024. Walk every design decision.

**Marks:**
- Multiple area shapes, one per sector, stacked.

**Channels:**
- **x-position:** time (months from 2022-01 to 2024-12). Continuous, uniform spacing.
- **y-position (top edge of total):** total funding across all sectors at each time. Quantitative, position-along-common-scale.
- **y-position (boundaries between layers):** the cumulative sum at each layer transition.
- **Layer thickness (vertical extent of each colored region):** that sector's funding at each time. The layer-thickness channel is *length without baseline* for layers above the bottom — the second-highest-accuracy magnitude channel, but worse than position-along-common-scale.
- **Color hue:** sector identity (categorical, 5 colors).
- **Layer ordering:** sectors ordered with the most stable at the bottom (Food Security, the largest and most stable layer) and more variable sectors above.

**Zero baseline:** yes, on the bottom of the stack. The total area below the topmost edge encodes the cumulative funding magnitude correctly.

**Layer-thickness channel limitation:** the second sector (Shelter) has a baseline that varies with time (the Food Security layer's top edge). The eye cannot read Shelter's exact value as easily as Food Security's. This is the fundamental trade-off of stacked area: total trajectory is accurate; individual layer values are less so.

### Building it with Claude Code

The four-move prompt:

```
**Show what I have:**
Monthly humanitarian funding data, January 2022 through December 2024
(36 months). Five sectors per month. Sample (one month):

  2022-01, Food Security, 380.2
  2022-01, Shelter, 142.7
  2022-01, Water and Sanitation, 98.4
  2022-01, Health, 87.3
  2022-01, Protection, 64.1

Data file: data/funding-by-sector.csv

See pantry/visualization/stacked-area.html for the visual pattern.

**Say what I want:**
Stacked area chart in D3 v7. Single self-contained HTML file with
inline CSS and inline D3 (loaded via CDN). Responsive to window
resize.

**Constrain it:**
- Marks: filled area paths, one per sector.
- x-position: month (continuous time axis, 2022-01 through 2024-12).
- y-position (bottom of stack): zero baseline (non-negotiable).
- y-position (top of stack at each x): cumulative sum across sectors.
- Layer ordering (bottom to top): Food Security, Shelter, Water and
  Sanitation, Health, Protection. (Most stable / largest at bottom.)
- Color hue: sector identity. Use d3.scaleOrdinal with five distinct
  hues: Food Security #8B0000, Shelter #6B6B5E, Water #5C3317,
  Health #4A4A4A, Protection #9B957F.
- x-axis ticks at year boundaries (2022, 2023, 2024) plus mid-year
  marks for orientation.
- y-axis ticks at $200M, $400M, $600M, $800M, $1B (or appropriate
  for total range).
- Legend on the right side, with sector colors and labels.
- Subtitle: "Monthly Humanitarian Funding by Sector, 2022-2024
  (USD millions)".
- Margins: top 60, right 200 (right margin for legend), bottom 40,
  left 60.
- Dark mode support via prefers-color-scheme.

**Verify:**
Restate the channel decomposition. Then write D3 v7 code with comments
showing which line implements which channel. List any decisions not
specified above.
```

### Audit checklist

After Claude Code returns the chart, audit using the Evergreen/Emery five-category subset:

- **Text:** Subtitle clear; sector labels in legend; y-axis units explicit.
- **Arrangement:** Layer ordering matches specification (largest/stablest at bottom).
- **Color:** Five distinct hues; categorical mapping; check color-blind safety.
- **Lines:** Light gridlines at y-ticks; layer boundaries visible but not heavy.
- **Overall:** Zero baseline at bottom; total trajectory is the readable upper edge; no chartjunk.

If the layer ordering came out alphabetical (Claude Code's default) instead of the specified order, the follow-up prompt is:

> "Layer ordering should be Food Security at bottom, then Shelter, Water and Sanitation, Health, Protection at top. Reorder via d3.stack().order(d3.stackOrderInsideOut) or by setting the keys explicitly. The ordering puts the most stable layer at the bottom for the most readable baseline."

---

## Chapter summary

You can now do four things you could not do before this chapter.

You can build a line chart, area chart, stacked area, stream graph, spiral, Gantt, or timeline — choosing the form based on whether the data has continuous trajectory, magnitude, cyclic structure, or interval structure.

You can apply the zero-baseline rule correctly across the temporal family: required for area charts (because area is the channel) and stacked area charts (for the bottom of the stack); not required for line charts (because point position is the channel).

You can recognize when a non-line form earns its complexity (stream graphs for organic-shape rhetorical force; spiral plots for cyclic pattern emphasis) and when it does not, citing Cleveland & McGill's accuracy ranking and the perceptual mechanism each form depends on.

You can specify a multi-series temporal chart for Claude Code precisely enough to produce a publishable output on the first attempt — including layer ordering for stacked area, smoothing curves for line charts, and tick placement for the temporal axis.

The thing to watch for, going forward, is the temptation to treat all temporal charts as variations on the line chart. The family is broader than that; the right form depends on what channel the data needs to use. Area charts are line charts plus area-as-channel; the addition triggers the zero-baseline rule. Stacked area is area charts plus composition; the addition triggers the layer-ordering decision. Each addition is a real channel choice with real perceptual consequences.

---

## Key terms

- **Line chart.** Path connecting time-stamped values; channel is point position; zero baseline not required.
- **Area chart.** Line chart with area below the line filled; channel is area; zero baseline required.
- **Stacked area chart.** Multiple area series stacked; total trajectory + composition.
- **Stream graph.** Stacked area with centered baseline; sacrifices precision for organic-shape rhetorical force.
- **Spiral plot.** Time wrapped around an Archimedean spiral; cycle structure as the primary view.
- **Gantt chart.** Tasks as horizontal bars across time; both x-position (start, end) and bar length (duration) carry data.
- **Marey diagram.** Time-distance chart (MBTA project model); position-on-x and position-on-y both quantitative.
- **Gestalt continuity.** Elements arranged in a smooth flow are perceived as belonging together. Time on x-axis, no skipped intervals.
- **Don't-skip-intervals rule.** The temporal axis must maintain uniform spacing; skipping a period violates Gestalt continuity.
- **Layer ordering (stacked area).** Most stable / largest series at the bottom; most variable / smallest at the top. The bottom layer has a fixed zero baseline; layers above have variable baselines, so eye-precision degrades upward.

---

## Discussion questions

1. The zero-baseline rule applies to area charts but not to line charts. The two forms can show the same data. Why does the addition of area as a channel trigger the rule? Frame in marks-and-channels terms.
2. Stream graphs are aesthetically distinctive but perceptually less accurate than stacked area charts. When is the trade-off worth it? Apply Cairo's frame: when does rhetorical force compensate for precision loss, and when is the loss a moral failure?
3. Spiral plots emphasize cyclic structure at the cost of trend visibility. What kind of data justifies this trade-off? Where would a small-multiples line chart (one panel per year) outperform a spiral plot?
4. The MBTA project's Marey diagram is a hybrid form (Gantt-like + line-chart-like). What does it offer that neither form alone provides? When in your professional work would a Marey diagram outperform standard alternatives?
5. *Cross-chapter synthesis.* Chapter 5 (comparison charts) and Chapter 6 (temporal charts) overlap on the line-vs-bar question — when is monthly data a comparison, and when is it a trend? Frame the boundary.

---

## Exercises

### Warm-up

**Exercise 6.1** — *Form selection.* For each of the following, name the right temporal form (line, area, stacked area, stream graph, spiral, Gantt, timeline) and justify the choice:
- Daily website visits over a year, single series, focus on trend.
- Monthly carbon emissions by industry across a decade, focus on composition.
- Hourly energy consumption over a week, focus on the daily cycle.
- Project tasks with start dates, durations, and dependencies.
- Annual GDP per capita for 200 countries, focus on long-term trends.

**Exercise 6.2** — *Zero-baseline diagnosis.* You see an area chart of daily temperature with the y-axis from 50°F to 90°F. Identify the proportional ink violation. Specify two redesigns: keep the area encoding but fix the baseline; remove the area encoding and use a line chart.

**Exercise 6.3** — *Layer ordering.* You're building a stacked area chart of monthly humanitarian funding across five sectors. The largest sector (Food Security) is also the most stable. The smallest sector (Communications) is the most variable. What ordering puts the chart's accuracy where it matters most?

### Application

**Exercise 6.4** — *Build a line chart with Claude Code.* Take a multi-series temporal dataset. Write the four-move prompt. Generate. Audit. Iterate to publishable. Document the iteration log.

**Exercise 6.5** — *Stacked area redesign.* Take a stacked area chart you've seen and apply layer-ordering analysis. Is the most stable layer at the bottom? If not, redesign with Claude Code.

**Exercise 6.6** — *Cyclic data: spiral vs. small multiples.* Take a dataset with strong cyclic structure (monthly sales, hourly traffic). Build it as both a spiral plot and as small multiples (one panel per cycle). Compare reading speed and accuracy with two colleagues.

### Synthesis

**Exercise 6.7** — *Temporal-chart audit.* Find five temporal charts in published reports. Audit each using the Evergreen/Emery five-category subset plus the temporal-specific failures (zero baseline for areas, skipped intervals, layer ordering). Rate the publication's overall temporal-chart discipline.

**Exercise 6.8** — *Gantt vs. timeline.* Pick a sequence of events from your professional context. Build it as both a Gantt chart and a timeline. Compare what each form makes visible.

### Challenge

**Exercise 6.9** — *Build a Marey diagram.* Following the MBTA project model, build a Marey diagram for a transit or transportation dataset (real or simulated). Use Claude Code. Audit against the MBTA project's published example.

**Exercise 6.10** — *Smoothing experiment.* Take a noisy time series. Build it with `d3.curveLinear` (no smoothing), `d3.curveMonotoneX` (mild smoothing), `d3.curveBasis` (heavy smoothing). Compare what each reveals and hides. Identify which is appropriate for which audience and question.

---

## LLM Exercise — Chapter 6: Temporal Charts

**Project:** [TBD — selected after Chapter 00]

**What you're building this chapter:** A multi-series temporal chart with explicit form selection (line / area / stacked area / spiral / Gantt) and the audit document showing why this form is right for the data.

**Tool:** Claude Code (for the build) + Claude chat (for the audit and iteration).

---

**The Prompt (audit + build):**

```
I have a temporal dataset of [DESCRIBE: number of time points, frequency,
number of series, what each series represents, total range]. The
communication goal is [DESCRIBE: what the reader needs to know in 5
seconds].

Walk me through the temporal-chart design:

1. Confirm the family is temporal. If the data is event-based without
   meaningful duration, flag it (timeline rather than time-series).

2. Choose the form: line, area, stacked area, stream graph, spiral,
   Gantt, or small multiples. Justify the choice using:
   - The communication question (trajectory vs. composition vs. cycle
     vs. interval).
   - The number of series (1 to 5 for line/stacked area; 6+ pushes to
     small multiples).
   - The cyclic structure (if any) of the data.
   - The Cleveland & McGill ranking and Stevens' power law on area
     perception.

3. Apply the zero-baseline rule. If the form uses area as a channel
   (area chart, stacked area, stream graph), zero baseline is required.
   If the form uses point position (line chart), zero baseline is
   optional.

4. Specify channels using Chapter 1's framework.

5. Specify layer ordering (for stacked area), smoothing (for line
   charts), tick placement (for the temporal axis).

6. Write a four-move Claude Code prompt that produces the chart.

After Claude Code returns, audit using the Evergreen/Emery subset plus
the temporal-specific checks: zero baseline (where required), no
skipped intervals on x-axis, layer ordering correct, smoothing
appropriate.
```

---

**What this produces:** Audit document plus working temporal chart. Save as `chapter-06-temporal-audit.md` and `chapter-06-temporal.html`.

**How to adapt this prompt:**
- *For your own dataset:* Replace the description.
- *For ChatGPT / Gemini:* Works as-is.
- *For a Claude Project:* Save the temporal-chart framework as system context.
- *For Cowork:* Use Cowork to read the data file directly.

**Connection to previous chapters:** Builds on Chapter 1 (channel ranking; area-as-channel mechanism for the zero-baseline rule), Chapter 2 (chart selection — confirming the temporal family), Chapter 3 (data audit — temporal data type identification), Chapter 4 (Claude Code workflow), Chapter 5 (the zero-baseline rule applied differently across families).

**Preview of next chapter:** Chapter 7 examines distribution charts — histograms, box plots, violins, KDE. The questions shift from "how is this changing over time" to "what does this variable's spread look like." The marks-and-channels framework still applies, with new design decisions (bin width, kernel choice, IQR encoding).

---

## Visual suggestions

This chapter is about time-series chart selection. Each chart family it discusses has a Part II reference; the focal figure here is the chapter's central worked example.

Part II references for time-series charts: [Line Graph](43-line-graph.md), [Area Graph](19-area-graph.md), [Stacked Area](66-stacked-area.md), [Stream Graph](69-stream-graph.md), [Spiral Plot](65-spiral-plot.md), [Gantt Chart](38-gantt-chart.md), [Timeline](72-timeline.md), [Timetable](73-timetable.md). Each Part II chapter has its own prompt.

### Figure 6.1 — The HAI AI capability gap line chart

The chapter's central worked example. A multi-series line chart showing AI capability index across high-, middle-, and low-income country groups from 2016 to 2024. The gap widens visibly. The chart demonstrates the line-chart-vs-area-chart decision (line for trajectory comparison, area for cumulative magnitude) and the differential application of the zero-baseline rule (lines do not require zero; areas do).

See [Line Graph](43-line-graph.md) in Part II for the canonical reference.

```
Generate a multi-series line chart in D3 v7 with a line/area toggle. Two files:

1. `chapter-06-fig-01.html` — full HTML with inline CSS and inline D3 v7. Three time-series lines on one chart, with a toggle to switch between line rendering (no zero-baseline requirement) and area rendering (zero baseline required). Page subtitle: "Trajectory vs. magnitude — when zero baseline matters."

2. `chapter-06-fig-01/data.json` — the dataset.

Data shape:
- Three series of monthly or annual values from 2016 to 2024.
  - `series`: object with three keys (`high_income`, `middle_income`, `low_income`), each a time-indexed array of `{date, value}`.

{DATA NEEDED} — An index measuring AI capability across country income groups. UNESCO, ITU, or Stanford AI Index by country group; the World Bank's digital adoption index also works. Annual values 2016–2024.

Encoding:
- x-position: date (linear time scale).
- y-position: capability index value.
- One line per income group; distinct hues (walnut, dark gray, blood-red).
- Toggle: line mode vs. area mode. In line mode, y-axis fits to data range; in area mode, y-axis starts at zero.
- Direct labels at line endpoints rather than a legend.

Caption explains: "Line mode emphasizes trajectory and gap; area mode emphasizes cumulative magnitude. The zero baseline is required for areas because the area itself encodes magnitude; for lines, what matters is the slope, and a tight y-axis range often reads better."

Style: warm monochrome.

Provide both files as separate code blocks.
```

---

## Further reading

- **Barry, Mike, and Brian Card. (2014).** "Visualizing MBTA Data." The Marey diagram and the iteration philosophy.
- **Wickham, Hadley. (2010).** "A Layered Grammar of Graphics." Wickham's framework on the channels for time-series visualization.
- **Tufte, Edward R. (1983).** *The Visual Display of Quantitative Information.* The Minard chart and Tufte's reading of it; relevant here as the canonical multi-channel temporal chart.
- **The book's pantry** — `line-graph.html`, `area-graph.html`, `stacked-area.html`, `stream-graph.html`, `spiral-plot.html`, `gantt-chart.html` for the working examples.

---

## Tags

time-series, temporal-charts, line-chart, area-chart, stacked-area, stream-graph, spiral-plot, Gantt-chart, timeline, Marey-diagram, zero-baseline, area-as-channel, Gestalt-continuity, MBTA-project, layer-ordering, smoothing, D3, Claude-Code
