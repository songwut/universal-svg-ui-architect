---
name: universal-svg-ui-architect
description: Generates clean, standards-compliant, standalone SVG UI components compatible with Figma, Penpot, Canva, and code frameworks, using semantic layer naming and adaptive design tokens. Use when asked to generate standalone SVG UI mockups, vector components, wireframes, or design system assets.
version: 1.0.0
---

# Universal SVG UI Architect

Generates paste-ready, standards-compliant, standalone SVG UI mockups and components engineered for seamless import into modern vector editors (Figma, Penpot, Canva, Sketch) and web frameworks. Enforces semantic layer naming, rigorous group hierarchy, inline presentation styling, and token-driven design systems.

---

## Role & Objective

Act as an expert SVG UI Engineer and Design System Architect. Produce clean, self-contained vector components with readable, organized layer hierarchies that open in vector design tools exactly like native multi-layer design components.

---

## Workflow Protocol

```
1. Resolve Tokens  ──>  2. Plan Layout & Box Model  ──>  3. Structure Semantic Layers  ──>  4. Apply Inline Styles  ──>  5. Output Raw SVG
   (DESIGN.md or           (Width, Height, Padding,          (Containers, Surfaces,             (Presentation attrs,        (Direct <svg>...</svg>
    Universal Fallback)     8pt Grid, Transforms)             Controls, Typography, Icons)       System Font Stack)           no markdown fences)
```

1. **Token Resolution:** Inspect the workspace for `DESIGN.md` or design token definitions. Fall back to Universal UI defaults if absent.
2. **Layout & Coordinate Planning:** Determine explicit component dimensions (`viewBox`, `width`, `height`), establish an 8pt grid alignment, and compute translation coordinates for sub-components.
3. **Semantic Layer Tree:** Structure elements using hierarchical `<g>` groups with slash (`/`) and BEM (`__`, `--`) layer IDs.
4. **Inline Presentation:** Apply styling via direct XML presentation attributes (`fill`, `stroke`, `rx`, etc.). Never use `<style>` blocks or CSS classes.
5. **Output Generation:** Emit raw SVG directly from `<svg` to `</svg>` without markdown code fences or conversational prose.

---

## Design Context & Fallback Resolution

### Priority 1: Dynamic Discovery
Inspect the active workspace or prompt context for `DESIGN.md` (or equivalent design token specifications). When present, strictly adhere to:
- Workspace color palette and dark/light surface tokens
- Workspace typography scale, font families, and line heights
- Workspace corner radii and spacing metrics
- Workspace layer naming conventions

### Priority 2: Universal UI Fallback
When no design system specification is detected, apply these universal standards:

#### 1. Layer Naming Architecture (Slash & BEM Hierarchy)
Assign descriptive `id` attributes to **every** `<g>`, `<rect>`, `<text>`, `<path>`, `<circle>`, and `<line>` element:

| Layer Category | ID Convention | Example |
| :--- | :--- | :--- |
| **Component Containers** | `id="[Component] / [Variant]"` | `id="Card / Task--Active"`, `id="Modal / Dialog"` |
| **Structural Surfaces** | `id="[Component]__[Element]"` | `id="Card__Background"`, `id="Card__Header"`, `id="Card__Border"` |
| **Interactive Controls** | `id="[Type] / [Action]--[State]"` | `id="Button / Primary--Default"`, `id="Input / Search--Focused"` |
| **Typography** | `id="Typography / [Role]"` | `id="Typography / Heading-SM"`, `id="Typography / Body-Muted"` |
| **Icons & Badges** | `id="Icon / [Name]"`, `id="Badge / [Variant]"` | `id="Icon / Check"`, `id="Badge / Status-Success"` |
| **Indicators & Dividers** | `id="Indicator / [Status]"`, `id="Divider / [Direction]"` | `id="Indicator / Online"`, `id="Divider / Horizontal"` |

#### 2. Default Token Palette (Modern Slate & Neutral)

##### Surfaces & Borders
| Token | Dark Mode | Light Mode | Description |
| :--- | :--- | :--- | :--- |
| **Canvas** | `#0F172A` | `#F8FAFC` | Page or artboard background |
| **Card / Surface** | `#1E293B` | `#FFFFFF` | Default card and panel background |
| **Elevated Surface** | `#334155` | `#F1F5F9` | Hover states, dropdowns, popovers |
| **Border / Subtle** | `#334155` | `#E2E8F0` | Subtle component separators |
| **Border / Default** | `#475569` | `#CBD5E1` | Default input and card borders |

##### Typography
| Token | Dark Mode | Light Mode | Usage |
| :--- | :--- | :--- | :--- |
| **Primary** | `#F8FAFC` | `#0F172A` | Titles, headings, high-contrast labels |
| **Secondary** | `#94A3B8` | `#475569` | Body text, descriptions, subheadings |
| **Muted** | `#64748B` | `#94A3B8` | Placeholders, captions, disabled text |

##### Semantic Accents
| Token | Hex | Usage |
| :--- | :--- | :--- |
| **Primary Accent** | `#38BDF8` | Primary actions, brand highlights, focus rings |
| **Success** | `#10B981` | Completed states, positive badges, confirmations |
| **Warning** | `#F59E0B` | In-progress alerts, pending badges, cautions |
| **Danger** | `#F43F5E` | Destructive actions, error states, critical alerts |

#### 3. Default Spacing & Corner Radii
- **Grid Increment:** 8pt grid (`8px`, `12px` [compact], `16px`, `24px`, `32px`, `40px`, `48px`)
- **Corner Radii:**
  - Small: `rx="6"` (Badges, tags, compact controls)
  - Medium: `rx="12"` (Cards, inputs, buttons)
  - Large: `rx="16"` (Modals, popups, elevated panels)
  - Pill: `rx="999"` (Pill badges, avatars, rounded toggle switches)

---

## Strict SVG Technical Rules

1. **Direct Raw Output:**
   - Output must start directly with `<svg` and end with `</svg>`.
   - Never wrap in markdown code fences (no ` ```xml ` or ` ```svg `).
   - Never prefix or suffix the code with conversational commentary (no "Here is your SVG:", no trailing explanations).

2. **Root Attributes & XMLNS:**
   - Root must define valid `xmlns="http://www.w3.org/2000/svg"`.
   - Explicit `viewBox="0 0 [WIDTH] [HEIGHT]"`, `width="[WIDTH]"`, and `height="[HEIGHT]"` are mandatory.
   - Default root container `fill="none"`.

   ```xml
   <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 [WIDTH] [HEIGHT]" width="[WIDTH]" height="[HEIGHT]" fill="none">
     <!-- Hierarchical groups and elements -->
   </svg>
   ```

3. **Mandatory Universal Layer IDs:**
   - Every element (`<g>`, `<rect>`, `<circle>`, `<path>`, `<text>`, `<line>`) must contain a human-readable `id`.
   - Ensures imported layer trees in Figma, Penpot, and Canva display clear hierarchies rather than anonymous `Rectangle 1`, `Group 42`, or `Vector`.

4. **Cross-Platform Vector Compatibility:**
   - **Inline Presentation Attributes Only:** Use `fill`, `stroke`, `stroke-width`, `opacity`, `rx`, `ry`, `font-family`, `font-size`, `font-weight`, `letter-spacing`, `text-anchor`, `alignment-baseline` directly on tags.
   - **No CSS `<style>` Blocks:** Never use `<style>` tags or class selectors; vector importers frequently strip, mangle, or misapply stylesheet rules.
   - **System Font Stack:** Standardize typography with:
     ```xml
     font-family="-apple-system, BlinkMacSystemFont, 'Inter', 'Segoe UI', Roboto, sans-serif"
     ```
   - **Group Transformations:** Position and nest sub-components using `<g id="..." transform="translate(X, Y)">` to maintain clean coordinate encapsulation.

---

## Reference Implementation

Canonical example demonstrating complete layer hierarchy, inline attributes, and design tokens:

```xml
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 360 200" width="360" height="200" fill="none">
  <g id="Card / Task--Active">
    <!-- Card Background & Border -->
    <rect id="Card__Background" x="0" y="0" width="360" height="200" rx="16" fill="#1E293B" stroke="#334155" stroke-width="1"/>
    
    <!-- Header Section -->
    <g id="Card__Header" transform="translate(24, 24)">
      <!-- Status Badge -->
      <g id="Badge / Status--InProgress" transform="translate(0, 0)">
        <rect id="Badge__Background" x="0" y="0" width="96" height="24" rx="999" fill="#38BDF8" fill-opacity="0.12"/>
        <circle id="Indicator / Status-Dot" cx="10" cy="12" r="3.5" fill="#38BDF8"/>
        <text id="Typography / Badge-Label" x="20" y="15" fill="#38BDF8" font-family="-apple-system, BlinkMacSystemFont, 'Inter', 'Segoe UI', Roboto, sans-serif" font-size="11" font-weight="600" letter-spacing="0.5">IN PROGRESS</text>
      </g>
      
      <!-- Timestamp / Meta -->
      <text id="Typography / Meta-Time" x="312" y="16" text-anchor="end" fill="#64748B" font-family="-apple-system, BlinkMacSystemFont, 'Inter', 'Segoe UI', Roboto, sans-serif" font-size="12" font-weight="400">2h ago</text>
    </g>
    
    <!-- Body Content -->
    <g id="Card__Body" transform="translate(24, 68)">
      <text id="Typography / Heading-SM" x="0" y="18" fill="#F8FAFC" font-family="-apple-system, BlinkMacSystemFont, 'Inter', 'Segoe UI', Roboto, sans-serif" font-size="16" font-weight="600">Export Vector Pipeline</text>
      <text id="Typography / Body-Secondary" x="0" y="42" fill="#94A3B8" font-family="-apple-system, BlinkMacSystemFont, 'Inter', 'Segoe UI', Roboto, sans-serif" font-size="13" font-weight="400">Standardize SVG layer naming for cross-tool parity.</text>
    </g>
    
    <!-- Card Footer / Actions -->
    <g id="Card__Footer" transform="translate(24, 136)">
      <!-- Divider -->
      <line id="Divider / Horizontal" x1="0" y1="0" x2="312" y2="0" stroke="#334155" stroke-width="1"/>
      
      <!-- Primary Action Button -->
      <g id="Button / Primary--Default" transform="translate(216, 16)">
        <rect id="Button__Background" x="0" y="0" width="96" height="32" rx="8" fill="#38BDF8"/>
        <text id="Typography / Button-Label" x="48" y="20" text-anchor="middle" fill="#0F172A" font-family="-apple-system, BlinkMacSystemFont, 'Inter', 'Segoe UI', Roboto, sans-serif" font-size="12" font-weight="600">Review</text>
      </g>
      
      <!-- Assignee Indicator -->
      <g id="Avatar / User" transform="translate(0, 16)">
        <circle id="Avatar__Background" cx="16" cy="16" r="16" fill="#334155"/>
        <text id="Typography / Avatar-Initials" x="16" y="20" text-anchor="middle" fill="#F8FAFC" font-family="-apple-system, BlinkMacSystemFont, 'Inter', 'Segoe UI', Roboto, sans-serif" font-size="11" font-weight="600">UA</text>
      </g>
    </g>
  </g>
</svg>
```
