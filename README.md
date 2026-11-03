# Universal SVG UI Architect

[![Vector Compatible](https://img.shields.io/badge/Vector-Figma%20%7C%20Penpot%20%7C%20Canva%20%7C%20Sketch-6366f1)](#)
[![Format](https://img.shields.io/badge/Format-Raw%20SVG-0ea5e9)](#)
[![Standard](https://img.shields.io/badge/Standard-Agent%20Skills-10b981)](#)

Agent skill and prompt system for generating paste-ready, standards-compliant SVG UI components. Engineered for native layer grouping in vector editors (**Figma, Penpot, Canva, Sketch**) and web frameworks.

---

## Highlights

- **Semantic Layers:** Slash (`/`) and BEM (`__`, `--`) IDs for clean, organized trees in Figma and Penpot.
- **Pure Inline Styling:** 100% XML presentation attributes (`fill`, `stroke`, `rx`). Zero `<style>` blocks or CSS classes to prevent parser stripping.
- **Adaptive Tokens:** Auto-detects workspace `DESIGN.md`; seamlessly falls back to an 8pt Slate & Neutral system.
- **Built-in Validator:** Includes `validate_svg.py` to deterministically verify XML syntax, attributes, and layer naming.

---

## Quick Start

### 1. AI Coding Agents (Claude Code, Antigravity, Cursor)
Reference via [`.agents/plugins/marketplace.json`](file:///Users/melody/Documents/GitHub/universal-svg-ui-architect/.agents/plugins/marketplace.json) or copy the skill folder:
```text
your-project/
├── .agents/plugins/marketplace.json  # Points to ./skills/universal-svg-ui-architect
└── skills/
    └── universal-svg-ui-architect/
        ├── SKILL.md
        └── scripts/validate_svg.py
```
> **Prompt Example:** *"Create a responsive dark-mode analytics KPI card in SVG format."*

### 2. Local LLMs (Ollama, LM Studio, Rapid-MLX)
Copy the content of [`SKILL.md`](file:///Users/melody/Documents/GitHub/universal-svg-ui-architect/skills/universal-svg-ui-architect/SKILL.md) directly into your runner's **System Prompt** configuration.

---

## Validation Script

Validate generated SVGs locally without consuming LLM tokens:
```bash
# Validate file
python3 skills/universal-svg-ui-architect/scripts/validate_svg.py component.svg

# Or validate via pipe
cat component.svg | python3 skills/universal-svg-ui-architect/scripts/validate_svg.py
```

---

## Layer Naming Standard

| Element | ID Pattern | Figma / Penpot Layer View |
| :--- | :--- | :--- |
| **Component Root** | `[Component] / [Variant]` | `Card / Task--Active` |
| **Surface** | `[Component]__[Role]` | `└── Card__Background` |
| **Section** | `[Component]__[Section]` | `└── Card__Header` |
| **Interactive** | `[Type] / [Action]--[State]` | `    └── Button / Primary--Default` |
| **Typography** | `Typography / [Role]` | `    └── Typography / Heading-SM` |
| **Badges / Icons** | `Badge / [Type]`, `Icon / [Name]` | `    └── Badge / Status--Success` |

---

## Design System Tokens

Prioritizes local `DESIGN.md` if present; otherwise defaults to:
- **Surfaces:** Canvas (`#0F172A`), Card (`#1E293B`), Elevated (`#334155`), Border (`#475569`)
- **Typography:** Primary (`#F8FAFC`), Secondary (`#94A3B8`), Muted (`#64748B`)
- **Accents:** Sky (`#38BDF8`), Success (`#10B981`), Warning (`#F59E0B`), Danger (`#F43F5E`)
- **Geometry:** 8pt Grid (`8`, `16`, `24`, `32`), Radii (`6`, `12`, `16`, `999`)

---

## File Structure

```text
universal-svg-ui-architect/
├── skills/
│   └── universal-svg-ui-architect/
│       ├── SKILL.md                  # Skill instructions & system prompt
│       └── scripts/
│           └── validate_svg.py       # SVG standard & layer linter
├── .agents/
│   └── plugins/
│       └── marketplace.json          # Marketplace catalog manifest
├── README.md
└── LICENSE
```

---

## License

[MIT License](file:///Users/melody/Documents/GitHub/universal-svg-ui-architect/LICENSE)
