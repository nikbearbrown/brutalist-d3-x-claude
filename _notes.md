# Run Notes — Brutalist d3 x Claude

*Run log for the curriculum enrichment generator workflow on this book.*

---

## Run summary — 2026-05-08

**State at start.** Book existed with substantial planning scaffolding (book.md, outline.md, vision.md, architecture.md, chapters-spec.md, risks.md) but all four Tic TOC documents were initially templated with `[NEEDS HUMAN INPUT]` markers. User updated all four documents during the run with substantial theoretical positioning (Few > Tufte; Cairo's ethical frame; Bertin → Cleveland & McGill → Munzner spine; Friendly history; Gestalt principles; MBTA process model; Evergreen/Emery checklist). The pantry was substantially expanded mid-run with reference docs (Cairo, Tufte, Few, Bertin notes, FT Visual Vocabulary, chartjunk debate, Evergreen checklist, Friendly's Handbook, Shneiderman's Eyes Have It, Visualizing Percentages 20 Ways, Visualizing Origin to Destination Flows, etc.).

**State category.** Closest mapping: State B-equivalent with the chapter specifications playing the role that source subfolders did in prior books. Each of the 15 chapter specs in `chapters-spec.md` was detailed enough to draft directly from spec + pantry reference material.

**Decisions taken.**
- **Path A** (pilot first), then **march** after pilot calibration. User explicitly approved the pilot rewrite to match updated specs, then explicitly authorized the full march on remaining chapters plus front matter and Chapter 00.
- **Brutalist framing** for the front matter — the book is the D3 renderer module of the Brutalist system; preface explicitly positions it that way.
- **No specific running project locked in this run** (Step 3 of the curriculum enrichment generator). The user did not select a project; the book's pedagogy already structures Chapter 15 as the capstone project. A formal running-project menu (3-5 options) was not produced.

**Voice and method.** Course textbook register, scene-anchored opening for each chapter, 12-section anatomy from the updated chapters-spec.md, theoretical sources introduced at the moments specified, Few-resolved stance on chartjunk throughout, Cairo's ethical frame applied at each chapter where appropriate.

---

## Chapters written / rewritten

| File | Title | Status | Notes |
|------|-------|--------|-------|
| `00-frontmatter.md` | Front matter | Drafted | Brutalist-applied-to-D3 preface; copyright; dedication |
| `01-introduction.md` | Introduction | Drafted | FiveThirtyEight Nigeria case; book overview; Cairo's graphicacy concept |
| `01a-chapter-00.md` | Chapter 00 — Claude Basics | Drafted | Four-move prompt structure; three D3-specific failure modes; three-layer verification |
| `02-chapter-01.md` | Chapter 1 — Marks and Channels | Pilot, then **rewritten** | Two-scatterplots opening; Bertin/Cleveland/Munzner spine; Stevens' power law; HAI box plot worked example |
| `03-chapter-02.md` | Chapter 2 — Chart Selection | Drafted | 14-slice pie chart hook; Cairo's four-step framework; FT Visual Vocabulary; eight functional categories |
| `04-chapter-03.md` | Chapter 3 — Reading a Dataset | Drafted | "Visualize refugee flows" hook; data types; analyst vs. reader; "compared with what?" |
| `05-chapter-04.md` | Chapter 4 — Working with Claude Code | Drafted | Two prompts hook; MBTA iteration model; Evergreen/Emery audit subset; full pipeline walkthrough |
| `06-chapter-05.md` | Chapter 5 — Comparison Charts | Pilot, then **rewritten** | HAI AI adoption opening; bar/column dichotomy; zero-baseline rule with Few-resolved stance; Cairo moral framing |
| `07-chapter-06.md` | Chapter 6 — Temporal Charts | Drafted | HAI AI capability gap line chart; zero baseline for areas; Marey diagram; Gestalt continuity |
| `08-chapter-07.md` | Chapter 7 — Distribution Charts | Drafted | HAI box plot opening; Tukey 1.5×IQR; bin-width problem; KDE bandwidth; graphicacy |
| `09-chapter-08.md` | Chapter 8 — Relationship Charts | Drafted | HAI scatterplot opening; correlation-is-not-causation as Cairo-class moral; Stevens' power law on bubbles |
| `10-chapter-09.md` | Chapter 9 — Part-to-Whole Charts | Drafted | Five-slice pie; Cleveland & McGill on angle; Nightingale rose with rhetorical-vs-analytical distinction |
| `11-chapter-10.md` | Chapter 10 — Hierarchy Charts | Drafted | HAI circle packing opening; treemap squarification; depth limits; Shneiderman 1991 |
| `12-chapter-11.md` | Chapter 11 — Flow/Network | Drafted | HAI Sankey; width-as-channel; hairball problem; chord ribbon vs. non-ribbon |
| `13-chapter-12.md` | Chapter 12 — Spatial Charts | Drafted | HAI choropleth opening; area-size distortion; Dupin 1826; Snow 1854; ratio vs. absolute |
| `14-chapter-13.md` | Chapter 13 — Specialized Charts | Drafted | Candlestick OHLC; Kagi/P&F time-independent; bullet graph (Few); radar axis-order |
| `15-chapter-14.md` | Chapter 14 — Design Principles | Drafted | Tufte/Few/Cairo synthesis; Evergreen/Emery 22-point checklist applied in full |
| `16-chapter-15.md` | Chapter 15 — Complete Project | Drafted | MBTA process model end-to-end; UNHCR humanitarian dataset; Brutalist phases A-E |
| `99-back-matter.md` | Back matter | Drafted | Acknowledgments, author bio, Chart Type Reference one-pager, references, colophon |

**Total:** 19 documents, approximately 130,000 words.

---

## Pilot, rewrite, and march sequence

1. Initial pilot (Ch 1, Ch 5) drafted before the user updated the planning docs. The pilot used:
   - Course-textbook 11-section anatomy (close to but not exactly the spec's 12-section anatomy).
   - Fabricated workplace scenarios as opening hooks (Claude Code workflow conversation in Ch 1; truncated 12-13% chart in Ch 5).
   - More absolutist treatment of the zero-baseline rule than the user's `Tuftish_principles_NBB` notes warrant.

2. User updated `vision.md`, `architecture.md`, `chapters-spec.md` with a substantial "Theoretical Position (resolved)" section that named the Few > Tufte stance, the Cairo ethical frame, the Bertin → Cleveland & McGill → Munzner lineage, and specific theoretical sources per chapter.

3. User asked for a recheck. The recheck identified the calibration gap between the pilot and the updated specs. The user authorized a rewrite.

4. Pilot rewritten. Both Ch 1 and Ch 5 redrafted to match the updated specs:
   - Ch 1 opening shifted to two scatterplots (per the spec).
   - Ch 1 worked example shifted to the HAI box plot (per the spec).
   - Ch 1 added explicit Bertin → Cleveland & McGill → Munzner lineage with Stevens' power law as the perceptual mechanism.
   - Ch 5 opening shifted to the HAI AI adoption bar chart (per the spec).
   - Ch 5 stance shifted from absolutist to Few-resolved (zero baseline non-negotiable because of the channel mechanism, but other Tufte heuristics treated as guides not commandments).
   - Both chapters adopted the 12-section anatomy from the updated spec.

5. User authorized the full march. Ch 2, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15 plus front matter, intro, Chapter 00, and back matter all drafted in five batches.

---

## Known gaps and rough edges

These are explicitly flagged for future revision passes.

1. **Chapter length variance.** Chapters generally landed in the 5,500–7,500 word range. Some are longer (Ch 1, Ch 5 in their rewritten forms; Ch 14 with the full 22-point checklist). Per the user's prior "rough drafts" mandate (carried over from earlier books in this session), no padding was done.

2. **Step 3 of the curriculum enrichment generator (running project) was not formally executed.** The book's structure already includes a capstone project (Chapter 15) that effectively serves the running-project role. A formal three-to-five-options menu was not produced. If the book is adopted for course use, the instructor can either use Chapter 15's UNHCR humanitarian-data project as the running project or substitute a domain-specific dataset.

3. **Step 4 of the curriculum enrichment generator (Dig Deeper + LLM Exercise enrichment) is partially complete.** Each chapter has Dig Deepers embedded inline and an LLM Exercise at the chapter end. The LLM Exercises were written as project-agnostic (since no project was locked in Step 3); they reference "[TBD — selected after Chapter 00]" as a placeholder. If a running project is later locked, the LLM Exercises will need to be retuned with project-specific prompt blocks (as was done for the prior three books in this session).

4. **No primary-source verification pass.** Each chapter contains many specific names, dates, paper citations, and historical claims. None has been independently verified. A revision pass should apply `[verify]` flags and verify each. Particularly dense citation chapters: Ch 1 (Bertin, Cleveland & McGill, Heer & Bostock, Munzner, Stevens), Ch 14 (Tufte, Few, Cairo, Evergreen/Emery, Bateman et al., Pandey et al.).

5. **The pilot's first version was retained in the older form of `02-chapter-01.md` and `06-chapter-05.md` until the rewrite overwrote it.** No history is preserved of the pilot version; if it would be useful for the user to compare, it would need to be reconstructed from the conversation history.

6. **Build pipeline integration not tested.** The `build.sh` / `metadata.yaml` Kindle pipeline exists but has not been run against the new chapter files in this session. Filename ordering (`00-frontmatter.md` → `01-introduction.md` → `01a-chapter-00.md` → `02-chapter-01.md` → ... → `99-back-matter.md`) follows the existing convention but should be tested with `./build.sh` to confirm the EPUB compiles correctly.

7. **The Brutalist framing in the front matter** is from the user-pasted Brutalist documentation; that documentation is not separately included in the pantry as a reference document. If the book's preface refers to Brutalist as a system the reader can find documentation for, the Brutalist documentation should accompany the published book.

8. **Sociology / political-science / finance carryovers.** No carryover. This book is independent of the prior three.

---

## Revisions

*Track changes from this point forward in this section.*

### 2026-05-08 — Initial run
- 19 documents drafted (front matter, intro, Ch 00, Chs 1-15, back matter).
- Pilot drafted, then rewritten against updated specs.
- Full march completed in five batches.
- Brutalist framing established in front matter.
