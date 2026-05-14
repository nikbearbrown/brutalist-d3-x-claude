# Part II — Examples

Sixty-one chart types, alphabetically. Each chapter is short — a placeholder image, the rich pedagogical text from the working pantry page, a single Claude Code prompt that generates a similar chart and its data file together, and a link to [bearbrown.co](https://www.bearbrown.co/) where the original code and data live. Browse, take what you need, skip what you don't. The prompts are the value: paste one into Claude Code and you have a working chart of that type in seconds, with a data file you can replace with your own.

---

# Arc Diagram

*Co-occurrence reveals who shares the most scenes*

![Arc Diagram](../images/18-arc-diagram.jpg)

Also known as: Arc Graph · Linear Network Diagram · One-Dimensional Network

## What this chart type is

An **Arc Diagram** places all nodes on a single horizontal axis and draws the connections between them as curved arcs above that line. Arc **thickness** encodes the strength or frequency of each relationship. **Node size** encodes a second quantitative variable — here, the total number of scenes each character appears in.

The perceptual mechanisms at work are *stroke weight* and *spatial proximity* — two preattentive channels that let the eye detect dominant connections before conscious reasoning begins. The arc's height is determined by the horizontal distance between its two endpoints: nodes that are far apart on the axis produce tall arcs; adjacent nodes produce shallow, tight curves.

Arc diagrams are best suited for *co-occurrence* and *co-authorship* data — situations where relationship strength matters more than cluster membership, and where an honest one-dimensional layout is preferable to a force-directed 2D layout that implies spatial meaning the data does not have.

## How to read this chart

Characters are arranged along the horizontal axis. Each arc connects two characters who appear together in at least one scene. **Thicker, darker arcs** (blood-red) represent the most frequent co-occurrences. **Thin, muted arcs** (grey) represent rare shared appearances.

**Hover any node** to highlight only the arcs connected to that character — all other arcs dim out. This isolates the character's relational network. **Hover any arc** to see the exact shared-scene count in the tooltip. Use the *sort* button to reorder nodes by total connections (descending) or alphabetically — sorting by connections places the most-connected characters near the centre, reducing arc crossing and exposing the hub structure.

Node order is the single most consequential design decision in an arc diagram: alphabetical order maximises arc crossings; connection-sorted order minimises them. Try both with the toggle above.

## Why arc diagrams — not force-directed graphs

A 2D force-directed graph places nodes wherever spring physics settle — a result that varies by run and initial conditions, and implies that *proximity means relatedness* . For co-occurrence data, that implication is false: two characters may appear far apart in the layout simply because the physics converged that way, not because they are unrelated.

The arc diagram is honest: it admits the data is a *list* , not a *map* . The axis is stable, reproducible, and sortable. The trade-off is that **cluster visibility** is reduced — communities that would form visually distinct blobs in a 2D network layout appear as overlapping arc bundles in an arc diagram. When cluster detection is the primary goal, a force-directed or community-layout graph is the better choice.

## Strengths and limitations

**Strengths:** Preserves exact values (arc thickness encodes the raw count, not a binned category). Sortable axis gives the analyst direct control over the visual hierarchy. Scales cleanly to 10–25 nodes; beyond that, arc crossings become visually dense.

**Limitations:** Does not reveal community structure as clearly as 2D network layouts. Arc crossings increase as O(n²) with node count — charts with more than ~30 nodes become difficult to read without filtering. Does not support directed edges (arrows) as cleanly as a Sankey or DAG layout. Values at the extremes of the weight scale (very thick vs very thin) are distinguishable; values in the middle range can be hard to compare precisely.

## Framework reference

> // FT Visual Vocabulary · Abela · Tufte FT Visual Vocabulary: Relationship — Connection. Abela quadrant: Relationship (show connections between entities, not comparison or composition). Tufte principle: every pixel of arc thickness encodes a real value — the axis line itself is the only non-data ink in the chart.

## About this example — fictional novel character co-occurrence

This diagram maps the shared-scene relationships among **eight characters** from a fictional novel. Each node represents one character; node size encodes their total scene count across the full narrative. Each arc represents at least one shared scene; arc thickness encodes the number of scenes shared.

**Elara** is the clear hub — she appears in 42 scenes and shares the most scenes with **Fenn** (18 co-appearances), followed by **Voss** (12). The **Lena–Dax** connection is the thinnest arc in the chart (2 shared scenes), suggesting they appear together only briefly. **Fenn–Voss** (14 shared scenes) is the strongest secondary relationship, hinting at a subplot that runs parallel to Elara's main arc. The sort-by-connections order places Elara and Fenn adjacent at the left, compressing the heaviest arcs into a tight, readable cluster on the left side of the axis.

To substitute real data, replace the `nodes` and `links` arrays in `arc-diagram/data.json` . Each node needs an `id` , `label` , and `totalScenes` (or equivalent total-activity metric). Each link needs `source` , `target` (matching node ids), and `weight` (the co-occurrence count).

## Prompt

Paste this into Claude Code to generate a working version of this chart, plus its data file. The result will not be a perfect replica — the goal is that the reader can run the prompt, get a chart of this type, and read its source.

```
Generate a complete, self-contained arc diagram in D3 v7. Two files:

1. `arc-diagram.html` — a full HTML page with inline CSS and inline D3 v7 (loaded from `https://cdnjs.cloudflare.com/ajax/libs/d3/7.8.5/d3.min.js`). The chart should fill the viewport, be responsive on resize, support keyboard focus on interactive elements, and include a tooltip on hover. The page title is "Arc Diagram" and the slide subtitle is "Co-occurrence reveals who shares the most scenes".

2. `arc-diagram/data.json` — the data file the chart loads via `d3.json("./arc-diagram/data.json")`, with a fallback inline literal in the HTML if the fetch fails.

Data shape:
- Character co-occurrence network from a fictional novel. Each node is a character; each link records how many scenes two characters share.
  - `nodes[].id`: string — unique identifier, matches source/target in links
  - `nodes[].label`: string — display name shown on the axis
  - `nodes[].totalScenes`: number — total scenes this character appears in (drives node radius)
  - `links[].source`: string — id of first character in the pair
  - `links[].target`: string — id of second character in the pair
  - `links[].weight`: number — shared scene count (drives arc thickness and color)

Encoding: use the perceptually honest channel for this chart type (arc diagram). Do not invent decorative encodings. Annotate the chart with a one-line in-chart subtitle that names what the chart shows. Include an accessibility `<title>` and `<desc>` inside the SVG.

Style: warm monochrome — black, dark walnut, blood-red accents only. Serif font for body text, JetBrains Mono for labels and controls. No drop shadows, no rounded corners, no gradients. Clean editorial register suitable for a print-ready textbook page.

Provide both files as separate code blocks. Do not explain — just produce the files.
```

The original code and data — copy-paste-ready — live at [bearbrown.co](https://www.bearbrown.co/).

---

## AI Wayback Machine

The ideas in this chapter didn't appear from nowhere. **Leonhard Euler** solved the Königsberg-bridges puzzle in 1735 by abstracting a city into nodes and edges and asking which path crossed each bridge exactly once. That single diagram founded graph theory — the mathematics that arc diagrams, force-directed networks, and every modern network visualization are built on. The arcs in this chapter trace back to those bridges.

![Leonhard Euler, circa 1750. AI-generated portrait based on a public domain engraving.](../images/leonhard-euler.jpg)
*Leonhard Euler, circa 1750. AI-generated portrait based on a public domain engraving (Wikimedia Commons).*

**Run this:**

```
Who was Leonhard Euler, and how does his solution to the Königsberg-bridges problem connect to the arc-diagram form we covered in this chapter? Keep it to three paragraphs. End with the single most surprising thing about his career or ideas.
```

→ Search **"Leonhard Euler Königsberg bridges"** on Wikipedia. See what the model got right, got wrong, or left out.

**Now make the prompt better.** Try one of these:

- Ask it to walk through how Euler's bridge-crossing condition (every vertex has even degree, except possibly the start and end) shows up when modern arc diagrams are checked for visual legibility.
- Ask it to compare Euler's purely topological diagram with what a modern arc diagram adds on top — order along the axis, arc length, weighting.

What changes? What gets better? What gets worse?
