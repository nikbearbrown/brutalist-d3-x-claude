---

## Acknowledgments

This book exists because the Humanitarians AI team built and shared an extraordinary D3 example set — over 60 working visualizations covering the full chart taxonomy. The pantry of working examples that this book repeatedly references is their work; the book is what happens when those examples meet a teaching framework.

The Brutalist system architecture from which this book's renderer module is drawn evolved across many conversations and a number of false starts. The After Effects module came first; the D3 module benefits from everything the After Effects, Blender, Remotion, and SVG/GSAP modules taught about what stays the same across renderers and what does not. The "designer interrogation, AI execution, and the boundary between them" formulation predates this book and improves it. The current state of the series — this book, its sister books, and the working framework documentation — lives at [brutalist.art](https://www.brutalist.art/).

Specific theoretical debts: Jacques Bertin's *Sémiologie Graphique* and the late William Cleveland and Robert McGill's perceptual experiments are the foundations on which Chapter 1 rests. Tamara Munzner's *Visualization Analysis and Design* is the modern synthesis that makes the framework teachable. Edward Tufte's principles on data-ink ratio and proportional ink shape Chapter 5 and Chapter 14, refined through Stephen Few's clarity-over-minimization position. Alberto Cairo's *The Truthful Art* and *How Charts Lie* supply the ethical frame that runs throughout. Stephanie Evergreen and Ann Emery's data visualization checklist is the audit instrument Chapter 14 walks. Mike Barry and Brian Card's MBTA visualization project is the process model that Chapters 4 and 15 adopt. Curran Kelleher's marks-and-channels video is the accessible entry point Chapter 1 references repeatedly.

To anyone who watched a Claude Code prompt produce a chart that surprised them — and then stopped to think about why — this book is for you.

---

## About the Author

**Nik Bear Brown** teaches data science, AI, and visualization at Northeastern University. His work spans machine learning, generative AI, data visualization, and the design of AI-assisted production pipelines. He is the author of the *with LLMs* textbook series and the architect of the **Brutalist** system for AI-assisted creative production — the renderer-agnostic framework whose D3 module is this book and whose other modules include *Brutalist After Effects x Claude*, *Brutalist Blender x Claude*, and *Brutalist Remotion x Claude*. The framework lives at [brutalist.art](https://www.brutalist.art/).

He works in Boston and writes occasionally at his website. He is on most of the major social-media platforms under variations of his name.

---

## Chart Type Reference

A one-page decision guide. Print this; pin it to a wall; consult before any new chart.

### Comparison

- **Bar chart (vertical column).** 4–10 categories, short labels.
- **Bar chart (horizontal).** Long labels, 5–15 categories.
- **Multiset (grouped) bars.** 2–4 sub-categories per category.
- **Stacked bars.** Total + composition matters.
- **Small multiples.** Cross-sub-category comparison; many sub-categories.
- **Radial bars.** Cyclic data only; otherwise linear bars win.

### Change over time

- **Line chart.** Trajectory, multi-series legible up to ~5 lines.
- **Area chart.** Cumulative magnitude; zero baseline required.
- **Stacked area.** Total + composition over time.
- **Stream graph.** Centered baseline; rhetorical force over precision.
- **Spiral plot.** Cyclic structure as primary view.
- **Gantt chart.** Tasks with durations.
- **Marey diagram.** Time + space; transit-style.

### Distribution

- **Histogram.** Single variable, n > 50.
- **Box plot.** Cross-group comparison; quartile-precise.
- **Violin plot.** Multimodality reveal.
- **Density plot.** Smooth distribution comparison.
- **Stem-and-leaf.** Small datasets, preserve raw values.

### Relationship

- **Scatterplot.** Two quantitative; cloud shape.
- **Bubble chart.** Three quantitative; area-not-radius (`d3.scaleSqrt`).
- **Connected scatter.** Two variables over time; path matters.
- **Parallel coordinates.** 3+ quantitative; interactive.
- **Heatmap.** Two categorical + intensity; or 2D joint distribution.

### Part-to-whole

- **Pie chart.** ≤5 slices, significant differences.
- **Donut chart.** Same as pie + center summary.
- **Waffle chart.** ≤5 categories, percentage-precise.
- **Stacked bar (single).** 2-6 categories; total + proportion.
- **Marimekko.** 2D part-to-whole; business audiences.

### Hierarchy

- **Treemap.** Regular depth ≤3 levels.
- **Sunburst.** Depth-focused, ≤5 levels.
- **Circle packing.** Irregular depth.
- **Tree diagram.** Exact structure; ≤50 nodes.

### Flow

- **Sankey.** Quantitative flow with width-as-channel.
- **Alluvial.** Sankey across time.
- **Chord (ribbon).** Inter-entity flow with magnitude.
- **Chord (non-ribbon).** Connection existence only.
- **Arc diagram.** Linear node arrangement, connection focus.
- **Force-directed.** Network with cluster structure; ≤50 nodes.

### Spatial

- **Choropleth.** Rate data, comparable region areas, equal-area projection.
- **Dot density map.** Absolute counts, spatial pattern.
- **Bubble map.** Magnitude at locations, area-not-radius.
- **Connection/flow map.** Origin-destination data.

### Specialized

- **Candlestick / OHLC.** Financial OHLC data.
- **Kagi / Point & Figure.** Time-independent financial.
- **Bullet graph.** Dashboard performance metrics (replaces gauge).
- **Radar / spider.** 3-7 dimensions; axis-order matters.
- **Polar area.** Cyclic data; rhetorical contexts.

---

## Selected References

### Primary references (theory)

Bertin, Jacques. *Semiology of Graphics: Diagrams, Networks, Maps.* Translated by William J. Berg. ESRI Press, 2010 (originally 1967).

Cairo, Alberto. *The Truthful Art: Data, Charts, and Maps for Communication.* New Riders, 2016.

Cairo, Alberto. *How Charts Lie: Getting Smarter About Visual Information.* W. W. Norton, 2019.

Cleveland, William S., and Robert McGill. "Graphical Perception: Theory, Experimentation, and Application to the Development of Graphical Methods." *Journal of the American Statistical Association* 79, no. 387 (1984): 531–554.

Heer, Jeffrey, and Michael Bostock. "Crowdsourcing Graphical Perception: Using Mechanical Turk to Assess Visualization Design." In *Proceedings of CHI 2010*, 203–212. ACM, 2010.

Munzner, Tamara. *Visualization Analysis and Design.* CRC Press, 2014.

Stevens, S. S. "On the Psychophysical Law." *Psychological Review* 64, no. 3 (1957): 153–181.

Tufte, Edward R. *The Visual Display of Quantitative Information.* 2nd ed. Graphics Press, 2001 (originally 1983).

Tufte, Edward R. *Envisioning Information.* Graphics Press, 1990.

### Primary references (practice)

Barry, Mike, and Brian Card. "Visualizing MBTA Data." Master's thesis project documentation, MIT, 2014. Available at mbtaviz.github.io.

Evergreen, Stephanie. *Effective Data Visualization: The Right Chart for the Right Data.* SAGE Publications, 2019.

Few, Stephen. *Show Me the Numbers: Designing Tables and Graphs to Enlighten.* 2nd ed. Analytics Press, 2012.

Few, Stephen. *Information Dashboard Design: Displaying Data for At-a-Glance Monitoring.* 2nd ed. Analytics Press, 2013.

Few, Stephen. "The Chartjunk Debate: A Close Examination of Recent Findings." *Visual Business Intelligence Newsletter* (April–June 2011).

Friendly, Michael. "A Brief History of Data Visualization." In *Handbook of Data Visualization*, edited by Chun-houh Chen, Wolfgang Härdle, and Antony Unwin, 15–56. Springer, 2008.

Knaflic, Cole Nussbaumer. *Storytelling with Data: A Data Visualization Guide for Business Professionals.* Wiley, 2015.

Murray, Scott. *Interactive Data Visualization for the Web: An Introduction to Designing with D3.* 3rd ed. O'Reilly, 2023.

Wilke, Claus O. *Fundamentals of Data Visualization: A Primer on Making Informative and Compelling Figures.* O'Reilly, 2019.

### Empirical research cited

Bateman, Scott, Regan L. Mandryk, Carl Gutwin, Aaron Genest, David McDine, and Christopher Brooks. "Useful Junk? The Effects of Visual Embellishment on Comprehension and Memorability of Charts." In *Proceedings of CHI 2010*, 2573–2582. ACM, 2010.

Pandey, Anshul Vikram, Anjali Manivannan, Oded Nov, Margaret Satterthwaite, and Enrico Bertini. "How Deceptive Are Deceptive Visualizations?: An Empirical Analysis of Common Distortion Techniques." In *Proceedings of CHI 2015*, 1469–1478. ACM, 2015.

Weissgerber, Tracey L., Natasa M. Milic, Stacey J. Winham, and Vesna D. Garovic. "Beyond Bar and Line Graphs: Time for a New Data Presentation Paradigm." *PLOS Biology* 13, no. 4 (2015): e1002128.

### Algorithmic and implementation references

Bostock, Michael. "D3: Data-Driven Documents." Various versions. d3js.org.

Bruls, Mark, Kees Huizing, and Jarke J. van Wijk. "Squarified Treemaps." In *Data Visualization 2000*, 33–42. Springer, 2000.

Shneiderman, Ben. "Tree Visualization with Tree-maps: 2-d Space-Filling Approach." *ACM Transactions on Graphics* 11, no. 1 (1992): 92–99.

Shneiderman, Ben. "The Eyes Have It: A Task by Data Type Taxonomy for Information Visualizations." In *Proceedings of the IEEE Symposium on Visual Languages 1996*, 336–343. IEEE, 1996.

Tukey, John W. *Exploratory Data Analysis.* Addison-Wesley, 1977.

### Pantry references (working examples and reference docs)

The book's pantry directory contains working D3 examples and reference documents that the chapters draw on directly. Key items:

- `pantry/visualization/` — 30+ working D3 chart examples.
- `pantry/markchennls.txt` — Curran Kelleher's marks-and-channels video transcript.
- `pantry/Tuftish_principles_NBB.txt` — Author's working notes on Tufte's principles.
- `pantry/Semiology_of_Graphics_NBB.txt` — Author's notes on Bertin.
- `pantry/Visual-vocabulary.txt` — The Financial Times Visual Vocabulary.
- `pantry/the_chartjunk_debate.txt` — Stephen Few's chartjunk debate analysis.
- `pantry/Cairo Ethical Infographics.txt` — Cairo on the ethical frame.
- `pantry/Cairo Uncertainty and graphicacy.txt` — Cairo on uncertainty.
- `pantry/EvergreenDataVizChecklist.txt` — The 22-point checklist.
- `pantry/Visualizing-Percentages-20-Ways-InfoNewt.html` — 20 alternatives to pie charts.
- `pantry/Visualizing Origin to Destination Flows.html` — Flow visualization reference.
- `pantry/Handbook of Data Visualization 2008 Friendly.txt` — Friendly's history.
- `pantry/Shneiderman 1996 the eyes have it.docx` — Shneiderman's overview-zoom-details.

---

## Colophon

This book was written using a Claude Code-assisted workflow. The Brutalist system architecture, in which the book's preface positions itself as a renderer module, was the working framework throughout. Each chapter went through the four-move prompt structure (show, say, constrain, verify) and the Evergreen/Emery audit checklist. Iteration logs are preserved in the project's `_notes.md`.

The book is set in Inter for body text. Code samples use the system monospace stack. The compiled EPUB respects the reader's preferred color scheme (`prefers-color-scheme`), which is a small mercy.

The cover image is a stylized version of one of the Humanitarians AI charts — a reminder that the working examples this book references are the laboratory in which the book was built.
