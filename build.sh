#!/bin/bash
set -e

BOOK_SLUG="brutalist-d3-x-claude"
METADATA="metadata.yaml"
OUTPUT_DIR="output"

mkdir -p "$OUTPUT_DIR"

# Compile chapters in filename order
# 00-frontmatter → 01-introduction → 02..NN chapters → 99-back-matter
cat $METADATA chapters/*.md > "$OUTPUT_DIR/combined.md"

# Resource paths so pandoc finds images.
RESOURCE_PATH=".:images:chapters"

# Create EPUB version with normalized paths (../images/ → images/)
# so pandoc can resolve them via --resource-path.
cp "$OUTPUT_DIR/combined.md" "$OUTPUT_DIR/combined-epub.md"
sed -i 's|\.\./images/|images/|g' "$OUTPUT_DIR/combined-epub.md"

# EPUB (primary — upload this to KDP)
pandoc "$OUTPUT_DIR/combined-epub.md" \
  --from markdown \
  --to epub3 \
  --epub-cover-image=cover.jpg \
  --css=styles/kindle.css \
  --css=styles/kindle-book.css \
  --resource-path="$RESOURCE_PATH" \
  --toc --toc-depth=2 \
  --output="$OUTPUT_DIR/$BOOK_SLUG.epub"

# HTML (proofing — copy styles so relative CSS links work from output/)
mkdir -p "$OUTPUT_DIR/styles"
cp styles/kindle.css styles/kindle-book.css "$OUTPUT_DIR/styles/" 2>/dev/null || true

pandoc "$OUTPUT_DIR/combined.md" \
  --from markdown \
  --to html5 \
  --standalone \
  --css=styles/kindle.css \
  --css=styles/kindle-book.css \
  --resource-path="$RESOURCE_PATH" \
  --toc \
  --output="$OUTPUT_DIR/$BOOK_SLUG.html"

echo "Built: $OUTPUT_DIR/$BOOK_SLUG.epub"
echo "Built: $OUTPUT_DIR/$BOOK_SLUG.html"
