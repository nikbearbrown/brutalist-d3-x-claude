# Gantt Chart

*Development In Progress — Planning & Design Complete, Testing Pending*

![Gantt Chart](../images/38-gantt-chart.jpg)

Also known as: Bar Schedule · Project Timeline · Critical Path Diagram

## What this chart type is

A **Gantt chart** encodes a project schedule as a two-dimensional table: tasks on the y-axis (categorical), time on the x-axis (ordinal or continuous date scale). Each task is a horizontal bar whose *position* encodes start date, whose *length* encodes duration, and whose *fill* encodes phase membership. A partial fill within the bar encodes completion percentage — a fourth variable layered on the same visual element.

The perceptual mechanisms exploited are **position along a common scale** for date alignment, and **length** for duration comparison. Overlapping bars are immediately visible as parallel work; gaps in the schedule appear as empty horizontal space. A fifth layer — the dependency arrow — encodes sequencing relationships between tasks, which would be invisible in any other chart type.

The Gantt chart was developed by Henry Gantt during World War I for production scheduling. It became the standard project management tool because it makes both *overlap* and *sequence* perceptually immediate — two properties that no table or list can communicate without arithmetic.

## How to read this chart

Tasks are listed top-to-bottom on the left axis. The horizontal date scale runs left to right. Each bar spans from the task's start date to its end date — bar length equals duration. **Darker fill** (high opacity) shows the completed portion; **lighter fill** (low opacity) shows remaining work. The completion percentage appears inside wide bars or to the right of the label column.

Tasks with an **obsidian stroke outline** are on the critical path — any delay to these tasks delays the entire project end date. **Diamond markers** above the timeline are milestones — zero-duration events marking key sign-offs or deliverables. The **red dashed vertical line** marks today: any bar that ends before today's line but shows incomplete fill is a late task.

**Click any phase legend item** to highlight that phase and dim others. Click any task bar to toggle the same filter. Hover any bar or diamond for the exact values in the tooltip. Click Reset to clear the filter.

## Four encoding layers

The Gantt chart stacks four distinct encodings onto a single rectangular element — which is both its power and its complexity ceiling.

**Position (x)** encodes start and end date against a shared timeline. **Length** encodes duration. **Fill colour** encodes phase category (with redundant stroke-width for the critical path — a WCAG-compliant second channel so the distinction works in monochrome). **Partial fill** encodes completion percentage: the complete portion renders at full opacity; the remaining portion at 0.28 opacity.

Dependency arrows add a fifth encoding layer — sequencing relationships between tasks that would be completely invisible in a table. This implementation uses *elbow connectors* rather than diagonal lines, because diagonal lines cross multiple task rows and create visual noise the viewer reads as additional data.

## What the alternatives would break

A **timeline chart** (single axis of events) handles dates but loses task duration and parallel execution — the critical signal that two tasks are running simultaneously disappears into a point. You cannot see overlap in a timeline; you can only see sequence.

A **table** shows all data fields but destroys the spatial relationship between tasks: overlapping date ranges are invisible, and the critical path — which requires tracing the longest dependency chain — cannot be identified without computation. The Gantt chart makes both overlap and sequence perceptually immediate, without any arithmetic from the viewer.

## About this example — Humanitarian Data Platform Phase 1 schedule

This Gantt chart shows the **Humanitarian Data Platform Phase 1** project schedule — a fictional 14-task project spanning approximately 12 weeks. Five phases are colour-coded: **Planning** (walnut), **Design** (blood-red), **Development** (dim-gray), **Testing** (mist), and **Deployment** (obsidian). Planning and Design phases are complete (100% fill). Development is in progress at approximately 55–70% completion across its tasks. Testing and Deployment have not yet started (0% fill, bars shown in low-opacity outline only).

The **critical path** (obsidian-outlined bars) runs through the Data Model task in Design, the API and Database tasks in Development, and the Integration Testing task — tracing the longest dependency chain from project start to go-live. Any slip on these tasks pushes the Go-Live milestone. The **today line** (red dashed) falls mid-project, making it immediately visible that the API Development task is running slightly behind schedule relative to its planned duration.

Four milestones mark the key hand-off points: **Project Kickoff** (start), **Design Sign-off** (transition to development), **Beta Release** (transition to testing), and **Go-Live** (project completion). Dependency arrows connect each task to its successor(s), using elbow connectors that exit horizontally, step vertically across rows, and arrive horizontally — visually encoding the finish-to-start relationship without creating diagonal noise. To substitute real project data, replace the `tasks` , `phases` , `milestones` , and `dependencies` arrays in `gantt-chart/data.json` .

## Prompt

Paste this into Claude Code to generate a working version of this chart, plus its data file. The result will not be a perfect replica — the goal is that the reader can run the prompt, get a chart of this type, and read its source.

```
Generate a complete, self-contained gantt chart in D3 v7. Two files:

1. `gantt-chart.html` — a full HTML page with inline CSS and inline D3 v7 (loaded from `https://cdnjs.cloudflare.com/ajax/libs/d3/7.8.5/d3.min.js`). The chart should fill the viewport, be responsive on resize, support keyboard focus on interactive elements, and include a tooltip on hover. The page title is "Gantt Chart" and the slide subtitle is "Development In Progress — Planning & Design Complete, Testing Pending".

2. `gantt-chart/data.json` — the data file the chart loads via `d3.json("./gantt-chart/data.json")`, with a fallback inline literal in the HTML if the fetch fails.

Data shape:
- Project schedule for the Humanitarian Data Platform Phase 1. Fictional placeholder with realistic structure. Proves Gantt renders before real data is substituted.
  - `tasks[].id`: string — unique task identifier (t01, t02, ...)
  - `tasks[].label`: string — task name displayed on chart row
  - `tasks[].phase`: string — phase id, must match a phases[].id
  - `tasks[].start`: string — ISO date YYYY-MM-DD, bar left edge
  - `tasks[].end`: string — ISO date YYYY-MM-DD, bar right edge
  - `tasks[].completion`: number — 0–100, percentage of task complete
  - `tasks[].critical`: boolean — true = critical path (distinct stroke)
  - `milestones[].id`: string — unique milestone identifier
  - `milestones[].label`: string — short label (5–10 chars) displayed above diamond
  - `milestones[].date`: string — ISO date YYYY-MM-DD
  - `dependencies[].from`: string — task id of predecessor (arrow source)
  - `dependencies[].to`: string — task id of successor (arrow target)
  - `phases[].id`: string — phase key referenced by tasks
  - `phases[].label`: string — phase name for legend
  - `phases[].fill`: string — hex color, mapped from hai palette

Encoding: use the perceptually honest channel for this chart type (gantt chart). Do not invent decorative encodings. Annotate the chart with a one-line in-chart subtitle that names what the chart shows. Include an accessibility `<title>` and `<desc>` inside the SVG.

Style: warm monochrome — black, dark walnut, blood-red accents only. Serif font for body text, JetBrains Mono for labels and controls. No drop shadows, no rounded corners, no gradients. Clean editorial register suitable for a print-ready textbook page.

Provide both files as separate code blocks. Do not explain — just produce the files.
```

The original code and data — copy-paste-ready — live at [bearbrown.co](https://www.bearbrown.co/).
