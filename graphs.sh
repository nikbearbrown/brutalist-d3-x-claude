#!/bin/bash
# ─────────────────────────────────────────────────────────────────────────────
# graphs.sh
#
# Always run from repo root:
#   ./graphs.sh                      # process all chapters
#   ./graphs.sh chapters/01-foo.md   # process one chapter
#
# For each <!-- → [TYPE: description] --> comment in each chapter:
#   - TABLE / tabular INFOGRAPHIC / tabular CHART
#       → classed markdown table inserted below comment
#   - DIAGRAM / IMAGE / non-tabular INFOGRAPHIC / spatial CHART
#       → placeholder .jpg written to images/, image reference inserted
#
# Skips chapters with no figure comments.
# Writes chapters/BASENAME-updated.md — originals untouched.
# Appends a CSS log to styles/kindle-book.css on each run.
#
# Promote when ready:
#   for f in chapters/*-updated.md; do mv "$f" "${f/-updated/}"; done
#
# Dependencies: ImageMagick (convert), bash 3.2+ (macOS compatible)
# ─────────────────────────────────────────────────────────────────────────────
set -e

CHAPTERS_DIR="chapters"
IMAGES_DIR="images"
STYLES_DIR="styles"
KINDLE_BOOK_CSS="$STYLES_DIR/kindle-book.css"

for dir in "$CHAPTERS_DIR" "$IMAGES_DIR" "$STYLES_DIR"; do
  if [[ ! -d "$dir" ]]; then
    echo "Error: expected directory '$dir' not found." >&2
    echo "Run this script from the repo root." >&2
    exit 1
  fi
done

touch "$KINDLE_BOOK_CSS"

FILES=()
if [[ -n "$1" ]]; then
  if [[ -f "$1" ]]; then
    FILES=("$1")
  else
    echo "Error: file not found: $1" >&2
    exit 1
  fi
else
  while IFS= read -r -d '' f; do
    FILES+=("$f")
  done < <(find "$CHAPTERS_DIR" -maxdepth 1 -name "*.md" -print0 | sort -z)
fi

if [[ ${#FILES[@]} -eq 0 ]]; then
  echo "No .md files found in $CHAPTERS_DIR" >&2
  exit 1
fi

IMG_W=1600
IMG_H=900
IMG_BG="#d0cec8"
IMG_FG="#1a1814"
IMG_ACCENT="#9a7d3a"

uppercase() { echo "$1" | tr '[:lower:]' '[:upper:]'; }

ucfirst() {
  local str="$1"
  local first
  first=$(echo "${str:0:1}" | tr '[:lower:]' '[:upper:]')
  echo "${first}${str:1}"
}

truncate_desc() {
  local desc="$1"
  local first
  first=$(echo "$desc" | sed 's/ — .*//')
  if [[ ${#first} -lt ${#desc} && ${#first} -gt 10 ]]; then echo "$first"; return; fi
  first=$(echo "$desc" | sed 's/;.*//')
  if [[ ${#first} -lt ${#desc} && ${#first} -gt 10 ]]; then echo "$first"; return; fi
  if [[ ${#desc} -gt 80 ]]; then echo "${desc:0:77}..."; return; fi
  echo "$desc"
}

make_placeholder() {
  local filepath="$1"
  local fig_label="$2"
  local type_tag="$3"
  local short_desc="$4"
  local wrapped
  wrapped=$(echo "$short_desc" | fold -s -w 40)

  convert \
    -size ${IMG_W}x${IMG_H} xc:"$IMG_BG" \
    -font "Helvetica" \
    -pointsize 28 -fill "$IMG_ACCENT" -gravity North \
    -annotate +0+80 "${fig_label} — PLACEHOLDER" \
    -pointsize 18 -fill "$IMG_FG" -gravity North \
    -annotate +0+140 "$type_tag" \
    -pointsize 22 -fill "$IMG_FG" -gravity Center \
    -annotate +0-40 "$wrapped" \
    -strokewidth 3 -stroke "$IMG_ACCENT" -fill none \
    -draw "rectangle 40,40 $((IMG_W-40)),$((IMG_H-40))" \
    "$filepath" 2>/dev/null

  echo "    → image: $(basename "$filepath")" >&2
}

classify() {
  local type_tag
  type_tag=$(uppercase "$1")
  local description="$2"

  case "$type_tag" in
    TABLE)
      if echo "$description" | grep -qi "contrast\|vs\|versus\|comparison"; then
        echo "infographic-table"
      elif echo "$description" | grep -qi "data\|results\|measure\|count\|number\|rate\|score"; then
        echo "data-table"
      else
        echo "comparison-table"
      fi
      ;;
    INFOGRAPHIC)
      if echo "$description" | grep -qi "contrast\|vs\|versus\|comparison\|columns\|rows\|side.by.side\|properties"; then
        echo "infographic-table"
      else
        echo "image"
      fi
      ;;
    CHART)
      if echo "$description" | grep -qi "columns\|rows\|comparison\|vs"; then
        echo "data-table"
      else
        echo "image"
      fi
      ;;
    IMAGE|DIAGRAM|*)
      echo "image"
      ;;
  esac
}

render_table() {
  local description="$1"
  local fig_label="$2"
  local css_class="$3"

  local col1="Property"
  local col2="Value"

  if echo "$description" | grep -qi " vs\.* "; then
    col1=$(echo "$description" | sed 's/.*contrast of //i' | sed 's/ vs\.* .*//i' | sed 's/^ *//;s/ *$//')
    col2=$(echo "$description" | sed 's/.* vs\.* //i' | sed 's/ —.*//;s/ -.*//' | sed 's/^ *//;s/ *$//')
    col1=$(ucfirst "$col1")
    col2=$(ucfirst "$col2")
  fi

  local rows_hint=""
  if echo "$description" | grep -qi "rows"; then
    rows_hint=$(echo "$description" | sed 's/.*rows[^:]*: //i' | sed 's/;.*//' | sed 's/ and /,/g')
  fi

  echo ""
  echo "*${fig_label}*"
  echo ""
  echo "| | **${col1}** | **${col2}** |"
  echo "|---|---|---|"

  if [[ -n "$rows_hint" ]]; then
    IFS=',' read -ra ROW_NAMES <<< "$rows_hint"
    for row in "${ROW_NAMES[@]}"; do
      row=$(echo "$row" | sed 's/^ *//;s/ *$//')
      row=$(ucfirst "$row")
      echo "| **${row}** | _fill in_ | _fill in_ |"
    done
  else
    echo "| **Row 1** | _fill in_ | _fill in_ |"
    echo "| **Row 2** | _fill in_ | _fill in_ |"
  fi

  echo ""
  echo ": {.${css_class}}"
  echo ""
}

TOTAL_IMAGES=0
TOTAL_TABLES=0
TOTAL_SKIPPED=0
CSS_LOG=""

for CHAPTER_FILE in "${FILES[@]}"; do

  if ! grep -qE '<!-- → \[' "$CHAPTER_FILE"; then
    BASENAME=$(basename "$CHAPTER_FILE" .md)
    echo "Skipping: $BASENAME (no figure comments)" >&2
    TOTAL_SKIPPED=$((TOTAL_SKIPPED + 1))
    continue
  fi

  BASENAME=$(basename "$CHAPTER_FILE" .md)
  CHAPTER_SLUG="${BASENAME#chapter-}"
  CHAPTER_NUM=$(echo "$CHAPTER_SLUG" | grep -oE '^[0-9]+' | sed 's/^0*//')
  [[ -z "$CHAPTER_NUM" ]] && CHAPTER_NUM="0"

  OUT_FILE="${CHAPTERS_DIR}/${BASENAME}-updated.md"
  FIG_COUNT=0

  echo "" >&2
  echo "Processing: $BASENAME" >&2

  while IFS= read -r line; do

    if echo "$line" | grep -qE '<!-- → \['; then

      COMMENT_CONTENT=$(echo "$line" | sed 's/.*<!-- → \[//;s/\].*//')
      TYPE_TAG=$(echo "$COMMENT_CONTENT" | sed 's/:.*//' | tr -d ' ')
      DESCRIPTION=$(echo "$COMMENT_CONTENT" | sed 's/^[^:]*: *//')

      FIG_COUNT=$((FIG_COUNT + 1))
      FIG_LABEL="Figure ${CHAPTER_NUM}.${FIG_COUNT}"

      RENDER_AS=$(classify "$TYPE_TAG" "$DESCRIPTION")
      SHORT_DESC=$(truncate_desc "$DESCRIPTION")
      TYPE_UPPER=$(uppercase "$TYPE_TAG")

      if [[ "$RENDER_AS" == "image" ]]; then
        IMG_FILENAME="${CHAPTER_SLUG}-fig-$(printf "%02d" $FIG_COUNT).jpg"
        make_placeholder "${IMAGES_DIR}/${IMG_FILENAME}" \
          "$FIG_LABEL" "$TYPE_UPPER" "$SHORT_DESC"
        TOTAL_IMAGES=$((TOTAL_IMAGES + 1))

        echo "$line"
        echo ""
        echo "![${FIG_LABEL} — ${SHORT_DESC}](images/${IMG_FILENAME})"
        echo ""

        CSS_LOG="${CSS_LOG}\n/* ${FIG_LABEL} (${BASENAME}): image — replace ${IMG_FILENAME} */"
      else
        TOTAL_TABLES=$((TOTAL_TABLES + 1))
        echo "$line"
        render_table "$DESCRIPTION" "$FIG_LABEL" "$RENDER_AS"
        CSS_LOG="${CSS_LOG}\n/* ${FIG_LABEL} (${BASENAME}): .${RENDER_AS} */"
        echo "    → table (${RENDER_AS}): ${FIG_LABEL}" >&2
      fi

    else
      echo "$line"
    fi

  done < "$CHAPTER_FILE" > "$OUT_FILE"

  echo "  Written: $OUT_FILE" >&2

done

if [[ -n "$CSS_LOG" ]]; then
  {
    echo ""
    echo "/* ── graphs.sh run: $(date '+%Y-%m-%d %H:%M') ── */"
    printf "$CSS_LOG\n"
  } >> "$KINDLE_BOOK_CSS"
  echo "" >&2
  echo "CSS log appended to: $KINDLE_BOOK_CSS" >&2
fi

echo "" >&2
echo "────────────────────────────────────────────" >&2
echo "Done." >&2
echo "  Skipped (no comments) : $TOTAL_SKIPPED" >&2
echo "  Tables rendered       : $TOTAL_TABLES" >&2
echo "  Images generated      : $TOTAL_IMAGES" >&2
echo "" >&2
echo "Review -updated.md files, then promote:" >&2
echo '  for f in chapters/*-updated.md; do mv "$f" "${f/-updated/}"; done' >&2
echo "────────────────────────────────────────────" >&2
