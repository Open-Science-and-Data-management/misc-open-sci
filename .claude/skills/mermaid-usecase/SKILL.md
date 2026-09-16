---
name: mermaid-usecase
description: >
  Write valid Mermaid use case diagrams (`usecase-beta`, Mermaid 12+). Use this
  skill whenever the user asks for a use case diagram, UML use case diagram,
  actor/system interaction diagram, or any diagram in .md/.mmd files that
  starts with `usecase-beta` — including PlantUML use case diagrams being
  converted to Mermaid. Also use it when a `usecase-beta` diagram fails to
  render or errors, since this syntax has many easy-to-hit parse traps.
---

# Mermaid Use Case Diagrams

Use case diagrams require **Mermaid v12.0.0+** and the `usecase-beta` keyword.
The syntax is close to flowchart but has strict rules that fail silently or
with confusing errors. Full grammar, all operators, styling, and the complete
PlantUML migration list: read `references/usecase-syntax.md` when you need a
feature not covered below (actor variants, JSON tables, edge styling,
animation, colorScheme).

## Minimal correct diagram

```mermaid
usecase-beta
direction LR
actor Customer("Customer")
systemBoundary "Order system"
  Checkout("Place order")
end
Customer --> Checkout
```

## Core grammar

- First line: `usecase-beta`. One statement per physical line — no semicolons.
- `direction`: `TD`/`TB`/`BT`/`LR`/`RL`.
- Actor: `actor ID` or `actor ID("Label")`. IDs match `[A-Za-z0-9_]+`.
- Use case: `ID("Label")` = ellipse, `ID[Label]` = rectangle. A quoted
  declaration `"Reset password"` (no ID) gets a deterministic ID.
- **Every actor must have an explicit `actor` declaration** somewhere —
  position in a relationship never implies an actor. Undeclared relationship
  endpoints become ellipse use cases.
- Boundary: `systemBoundary ID["Title"]` … `end`. One level deep — only actor
  and use case declarations inside. All relationships, notes, classes stay at
  top level.
- Comments: `%%` whole-line only. `//` and `#` are NOT comments.

## Relationships

| Intent | Operator | Example |
|---|---|---|
| Association | `--`, `-->`, `<--`, `--o`, `--x`, `o--`, `x--` | `Customer --> Checkout` |
| Include (source includes target) | `..> : include` | `Checkout ..> : include Payment` |
| Extend (source extends base) | `..> : extend` | `Coupon ..> : extend Checkout` |
| Generalization (specialized → general) | `--\|>` | `Admin --\|> Person` |

- Labelled association: `User -- "label" --> Login`. A label containing the
  word "include"/"extend" is still an association — only `..> : include` /
  `..> : extend` carry UML semantics.
- Extra dashes lengthen an edge: `A ---> B`. Not allowed on `..>`, `--o`,
  `--x`, `--|>`.
- Notes: `note for ID "text"` or Markdown form `` note for ID "`text`" ``
  (physical newlines allowed inside backticks). One target, no placement
  keywords.

## Parse traps (these fail or render wrong)

- `\n` in labels prints literally — use a Markdown string with a real newline:
  `` Reset("`Reset
  password`") ``.
- Backslash never escapes: `A("Paren \( x")` shows the `\`. Write the char
  directly or use entity codes `#quot; #39; #40; #41; #91; #93; #96;`.
- Reserved in unquoted labels: `()[]{}` quotes and the sequences `--`, `-->`,
  `<--`, `--o`, `--x`, `--|>`, `..>`, `:::`, `@{`, `<<`. Quote the label or use
  entity codes.
- Styling is `classDef`/`class`/`style`/`:::` only. Actor metadata keys like
  `fillColor`, `strokeColor` are **errors**. Valid actor metadata: only
  `type: hollow|awesome`, `icon: "pack:name"`, `business: true`, plus one
  `<<Stereotype>>`.
- PlantUML constructs that are parse errors: `as` aliases, `skinparam`,
  `left/right/up/down` hints, note placement keywords, standalone/multi-target
  notes, separators, `newpage`, nested boundaries.

## Styling quick form

```mermaid
usecase-beta
actor Customer:::external
Checkout("Checkout"):::critical
Customer --> Checkout
classDef external stroke:#7f8ea3
classDef critical stroke:#c33,stroke-width:3px
```

Hardcoded `fill` breaks in dark themes — pair it with `color`:
`classDef system fill:#f8f8ff,color:#333`.

## Workflow

1. Collect actors, use cases, boundaries, and which relationships are include/
   extend/generalization vs plain association.
2. Write the diagram; give every actor an explicit declaration and use stable
   explicit IDs for anything referenced more than once.
3. Add `accTitle:` / `accDescr` for accessibility when embedding in docs.
4. Verify before delivering: render with `npx -y @mermaid-js/mermaid-cli -i
   in.mmd -o out.svg` (needs v12+ of mermaid under the hood) or paste into the
   Mermaid live editor. A syntax-correct-looking diagram can still fail —
   verify, don't assume.
