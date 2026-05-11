# Timeline

*Three Simultaneous Revolutions — Legal, Digital, and Financial —Accelerating in Parallel as Operations Scale and Multiply*

![Timeline](../images/72-timeline.jpg)

## What this chart is

A scaled timeline places events on a proportional time axis — the spatial distance between two events encodes the actual time interval between them. This is the defining property that separates a timeline from a simple list: **the gap between events is data** . A 15-year gap between two legal milestones occupies 15× the horizontal space of a 1-year gap. The viewer reads clustering, isolation, and acceleration directly from spatial density, without calculation. This chart uses two event types: **point events** (circles) for moments in time, and **span events** (rectangles) for durations — encoding the temporal structure of each event in its own geometric form.

## Why multi-track

When events cluster by thematic category, a single-axis timeline becomes illegible: events at the same date overlap, and the viewer cannot parse which event belongs to which domain. Multi-track timelines separate events into horizontal swim lanes while maintaining a **shared time axis** — the most important property, because it lets the viewer look down a vertical line at any date and see what was happening simultaneously across all tracks. The vertical scan reveals co-occurrence: the 2016 column shows the World Humanitarian Summit, the Grand Bargain signing, and a funding reform peak all at the same moment — pattern that no separate track can convey.

## Point events vs. span events

The choice of circle vs. rectangle is not decorative — it encodes **temporal structure** . A point event (circle) conveys: this thing happened at a specific moment; its duration is irrelevant or negligible. A span event (rectangle) conveys: this thing persisted across time; its duration is part of the data. Using circles for multi-year crises would misrepresent them as instantaneous. Using rectangles for legislative votes would imply a duration that doesn't exist. Mixing both types on the same axis, as this chart does, gives each event **the temporal shape that matches its actual nature** . The gestalt reading of the whole chart then shows which domains operate in bursts versus sustained engagements.

## What the alternatives would break

A **table** lists events chronologically but loses the spatial interval: the reader cannot see that 1994–2004 was a decade-long gap in major financing architecture. A **calendar view** handles daily granularity but collapses across decades — a 30-year humanitarian history becomes 360 cells that show nothing. A **Gantt chart** (built earlier in this series) is appropriate for future tasks with dependency relationships; a timeline is appropriate for historical events where the relationships are temporal proximity and co-occurrence, not dependency chains. The Catalogue's note about combining other visualizations with timelines points to sparklines, bar charts, or population data on individual tracks — all valid extensions of this base structure.

## Prompt

Paste this into Claude Code to generate a working version of this chart, plus its data file. The result will not be a perfect replica — the goal is that the reader can run the prompt, get a chart of this type, and read its source.

```
Generate a complete, self-contained timeline in D3 v7. Two files:

1. `timeline.html` — a full HTML page with inline CSS and inline D3 v7 (loaded from `https://cdnjs.cloudflare.com/ajax/libs/d3/7.8.5/d3.min.js`). The chart should fill the viewport, be responsive on resize, support keyboard focus on interactive elements, and include a tooltip on hover. The page title is "Timeline" and the slide subtitle is "Three Simultaneous Revolutions — Legal, Digital, and Financial —Accelerating in Parallel as Operations Scale and Multiply".

2. `timeline/data.json` — the data file the chart loads via `d3.json("./timeline/data.json")`, with a fallback inline literal in the HTML if the fetch fails.

Data shape:
- Multi-track timeline of key events in humanitarian response history 1991–2024. Four thematic tracks with both point events (single date) and span events (start–end duration). Fictional structuring of plausible historical events — proves the timeline renders before real data is substituted.
  - `domain`: array [ISO date, ISO date] — x-axis start and end
  - `today`: string ISO date — draws a reference line at this date
  - `tracks[].id`: string — unique track identifier
  - `tracks[].label`: string — track name displayed in left header column
  - `tracks[].color`: string — hex color from/derived from hai palette
  - `tracks[].events[].id`: string — unique event identifier
  - `tracks[].events[].label`: string — short label displayed on chart (≤18 chars)
  - `tracks[].events[].description`: string — full detail shown in tooltip
  - `tracks[].events[].type`: string — 'point' (single moment) or 'span' (duration)
  - `tracks[].events[].date`: string ISO date — used for type='point' events
  - `tracks[].events[].start`: string ISO date — start of type='span' events
  - `tracks[].events[].end`: string ISO date — end of type='span' events

Encoding: use the perceptually honest channel for this chart type (timeline). Do not invent decorative encodings. Annotate the chart with a one-line in-chart subtitle that names what the chart shows. Include an accessibility `<title>` and `<desc>` inside the SVG.

Style: warm monochrome — black, dark walnut, blood-red accents only. Serif font for body text, JetBrains Mono for labels and controls. No drop shadows, no rounded corners, no gradients. Clean editorial register suitable for a print-ready textbook page.

Provide both files as separate code blocks. Do not explain — just produce the files.
```

The original code and data — copy-paste-ready — live at [bearbrown.co](https://www.bearbrown.co/).
