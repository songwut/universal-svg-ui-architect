# Universal SVG UI Architect

[![Vector Compatible](https://img.shields.io/badge/Vector-Figma%20%7C%20Penpot%20%7C%20Canva%20%7C%20Sketch-6366f1)](#)
[![Format](https://img.shields.io/badge/Format-Raw%20SVG-0ea5e9)](#)
[![Tokens](https://img.shields.io/badge/Tokens-Tailwind%20Semantic-38bdf8)](#)
[![Standard](https://img.shields.io/badge/Standard-Agent%20Skills-10b981)](#)

Agent skill and prompt system for generating paste-ready, standards-compliant SVG UI components. Engineered for seamless import into vector editors (**Figma, Penpot, Canva, Sketch**) while preserving Tailwind-mapped semantic tokens for automated UI-to-code pipelines.

---

## Highlights

- **Dual-Layer Architecture:** Combines clean Kebab-case `id` and scoped Tailwind semantic tokens (`class="bg-surface text-primary border-default"`) for AI code generators with inline XML presentation attributes (`fill`, `stroke`, `rx`) for pixel-perfect vector import.
- **Zero-Shot Deterministic Geometry:** Enforces `dominant-baseline="central"`, isolated local `(0,0)` origins with `<g transform="translate(X, Y)">`, and integer 8pt grid snapping—eliminating layout drift without post-generation validation scripts.
- **Adaptive Design Context:** Automatically consumes a custom `DESIGN.md` when uploaded in the workspace, or dynamically synthesizes a domain-specific token palette with an inline notification header.

---

## Quick Start

### 1. AI Coding Agents (Claude Code, Antigravity, Cursor)
Reference via `.agents/plugins/marketplace.json` or copy the skill folder into your workspace:
```text
your-project/
├── DESIGN.md                         # (Optional) Custom design tokens
├── .agents/plugins/marketplace.json  # Points to ./skills/universal-svg-ui-architect
└── skills/
    └── universal-svg-ui-architect/
        └── SKILL.md
```
> **Prompt Example:** *"Create a dark-mode SaaS deployment status card in SVG format."*

### 2. Local LLMs (Ollama, LM Studio, Rapid-MLX)
Copy the content of `SKILL.md` directly into your runner's **System Prompt** configuration.

---

## Dual-Layer Semantic Standard

Every SVG element carries both architectural design tokens and rendered presentation values:

| UI Element Role | `id` (Kebab-case) | `class` (Scoped Semantic Tokens) | Inline Attributes (Vector Render) |
| :--- | :--- | :--- | :--- |
| **Card Surface** | `id="card-bg"` | `class="bg-surface border-default rounded-lg"` | `fill="#0F172A" stroke="#1E293B" rx="12"` |
| **Elevated Panel** | `id="panel-bg"` | `class="bg-surface-raised border-subtle rounded-md"` | `fill="#1E293B" stroke="#334155" rx="8"` |
| **Primary Button** | `id="btn-primary-bg"` | `class="bg-primary rounded-md"` | `fill="#38BDF8" rx="8"` |
| **Heading Text** | `id="text-title"` | `class="text-primary font-semibold"` | `fill="#F8FAFC" font-size="16" font-weight="600"` |
| **Muted Text** | `id="text-meta"` | `class="text-muted font-regular"` | `fill="#64748B" font-size="12" font-weight="400"` |
| **Status Badge** | `id="badge-success-bg"` | `class="bg-status-success/15 text-status-success rounded-full"` | `fill="#10B981" fill-opacity="0.15" rx="999"` |

---

## Design Token Resolution

1. **Custom (`DESIGN.md`):** Upload or place `DESIGN.md` in your workspace to enforce your exact brand palette, typography scale, and spacing tokens.
2. **Contextual Auto-Gen:** If `DESIGN.md` is absent, the skill automatically generates a cohesive design system tailored to your prompt's domain and adds an inline notice:
   ```xml
   <!-- [Token Mode: Auto-Generated for <Context/Theme> | Upload DESIGN.md to use custom tokens] -->
   ```

---

## File Structure

```text
universal-svg-ui-architect/
├── skills/
│   └── universal-svg-ui-architect/
│       └── SKILL.md                  # Skill instructions & deterministic rules
├── .agents/
│   └── plugins/
│       └── marketplace.json          # Marketplace catalog manifest
├── README.md
└── LICENSE
```

---

## License

MIT License