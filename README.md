# Gravity Components

Full component showcase for the [Gravity Design System](https://gravity.group.one) — v5.38.6.

## Structure

```
gravity-components/
├── index.html        ← all 35 component cards
├── src/
│   ├── styles.css    ← custom layout & card styles
│   └── main.js       ← interactive JS (accordion, tabs, chips, etc.)
└── .vscode/
    ├── settings.json ← editor config
    └── extensions.json ← recommended extensions
```

## Dev server

```bash
npm install
npm run dev
```

Opens at `http://localhost:5173`

## Adding a component

1. Copy a `<div class="comp-card">` block in `index.html`
2. Paste it inside the right `<div class="comp-grid">` section
3. Replace the `.comp-preview` contents with your Gravity HTML
4. Update `.comp-name`, `.comp-class`, and the `href` on `.comp-docs-link`

## Gravity CDN

All assets use CDN v5.38.6:
```
https://gravity.group-cdn.one/v5.38.6/
```

Icons: `/icons/*.svg`  
Logos: `/logos/*.svg`  
CSS:   `/css/brands/group-one.min.css`  
JS:    `/index.umd.js`

## Components

| Category | Count |
|---|---|
| Components | 21 |
| Form Components | 13 |
| AI Components | 1 |
| **Total** | **35** |
