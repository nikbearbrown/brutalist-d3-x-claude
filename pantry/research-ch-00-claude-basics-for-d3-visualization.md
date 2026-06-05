# Research: Chapter 00 — Claude Basics for D3 Visualization
## Brutalist d3 x Claude

**Chapter one-line:** Use Claude Code to implement D3 only after the chart has been specified.
**Research date:** 2026-06-01

---

## 1. Primary Sources

1. Anthropic, "Claude Code overview." Source: https://code.claude.com/docs  
   Official source for Claude Code as an agentic coding tool that can inspect files, edit code, run commands, and support repository work.

2. Anthropic, "How Claude Code works." Source: https://code.claude.com/docs/en/how-claude-code-works  
   Supports explaining Claude Code as a tool-using workflow rather than a chat-only assistant.

3. Anthropic, "Configure permissions." Source: https://code.claude.com/docs/en/permissions  
   D3 projects involve local files and command execution, so permissions and approval gates are part of the workflow.

4. Anthropic, "Be clear, direct, and detailed." Source: https://anthropic.mintlify.app/en/docs/build-with-claude/prompt-engineering/be-clear-and-direct  
   Anchors the chapter's prompt/specification discipline.

5. D3 official docs. Source: https://d3js.org/  
   Source for current D3 modules and implementation concepts.

6. D3, "What is D3?" Source: https://d3js.org/what-is-d3  
   Useful for explaining D3 as composed primitives rather than prebuilt chart commands.

7. Observable Plot docs. Source: https://observablehq.com/plot/  
   Comparison source for when a higher-level charting API may be enough.

8. Zamfirescu-Pereira et al., "Why Johnny Can't Prompt," CHI 2023. Source: https://people.eecs.berkeley.edu/~bjoern/papers/zamfirescu-johnny-chi2023.pdf  
   Supports teaching concrete prompt/spec patterns rather than prompt folklore.

9. Microsoft, "Guidelines for Human-AI Interaction," CHI 2019. Source: https://www.microsoft.com/en-us/research/project/guidelines-for-human-ai-interaction/publications/  
   Supports user control, feedback, correction, and recoverability.

10. Mark Chen et al., "Evaluating Large Language Models Trained on Code," 2021. Source: https://arxiv.org/abs/2107.03374  
    Supports execution-based verification for generated code.

## 2. Core Concept — State of the Field

Claude Code is useful for D3 because D3 implementation has many mechanical moving parts: data loading, scales, axes, SVG groups, joins, labels, styles, and interaction. But Claude Code cannot know the visual argument unless the user specifies it.

The chapter should teach a "four-move" prompt rhythm: data structure, chart purpose, encoding decisions, and verification/audit criteria.

## 3. Application Domain Examples

1. Vague prompt: "Make a bar chart."
2. Better prompt: "Encode sector as y position, value as x length, zero baseline, sorted descending, labels visible."
3. Claude-generated D3 with radius instead of area for bubbles.
4. Claude-generated chart missing axis labels or source note.
5. Iterative correction: one issue per prompt.

## 4. Book's Thesis Connection

This chapter operationalizes the thesis: Claude can write the D3, but the reader must specify marks, channels, constraints, and audit criteria. The first Claude skill is not clever prompting; it is visual specification.

## 5. AI Wayback Machine — Candidate Figures

1. Mike Bostock — D3's practical lineage.
2. Grace Hopper — executable instructions and debugging.
3. Margaret Hamilton — software verification and disciplined implementation.
4. Jacques Bertin — visual variables as specification vocabulary.

## 6. Pedagogical Delivery Research

Teach with side-by-side prompts and outputs. Students should see that weak prompts create plausible charts and strong specifications create auditable charts.

Common misconceptions:

- "Claude knows chart defaults."
- "D3 errors are the main risk."
- "If it renders, it works."
- "One correction prompt can fix everything."

## 7. Representation and Display Research

Recommended D3 prompt template:

```text
Goal:
Data fields:
Reader question:
Chart type:
Marks:
Channels:
Scales/axes:
Labels/annotations:
Interaction:
Do not:
Verify:
```

## 8. Open Questions and Research Gaps

1. Re-check Claude Code interface and permission details before publication.
2. Decide whether examples use local HTML files, Observable, CodePen, or all three.
3. Add a troubleshooting table for common generated-D3 failures.

