#!/usr/bin/env python3
"""
Generate brutalist placeholder images for missing chapter figures.
Replace these with real images later. Each placeholder is labeled with its
filename so it's obvious which one needs replacement.
"""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

BOOK_ROOT = Path(__file__).parent
IMAGES = BOOK_ROOT / "images"
MISSING_LIST = Path("/tmp/missing.txt")

FONT_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
FONT_MONO = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf"

# Size by image type
def size_for(name: str):
    # Portraits — people, named individuals
    if name.endswith(".jpg") and "-" in name and not name[0].isdigit():
        return (800, 1000)  # portrait orientation
    # Numbered chart-type figures
    return (1200, 800)  # landscape


def draw_placeholder(path: Path):
    name = path.name
    w, h = size_for(name)
    img = Image.new("RGB", (w, h), "white")
    d = ImageDraw.Draw(img)

    # Brutalist heavy border
    border = 18
    d.rectangle([0, 0, w - 1, h - 1], outline="black", width=border)

    # Diagonal cross — visual signal "this is a placeholder"
    d.line([(border, border), (w - border, h - border)], fill="black", width=4)
    d.line([(w - border, border), (border, h - border)], fill="black", width=4)

    # White label panel in middle
    pad_x = 60
    panel_h = 220
    panel_top = (h - panel_h) // 2
    d.rectangle(
        [pad_x, panel_top, w - pad_x, panel_top + panel_h],
        fill="white",
        outline="black",
        width=8,
    )

    # Text
    try:
        f_label = ImageFont.truetype(FONT_BOLD, 36)
        f_name = ImageFont.truetype(FONT_MONO, 22)
        f_note = ImageFont.truetype(FONT_BOLD, 20)
    except OSError:
        f_label = f_name = f_note = ImageFont.load_default()

    label = "PLACEHOLDER"
    # Center text horizontally
    def centered(text, font, y):
        bbox = d.textbbox((0, 0), text, font=font)
        tw = bbox[2] - bbox[0]
        d.text(((w - tw) // 2, y), text, font=font, fill="black")

    centered(label, f_label, panel_top + 30)
    centered(name, f_name, panel_top + 95)
    centered("REPLACE BEFORE PUBLISH", f_note, panel_top + 150)

    img.save(path, "JPEG", quality=85)
    return path


def make_cover(path: Path):
    # Kindle recommended: 1600 x 2560
    w, h = 1600, 2560
    img = Image.new("RGB", (w, h), "white")
    d = ImageDraw.Draw(img)

    # Massive brutalist border
    border = 60
    d.rectangle([0, 0, w - 1, h - 1], outline="black", width=border)

    # Top black bar
    bar_h = 400
    d.rectangle([border, border, w - border, border + bar_h], fill="black")

    try:
        f_title = ImageFont.truetype(FONT_BOLD, 140)
        f_sub = ImageFont.truetype(FONT_BOLD, 60)
        f_byline = ImageFont.truetype(FONT_MONO, 56)
        f_warn = ImageFont.truetype(FONT_BOLD, 44)
    except OSError:
        f_title = f_sub = f_byline = f_warn = ImageFont.load_default()

    def centered(text, font, y, fill="black"):
        bbox = d.textbbox((0, 0), text, font=font)
        tw = bbox[2] - bbox[0]
        d.text(((w - tw) // 2, y), text, font=font, fill=fill)

    # Title in white on black bar
    centered("BRUTALIST", f_title, border + 80, fill="white")
    centered("D3 × CLAUDE", f_title, border + 230, fill="white")

    # Subtitle in middle
    centered("Data Visualization", f_sub, 1100)
    centered("From First Principles", f_sub, 1180)

    # Byline near bottom
    centered("NIK BEAR BROWN", f_byline, h - 600)

    # Diagonal line for placeholder signal
    d.line([(border, h - 400), (w - border, h - 400)], fill="black", width=8)

    # Placeholder warning
    centered("PLACEHOLDER COVER", f_warn, h - 320)
    centered("REPLACE BEFORE PUBLISH", f_warn, h - 250)

    img.save(path, "JPEG", quality=90)
    return path


def main():
    IMAGES.mkdir(exist_ok=True)
    missing = [
        line.strip()
        for line in MISSING_LIST.read_text().splitlines()
        if line.strip()
    ]
    print(f"Creating {len(missing)} image placeholders...")
    for name in missing:
        out = IMAGES / name
        draw_placeholder(out)
    print(f"Done. Wrote {len(missing)} files to {IMAGES}")

    cover = BOOK_ROOT / "cover.jpg"
    make_cover(cover)
    print(f"Wrote cover: {cover}")


if __name__ == "__main__":
    main()
