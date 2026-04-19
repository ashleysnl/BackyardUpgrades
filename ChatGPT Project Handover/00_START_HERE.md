# Backyard Upgrades: ChatGPT Project Handover

This folder is a clean handoff package for continuing the Backyard Upgrades website project inside a ChatGPT Project folder.

## What this project is

Backyard Upgrades is a static content website built to showcase outdoor living articles with a premium visual design. It currently includes:

- A styled homepage with featured sections, article search, and category filters
- A reusable article page that loads Markdown article content
- 10 publish-ready affiliate articles upgraded from the original handoff packages
- Affiliate-tagged Amazon product links embedded in article content and product cards
- A lightweight product-image system with local assets, per-product image mapping, and manifest-driven fallbacks
- Supporting trust pages for about, affiliate disclosure, and privacy
- `robots.txt` and `sitemap.xml` already aligned to the current GitHub Pages deployment

## Where the working site lives

- Site root: `/Users/AshleySkinner/Documents/00_Engineering/04_Code/53_Affliate Marketing/site`
- Main homepage: `/Users/AshleySkinner/Documents/00_Engineering/04_Code/53_Affliate Marketing/site/index.html`
- Article template: `/Users/AshleySkinner/Documents/00_Engineering/04_Code/53_Affliate Marketing/site/article.html`
- Article manifest: `/Users/AshleySkinner/Documents/00_Engineering/04_Code/53_Affliate Marketing/site/content/articles.json`
- Article Markdown files: `/Users/AshleySkinner/Documents/00_Engineering/04_Code/53_Affliate Marketing/site/content/articles/`

## Best order for a new ChatGPT session

1. Read `01_PROJECT_SUMMARY.md`
2. Read `02_SITE_STRUCTURE.md`
3. Read `03_CONTENT_INVENTORY.md`
4. Read `04_PUBLISHING_WORKFLOW.md`
5. Read `site/README.md` for the current live-site structure
6. Use `05_CHATGPT_PROMPTS.md` to continue the next phase quickly

## Immediate priorities

- Add favicon and brand assets
- Tighten internal links between related articles inside article body copy
- Replace the remaining hose-timer search link with an approved exact product URL if one becomes available
- Improve article-level SEO/share behavior if the site needs stronger organic search support later
- Re-check crawl files and canonicals only if the host changes away from GitHub Pages
- Optionally improve internal links, schema, and richer SEO polish

## Local preview command

```bash
cd "/Users/AshleySkinner/Documents/00_Engineering/04_Code/53_Affliate Marketing/site"
python3 -m http.server 8000
```

Then open `http://localhost:8000`.
