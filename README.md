# Universal SVG UI Architect

[![Vector Compatible](https://img.shields.io/badge/Vector-Figma%20%7C%20Penpot%20%7C%20Canva%20%7C%20Sketch-6366f1)](#)
[![Format](https://img.shields.io/badge/Format-Raw%20SVG-0ea5e9)](#)
[![Design Tokens](https://img.shields.io/badge/Design%20Tokens-Dynamic%20%7C%20Adaptive-10b981)](#)
[![Compatibility](https://img.shields.io/badge/Compatible-Antigravity%20%7C%20Ollama%20%7C%20Rapid--MLX-f59e0b)](#)

**Universal SVG UI Architect** is a standardized agent skill and prompt system that generates paste-ready, standards-compliant, standalone SVG UI mockups and vector components. 

It is engineered from the ground up for seamless import into modern vector tools (**Figma**, **Penpot**, **Canva**, **Sketch**) and code frameworks. By enforcing semantic layer naming (Slash & BEM conventions), rigorous group nesting, inline presentation attributes, and adaptive design token discovery, imported SVGs display clean, organized layer hierarchies instead of messy, unorganized vector shapes.

---

## Key Features

- **Semantic Layer Architecture:** Uses Slash (`/`) and BEM (`__`, `--`) layer IDs (`id="Card / Task--Active"`, `id="Typography / Heading-SM"`, `id="Button / Primary--Default"`) so your layers panel in Figma, Penpot, and Sketch stays organized and legible.
- **Zero-Style Cross-Platform Compatibility:** Uses pure inline XML presentation attributes (`fill`, `stroke`, `rx`, `transform`) without `<style>` tags or CSS classes. This prevents vector importers (especially Canva and older Figma parsers) from stripping or mangling styles.
- **Adaptive Design Tokens & `DESIGN.md`:** Automatically searches for and applies local `DESIGN.md` tokens. If none are present, it falls back to a modern Slate & Neutral 8pt design system.
- **Direct Paste-Ready Output:** Formats output directly from `<svg>` to `</svg>`, ready to paste or save straight into your design canvas or codebase.
- **Universal Execution:** Runs natively as an AI coding agent skill (Antigravity, Claude Code, Cursor) or directly as a System Prompt in local LLM runtimes (**Rapid-MLX**, **Ollama**, **LM Studio**, **Jan**).

---

## How to Use

### Method 1: Using with AI Coding Agents (Antigravity, Claude Code, Cursor)

If you are using an agentic environment that supports skills and workspace project files:

1. **Workspace Installation:**
   Place this repository or the skill file inside your project's `.agents/skills/` directory:
   ```text
   your-project/
   ├── .agents/
   │   └── skills/
   │       └── universal-svg-ui-architect/
   │           └── SKILL.md
   ```
2. **Execution:**
   Simply prompt your agent naturally:
   > *"Create a responsive dark-mode analytics KPI card in SVG format."*
   > *"Design a user profile settings modal in standalone SVG."*
   
   The agent will automatically trigger `universal-svg-ui-architect` and generate the vector component.

---

### Method 2: Direct System Prompt in Local LLMs (Rapid-MLX, Ollama, LM Studio)

When running local LLMs through apps like **Rapid-MLX**, **Ollama** (Open-WebUI / Web interfaces), **LM Studio**, or **Jan** that do not natively index `.md` workspace files:

1. Open [`SKILL.md`](./SKILL.md).
2. Copy everything starting from `# Role & Objective` down to the end of the file (omit the YAML frontmatter).
3. Paste the copied text directly into the **System Prompt** (or **System**) configuration box in your local LLM runner:
   - **Rapid-MLX:** Paste into the `System Prompt` input field in model settings.
   - **Ollama / Open-WebUI:** Add to your Modelfile under `SYSTEM """..."""` or in chat settings.
   - **LM Studio:** Paste into `System Prompt` under the presets/chat configuration sidebar.
4. **Custom Theming on the Fly:**
   Whenever you want the model to follow a custom design system, simply paste the text of your `DESIGN.md` directly into the chat message alongside your prompt. The model will automatically prioritize your provided tokens over the universal fallback palette!

---

## Design System & Fallback Resolution

```
                  ┌──────────────────────────────┐
                  │ Does DESIGN.md exist /       │
                  │ provided in context?         │
                  └──────────────┬───────────────┘
                                 │
                 YES ────────────┴──────────── NO
                  │                             │
                  ▼                             ▼
       ┌──────────────────────┐      ┌──────────────────────┐
       │ Priority 1:          │      │ Priority 2:          │
       │ Apply DESIGN.md      │      │ Universal Slate      │
       │ Tokens & Palette     │      │ Fallback Standards   │
       └──────────────────────┘      └──────────────────────┘
```

### 1. Dynamic Discovery (`DESIGN.md`)
When a `DESIGN.md` file is present in your workspace (or pasted into your chat prompt), the model automatically matches your:
- Brand colors (surfaces, borders, text, accents)
- Typography scales and font choices
- Corner radii (`rx`) and 8pt spacing grid

#### Example `DESIGN.md` Template
You can drop a file named `DESIGN.md` into your root directory or paste it into your chat:

```markdown
# Design System Tokens

## Colors (Light / Dark)
- Canvas: #09090B / #FAFAFA
- Surface / Card: #18181B / #FFFFFF
- Border: #27272A / #E4E4E7
- Text Primary: #FAFAFA / #09090B
- Text Secondary: #A1A1AA / #71717A
- Accent Primary: #6366F1
- Accent Success: #22C55E
- Accent Danger: #EF4444

## Geometry & Spacing
- Base Grid: 8pt
- Radii: Sm = 6, Md = 10, Lg = 16, Pill = 999
- Typography: Inter, -apple-system, sans-serif
```

### 2. Universal UI Fallback Tokens
If no `DESIGN.md` is provided, the model adheres to modern slate defaults:

- **Surfaces:** Dark Canvas (`#0F172A`), Card (`#1E293B`), Elevated (`#334155`), Border (`#475569`)
- **Typography:** Primary (`#F8FAFC` dark / `#0F172A` light), Secondary (`#94A3B8`), Muted (`#64748B`)
- **Accents:** Primary Sky (`#38BDF8`), Success Emerald (`#10B981`), Warning Amber (`#F59E0B`), Danger Rose (`#F43F5E`)
- **Grid & Radii:** 8pt grid (`8`, `12`, `16`, `24`, `32`), Radii (`6`, `12`, `16`, `999`)

---

## Layer Naming Hierarchy (Slash & BEM)

Every single element is tagged with a human-readable `id`. When imported into vector software, this creates a clean component tree:

| Element Type | ID Pattern | Sample Layer Tree in Figma/Penpot |
| :--- | :--- | :--- |
| **Component Root** | `[Component] / [Variant]` | `Card / Task--Active` |
| **Surface / Background**| `[Component]__[Role]` | `└── Card__Background` |
| **Structural Section** | `[Component]__[Section]` | `└── Card__Header` |
| **Interactive Control** | `[Type] / [Action]--[State]` | `    └── Button / Primary--Default` |
| **Typography** | `Typography / [Role]` | `    └── Typography / Heading-SM` |
| **Badges & Icons** | `Badge / [Type]`, `Icon / [Name]` | `    └── Badge / Status--InProgress` |

---

## Example Prompts

Here are prompt templates you can use with your agent or Local LLM:

### 1. Task Card Component
> "Generate a standalone SVG task card (width 360, height 200) in dark mode. Include a status pill badge 'In Progress', task title, description, user avatar, and an action button."

### 2. Analytics Metric / KPI Card
> "Create a 320x160 metric KPI card showing Monthly Recurring Revenue (\$48,250), an upward growth badge (+12.4%), and a secondary subtitle."

### 3. Navigation Bar
> "Build a modern desktop navbar (width 1200, height 72) in dark mode with a logo container, 4 navigation links (Dashboard, Projects, Analytics, Settings), and a 'New Project' CTA button."

### 4. Interactive Dialog / Modal
> "Generate a 480x280 confirmation modal for 'Delete Deployment' with a danger accent, warning icon, confirmation body text, Cancel button, and Delete button."

---

## Importing into Design Tools

1. **Figma:**
   - Copy the generated `<svg>...</svg>` text directly to your clipboard and press `Cmd + V` / `Ctrl + V` onto any Figma canvas, or save it as `.svg` and drag it in.
   - Expand the layer tree: notice that every layer is named with Slash and BEM conventions, matching native component grouping.
2. **Penpot:**
   - Import the `.svg` file or paste vector elements directly. All coordinates and inline fills will render 1:1.
3. **Canva:**
   - Upload the saved `.svg` file. Because all styling uses inline presentation attributes (no `<style>` tags), Canva will reliably preserve colors, strokes, and border radii.

---

## File Structure

```text
universal-svg-ui-architect/
├── SKILL.md                                      # Core skill definition and system prompt
├── README.md                                     # Usage guide and integration documentation
└── .agents/
    └── skills/
        └── universal-svg-ui-architect/
            └── SKILL.md                          # Symlinked for native workspace agent discovery
```

---

## License

MIT License. Free for personal and commercial use in UI engineering workflows and agent systems.
