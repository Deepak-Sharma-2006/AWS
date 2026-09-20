---
name: sih-presentation-cloner
description: >-
  Systematic 1:1 reverse-engineering and cloning of championship Smart India Hackathon (SIH) presentation
  decks into native PPTX/PDF decks with pixel-accurate layout geometry, custom vector diagrams, and dense technical content.
metadata:
  origin: Antigravity-Governance
---

# SIH Presentation Cloner — Championship Deck Synthesis Protocol

> **Purpose**: Enables 1:1 structural reverse-engineering and flawless cloning of winning Smart India Hackathon (SIH) evaluation decks. Converts reference PDF/PPTX layouts into clean, non-AI-looking, institutional-grade PowerPoint presentations with real vector diagrams, precise coordinate geometry, and exhaustive domain content.

---

## 1. Non-Negotiable Operational Principles

1. **1:1 Structural Parity**:
   - Slide count is strictly locked to the official SIH 6-slide format:
     - Slide 1: Official Title Page (PS ID, Title, Theme, Category, Team ID, Team Name, Official SIH Emblem).
     - Slide 2: Idea Title & Proposed Solution (Core Pillar bullets on Left, Comprehensive Architecture Diagram on Right).
     - Slide 3: Technical Approach (Layered Stack on Left/Center, Sequential Process Flow Diagram, Live Demo Links).
     - Slide 4: Feasibility and Viability (4-Dimension Matrix, Challenges vs. Mitigations, Supporting Facts Callout Card).
     - Slide 5: Impact and Benefits (Stakeholder Quadrants, Quantitative Outlier Insights, Structured 3-Column Benefits Table).
     - Slide 6: Research and References (Statutory & Academic Citations, Competitive Benchmark Matrix with Check/Cross Glyphs, 8-Step Research Pipeline, Demo Links).
2. **Zero "AI-Generated" Aesthetic**:
   - Strictly prohibit generic AI 3D bubbles, floating robotic spheres, or psychedelic gradients.
   - Use clean, authoritative institutional design: crisp vector line diagrams, rounded card containers, native PowerPoint shapes, high-contrast typography, and official hackathon branding.
3. **True Embedded Visuals**:
   - Visual diagrams (architectures, pipelines, chevron flows, tech badges) must be programmatically rendered as high-DPI vector/PNG assets using `matplotlib` / `PIL` and placed with precise millimeter coordinates via `python-pptx`.
4. **Information Density & Factual Grounding**:
   - Retain 100% of technical specifics (protocols, algorithms, latencies, statutory citations, court-admissibility guarantees) without superficial summarizing.

---

## 2. Execution Pipeline

```
[Reference Extraction] -> [Geometry & Color Mapping] -> [Vector Diagram Generation] -> [python-pptx Assembly] -> [Visual Verification]
```

### Stage 1: Reference Layout Extraction
- Convert reference PDF pages to high-resolution PNGs (`pymupdf` at 300 DPI).
- Extract exact coordinate bounding boxes:
  - Top header zone: `y = 0.4"` to `1.2"`
  - Slide body bounds: `left = 0.6"`, `width = 12.13"`, `height = 5.8"`
  - Bottom template banner: `y = 7.0"` to `7.5"`
  - Team identifier oval: Top-left `x = 0.5"`, `y = 0.4"`, `w = 1.8"`, `h = 0.8"`

### Stage 2: Color Palette Harmonization
- Adopt sovereign defense / institutional palette:
  - Background: Pure White (`#FFFFFF`)
  - Primary Title / Accent: Deep Sovereign Navy (`#0B2545` or `#0F3A70`)
  - Secondary Accent / Highlighting: Sovereign Saffron / Amber (`#D97706` / `#F59E0B`)
  - Verification & Success: Emerald Forest (`#059669`)
  - Card & Container Fill: Light Slate / Crisp Grey (`#F8FAFC`, Border `#CBD5E1`)
  - High-Contrast Text: Charcoal Slate (`#0F172A`)

### Stage 3: Visual Diagram Generation (`PIL` & `matplotlib`)
- **Architecture Diagram (Slide 2)**: Hierarchy tree with Users -> Layer Routers -> Modular Feature Cards.
- **Process Flow (Slide 3)**: Crisp horizontal chevron/card flow with phase icons and connection arrows.
- **Tech Stack Grid (Slide 3)**: Categorized technology badges with official brand glyphs.
- **Research Methodology Flow (Slide 6)**: 8-node linear pipeline with sequential connectors.

### Stage 4: Programmatic PPTX Compilation (`python-pptx`)
- Enforce 16:9 widescreen format (`13.333" x 7.5"`).
- Render native shapes:
  - Team Oval Pill with outline.
  - Centered Slide Category Header (`TITLE PAGE`, `IDEA TITLE`, etc.).
  - Bottom Footer Ribbon with `@SIH Idea submission- Template` and Slide Index.
  - Bulleted text boxes with custom paragraph spacing, bold prefix runs, and tight line height.
  - Native tables with alternating row shading, bold headers, and colored status indicators.
  - Callout cards with rounded corners and subtle shadow/borders.

### Stage 5: Verification & Export
- Convert generated `.pptx` slides to images via LibreOffice / PyMuPDF.
- Visually verify against reference slides to ensure 1:1 structural alignment, zero overflow, and pristine visual hierarchy.
