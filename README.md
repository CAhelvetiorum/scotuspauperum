# Guillermus Gorris, *Scotus pauperum* (Toulouse 1486) — edition & translation

Static GitHub Pages site (no build step) presenting the Latin text and an English translation in parallel
columns, with the critical apparatus in the margins (footnotes on narrow screens).

- Site: `docs/` (set GitHub Pages → *Deploy from branch* → `/docs`).
- Text: `docs/text/{latin,english}/NNN.md`; sections listed in `docs/text/manifest.json`.
- Apparatus: `docs/notes/notes.json`.
- Conventions: [EDITORIAL.md](EDITORIAL.md).
- Helper scripts (scan cropping, note generation): `work/`.

Local preview: `cd docs && python3 -m http.server 8000`, then open http://localhost:8000/.
