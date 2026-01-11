---
description: Phase 1/3 - Text & Structure Extraction for Lecture Analysis
---

# Phase 1: Text & Structure Extraction

**Goal:** Create the initial Markdown skeleton with all headers, concepts, and textual notes.
**Output:** `resources/claude_analysis/lec-{NUM}.md` (Skeleton)

---

## Available OCR Resources (Reference Only)

Pre-extracted OCR text is available for all lectures:

| Source | Location |
|--------|----------|
| **EasyOCR** | `resources/easyocr/lec-{NUM}.md` |
| **PDFtoText** | `resources/pdftotext/lec-{NUM}.md` |

> [!WARNING]
> **Do NOT rely on these files.** Primary extraction should come from viewing the images directly.
> Only check these if you suspect something extra was missed from the images.

---

## Step 1: Convert PDF to Images
**(Skip if images already exist)**

// turbo
```bash
cd /home/abhay/repos/dsa
.venv/bin/python pdf_to_images.py "lectures/L{NUM} - {NAME}.pdf" "resources/claude_analysis/L{NUM}"
```

**Location:** `resources/claude_analysis/L{NUM}/page_XX.png`

---

## Step 2: Extract Text & Structure

**Instruction:**
Iterate through EVERY page image in `resources/claude_analysis/L{NUM}/`.
For each image:
1.  **View** the image.
2.  **Identify** the main Header/Topic (e.g., "DFS", "Adjacency Matrix").
3.  **Extract** key definitions, bullet points, and specific handwritten notes (text only).

---

## Step 3: Write Skeleton Markdown

**Action:** Create/Overwrite `resources/claude_analysis/lec-{NUM}.md` with the following structure:

```markdown
# Lecture {NUM} - {Topic Name}

**Source:** `L{NUM} - {Name}.pdf`

---

## Topic 1: {Name}

### Concept Explanation
- {Extracted Definitions}
- {Key Handwritten Insights}

---

## Topic 2: {Name}
...
```

**Rules:**
- Focus on **Hierarchy** (Topics -> Subtopics).
- Capture **Definitions** accurately.
- Do **NOT** focus on drawing complex diagrams yet (placeholders like `[Diagram: DFS Tree]` are fine).
- Do **NOT** search for links yet.
