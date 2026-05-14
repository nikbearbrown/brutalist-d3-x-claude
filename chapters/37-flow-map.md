# Flow Map

*Syria, Venezuela and Afghanistan Generate the Largest Displacement Corridors — Three Countries Account for Over Half of All Tracked Flows*

![Flow Map](../images/37-flow-map.jpg)

## What this chart is

A flow map draws directed lines between geographic points where the thickness of each line encodes the volume of the movement. The viewer reads two things simultaneously: the geographic path of a flow (where it goes) and its magnitude (how much moves). The key perceptual contract of a flow map — absent in connection maps — is that width is data. A thick ribbon means more; a thin ribbon means less. The ribbon is a proportional symbol stretched along a path. Flow maps sit in the FT Visual Vocabulary's Spatial / Movement category. They are the geographic equivalent of a Sankey diagram — except the node positions are geographic facts, not layout choices.

## Why it was chosen here

The data has three simultaneous qualities that the flow map handles and no other chart type does: directionality (from crisis origin to host country), volume (magnitude of movement, which varies by orders of magnitude across corridors), and geography (the physical distance and direction of each corridor are meaningful — Syria to Turkey is a different story from Syria to Germany). Removing any of these qualities changes what you can read from the chart.

The connection map handles a similar dataset but with a different message: it shows the structure of a logistics network where the volume difference between corridors is secondary. Here, the message is about which corridors dominate — Syria to Turkey's ribbon is more than four times wider than Syria to Germany's. That magnitude difference is the story, and a tapered ribbon makes it legible at a glance.

## What the alternatives lose

A connection map would replace the tapered ribbon with a uniform-width stroke, encoding volume only through stroke-width — a weaker perceptual channel than area. The viewer has to mentally compare line widths rather than areas, which is harder and less accurate. More critically, a connection map implies bidirectional relationships; a flow map implies directional movement. A Sankey diagram would encode volume accurately through ribbon width at every point in the flow — but it would discard geography entirely. The fact that Uganda and Kenya both border South Sudan and receive its largest flows is visible in the flow map; in a Sankey it is invisible. A bubble map would show total outgoing displacement per origin as a circle but would erase every destination, every corridor, and every directionality.

// design decision — tapered filled ribbons, not stroked lines The flows are drawn as filled SVG paths — closed quadratic Bézier polygons that taper from a wide base at the origin to an integrated arrowhead at the destination. stroke-width on an SVG path is constant along the entire length; a filled polygon can genuinely taper, encoding directionality in the shape itself (wide = origin, narrow = destination). Perceived area of a filled shape is a more accurate magnitude channel than perceived width of a stroked line — the same Flannery principle that governs bubble maps. Width is scaled via d3.scaleSqrt() so that perceived area is proportional to the flow volume rather than the radius.

## Framework reference

> // framework — FT Visual Vocabulary The FT Visual Vocabulary distinguishes flow maps from connection maps on directionality and volume encoding: use a connection map when the story is about network structure and link presence; use a flow map when the magnitude of each directed flow is the primary variable. The operative test: does the width of each line carry a data value? If yes, it is a flow map.

## Prompt

Paste this into Claude Code to generate a working version of this chart, plus its data file. The result will not be a perfect replica — the goal is that the reader can run the prompt, get a chart of this type, and read its source.

```
Generate a complete, self-contained flow map in D3 v7. Two files:

1. `flow-map.html` — a full HTML page with inline CSS and inline D3 v7 (loaded from `https://cdnjs.cloudflare.com/ajax/libs/d3/7.8.5/d3.min.js`). The chart should fill the viewport, be responsive on resize, support keyboard focus on interactive elements, and include a tooltip on hover. The page title is "Flow Map" and the slide subtitle is "Syria, Venezuela and Afghanistan Generate the Largest Displacement Corridors — Three Countries Account for Over Half of All Tracked Flows".

2. `flow-map/data.json` — the data file the chart loads via `d3.json("./flow-map/data.json")`, with a fallback inline literal in the HTML if the fetch fails.

Data shape:
- Global forced displacement flows by origin country, 2024 (simulated). Each flow is a directed origin-to-host corridor with a volume in thousands of displaced persons. Replace with real migration, trade, logistics, or any directed-flow dataset.
  - `nodes[].id`: string, unique short identifier
  - `nodes[].name`: string, full country or place name
  - `nodes[].lon`: number, longitude WGS84 (decimal degrees)
  - `nodes[].lat`: number, latitude WGS84 (decimal degrees)
  - `nodes[].role`: string, 'origin' | 'destination'
  - `nodes[].color`: string, hex color for flow ribbons leaving this origin (origin nodes only)
  - `nodes[].region`: string, geographic region label
  - `flows[].source`: string, node id of displacement origin
  - `flows[].target`: string, node id of host/destination country
  - `flows[].volume_k`: number, displaced persons in thousands — encodes ribbon width (sqrt scale)
  - `flows[].category`: string, displacement category
  - `flows[].year`: number, reference year

Encoding: use the perceptually honest channel for this chart type (flow map). Do not invent decorative encodings. Annotate the chart with a one-line in-chart subtitle that names what the chart shows. Include an accessibility `<title>` and `<desc>` inside the SVG.

Style: warm monochrome — black, dark walnut, blood-red accents only. Serif font for body text, JetBrains Mono for labels and controls. No drop shadows, no rounded corners, no gradients. Clean editorial register suitable for a print-ready textbook page.

Provide both files as separate code blocks. Do not explain — just produce the files.
```

The original code and data — copy-paste-ready — live at [bearbrown.co](https://www.bearbrown.co/).

---

## AI Wayback Machine

The ideas in this chapter didn't appear from nowhere. **Harry Beck** designed the London Underground map in 1933 — abandoning geographic accuracy for topological clarity, with lines drawn at 45° and 90° angles and stations evenly spaced. The map is the ancestor of every modern transit and flow diagram.

![Harry Beck, circa 1933. AI-generated portrait based on a public domain photograph.](../images/harry-beck.jpg)
*Harry Beck, circa 1933. AI-generated portrait based on a public domain photograph (Wikimedia Commons).*

**Run this:**

```
Who was Harry Beck, and how does his London Underground map connect to the flow map we covered in this chapter? Keep it to three paragraphs. End with the single most surprising thing about his career or ideas.
```

→ Search **"Harry Beck"** on Wikipedia.

**Now make the prompt better.** Try one of these:

- Ask it to compare Beck's 1933 topological map with a geographically accurate London Underground map — what's gained, what's lost?
- Ask it about how Beck was paid for the map (or wasn't), and what that says about the design profession of the time.

What changes? What gets better? What gets worse?
