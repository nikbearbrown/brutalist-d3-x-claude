# Connection Map

*Europe and North America Anchor a Hub-and-Spoke Aid Network That Converges on East Africa and the Levant*

![Connection Map](../images/31-connection-map.jpg)

## What this chart is

A connection map encodes geographic relationships by drawing lines between points placed at their real coordinates. The lines are the data. Positions are geographic facts. What the viewer reads is not the magnitude of a place but the structure of its connections: how many it has, how far they reach, how concentrated they are. The perceptual channel is proximity and density of lines. A node with many thick arcs is obviously central; an isolated node with one thin arc is obviously peripheral. Unlike a choropleth or a bubble map, the connection map says nothing about a region's intrinsic attributes — it only speaks to what each place is connected to.

## Why it was chosen here

The data is a logistics network: specific origin-destination pairs with a flow volume. The message is structural — the network converges on a small number of field sites from a distributed set of hubs. That is a connection story, not a magnitude story. A bubble map would encode aid volume at each location but would erase the corridor structure entirely — you would see which cities receive the most tonnage, but not which hubs supply them or how the network is wired. The connection map shows the wiring.

Secondary encoding: arc stroke-width is proportional to annual tonnage via a `d3.scaleSqrt()` mapping — the same sqrt-area principle as proportional symbol maps, here applied to perceived line weight. Color differentiates hub-to-hub corridors from regional connections when the filter buttons are active. Shape redundantly encodes node type (filled circle = hub, outlined circle = field site) so the distinction is not color-dependent alone.

## What a flow map would break — and what it would add

A flow map is a specialised form of connection map that encodes directionality and often merges parallel routes into a single tapered ribbon. It would be correct here — aid flows from hubs to field sites, not the other way. The reason it was not chosen: the routes share many intermediate paths and a proper flow map would need to merge those paths, which requires Sankey-style path merging that adds significant rendering complexity for a marginal gain in this dataset. The connection map's arrowheads carry enough directionality for the message at hand.

The other honest alternative: a matrix/adjacency heatmap, which would make the hub-by-field-site combinations legible without any geography. Rejected because the geographic position of Nairobi relative to Amman relative to Dakar is informative — it reveals the spatial concentration in East Africa and the Levant, which would be invisible in a matrix.

// design decision — great circle arcs vs. projected straight lines The arcs follow great circle routes — the shortest path between two points on a sphere. This is implemented by passing each connection as a GeoJSON LineString to d3.geoPath().projection(naturalEarth) , which automatically interpolates the geodesic. On a Mercator or equirectangular projection, great circle arcs produce visible curves. On Natural Earth 1 (used here), the effect is subtler but remains geometrically honest. Straight lines in projected space would be shorter visually but incorrect physically. Geodesics were used because this is an aid-logistics dataset where the real route geometry is the subject.

## Framework reference

> // framework — FT Visual Vocabulary The FT Visual Vocabulary places connection maps in its Spatial category alongside choropleths and bubble maps. Its note on the type: connection maps are best when the connection itself is the story — not the attributes of the connected places. The operative test: could you make this point without geography? If showing which cities are connected without their actual positions would lose the story, geography is earning its keep and a connection map is the tool.

## Prompt

Paste this into Claude Code to generate a working version of this chart, plus its data file. The result will not be a perfect replica — the goal is that the reader can run the prompt, get a chart of this type, and read its source.

```
Generate a complete, self-contained connection map in D3 v7. Two files:

1. `connection-map.html` — a full HTML page with inline CSS and inline D3 v7 (loaded from `https://cdnjs.cloudflare.com/ajax/libs/d3/7.8.5/d3.min.js`). The chart should fill the viewport, be responsive on resize, support keyboard focus on interactive elements, and include a tooltip on hover. The page title is "Connection Map" and the slide subtitle is "Europe and North America Anchor a Hub-and-Spoke Aid Network That Converges on East Africa and the Levant".

2. `connection-map/data.json` — the data file the chart loads via `d3.json("./connection-map/data.json")`, with a fallback inline literal in the HTML if the fetch fails.

Data shape:
- Global humanitarian aid corridor network, FY 2024 (simulated). Nodes are coordination hubs and field operation sites. Links are active aid corridors with annual tonnage. Replace with real logistics, trade, transport, or relationship data.
  - `nodes[].id`: string, unique short identifier (e.g. 'GVA')
  - `nodes[].name`: string, display name — city and country
  - `nodes[].lon`: number, longitude in decimal degrees (WGS84)
  - `nodes[].lat`: number, latitude in decimal degrees (WGS84)
  - `nodes[].type`: string, 'hub' = coordination/donor centre | 'field' = recipient/operation site
  - `nodes[].org`: string, primary organisation operating at this node
  - `links[].source`: string, id of origin node
  - `links[].target`: string, id of destination node
  - `links[].volume_mt`: number, annual aid tonnage in metric tons — encodes line weight
  - `links[].program`: string, primary programme channel
  - `links[].active`: boolean, whether corridor is currently operational

Encoding: use the perceptually honest channel for this chart type (connection map). Do not invent decorative encodings. Annotate the chart with a one-line in-chart subtitle that names what the chart shows. Include an accessibility `<title>` and `<desc>` inside the SVG.

Style: warm monochrome — black, dark walnut, blood-red accents only. Serif font for body text, JetBrains Mono for labels and controls. No drop shadows, no rounded corners, no gradients. Clean editorial register suitable for a print-ready textbook page.

Provide both files as separate code blocks. Do not explain — just produce the files.
```

The original code and data — copy-paste-ready — live at [bearbrown.co](https://www.bearbrown.co/).
