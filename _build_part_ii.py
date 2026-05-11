#!/usr/bin/env python3
"""
Build Part II of Brutalist d3 x Claude.

For each chart in pantry/visualization/{slug}.html:
- Parse rich prose blocks (.expl-block, .example-block, .framework-box)
- Read pantry/visualization/{slug}/data.json schema (where available)
- Compose chapters/NN-{slug}.md with: title, image link, prose, prompt, bearbrown ref
- Copy black placeholder JPG to images/NN-{slug}.jpg
"""

import json, re, shutil
from pathlib import Path
from bs4 import BeautifulSoup

ROOT = Path(__file__).parent
PANTRY = ROOT / "pantry" / "visualization"
CHAPTERS = ROOT / "chapters"
IMAGES = ROOT / "images"
PLACEHOLDER = IMAGES / "_placeholder.jpg"

# Alphabetical pantry slugs
slugs = sorted(p.stem for p in PANTRY.glob("*.html"))
print(f"Found {len(slugs)} pantry HTML files")

# NN starts at 18
START_NN = 18

def text_of(el):
    """Get clean text from a BS4 element, preserving paragraph breaks."""
    if el is None:
        return ""
    paras = []
    for p in el.find_all(["p"], recursive=False):
        t = p.get_text(" ", strip=True)
        # Convert <strong> and <em> back to markdown
        t = re.sub(r"\s+", " ", t)
        if t:
            paras.append(t)
    if not paras:
        # fallback
        t = el.get_text(" ", strip=True)
        if t:
            paras.append(t)
    return "\n\n".join(paras)

def md_inline(el):
    """Convert paragraphs to markdown, preserving <strong>=** and <em>=*."""
    if el is None:
        return ""
    # Replace tags with markdown markers in-place
    for s in el.find_all("strong"):
        s.replace_with(f"**{s.get_text()}**")
    for e in el.find_all("em"):
        e.replace_with(f"*{e.get_text()}*"  )
    for c in el.find_all("code"):
        c.replace_with(f"`{c.get_text()}`")
    paras = []
    for p in el.find_all("p", recursive=True):
        t = p.get_text(" ", strip=True)
        t = re.sub(r"\s+", " ", t)
        if t:
            paras.append(t)
    return "\n\n".join(paras)

def parse_chart(slug):
    html_path = PANTRY / f"{slug}.html"
    if not html_path.exists():
        return None
    soup = BeautifulSoup(html_path.read_text(encoding="utf-8"), "html.parser")

    # Slide-title H1 (marketing tagline)
    h1 = soup.find("h1", class_="slide-title")
    slide_title = h1.get_text(strip=True) if h1 else ""

    # Aliases from old expl-header pattern only
    aliases = ""
    expl_header = soup.find("div", class_="expl-header")
    if expl_header:
        sub = expl_header.find("p", class_="subtitle")
        if sub:
            aliases = sub.get_text(strip=True)

    # Chart name = nicely-formatted slug (always predictable)
    # Title-case but preserve common acronyms
    parts = slug.split("-")
    titled = []
    acronyms = {"d3", "ohlc", "kde", "ai", "ui", "us", "uk", "kpi", "rgb", "csv"}
    small_words = {"and", "of", "the", "for", "to", "with", "in", "on", "by", "as", "at"}
    for i, p in enumerate(parts):
        if p in acronyms:
            titled.append(p.upper())
        elif i > 0 and p in small_words:
            titled.append(p)
        else:
            titled.append(p.capitalize())
    chart_name = " ".join(titled)

    blocks = []
    framework_text = ""

    # PATTERN 1: expl-block (used by arc-diagram, brainstorm, circle-packing, gantt-chart)
    expl_blocks = soup.find_all("div", class_="expl-block")
    if expl_blocks:
        for blk in expl_blocks:
            h3 = blk.find("h3")
            heading = h3.get_text(strip=True) if h3 else ""
            fb = blk.find("div", class_="framework-box")
            fb_text = ""
            if fb:
                fb_text = fb.get_text(" ", strip=True)
                fb.extract()
            body_md = md_inline(blk)
            blocks.append({"heading": heading, "body": body_md})
            if fb_text:
                framework_text = fb_text

    # PATTERN 2: learn-block — single container with multiple <h2> inside
    if not blocks:
        learn_blocks = soup.find_all("div", class_="learn-block")
        for lb in learn_blocks:
            # Capture framework-ref or framework-box
            for fclass in ("framework-ref", "framework-box"):
                fb = lb.find("div", class_=fclass)
                if fb:
                    framework_text = fb.get_text(" ", strip=True)
                    fb.extract()

            # Walk children — group <p>/text under nearest preceding <h2>/<h3>
            current_heading = ""
            current_body = []
            def flush():
                nonlocal current_heading, current_body
                if current_body:
                    body_md = "\n\n".join(current_body)
                    blocks.append({"heading": current_heading, "body": body_md})
                    current_body = []

            for child in lb.find_all(recursive=False):
                if child.name in ("h2", "h3", "h4"):
                    flush()
                    current_heading = child.get_text(strip=True)
                elif child.name == "p":
                    # markdown inline conversion in-place
                    for s in child.find_all("strong"):
                        s.replace_with(f"**{s.get_text()}**")
                    for e in child.find_all("em"):
                        e.replace_with(f"*{e.get_text()}*")
                    for c in child.find_all("code"):
                        c.replace_with(f"`{c.get_text()}`")
                    t = child.get_text(" ", strip=True)
                    t = re.sub(r"\s+", " ", t)
                    if t:
                        current_body.append(t)
                elif child.name == "div" and child.get("class"):
                    classes = child.get("class")
                    if any(c in ("framework-ref", "framework-box") for c in classes):
                        # already extracted above; skip
                        continue
                    # otherwise treat as a sub-block — pull text
                    t = child.get_text(" ", strip=True)
                    if t:
                        current_body.append(t)
            flush()

    # PATTERN 3: chart-explanation as top-level wrapper
    if not blocks:
        ce = soup.find("div", class_="chart-explanation")
        if ce:
            current_heading = ""
            current_body = []
            for child in ce.find_all(recursive=True):
                if child.name in ("h2", "h3"):
                    if current_body:
                        blocks.append({"heading": current_heading, "body": "\n\n".join(current_body)})
                        current_body = []
                    current_heading = child.get_text(strip=True)
                elif child.name == "p":
                    for s in child.find_all("strong"):
                        s.replace_with(f"**{s.get_text()}**")
                    for e in child.find_all("em"):
                        e.replace_with(f"*{e.get_text()}*")
                    t = child.get_text(" ", strip=True)
                    if t:
                        current_body.append(re.sub(r"\s+", " ", t))
            if current_body:
                blocks.append({"heading": current_heading, "body": "\n\n".join(current_body)})

    # PATTERN 4: no prose. Fall back to <title>'s meta description
    if not blocks:
        meta_desc = soup.find("meta", attrs={"name": "description"})
        if meta_desc and meta_desc.get("content"):
            blocks.append({"heading": "What this chart is", "body": meta_desc["content"].strip()})

    # The "About this example" block (old format only)
    example = soup.find("div", class_="example-block")
    example_md = ""
    example_heading = ""
    if example:
        h3 = example.find("h3")
        if h3:
            example_heading = h3.get_text(strip=True)
        example_md = md_inline(example)

    # Attach framework as its own pseudo-block at end
    if framework_text:
        blocks.append({"heading": "Framework reference", "body": "> " + framework_text})

    return {
        "slug": slug,
        "slide_title": slide_title,
        "chart_name": chart_name,
        "aliases": aliases,
        "blocks": blocks,
        "example_heading": example_heading,
        "example_body": example_md,
    }

def load_data_schema(slug):
    p = PANTRY / slug / "data.json"
    if not p.exists():
        return None
    try:
        d = json.loads(p.read_text(encoding="utf-8"))
        return d
    except Exception:
        return None

def gen_prompt(slug, info, data):
    """Generate a single Claude Code prompt that produces both D3 + JSON."""
    chart_name = info["chart_name"]
    slide_title = info["slide_title"] or chart_name

    # Describe the data shape from schema
    schema_desc = ""
    if data and isinstance(data, dict):
        schema = data.get("_schema", {})
        if isinstance(schema, dict):
            fields = schema.get("fields", {})
            desc = schema.get("description", "")
            if desc or fields:
                schema_desc = "\nData shape:\n"
                if desc:
                    schema_desc += f"- {desc}\n"
                for k, v in fields.items():
                    schema_desc += f"  - `{k}`: {v}\n"

    if not schema_desc:
        # No data schema available; describe inline
        schema_desc = "\nDecide a reasonable data shape for this chart type and invent themed sample values.\n"

    prompt = f"""Generate a complete, self-contained {chart_name.lower()} in D3 v7. Two files:

1. `{slug}.html` — a full HTML page with inline CSS and inline D3 v7 (loaded from `https://cdnjs.cloudflare.com/ajax/libs/d3/7.8.5/d3.min.js`). The chart should fill the viewport, be responsive on resize, support keyboard focus on interactive elements, and include a tooltip on hover. The page title is "{chart_name}" and the slide subtitle is "{slide_title}".

2. `{slug}/data.json` — the data file the chart loads via `d3.json("./{slug}/data.json")`, with a fallback inline literal in the HTML if the fetch fails.
{schema_desc}
Encoding: use the perceptually honest channel for this chart type ({chart_name.lower()}). Do not invent decorative encodings. Annotate the chart with a one-line in-chart subtitle that names what the chart shows. Include an accessibility `<title>` and `<desc>` inside the SVG.

Style: warm monochrome — black, dark walnut, blood-red accents only. Serif font for body text, JetBrains Mono for labels and controls. No drop shadows, no rounded corners, no gradients. Clean editorial register suitable for a print-ready textbook page.

Provide both files as separate code blocks. Do not explain — just produce the files."""
    return prompt

# Build each chapter
manifest = []
for i, slug in enumerate(slugs):
    nn = START_NN + i
    info = parse_chart(slug)
    if info is None:
        print(f"SKIP {slug} — no HTML")
        continue
    data = load_data_schema(slug)
    prompt = gen_prompt(slug, info, data)

    # Compose markdown
    title = info["chart_name"]
    slide_title = info["slide_title"]
    aliases = info["aliases"]
    parts = [f"# {title}", ""]
    if slide_title:
        parts.append(f"*{slide_title}*")
        parts.append("")
    parts.append(f"![{title}](../images/{nn:02d}-{slug}.jpg)")
    parts.append("")
    if aliases:
        parts.append(f"{aliases}")
        parts.append("")

    for blk in info["blocks"]:
        if blk["heading"]:
            parts.append(f"## {blk['heading']}")
            parts.append("")
        if blk["body"]:
            parts.append(blk["body"])
            parts.append("")

    if info["example_heading"]:
        parts.append(f"## {info['example_heading']}")
        parts.append("")
    if info["example_body"]:
        parts.append(info["example_body"])
        parts.append("")

    parts.append("## Prompt")
    parts.append("")
    parts.append("Paste this into Claude Code to generate a working version of this chart, plus its data file. The result will not be a perfect replica — the goal is that the reader can run the prompt, get a chart of this type, and read its source.")
    parts.append("")
    parts.append("```")
    parts.append(prompt)
    parts.append("```")
    parts.append("")
    parts.append(f"The original code and data — copy-paste-ready — live at [bearbrown.co](https://www.bearbrown.co/).")
    parts.append("")

    md = "\n".join(parts)

    out_path = CHAPTERS / f"{nn:02d}-{slug}.md"
    out_path.write_text(md, encoding="utf-8")

    # Image placeholder
    img_path = IMAGES / f"{nn:02d}-{slug}.jpg"
    shutil.copy(PLACEHOLDER, img_path)

    manifest.append((nn, slug, info["chart_name"], len(info["blocks"]), data is not None))

print(f"\n=== Wrote {len(manifest)} chapters ===")
for nn, slug, name, blockcount, has_data in manifest:
    flag = "✓" if has_data else "·"
    print(f"  {nn:02d} {flag} {slug:30s} {name}  ({blockcount} prose blocks)")
