# Backyard Upgrades

Static affiliate-ready editorial site for backyard buying guides and outdoor living content.

## Project structure

- `site/` live static website
- `ChatGPT Project Handover/` project continuity and handoff docs
- `Codex Handoff/` original source packages used to build and upgrade the site

GitHub Pages note:

- the repo root includes a small `index.html` redirect so the Pages URL forwards into `site/`

## Local preview

```bash
cd site
python3 -m http.server 8000
```

Then open `http://localhost:8000`.

## Notes

- No framework, build step, backend, or package manager
- Designed to stay lightweight and GitHub Pages friendly
- Product image support uses static assets in `site/assets/images/products/`
