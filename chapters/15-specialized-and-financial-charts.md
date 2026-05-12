# Chapter 15 — Specialized and Financial Charts

*Conventions That Earn Their Strangeness.*

---

Open the pantry's `kagi-chart.html`. Or if you have a candlestick chart handy, open that instead. Each candlestick has four values encoded in it: the price at the start of the period (open), the highest price reached during the period (high), the lowest (low), and the price at the end (close). The rectangular body of the candle spans open to close. The thin wicks extend from the body to the high above and the low below. If the price went up during the period, the body is one color — conventionally green or white. If it went down, another — red or black.

Count what that convention encodes. Four quantitative values per period. All four encoded using **position** — the highest-accuracy channel from Cleveland and McGill. The body's position encodes open and close; the wick's position encodes high and low; the color encodes direction. In one glyph, a trader reads the trend (are candles mostly green or red?), the daily range (how tall are the wicks?), the daily volatility (how tall are the bodies relative to the wicks?), and the session's character (did the price close near the high or near the low?).

A line chart of closing prices shows the trend. That's one variable. The candlestick shows four variables in the same screen space, using a convention so efficient that it packs the week's trading psychology into a column of colored boxes you can scan in a few seconds.

This is what specialized chart conventions earn. They encode information that standard charts cannot — not because standard charts are limited by any fundamental perceptual principle, but because the convention bundles multiple data values into a single glyph whose reading the audience has already internalized. The convention is the compression algorithm, and reading it fluently is the audience's graphicacy.

This chapter is about that compact — where it works, and where it fails.

<!-- → [IMAGE: single candlestick period annotated with all four OHLC values — body top labeled "Close (or Open if down-period)," body bottom labeled "Open (or Close if down-period)," upper wick top labeled "High," lower wick bottom labeled "Low," body fill color labeled "Direction: green = close > open, red = close < open." A second panel shows a line chart of closing prices for the same time series. Caption: "The candlestick encodes four variables per period; the line chart encodes one. The efficiency is the convention's claim to exist."] -->

---

## What makes a convention earn its strangeness

The candlestick convention earns its strangeness because three conditions hold simultaneously. The audience has already learned it (financial graphicacy is widespread among traders and analysts). The encoding is perceptually honest (position is used throughout; color encodes direction, not magnitude). And the form encodes something genuinely harder to show in a standard chart — four time-series in a single glyph without any visual compression cheating.

Take those three conditions away and you get decorative noise. A gauge chart on a dashboard looks like an instrument panel from a cockpit. It uses a sweeping needle — encoding a single value as an angle — surrounded by a decorative dial face. The question the gauge answers is the same question a bullet graph answers: how does this value compare to a target? The bullet graph answers it with a horizontal bar and a target marker, both using position along a common scale. The gauge answers it with angular position, which ranks fourth in the Cleveland and McGill accuracy hierarchy, behind position, length, and color saturation. The gauge looks like a specialized instrument; the bullet graph looks like a bar. But the gauge is objectively less accurate for the same analytical task, and it uses more screen space.

Stephen Few made this argument in 2005. His bullet graph was not a new form so much as a discipline: stop using angle where position will do. The gauge chart's appearance of technical sophistication is decorative, not functional. Every dashboard gauge should be a bullet graph. The perceptual reasoning is exactly Chapter 07's reasoning about truncated bar charts applied to a different channel: the form encodes the data using a worse channel than is available, and the reader pays the accuracy cost.

The chapter's test for any specialized form: does it use an appropriate channel for its primary data? If a specialized form uses position (the best channel) and bundles information efficiently, it earns the learning cost. If it uses angle or area decoratively when position was available, it fails.

<!-- → [TABLE: earn-your-strangeness reference — rows: candlestick / Kagi / Point & Figure / bullet graph / radar chart / polar area. Columns: primary channel used, Cleveland & McGill rank of that channel, the specific analytical question only this form answers, the condition that makes it fail. Student uses this as a lookup card before choosing any specialized form.] -->

---

## Candlestick and OHLC charts

The candlestick is the standard form for financial price visualization because it uses position throughout. The body's height is the distance from open to close — a length measurement, channel rank two. The wick heights are position from the body edge to the extreme price — also length measurements. The color is a binary direction indicator, not a magnitude channel.

The OHLC chart is the older variant. Instead of a candle body, it uses a vertical bar spanning the full high-to-low range, with a small horizontal tick to the left marking the open and a tick to the right marking the close. The encoding is equivalent; the visual is slightly different. OHLC is more compact; candlestick is more readable for the open-close direction signal.

Both work only when the audience knows the convention. The candlestick encodes four quantitative values in a compact glyph, but if the reader does not know that the body spans open to close or that a green candle means the price rose, the chart is a collection of colored bars whose meaning is invisible. Financial graphicacy is the prerequisite.

Both fail when the OHLC structure is undefined. Daily candlesticks for an actively traded stock are natural — each day has a meaningful open and close. Weekly candlesticks aggregate five days into one glyph, which works. Second-by-second candlesticks for a low-volume stock produce candles where high and low are the same value (no trades occurred during most seconds), and the chart is meaningless.

For Claude Code work, specify which form and which time period explicitly in the prompt. The D3 ecosystem has several OHLC and candlestick implementations; the four-move prompt should name the library or the encoding explicitly rather than leaving the choice to default.

---

## Kagi and Point & Figure: removing time from the axis

Candlestick and OHLC charts have time on the x-axis. Each candle occupies one period of equal width, whether the period was eventful or quiet. Kagi and Point & Figure charts remove time from the axis entirely.

A Kagi chart has a price line that moves up when prices rise and down when they fall. The line does not advance along the x-axis based on elapsed time. It advances based on price movement. Crucially, the line only *reverses direction* when the price moves a configurable amount — typically four to seven percent — in the opposite direction. Small fluctuations are absorbed; the chart filters them out and shows only meaningful moves. When the trend reverses, the line also changes thickness: a rising market produces a thick line; a falling market produces a thin one. The thickness is a visual signal for the current trend direction.

A Point and Figure chart uses a different convention. Rising price columns are filled with Xs; falling columns with Os. A column switches when the price moves by a reversal amount in the opposite direction. The columns advance across the page as reversals occur, but no column corresponds to a specific time period. A period of price stability might produce no new columns at all.

Why would you want to remove time from the axis? The analytical questions these forms serve are not primarily temporal. A trader asking "is this stock in an uptrend or a downtrend?" is asking about price direction, not about what happened on Tuesday. A trader asking "what price levels has this stock repeatedly bounced off?" is asking about support and resistance — price zones that appear repeatedly in the data — not about when those zones appeared. Time is noise for these questions. The Kagi and Point & Figure forms filter it out.

The forms fail outside their context. In non-financial domains, price-reversal conventions don't translate. For a general audience, the chart conventions require explanation that costs more than the time-independence gains. For audiences who want to know *when* something happened as well as *that* it happened, the time-independence is a deficit, not a feature. The forms earn their strangeness specifically for the questions they were designed to answer: trend reversal detection, support and resistance identification, noise filtering for high-frequency price data.

---

## Bullet graphs and the gauge chart replacement

The bullet graph is a dashboard-design intervention. Stephen Few proposed it as a direct replacement for the gauge chart, which was (and still is) the dominant form for showing a single performance metric against a target in dashboard software.

The bullet graph has three components. The primary measure is a solid horizontal bar from zero to the current value. A target marker — a short vertical tick — sits at the target value. Qualitative performance bands — light gray regions of increasing darkness, labeled poor / acceptable / good or whatever the domain requires — run the full width of the chart behind both the bar and the marker.

In one chart: the actual value, the target, and the performance range.

The gauge chart has the same three components, encoded differently. The actual value is the needle's angle. The target is a marker on the dial face. The performance ranges are colored arcs along the dial's perimeter. But the primary channel for the actual value — the needle's angular position — ranks fourth in the Cleveland and McGill hierarchy. The bullet graph's primary channel — the bar's endpoint position along a common scale — ranks first. For the same analytical task, the bullet graph is measurably more accurate.

Few also showed that bullet graphs are far more pixel-efficient. A gauge chart occupies a roughly square area (the dial). A bullet graph occupies a narrow horizontal strip. A dashboard that shows six gauge charts uses the space a dashboard showing thirty bullet graphs would need. In high-information-density contexts — executive dashboards, operations centers, monitoring screens — this matters.

The design decisions in a bullet graph are deliberate. The background bands should use sequential luminance — light gray for the lowest band, progressively darker gray for higher bands — rather than a traffic-light red-yellow-green sequence. The luminance encoding avoids colorblindness issues and avoids the implication that "red" is always bad (which it isn't: a budget metric where spending is the bar might have a "good" zone at the low end). The target marker should contrast against both the bar and the background. The qualitative band labels should appear consistently on all bullets in a multi-metric stack.

The pantry's `bullet-graph.html` shows the standard Few-original form. Compare it to any gauge chart you can find and the argument becomes empirical rather than rhetorical.

<!-- → [IMAGE: side-by-side comparison of the same KPI rendered as a gauge chart and as a bullet graph — left: semicircular gauge dial with needle at 87%, decorative face, red-yellow-green arcs, legend below; right: horizontal bullet graph with dark bar to 87%, small vertical tick at target (85%), three sequential-luminance background bands, direct value label. Annotations: on the gauge, "Angular position: Cleveland & McGill rank 4." On the bullet: "Position along common scale: Cleveland & McGill rank 1." A size comparison at the bottom shows the gauge occupying ~6× the vertical space of the bullet. Caption: "Same data. The bullet graph is more accurate and uses less space. Few's argument is not stylistic."] -->

---

## Radar charts and the axis-order problem

A radar chart places multiple variables as axes radiating from a center. Each observation is a polygon connecting its values along these axes. For five variables per observation and four observations, you get four overlapping polygons on a five-spoked wheel.

The form seems to invite multi-dimensional comparison. In practice it introduces a specific channel failure that most of its users don't notice.

The polygon's shape depends on the order of the axes. Rearrange the axes and the same data produces a different-looking polygon. Not a slightly different polygon — a meaningfully different one. The "spiky" pattern that seems to characterize one observation's performance profile will move, flatten, or become a different kind of spike depending on which axes are adjacent. If the reader is drawing conclusions from the polygon's shape, they are drawing conclusions from the axis order, which is not an inherent property of the data.

This is a Bertin-class failure. The encoding channel — the polygon's shape — is partially determined by an arbitrary design decision rather than exclusively by the data values. No such problem exists in a bar chart: the bar for "revenue" always looks the same regardless of what other bars are adjacent to it.

There are mitigations. If the axes have a conceptual grouping — say, three axes representing customer experience metrics and three representing operational metrics — placing the grouped axes adjacent makes the polygon's shape partially meaningful. The conceptual grouping provides a non-arbitrary basis for the order, and the shape reflects that grouping. But the reader needs to know the grouping rationale; without it, the shape is uninterpretable.

For most multi-dimensional comparison tasks, parallel coordinates (a set of vertical axes placed side by side, with each observation as a line connecting its values across all axes) handle the same encoding more honestly. Parallel coordinates have the same axis-order problem — adjacent axes affect which patterns are visible — but the visual claim is more modest. The reader traces a line across axes rather than reading a polygon, and the line's behavior (rising or falling between adjacent axes) depends on the specific axis pair, not on all axes simultaneously.

Small multiples are the most conservative alternative: one bar chart per dimension, all using the same y-axis scale, arranged in a grid. The reader compares each dimension separately. Nothing is conflated; the axis-order problem cannot arise because the axes are never adjacent. The trade-off is that the holistic "shape" comparison that makes radar charts visually appealing is gone.

Radar charts earn their use when the audience has the graphicacy to decode them, the polygon shape reflects a meaningful conceptual grouping, and the goal is a gestalt comparison across a small number of observations (three or four overlapping polygons remain readable; eight become a tangled web). They fail when the axis order is arbitrary, when the polygon count is high, or when the audience lacks radar-chart literacy.

<!-- → [IMAGE: three-panel radar chart demonstration — all three panels use the same six-attribute dataset for the same three observations. Left: axes in original order (Speed, Strength, Endurance, Agility, Technique, Recovery). Center: axes reordered (Strength, Recovery, Speed, Technique, Endurance, Agility). Right: axes reordered again (Agility, Endurance, Recovery, Speed, Technique, Strength). The polygon shapes in all three panels look meaningfully different despite representing identical data. Caption: "Same data. Three axis orders. Three different-looking performance profiles. The shape is not the data — it is the axis order."] -->

---

## Polar area charts (a brief return)

The Nightingale rose chart reappears here because it is sometimes treated as a "specialized" form for cyclical data — monthly patterns arranged radially around a clock face. The polar area encoding was discussed in Chapter 11 in the context of rhetorical vs. analytical contexts; the same analysis applies here.

When the data is genuinely cyclic — twelve months of the year, twenty-four hours of the day, seven days of the week — the radial layout can reinforce the cyclic structure. A bar chart of monthly precipitation arranged linearly shows January adjacent to February, December at the far right; a polar area chart arranges December adjacent to January, making the December-January transition visible as a single spatial relationship. For genuinely cyclic data, this is the form's justification.

The outer-ring amplification distortion (area scales as the square of radial length) still applies. Every polar area chart used in an analytical context requires the disclosure annotation that Chapter 11 specified. For advocacy contexts, the distortion serves the rhetorical purpose. For analytical contexts, it misleads.

---

## When specialized charts become decorative noise

The connecting thread across all the failures in this chapter is the same: a specialized form used for its appearance rather than for the specific analytical question it was designed to answer.

Gauge charts look like professional instruments. They appear in enterprise dashboards because dashboard-software defaults include them, because they look sophisticated, and because the people commissioning the dashboards are not thinking about the Cleveland and McGill accuracy hierarchy. The appearance of specialized sophistication is itself a decorative feature — one that impedes accurate reading.

Kagi and Point and Figure charts appear in amateur investment analysis for the same reason. The forms look complex and technical; they confer an appearance of professional rigor. But without the specific analytical question they serve — trend reversal detection, support and resistance identification — they are noise dressed as signal.

Radar charts appear in product-comparison tables, sports-analytics dashboards, and performance reviews because they look holistic — all dimensions visible simultaneously in one shape. The shape reading is appealing precisely because it seems to reduce multi-dimensional complexity to a single gestalt. But the reduction is partly an artifact of the axis order, and the reader who draws conclusions from the shape is being partially misled.

The test is always: what specific analytical question does this form answer better than any standard alternative? For candlesticks: four OHLC values per period in a single efficient glyph, for a financially literate audience. For Kagi: trend reversals and support levels for an audience willing to ignore time. For bullet graphs: performance vs. target with qualitative bands, more accurately than a gauge. For radar charts: holistic multi-dimensional shape comparison, with the axis-order caveat, for audiences who will not draw fine-grained conclusions from the polygon's geometry.

When the answer to the test is "it looks more professional" or "it looks more sophisticated," the specialized form is decorative. The standard alternative is almost certainly better.

<!-- → [INFOGRAPHIC: the earn-your-strangeness decision tree — root: "Does this form answer a specific analytical question better than any standard chart?" Yes branch: "Is the audience familiar with the convention?" Yes → use the specialized form with documentation. No → provide the convention explanation. No branch: "Why are you using this form?" → "It looks professional" → replace with the standard form. Two example paths labeled: Candlestick (yes/yes → use it) and Gauge chart (no → replace with bullet graph). Caption: "The test is the discipline. Specialization earns its cost or it doesn't."] -->

---

## What you can now do

You can build candlestick and OHLC charts for financial data, encoding four values per period using position throughout, and you understand the graphicacy prerequisite that makes the convention legible.

You can build Kagi and Point and Figure charts for time-independent price analysis — trend reversals, support and resistance — and explain what question the time-independence serves and for whom.

You can build bullet graphs as Few-style dashboard alternatives to gauge charts, using position-along-a-common-scale for the primary value and sequential luminance for the qualitative bands, and you can explain why the bullet graph outperforms the gauge on both accuracy and pixel efficiency.

You can recognize the radar chart's axis-order failure, specify an axis order when the grouping structure provides a non-arbitrary rationale, and identify when parallel coordinates or small multiples are the more honest alternatives.

You can apply the test to any specialized form: what specific analytical question does this form answer better than a standard alternative? When the answer is clear, the form earns its strangeness. When the answer is "it looks more sophisticated," the form is noise.

---

## Exercises

### Warm-up

**Exercise 15.1 — Specialized form selection.** *(Tests: the earn-your-strangeness test)*
For each scenario below, apply the test ("what specific analytical question does this form answer better than any standard alternative?") and name the right form — or name the standard form if no specialized form earns its use:
- Daily stock price tracking with intraday volatility for a financially literate trading audience.
- A single performance metric vs. target on an executive dashboard.
- Multi-dimensional product comparison across 5 attributes for a general marketing audience.
- Long-term price trend analysis where small daily fluctuations are noise and the analyst cares only about meaningful reversals.
- Monthly precipitation over a year, for a climate-science audience who needs to emphasize seasonal cycles.

**Exercise 15.2 — Position vs. angle, quantified.** *(Tests: Few's bullet-vs-gauge argument)*
A dashboard gauge shows a revenue metric of $4.2M against a target of $4.0M. The gauge dial spans $0M to $6M, so the needle sits at 70% of the arc. A bullet graph for the same metric shows a bar reaching 70% of the axis from 0 to 6. Where they differ: the gauge needle sweeps through 180° of arc; the bullet bar extends along a linear axis. According to the Cleveland & McGill hierarchy, which channel does each form use for the primary metric? Which ranks higher? Write one paragraph making Few's argument from this specific example.

**Exercise 15.3 — Radar chart axis-order audit.** *(Tests: the axis-order problem)*
A radar chart compares three products across six attributes: Price, Quality, Speed, Support, Design, Durability. Describe what would happen to the polygon shapes if you reordered the axes to: Quality, Design, Price, Durability, Speed, Support. Would the pattern that "Product A is strong on operational attributes" remain visible, disappear, or change shape? Name the mitigation you would apply to make the axis order non-arbitrary.

### Application

**Exercise 15.4 — Build a bullet graph dashboard.** *(Tests: Few's specification applied)*
Take three performance metrics with actual values, targets, and qualitative bands — from your professional context or the worked example in this chapter. Build a stacked row of three bullet graphs with Claude Code. Audit: is the primary bar using position (not angle)? Are bands sequential luminance (not traffic-light hue)? Is the target marker visible against both bar and bands? Is the layout consistent across all three metrics?

**Exercise 15.5 — Build a candlestick chart.** *(Tests: OHLC encoding)*
Take financial OHLC data for at least 20 trading periods (stock, currency, or commodity — freely available from Yahoo Finance or similar). Build a candlestick chart with Claude Code. Audit: do wick positions correctly encode high and low? Does body color correctly encode direction (close > open = up color)? Are the bodies proportional to the open-close range?

**Exercise 15.6 — Gauge-to-bullet redesign.** *(Tests: position-vs-angle replacement)*
Find a gauge chart on a public dashboard — enterprise software demos, government data portals, and sports statistics sites all have them. Build the bullet graph replacement with Claude Code. Present both side by side. For the specific metric the gauge shows, write one paragraph documenting: what accuracy is lost by the gauge's use of angle, what accuracy is gained by the bullet's use of position, and whether the gauge has any advantage the bullet cannot replicate.

### Synthesis

**Exercise 15.7 — Radar vs. small multiples.** *(Tests: radar chart mitigation applied to real data)*
Take a multi-dimensional dataset comparing 3–4 observations across 5–6 attributes (athlete performance across speed/strength/endurance/agility/technique, or product ratings across multiple categories). Build a radar chart. Then build the same data as small multiples — one bar chart per attribute, shared y-axis, observations as grouped bars. For the question "which observation is strongest overall?", which form answers it more honestly and why? Cite the axis-order problem as the reason the radar chart's answer is partially unreliable.

**Exercise 15.8 — Kagi chart for a non-financial domain.** *(Tests: time-independence beyond finance)*
Identify a non-financial domain where time-independent visualization might serve a legitimate analytical question — climate data with regime shifts, sports streaks filtered to ignore noise, or project milestone sequences where elapsed time between milestones is irrelevant. Build a Kagi-style chart with Claude Code for that dataset. Evaluate: does the time-independence gain clarity or lose it? What question is answered better by removing time from the axis, and what question becomes unanswerable?

### Challenge

**Exercise 15.9 — Specialized chart audit portfolio.** *(Tests: the earn-your-strangeness test applied at scale)*
Find five examples of specialized charts used in published contexts — corporate dashboards, financial journalism, sports analytics, or academic research. For each, apply the test: does the form answer a specific analytical question better than any standard alternative? Classify each as: (a) earns its strangeness, (b) decorative — standard form would be better, or (c) borderline — defensible in this specific audience context. For each in category (b), build the standard-form replacement with Claude Code and document what accuracy is recovered.

**Exercise 15.10 — Replicate Few's bullet graph specification.** *(Tests: deep implementation of a designed form)*
Read Few's original 2005 "Bullet Graph Design Specification" (available online; also referenced in the pantry). Build a bullet graph that matches Few's original specification precisely: the bar fills the entire bullet width, the qualitative bands use luminance (not hue), the target marker is perpendicular to the bar and extends through the full bar height, the comparative measure (if present) is a block overlapping the primary bar. Compare your output to Few's published reference image. Document every discrepancy and the follow-up prompt that corrected it. This is the exercise that turns the specification into fluency.

---

## LLM Exercise — Chapter 15: Specialized and Financial Charts

**What you're building:** A specialized chart selected for a specific analytical question, with the domain-convention justification documented and the encoding decisions verified against the Cleveland and McGill hierarchy.

**Tool:** Claude Code (for the build) + Claude chat (for the audit).

### The prompt

```
I have data for a specialized-chart context: [DESCRIBE: financial OHLC,
dashboard performance metrics, multi-dimensional comparison, or cyclic
temporal pattern]. The audience is [DESCRIBE: financial literacy level,
dashboard context, graphicacy level].

Walk me through:

1. Confirm a specialized form earns its use vs. a standard alternative.
   Apply the test: what specific analytical question does this form
   answer better than a bar chart, line chart, or other standard form?
   If no clear answer exists, recommend the standard form instead.

2. Choose the specific form (candlestick / OHLC / Kagi / Point &
   Figure / bullet graph / radar chart / polar area) based on the
   analytical question and audience graphicacy.

3. For bullet graphs: specify the actual value, target value, and band
   thresholds. Confirm the primary channel is position (not angle).
   Specify band colors as sequential luminance (not traffic-light hue).

4. For radar charts: specify the axis order with rationale. Identify
   whether the axes have a conceptual grouping that makes the order
   non-arbitrary. If not, recommend parallel coordinates or small
   multiples instead.

5. For polar area charts: apply Cairo's rhetorical-vs-analytical frame.
   Is this advocacy or analysis? If analysis, include the disclosure
   annotation ("area scales as radial length squared").

6. Specify all channels using the Chapter 01 framework, citing the
   Cleveland & McGill ranking for the primary channel.

7. Write a single Claude Code prompt using the four-move structure
   (show, say, constrain, verify), specifying the appropriate D3
   implementation.

After Claude Code returns the chart, audit it for specialized-form
failures:
- Candlestick: do the wick positions correctly encode high and low?
  Does body color correctly encode direction (close > open = up color)?
- Bullet graph: is the primary bar using position (not angle)? Are
  bands sequential luminance (not traffic-light hue)? Is the target
  marker visible against both bar and bands?
- Radar chart: is the axis order documented? Would reordering the axes
  substantially change the polygon shape? If yes, consider redesign.

Flag any audit failure and write the follow-up prompt that corrects it.
```

**What this produces:** A markdown audit document and an HTML file containing the working D3 chart. Save as `chapter-15-specialized-audit.md` and `chapter-15-specialized.html`.

**How to adapt this prompt:**
- *For your own domain:* Replace the dataset description and analytical question.
- *For ChatGPT or Gemini:* Works as-is.
- *For a Claude Project:* Save the Chapter 01 channel framework, Few's bullet graph specification, and Cairo's rhetorical-vs-analytical frame as reference files; the per-chapter audit prompt becomes the user message for each new chart.
- *For Cowork:* Use Cowork to execute the Claude Code prompt and save the resulting HTML file directly to your project directory.

**Connection to previous chapters:** Builds on Chapter 01 (Cleveland & McGill hierarchy — the position-vs-angle distinction that grounds the bullet-graph argument), Chapter 07 (zero-baseline and channel honesty — the same proportional-ink thinking applied to specialized forms), Chapter 11 (Nightingale rose and the rhetorical-vs-analytical frame — applied here to polar area charts), Chapter 09 (distribution charts — radar charts are sometimes misused for distribution comparison where a parallel-coordinates or small-multiples form is more honest).

**Preview of next chapter:** Chapter 16 begins Part III: the design audit framework. The chart taxonomy is now fully mapped across Chapters 07–15. Chapter 16 applies the Evergreen/Emery checklist systematically across all Part II forms — this is where the selection decisions and channel decompositions from every chapter converge into a single audit discipline.

---

## Further reading

- **Few, Stephen. (2006).** *Information Dashboard Design.* The bullet graph specification, the argument against gauge charts, and the broader case for position-based dashboard encoding.
- **Few, Stephen. (2005).** "Bullet Graph Design Specification." *Perceptual Edge.* The original technical specification; available online. Read this alongside `bullet-graph.html` in the pantry.
- **Murphy, John J. (1999).** *Technical Analysis of the Financial Markets.* Candlestick, OHLC, Kagi, and Point & Figure charts in their native analytical context. Reading this makes the time-independence question concrete.
- **Cairo, Alberto. (2016).** *The Truthful Art.* Chapter 9 on form selection for specialized domains; the polar-area and Nightingale discussion connects directly to Chapter 15's treatment.
- **The book's pantry** — `kagi-chart.html`, `bullet-graph.html`, `radar-chart.html`. Each is the reference implementation for its form; compare the bullet graph's position encoding against any gauge chart to make Few's argument empirical.

---

*Tags: specialized-charts, candlestick, OHLC, Kagi, Point-and-Figure, bullet-graph, Few, radar-chart, spider-chart, polar-area, Nightingale, axis-order-problem, Cleveland-McGill, position-vs-angle, dashboard, D3, Claude-Code*
