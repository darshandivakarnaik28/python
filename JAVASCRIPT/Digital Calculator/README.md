# 16. Digital Calculator

A fully featured, semantic, and highly responsive **Digital Calculator** built using vanilla HTML, CSS, and JavaScript. This application supports basic arithmetic operations, dynamic calculation history logs, explicit keyboard inputs, robust error handling, and persistent data storage across browser reboots.

---

## 🚀 Features

### Core Calculator Mechanics
- **Number Buttons Functionality**: Standard digits (`0-9`) with visual click behaviors.
- **Operators Functionality**: Essential operators (`+`, `-`, `*`, `/`) with structural evaluation logic.
- **Equals Logic**: Multi-layered robust math parsing handling simple and chained workflows safely.
- **Clear & Delete Handling**: Complete terminal flushing (`AC`) alongside itemized backspace tracking (`DEL`).
- **Decimal Precision Parsing**: Smart monitoring to prevent multiple isolated decimal points within single operational operands.
- **Error Handling Architecture**: Graceful catching of edge cases (e.g., zero-division limits, malformed grammar inputs) without freezing app state.

### Modern Additions
- **Keyboard Input Interactivity**: Global event captures converting keystrokes directly into equivalent button configurations.
- **Persistent History Monitoring**: Logging operations inside a dedicated workspace, equipped with individual entry deletion, full purging, and structural session caching using browser **Local Storage**.
- **Responsive Adaptive Interface**: Crafted utilizing explicit **Flexbox** structural roots combined with tight mathematical **CSS Grid** alignments optimized uniformly across mobile, tablet, and widescreen viewports.

---

## 🗂️ Project Structure

```text
digital-calculator/
├── index.html
├── style.css
└── app.js
```

---

## 🛠️ Requirements Alignment Tracker

### 1. HTML Requirements Met
- `<header>`: Present with semantic app branding and metadata details.
- `<main>`: Core layout engine capturing layout wrapper frames.
- `<form>`: Realized as a non-submitting mathematical processing engine wrapper capturing structural numerical data.
- `<input>`: Dynamic, readonly calculation display window providing semantic access for calculation flows.
- `<select>`: Adaptive theme/history context configuration module natively handling local options.
- `<button>`: Formatted precisely for grid layouts, complete with aria-labels.
- **Semantic Lists/Tables**: Dedicated chronological calculation history logs arranged cleanly inside real lists.
- **Form Fields Labels**: Fully accessible visual/hidden text combinations tracking critical calculation states safely.

### 2. CSS Requirements Met
- **Flexbox Engine**: Powers macro setups, body balancing, header structural alignment, and list distributions.
- **CSS Grid Architecture**: Forms the underlying 4x5 button matrix framework providing pixel-perfect calculations.
- **Fluid Design Engine**: Scaled gracefully between small devices and high-density widescreen workspaces using responsive media query breakouts.
- **Hover/Focus Interactions**: Explicit focus state outlining and transform-scaled interactive response cues across interactive surfaces.

### 3. JavaScript Requirements Met
- **Modular Event Listeners**: Complete semantic layout mapping using targeted functional blocks.
- **Data Validation Handlers**: Comprehensive defensive checks identifying empty states, continuous multi-operators, or zero divisions.
- **Persistent State Controllers**: Pure CRUD operations (`Add` history entry, `Delete` entry, `Clear All` entries, `Render` lists) seamlessly bound to browser local memory keys.

---

## 📝 Usage & Operational Flow

1. **Initialize App**: Launching the workspace reads previous history elements dynamically out of Local Storage.
2. **Execute Calculations**: Tap layout buttons or type expressions manually on a hardware keyboard.
3. **Analyze Results**: Tapping `=` maps outputs swiftly onto the main operational viewport display.
4. **History Archiving**: Finalized statements automatically generate an append log item sent to the secondary view pane.
5. **Manage History**: Users can select filtering settings, delete specific lines sequentially, or execute complete wipe loops that update Local Storage automatically.
