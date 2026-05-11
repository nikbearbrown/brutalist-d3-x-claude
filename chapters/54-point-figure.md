# Point Figure

*Demand breakouts dominate the first half — supply reasserts at resistance and holds*

![Point Figure](../images/54-point-figure.jpg)

## What this chart is

A Point & Figure Chart encodes price action as a sequence of columns, each containing either X symbols (rising price, demand dominant) or O symbols (falling price, supply dominant). The x-axis is *not a time scale* — it is a column index. Time only appears as month markers on the first symbol of any new month, and these are informational annotations, not axis positions. The y-axis is the price scale.

Two parameters control the chart's resolution. The **box size** sets the minimum price move required to add a new symbol — it filters out moves smaller than this threshold. The **reversal amount** (expressed as a multiple of box size) sets the minimum price move in the opposite direction required to start a new column. Together they act as a two-stage noise filter: box size filters micro-fluctuations, reversal amount filters minor retracements.

## Why time disappears from the x-axis

Most financial charts plot price against time, which means quiet consolidation periods (low volatility, few price changes) take up the same horizontal space as high-activity periods. This time-scaling distorts the visual weight of price action: a three-week consolidation looks as wide as a three-week rally.

The P&F chart eliminates this distortion by only advancing to a new column when a reversal occurs. Each column represents a *price movement event* , not a time period. Quiet markets produce no new columns; active markets produce many. This makes the chart compact for consolidation and expressive for trend — the visual width is proportional to market activity, not elapsed time.

## Box size and reversal as editorial decisions

Box size and reversal amount are the two parameters the analyst controls, and they determine what the chart considers "signal" versus "noise." A **smaller box size** (e.g. $1) makes the chart more sensitive: more symbols per column, more columns, more reversals detected. The chart becomes wider and reveals more structure — useful for short-term trading.

A **larger box size** (e.g. $5) filters out minor fluctuations, producing fewer, taller columns that represent only major price movements. This is better for detecting long-term trends and major support/resistance levels. The reversal multiplier (typically 3×) means a new column only starts when the price reverses by three full box sizes — filtering out brief counter-trend moves.

This implementation exposes both parameters as sliders. Dragging box size from $1 to $6 on the same data shows how the same price series can produce a busy, detailed chart or a clean, structural one — the "right" setting depends entirely on the trading horizon and tolerance for noise.

## What the rejected alternative breaks

A **Candlestick Chart** encodes the same OHLC data but plots every session on the time axis regardless of whether meaningful price movement occurred. During consolidation phases, candlesticks produce a series of small, near-identical bodies that convey no directional information but consume significant chart space. The P&F chart collapses all quiet periods to nothing and expands only at decisive supply-demand shifts.

A **Line Chart** on closing prices discards open, high, and low — and still suffers the time-scale distortion problem. It cannot identify support and resistance levels as cleanly as P&F because those levels emerge from the structural alignment of column tops and bottoms, which the time-independent column layout makes visually apparent.

## Prompt

Paste this into Claude Code to generate a working version of this chart, plus its data file. The result will not be a perfect replica — the goal is that the reader can run the prompt, get a chart of this type, and read its source.

```
Generate a complete, self-contained point figure in D3 v7. Two files:

1. `point-figure.html` — a full HTML page with inline CSS and inline D3 v7 (loaded from `https://cdnjs.cloudflare.com/ajax/libs/d3/7.8.5/d3.min.js`). The chart should fill the viewport, be responsive on resize, support keyboard focus on interactive elements, and include a tooltip on hover. The page title is "Point Figure" and the slide subtitle is "Demand breakouts dominate the first half — supply reasserts at resistance and holds".

2. `point-figure/data.json` — the data file the chart loads via `d3.json("./point-figure/data.json")`, with a fallback inline literal in the HTML if the fetch fails.

Data shape:
- 180 trading days of fictional equity OHLC price data. Three-phase structure: bullish trend (days 1-60), sharp reversal and consolidation (days 61-110), second rally (days 111-180). Designed to produce interesting P&F column sequences with detectable breakouts.
  - `date`: string — ISO 8601 date YYYY-MM-DD (used for month markers and tooltip display only — not plotted on x-axis)
  - `high`: number — session high price in USD (used in X column extension and O column reversal detection)
  - `low`: number — session low price in USD (used in O column extension and X column reversal detection)
  - `close`: number — session close price in USD (used to seed the initial column direction)

Encoding: use the perceptually honest channel for this chart type (point figure). Do not invent decorative encodings. Annotate the chart with a one-line in-chart subtitle that names what the chart shows. Include an accessibility `<title>` and `<desc>` inside the SVG.

Style: warm monochrome — black, dark walnut, blood-red accents only. Serif font for body text, JetBrains Mono for labels and controls. No drop shadows, no rounded corners, no gradients. Clean editorial register suitable for a print-ready textbook page.

Provide both files as separate code blocks. Do not explain — just produce the files.
```

The original code and data — copy-paste-ready — live at [bearbrown.co](https://www.bearbrown.co/).
