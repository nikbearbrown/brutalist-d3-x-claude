# Candlestick Chart

*Price action reveals market psychology across trading sessions*

![Candlestick Chart](../images/27-candlestick-chart.jpg)

## What this chart is

A Candlestick Chart encodes four price dimensions per time period — open, high, low, close (OHLC) — into a single glyph. The *real body* spans the open-to-close range and is the primary signal: its height encodes price conviction, its colour encodes direction. The *wicks* (upper and lower shadows) extend to the session's extremes, encoding the full range of price exploration.

This is a glyph chart — a composite mark that packs four quantitative values into one symbol. It exploits position-along-axis (the most accurate perceptual channel) for the body, and length-from-reference for the wicks. The colour encoding is redundant with the body position: walnut means close > open, red means close < open.

## Why it was chosen here

The message is about market psychology across sessions — not a single price level, not a trend line, not a distribution. The viewer needs to see conviction (body height), direction (colour), and range exploration (wick length) simultaneously. No single-dimension chart can deliver all four OHLC values. A line chart collapses to close price only, discarding 75% of the available information. A simple OHLC bar chart encodes the same data but is perceptually harder to parse at density.

The candlestick's cultural familiarity in financial contexts is also an asset: experienced traders read candle patterns instantly. The chart meets the audience where they are.

## What the rejected alternative breaks

A **line chart on closing price** — the most common alternative — discards open, high, and low entirely. The viewer loses all information about intra-session volatility, gap openings, and the relationship between opening conviction and closing outcome. A session that opened high, sold off dramatically, but recovered to close flat appears identical to a calm session that never moved.

A **Box Plot** — visually similar — encodes statistical distribution (quartiles, median) across *many observations* . A candlestick encodes four *specific price events* within one time period. Confusing them is a category error: the box plot answers "how is this value distributed?", the candlestick answers "what happened during this session?".

## Prompt

Paste this into Claude Code to generate a working version of this chart, plus its data file. The result will not be a perfect replica — the goal is that the reader can run the prompt, get a chart of this type, and read its source.

```
Generate a complete, self-contained candlestick chart in D3 v7. Two files:

1. `candlestick-chart.html` — a full HTML page with inline CSS and inline D3 v7 (loaded from `https://cdnjs.cloudflare.com/ajax/libs/d3/7.8.5/d3.min.js`). The chart should fill the viewport, be responsive on resize, support keyboard focus on interactive elements, and include a tooltip on hover. The page title is "Candlestick Chart" and the slide subtitle is "Price action reveals market psychology across trading sessions".

2. `candlestick-chart/data.json` — the data file the chart loads via `d3.json("./candlestick-chart/data.json")`, with a fallback inline literal in the HTML if the fetch fails.

Data shape:
- Daily OHLC (Open, High, Low, Close) price data for a fictional equity. 60 trading sessions covering approximately 3 calendar months.
  - `date`: string — ISO 8601 date YYYY-MM-DD (x-axis position)
  - `open`: number — session opening price in USD
  - `high`: number — intra-session highest price in USD (top of upper wick)
  - `low`: number — intra-session lowest price in USD (bottom of lower wick)
  - `close`: number — session closing price in USD (determines body colour: walnut=bullish, red=bearish)
  - `volume`: number — number of shares traded (reserved for future volume histogram)
  - `pattern`: string|null — candlestick pattern identifier for annotation: 'doji', 'hammer', 'engulf', 'marubozu', or null

Encoding: use the perceptually honest channel for this chart type (candlestick chart). Do not invent decorative encodings. Annotate the chart with a one-line in-chart subtitle that names what the chart shows. Include an accessibility `<title>` and `<desc>` inside the SVG.

Style: warm monochrome — black, dark walnut, blood-red accents only. Serif font for body text, JetBrains Mono for labels and controls. No drop shadows, no rounded corners, no gradients. Clean editorial register suitable for a print-ready textbook page.

Provide both files as separate code blocks. Do not explain — just produce the files.
```

The original code and data — copy-paste-ready — live at [bearbrown.co](https://www.bearbrown.co/).
