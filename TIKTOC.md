# Brutalist d3 x Claude
## Compact Tik TOC Architecture

**Book type:** Course textbook / practitioner handbook  
**Status:** Retrospective architecture for an already substantial manuscript  

## Core Thesis

This book teaches analysts, researchers, designers, and students to make publication-quality interactive visualizations by separating the implementation burden of D3 from the human judgment of chart selection, perceptual honesty, and visual explanation. Claude can help write code, but the reader must know what visual argument the code is supposed to make.

## Primary Reader

A graduate student, analyst, journalist, researcher, or instructor who needs to communicate data visually and may have bounced off D3 because the API felt too difficult.

## Learning Arc

1. **Graphicacy before code:** marks, channels, perception, chart selection, and visual ethics.
2. **Claude-assisted implementation:** D3, SVG, HTML, interaction, and reproducible chart construction.
3. **Publication practice:** audit, refine, document, and defend a complete visualization project.

## Chapter Architecture

Chapters should preserve a concrete-to-abstract rhythm: start with a chart problem, name the perceptual/design principle, implement the figure, then audit the result. Every chapter should end with a reusable prompt/specification and a visual integrity checklist.

## Terminal Capability

The reader can take a dataset and communication goal, choose an appropriate chart, specify it clearly for Claude Code, produce a working D3/HTML artifact, and critique it for perceptual honesty and audience comprehension.

## Adoption Risks

- Too much D3 syntax can obscure the book's real value: visualization judgment.
- Too much theory can make the book feel less immediately useful.
- Claude-specific tooling may age; chart-selection principles will not.

## Production Notes

This book is already content-rich. The Tik TOC should be used to consolidate sequence, remove duplicated chart types, and make the final project arc visible to instructors.
