# Chapter 13 — Specialized and Financial Charts
*Conventions That Earn Their Strangeness.*

## Three suggested titles

- Specialized and Financial Charts: Candlestick, Kagi, Point & Figure, Bullet, Radar
- When Domain Conventions Encode Information Standard Charts Cannot
- Few's Bullet Graph: Position Beats Angle Wins Again

---

## Chapter overview

By the end of this chapter you will be able to build the family of specialized charts — candlestick / OHLC, Kagi, Point & Figure, bullet graph, radar/spider, polar area — and you will know when domain-specific conventions encode information that standard charts cannot. You will know why bullet graphs replace gauge charts (Few's argument: position beats angle, again), why Kagi and Point & Figure charts are time-independent (and what analytical question that serves), and how radar charts' axis-order dependence is a Bertin-class channel failure that limits when they earn their use.

---

## Learning objectives

1. **(Understand)** Explain why Kagi and Point & Figure charts are time-independent and identify the specific class of analytical question (trend reversal detection, support/resistance identification) for which this matters.
2. **(Apply)** Build a bullet graph as a dashboard component; explain why Few argued it replaces a gauge chart using the Cleveland & McGill accuracy hierarchy (position > angle).
3. **(Analyze)** Diagnose the outer-ring distortion in a radial bar chart — tracing the mechanism to the area-encoding problem in Bertin's framework — and explain why the same data in a standard bar chart is more perceptually honest.

---

## Opening case — the HAI candlestick chart

Open `pantry/visualization/kagi-chart.html` in a browser. (Substitute a candlestick implementation if more relevant to your context.) Each candlestick represents one period (a day, an hour, a minute, depending on the timeframe). The candlestick has four data values:

- **Open:** the price at the start of the period.
- **High:** the highest price reached during the period.
- **Low:** the lowest price.
- **Close:** the price at the end of the period.

The body of the candle (the rectangular region) spans Open to Close. If Close > Open, the body is one color (typically green or white); if Close < Open, another color (red or black). The wicks (thin lines extending above and below the body) span from the high (top wick) to the body, and from the body to the low (bottom wick).

In one glyph, four quantitative values are encoded — all using **position** (the highest-accuracy channel from Cleveland & McGill). The body's position encodes Open and Close; the wicks encode High and Low. The color encodes the direction (rising or falling).

This is what specialized chart conventions earn. A line chart of closing prices alone shows the trend. A candlestick chart shows the trend, the daily volatility (wick length), the daily direction (body color), and the daily range (body height + wick length) all simultaneously. For a trader making intraday decisions, the candlestick is more efficient than four separate line charts. The convention encodes information that standard charts cannot.

This chapter is about that — the family of specialized charts where domain-specific conventions earn their complexity. Each form solves a specific problem; using each form for the wrong problem produces worse charts than the standard alternatives.

---

## Theoretical grounding — Cleveland & McGill (position > angle), Bertin on radial encoding, Few on bullet graphs

**Cleveland & McGill: position is the highest-accuracy channel.** This recurs throughout the book; for specialized charts, it is the criterion that distinguishes useful forms from decorative ones. Bullet graphs use position-along-a-common-scale (the bullet's position on the bar) to encode the value. Gauge charts (which bullet graphs replace) use angle (rank 4). For the same analytical task, the bullet graph wins on accuracy. Few's argument: gauge charts are decorative; bullet graphs are functional. The choice is not stylistic — it is a measurable accuracy difference.

**Bertin on radial encoding.** Radial encodings (radial bars, polar areas, sunbursts in some implementations) face systematic challenges: the eye cannot judge length along a curve as accurately as length along a straight line, and the outer-ring distortion (longer arcs cover more area than inner-ring arcs of the same radial extent) introduces ratios the eye misreads. Radial encodings earn their use in specific cases (cyclic data, advocacy contexts where rhetorical force matters) but lose to linear alternatives in most analytical contexts.

**Few on bullet graphs.** Stephen Few proposed the bullet graph in 2005 as a replacement for gauge charts in dashboards. Few's argument: gauge charts use angle (a low-accuracy channel) to encode a quantitative value, often surrounded by decorative gauge faces and gradient backgrounds; bullet graphs use position (high-accuracy channel) on a simple horizontal bar with a target marker and qualitative bands (e.g., "below target," "at target," "above target"). For dashboard use — where data density matters and pixel efficiency is paramount — bullet graphs are unambiguously better. Few's writing on this is in the pantry's chartjunk-debate document and in his books.

---

## Concept 1 — Candlestick and OHLC charts

A candlestick chart visualizes financial price data with the OHLC (Open, High, Low, Close) convention. Each candlestick represents one time period; the convention encodes four values per period.

### When candlestick charts work

- Financial data with OHLC structure (any market with periodic snapshots — stocks, currencies, commodities).
- Audiences who can read the convention (traders, analysts, financial-news readers).
- The reader's question includes intraday volatility and direction, not just closing price.

### When they fail

- Audiences without financial graphicacy. The candlestick is a learned convention; readers without it see incomprehensible bars and wicks.
- Time periods where the OHLC structure is undefined or arbitrary. Daily candlesticks for a stock work; weekly candlesticks make the periods less natural; second-by-second candlesticks for a low-volume stock have most periods without trades.

### The OHLC variant

OHLC charts (also called bar charts in finance) use a vertical bar instead of the candle body. The bar spans High to Low. Open and Close are marked as small horizontal ticks (left side: Open; right side: Close). The OHLC chart conveys the same information as the candlestick but with a different visual encoding.

For Claude Code work: most contemporary financial charts use candlesticks; OHLC is the older convention. Specify which one you want.

---

## Concept 2 — Kagi and Point & Figure: time-independent charts

Two charts that *omit time as a primary axis*. Instead, the chart axis shows the price; the chart's structure represents price *movements* (reversals).

### Kagi charts

A Kagi chart has a price line that moves up while prices rise, moves down while prices fall, and *thickens or thins* when the trend reverses by a configurable amount (often 4–7%). The line's thickness encodes the trend direction; the path encodes the price movement.

What Kagi charts emphasize:

- **Trend reversals.** A thick line that thins (or vice versa) signals a trend change. The chart filters out small fluctuations and shows only meaningful moves.
- **Time-independence.** Periods with no price movement contribute nothing to the chart. Periods with rapid movement contribute proportionally more.

### Point & Figure charts

A Point & Figure (P&F) chart uses Xs to mark rising price columns and Os to mark falling columns. A column reverses (X switches to O or vice versa) only when the price moves a configurable amount in the opposite direction (the "reversal amount"). Like Kagi, the chart is time-independent.

What P&F charts emphasize:

- **Support and resistance levels.** Patterns of Xs and Os reveal price levels at which the market repeatedly turned. Traders use these as entry/exit signals.
- **Filtering noise.** Like Kagi, P&F removes small fluctuations and shows only meaningful price moves.

### When time-independent charts work

- Financial analysis where price reversals matter more than time-of-day.
- Audiences with strong financial graphicacy.
- Datasets with high-frequency noise (intraday traders) where time-based charts overwhelm.

### When they fail

- Non-financial domains. The conventions don't transfer.
- Audiences without financial training. The Kagi line thickness or P&F column transitions require explanation.

The pantry's `kagi-chart.html` shows the form. For Claude Code work, specify the reversal amount and the time period explicitly.

---

## Concept 3 — Bullet graphs: Few's dashboard form

A bullet graph is a horizontal bar with three components:

- **The primary measure** (the value being measured) shown as a bar from 0 to the value.
- **A target marker** (often a small vertical tick) showing the target value.
- **Qualitative bands** (background regions colored in light shades) showing performance ranges (poor / acceptable / good / excellent).

In one chart, three values are encoded: the actual measure, the target, and the qualitative range.

### When bullet graphs work

- Dashboard contexts where pixel efficiency matters.
- Performance metrics with clear targets and bands (revenue vs. budget; customer satisfaction; service-level agreements).
- Multiple metrics shown together as small multiples (a row of bullet graphs, one per metric).

### Why they replace gauge charts

Few's argument: gauge charts use angle (Cleveland & McGill rank 4) on a fixed gauge face; bullet graphs use position (rank 1) on a linear bar. For the same metric, the bullet graph reads more accurately and uses less screen space. The qualitative bands can be added to either form, but the position-vs-angle difference is non-negotiable.

### Design decisions

**Color of the primary bar.** Solid, high-contrast color. Fills the band that contains the value.

**Background bands.** Light luminance variations (light gray to dark gray); typically 3–5 bands. Can use color hue (red-yellow-green) but most modern bullet graphs use luminance to avoid colorblindness issues.

**Target marker.** A short vertical tick at the target value, perpendicular to the bar.

**Layout.** Horizontal is the default (matches reading direction). Vertical (bar pointing up) is also defensible but less conventional.

The pantry's `bullet-graph.html` shows the standard Few-original form.

> ### ↳ Dig Deeper — Bullet graph in your dashboards
>
> **Prompt:**
>
> > Take three dashboard metrics from my professional context (revenue vs. target, customer satisfaction score, service uptime). Build each as a bullet graph using Claude Code. Compare to the gauge chart alternative for the same data. Cite Few's argument (position > angle from Cleveland & McGill).
>
> **What to do with the output:** Save the bullet graphs as a dashboard prototype.

---

## Concept 4 — Radar charts: the axis-order problem

A radar chart (also called spider chart, polar chart) places multiple variables as axes radiating from a center. Each observation is a polygon connecting points along these axes.

### When radar charts work

- Comparing 3–7 quantitative variables across observations.
- The polygon shape carries meaning (a "balanced" polygon is symmetric; an "imbalanced" polygon is asymmetric).
- Audiences with graphicacy for the form.

### The axis-order failure

A radar chart's polygon shape depends on the *order* of the axes. If you reorder the axes, the same data produces a different-looking polygon. Patterns visible in one order disappear in another. The visualization mechanism is the eye reading the polygon's shape, but the shape is determined by axis order, not by the underlying multi-dimensional data structure.

This is a Bertin-class channel failure. Position is being used as a magnitude channel for each axis (good); but the *connection lines* between axes use the axis order as a structuring element, and the order is somewhat arbitrary. Different orders are not equivalent — but no order is uniquely "right."

### Mitigations

**Specify the order.** If certain axes are conceptually grouped, place them adjacent. The pattern then reflects the groupings.

**Use parallel coordinates instead.** Parallel coordinates (Chapter 8) use the same multi-axis encoding but linearly. The axis-order problem still exists but is less visually misleading.

**Use small multiples.** A row of bar charts, one per dimension, with shared y-axis. The reader compares each dimension separately.

For Claude Code work, specify the axis order in the prompt and document the rationale.

The pantry's `radar-chart.html` shows the form.

---

## Concept 5 — Polar area charts (Nightingale revisited)

The Nightingale rose chart (Chapter 9) is a polar area chart. The form returns here in the specialized-charts context because it is sometimes used with cyclical data (months of the year arranged radially).

The Cleveland & McGill ranking and Stevens' power law continue to apply: the radial-area encoding sublinear; the angular-perception is moderate; the chart works in advocacy contexts and fails in analytical ones unless explicit disclosure is provided.

For Claude Code work: if you are using a polar area chart, document the choice with the disclosure annotation discussed in Chapter 9.

---

## Mid-chapter checkpoint

Pick a specialized-chart context from your work. Identify whether the domain convention earns its complexity (financial OHLC for a financial audience; bullet graph for dashboards; radar for multi-dimensional comparison with audience graphicacy).

If the context is dashboard performance metrics, replace any gauge charts with bullet graphs. The redesign is unambiguously better; document the perceptual reasoning.

---

## Extended worked example — building a bullet graph dashboard

Take three dashboard metrics: monthly revenue ($M), customer satisfaction score (0-100), service uptime (%).

### Channel decomposition (per metric)

- Marks: rectangle (primary measure bar), tick (target), light rectangles (qualitative bands).
- x-position: value (quantitative).
- Bar color: solid; consistent across the three metrics.
- Band colors: light luminance variations (light to dark gray).
- Target tick: short vertical line at target position.

### The four-move prompt (single bullet graph)

```
**Show what I have:**
Three metrics with: actual value, target value, three band thresholds.
- Revenue: actual $4.2M, target $4.0M, bands: <$3M (poor), $3-4M
  (acceptable), >$4M (good).
- Customer satisfaction: actual 87, target 85, bands: <70 (poor),
  70-80 (acceptable), >80 (good).
- Service uptime: actual 99.7%, target 99.9%, bands: <99% (poor),
  99-99.9% (acceptable), >99.9% (excellent).

**Say what I want:**
Three bullet graphs in D3 v7. Single self-contained HTML file with
inline CSS and inline D3 (loaded via CDN). Vertical stack, one bullet
per metric. Responsive to window resize.

**Constrain it:**
- Marks: per metric: solid rectangle (primary bar), short vertical
  tick (target), 3 light rectangles (bands).
- x-position: value (quantitative; range per-metric).
- Primary bar: solid color (#0D0D0D or palette-appropriate).
- Bands: light luminance (light gray for bottom band, slightly darker
  for middle, darkest for top band) — sequential luminance encoding.
- Target tick: 8px vertical line, centered vertically on the bar,
  contrasting color (#8B0000).
- Per-metric label on the left.
- Per-metric value annotation on the right.
- Subtitle: "Performance Dashboard, FY2024 Q4".
- Margins: top 60, right 80, bottom 40, left 200 (left margin for
  metric labels).
- Dark mode support.

**Verify:**
Restate the channel decomposition. Confirm position-along-common-scale
encodes the value (Cleveland & McGill rank 1). Confirm bands use
luminance (not categorical hue) for sequential encoding. Confirm
target tick uses a contrasting color for visibility against both bar
and bands.
```

### Audit

Standard Evergreen/Emery plus:

- Position used as primary channel (not angle, as a gauge would use).
- Bands use sequential luminance.
- Target marker visible against both bar and band backgrounds.
- Three metrics presented as small multiples (consistent layout).

---

## Chapter summary

You can now do four things you could not do before this chapter.

You can build candlestick / OHLC charts for financial data, encoding four values per period in a single glyph using position as the magnitude channel.

You can build Kagi and Point & Figure charts for time-independent financial analysis where price reversals and support/resistance levels matter more than time-of-day.

You can build bullet graphs as Few-style dashboard alternatives to gauge charts, using position-along-a-common-scale (the highest-accuracy channel) instead of angle.

You can recognize the radar-chart axis-order problem and apply mitigations (specify order, use parallel coordinates instead, use small multiples for multi-dimensional comparison).

The thing to watch for, going forward, is the temptation to use a specialized chart because it is visually distinctive. The specialized forms earn their complexity in specific contexts; using them outside those contexts produces decorative noise.

---

## Key terms

- **Candlestick / OHLC chart.** Financial chart encoding four values (Open, High, Low, Close) per period using position.
- **Kagi chart.** Time-independent chart where line thickness encodes trend direction and reversals.
- **Point & Figure chart.** Time-independent chart using Xs and Os to mark price columns.
- **Bullet graph (Few).** Dashboard chart with primary measure (bar), target (tick), and qualitative bands (background luminance).
- **Radar chart / spider chart.** Multi-axis polar chart for comparing 3-7 dimensions across observations.
- **Axis-order problem.** Radar chart polygon shape depends on axis order; not unique.

---

## Discussion questions

1. Specialized charts earn their complexity through domain conventions. What makes a convention earn its place vs. become decorative?
2. Bullet graphs are demonstrably better than gauge charts. Why do dashboards still use gauges? What does this say about software defaults vs. design quality?
3. Time-independent charts (Kagi, P&F) are unfamiliar outside finance. What other domains might benefit from time-independent visualization?
4. Radar charts have axis-order problems. When is the form still defensible?
5. *Cross-chapter synthesis.* Chapter 13 closes Part II. The full taxonomy is now mapped. Chapter 14 will apply the design audit framework across all of Part II. Frame the relationship.

---

## Exercises

### Warm-up

**Exercise 13.1** — *Specialized form selection.* For each, choose the right form:
- Daily stock price tracking with intraday volatility.
- Performance metric vs. target on a dashboard.
- Multi-dimensional product comparison (5 dimensions).
- Long-term price trend analysis with reversal detection.
- Cyclical data (monthly cycles).

**Exercise 13.2** — *Bullet graph from gauge.* Find a gauge chart on a dashboard. Replace with a bullet graph using Claude Code.

**Exercise 13.3** — *Radar order audit.* Take a radar chart with 6 axes. Reorder the axes randomly. Compare the visual shapes. Note what the same data looks like in different orders.

### Application

**Exercise 13.4** — *Build a candlestick.* Take financial data with OHLC structure. Build with Claude Code.

**Exercise 13.5** — *Build a Kagi chart.* Specify the reversal amount. Build with Claude Code.

**Exercise 13.6** — *Audit a published specialized chart.* Find one in finance, sports, or science. Audit using Evergreen/Emery + specialized-specific.

### Synthesis

**Exercise 13.7** — *Bullet graph dashboard.* Build a 6-metric dashboard using bullet graphs as the primary form.

**Exercise 13.8** — *Radar vs. parallel coordinates.* Take multi-dimensional data. Build both a radar chart and a parallel coordinates chart. Compare what each reveals.

### Challenge

**Exercise 13.9** — *Time-independent in a non-financial domain.* Identify a non-financial domain where time-independent visualization could work (climate data with regime shifts? sports performance with streak detection?). Build a Kagi-style chart for it.

**Exercise 13.10** — *Replicate Few's bullet graph.* Build a bullet graph that exactly matches Few's original specification (gradient bands, primary measure, target, label conventions). Compare to Few's published image.

---

## LLM Exercise — Chapter 13: Specialized Charts

```
I have data for a specialized-chart context: [DESCRIBE: financial,
dashboard, multi-dimensional, etc.]. The audience is [DESCRIBE].

Walk me through:
1. Confirm a specialized form earns its use vs. a standard alternative.
2. Choose form: candlestick / OHLC / Kagi / P&F / bullet / radar /
   polar area.
3. For radar charts: specify axis order with rationale.
4. For bullet graphs: specify bands and target.
5. Specify channels.
6. Write four-move Claude Code prompt.

Audit using Evergreen/Emery + specialized-specific.
```

**Connection to previous chapters:** All of Part II — Chapter 13 is the closing taxonomy chapter. Chapter 1's Cleveland & McGill ranking grounds the bullet-vs-gauge argument; Chapter 9's Nightingale-rose discussion is reflected in polar area considerations.

**Preview of next chapter:** Chapter 14 begins Part III. The chart taxonomy is mapped; now we apply the design-audit framework across all Part II forms. The Tufte/Few/Cairo synthesis becomes the audit instrument.

---

## Visual suggestions

This chapter is about specialized and financial chart selection. Each chart family it discusses has a Part II reference; the focal figure here is the chapter's central worked example — Few's argument that bullet graphs replace gauge charts.

Part II references for specialized charts: [Bullet Graph](26-bullet-graph.md), [Candlestick Chart](27-candlestick-chart.md), [OHLC Chart](49-ohlc-chart.md), [Kagi Chart](30-kagi-chart.md), [Point and Figure](54-point-figure.md), [Radar Chart](57-radar-chart.md), [Span Chart](64-span-chart.md), [Illustration Diagram](41-illustration-diagram.md), [Venn Diagram](76-venn-diagram.md), [Word Cloud](78-word-cloud.md). Each Part II chapter has its own prompt.

### Figure 13.1 — Bullet graph vs. gauge chart for the same KPI

The chapter's central argument made visible. The same dashboard KPI rendered two ways: a gauge chart (the dashboard cliché — round dial with a needle) and a bullet graph (Few's replacement — a bar with target marker and qualitative bands). The reader sees what each chart lets them read.

See [Bullet Graph](26-bullet-graph.md) in Part II for the canonical reference.

```
Generate two side-by-side dashboard KPI panels in D3 v7. Two files:

1. `chapter-13-fig-01.html` — full HTML with inline CSS and inline D3 v7. Two SVG panels in a flex layout, each rendering the same KPI value. Page subtitle: "Bullet graph vs. gauge chart — Few's argument made visible."

2. `chapter-13-fig-01/data.json` — the dataset.

Data shape:
- Three KPIs, each with `actual`, `target`, and `bands` (poor / acceptable / good thresholds).
  - For example: response time (target = 24h, bands at 12 / 24 / 48 hours), program completion (target = 95%, bands at 70 / 90 / 95 / 100), donor satisfaction (target = 4.5, bands at 3.0 / 4.0 / 4.5 / 5.0).

{DATA NEEDED} — Three humanitarian-program KPIs with actual, target, and three qualitative bands per KPI. UNHCR or program-evaluation reports.

Left panel — gauge chart:
- A semicircular dial with a needle pointing at the current value.
- Bands (poor/acceptable/good) drawn as colored arcs.
- This is the dashboard cliché. Render it competently; do not improve the encoding beyond what is conventional.

Right panel — bullet graph:
- Horizontal bar showing the actual value.
- A small marker line showing the target.
- Background bands (poor/acceptable/good) drawn behind the bar in light gray gradations.
- Direct value label.

Caption beneath: "The bullet graph uses position-along-a-common-scale (Cleveland & McGill rank 1) for the actual value; the gauge uses angular position (rank 4). The bullet graph fits in less space and reads faster. Few's argument: replace gauges with bullets, in every dashboard, every time."

Style: warm monochrome.

Provide both files as separate code blocks.
```

---

## Further reading

- **Few, Stephen. (2006).** *Information Dashboard Design.* The bullet graph and dashboard design principles.
- **Murphy, John J. (1999).** *Technical Analysis of the Financial Markets.* Candlestick, OHLC, Kagi, P&F charts in financial context.
- **The book's pantry** — `kagi-chart.html`, `bullet-graph.html`, `radar-chart.html`.

---

## Tags

specialized-charts, candlestick, OHLC, Kagi, Point-and-Figure, bullet-graph, Few, radar-chart, spider-chart, polar-area, Nightingale, axis-order-problem, Cleveland-McGill, position-vs-angle, dashboard, D3, Claude-Code
