# Multimodal Distribution

*Multimodal Distribution*

![Multimodal Distribution](../images/45-multimodal-distribution.jpg)

## The concept

A **multimodal distribution** is a probability distribution with more than one local maximum (mode) in its probability density function. The most common case — **bimodal** — has exactly two peaks. The peaks appear because the data is a mixture of two or more distinct sub-populations, each with its own central tendency. The valley between peaks is called the **antimode** ; the larger peak is the **major mode** ; the smaller is the **minor mode** .

Common real-world examples: traffic volume (AM peak + PM peak), geyser eruption intervals, the size of weaver ant workers (two distinct castes), sediment grain sizes in geology, and galaxy colour distributions in astronomy.

## Why summary statistics mislead

This is the critical insight the Wikipedia article emphasises, and the reason this visualisation is built the way it is. For a strongly bimodal distribution, the **mean and median both fall in the antimode** — the least-populated valley between the two peaks. A single reported mean of 0 for a distribution with peaks at −2.5 and +2.0 is not just imprecise; it actively misrepresents the data. The standard deviation compounds the problem by spanning both peaks, appearing large without revealing the two-peak structure. The standard statistical summary (mean ± SD) is categorically wrong for multimodal data.

## How to detect bimodality — the three statistics shown

**Ashman's D** measures the separation between two Gaussian components relative to their spread: `D = |μ₁ − μ₂| / √(½(σ₁² + σ₂²))` . A value of **D > 2** indicates clean separation between the modes — the two sub-populations are distinct enough to be treated separately. Values below 2 suggest overlap that may or may not produce visible bimodality depending on the mixing weights.

**Sarle's bimodality coefficient β** uses the skewness (γ) and kurtosis (κ) of the combined distribution: `β = (γ² + 1) / κ` . The key threshold is **β > 5/9 ≈ 0.555** . Values above this suggest bimodal or multimodal structure; below it suggests unimodal. The logic: a bimodal distribution has low kurtosis (flat top, light tails between peaks) and/or high skewness — both increase β.

**KDE (kernel density estimation)** is the visual detection method: the smoothed density curve directly shows the number and position of modes as local maxima. The bandwidth is critical — too narrow and noise creates false modes; too wide and real modes merge into apparent unimodality. This chart uses Silverman's rule of thumb: `h = 0.9 × min(σ, IQR/1.34) × n^(−1/5)` .

## The chart design

Three layers are drawn simultaneously: (1) a **histogram** of sampled data (walnut fill, low opacity) showing the empirical distribution; (2) a **KDE curve** (solid walnut line) showing the smoothed density estimate; (3) **individual component curves** (dashed, colour-coded) showing each Gaussian component's contribution to the mixture. Seeing all three simultaneously reveals how the KDE's peaks emerge from the component overlap — a pedagogically essential view that is lost when only the aggregate is shown.

Vertical lines mark the **overall mean** (obsidian, solid) and the **antimode** (muted, dashed) — the exact location that a naive summary statistic would report as the "centre" of a distribution that has no observations near it.

## What the alternative would break

A **box plot** of bimodal data shows a wide IQR centred on the antimode, with the median in the gap between peaks — it is structurally incapable of revealing multimodality. A **bar chart of means ± SD** is even worse: it conveys false precision about a central value that is meaningless. The KDE curve is the correct primary representation for any dataset where the shape of the distribution is the message.

## Framework reference

> // Framework — FT Visual Vocabulary FT Visual Vocabulary category: Distribution — "How values in a dataset are distributed across a range." Abela quadrant: Distribution . Tufte principle applied: the three-layer chart (histogram + KDE + components) adds ink only when each layer reveals structure the others cannot — the histogram shows empirical frequency, the KDE shows continuous shape, and the component curves show the generative mechanism. Each layer earns its place.

## Prompt

Paste this into Claude Code to generate a working version of this chart, plus its data file. The result will not be a perfect replica — the goal is that the reader can run the prompt, get a chart of this type, and read its source.

```
Generate a complete, self-contained multimodal distribution in D3 v7. Two files:

1. `multimodal-distribution.html` — a full HTML page with inline CSS and inline D3 v7 (loaded from `https://cdnjs.cloudflare.com/ajax/libs/d3/7.8.5/d3.min.js`). The chart should fill the viewport, be responsive on resize, support keyboard focus on interactive elements, and include a tooltip on hover. The page title is "Multimodal Distribution" and the slide subtitle is "Multimodal Distribution".

2. `multimodal-distribution/data.json` — the data file the chart loads via `d3.json("./multimodal-distribution/data.json")`, with a fallback inline literal in the HTML if the fetch fails.

Data shape:
- Gaussian mixture parameters for multimodal distribution visualisation. Each component defines one mode (peak). The chart generates synthetic samples from the mixture and renders a KDE curve, histogram, and summary statistics. To show a real dataset, replace 'components' with your actual sample values in the 'samples' array and set 'useRealSamples': true.
  - `components`: array — each entry defines one Gaussian component: { mean, sd, weight }. Weights should sum to 1.
  - `n`: number — number of synthetic samples to draw from the mixture
  - `bandwidth`: number — KDE bandwidth (Silverman rule used if omitted)
  - `useRealSamples`: boolean — if true, use 'samples' array directly instead of generating from components
  - `samples`: array of numbers (optional) — real data values; used when useRealSamples is true

Encoding: use the perceptually honest channel for this chart type (multimodal distribution). Do not invent decorative encodings. Annotate the chart with a one-line in-chart subtitle that names what the chart shows. Include an accessibility `<title>` and `<desc>` inside the SVG.

Style: warm monochrome — black, dark walnut, blood-red accents only. Serif font for body text, JetBrains Mono for labels and controls. No drop shadows, no rounded corners, no gradients. Clean editorial register suitable for a print-ready textbook page.

Provide both files as separate code blocks. Do not explain — just produce the files.
```

The original code and data — copy-paste-ready — live at [bearbrown.co](https://www.bearbrown.co/).
