# Brutalist d3 x Claude

**Author:** Nik Bear Brown
**Publisher:** Bear Brown, LLC
**Status:** Draft
**Started:** 2026-05-07
**Series:** Brutalist — [brutalist.art](https://www.brutalist.art/)
**Sister volumes:** *Brutalist After Effects x Claude*, *Brutalist Blender x Claude*, *Brutalist Remotion x Claude* (additional renderer modules in development)

The Brutalist framework is a renderer-agnostic system for AI-assisted production: phase model (Audit → Schema → Generate → Verify → Handoff), labor separation (AI executes, human supervises), five supervisory capacities (PA, PF, TO, IJ, EI), and two governing files (`CLAUDE.md`, `PROJECT.md`). This book applies the framework to D3 data visualization. Other books in the series apply it to other renderers.

## Structure

```
book.md                 ← book description and high-level outline (planning)
outline.md              ← starter table of contents (planning)
vision.md               ← Tic TOC Phase 1: vision and positioning
architecture.md         ← Tic TOC Phase 2: learning architecture
chapters-spec.md        ← Tic TOC Phase 3: chapter specifications
risks.md                ← Tic TOC Phase 4: scope, market, risks
pantry/                 ← scratch storage for fragments, snippets, leftovers
chapters/
    00-frontmatter.md   ← copyright, dedication, preface
    01-introduction.md  ← Chapter 0 / Introduction
    02-chapter-01.md    ← Chapter 1
    ...
    04-chapter-03.md    ← Chapter 3
    99-back-matter.md   ← acknowledgments, about the author, notes, references, index
```

## Planning Documents

| File | Purpose |
|------|---------|
| `book.md` | One-sentence pitch, the argument, the gap, the reader, high-level outline. |
| `outline.md` | Chapter-level table of contents — keep in sync with `chapters/`. |
| `vision.md` | Tic TOC Phase 1 — book concept, type, learner profile, thesis, field positioning. |
| `architecture.md` | Tic TOC Phase 2 — learning outcomes, sequencing, three-act arc, prerequisites. |
| `chapters-spec.md` | Tic TOC Phase 3 — per-chapter specs, cases, contested claims, coverage gaps. |
| `risks.md` | Tic TOC Phase 4 — comparable texts, features, out of scope, adoption risks. |
| `pantry/` | Scratch storage for fragments and snippets that don't yet belong in a chapter. |

These files are for planning only. They are not compiled into the EPUB.

The four Tic TOC files are templated with `[NEEDS HUMAN INPUT]` markers
and a `*Phase N output from Tic TOC*` header signature. Run Tic TOC's
`/scaffold silent` to fill them from `book.md`, `outline.md`, `pantry/`,
and `chapters/`. Or build them section-by-section through the interactive
phase commands (`/i1` → `/m4`).

## Chapters

| File | Title | Status |
|------|-------|--------|
| 00-frontmatter.md | Front Matter (copyright, dedication, preface) | ☐ |
| 01-introduction.md | Introduction | ☐ |
| 02-chapter-01.md | Chapter 1 | ☐ |
| 03-chapter-02.md | Chapter 2 | ☐ |
| 04-chapter-03.md | Chapter 3 | ☐ |
| 99-back-matter.md | Back Matter (acknowledgments, notes, references, index) | ☐ |

## Build

```bash
./build.sh
```

Output goes to `output/` (gitignored).

## Figures

```bash
./graphs.sh
```

Processes `<!-- → [TYPE: description] -->` comments in every chapter:
- Tabular figures → classed markdown tables (`.infographic-table`, `.comparison-table`, `.data-table`)
- Non-tabular figures → placeholder images in `images/`, ready to replace
- CSS log appended to `styles/kindle-book.css` on each run

Review `chapters/*-updated.md`, then promote:
```bash
for f in chapters/*-updated.md; do mv "$f" "${f/-updated/}"; done
```

## Styles

| File | Purpose |
|------|---------|
| `styles/kindle.css` | Shared base — typography, figure table classes. Do not edit per book. |
| `styles/kindle-book.css` | Book-specific overrides. Edit freely. `graphs.sh` appends its log here. |

## Publish

Upload `output/brutalist-d3-x-claude.epub` to [KDP](https://kdp.amazon.com).
