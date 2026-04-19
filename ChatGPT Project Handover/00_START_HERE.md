# Backyard Upgrades: ChatGPT Project Handover

This folder is a clean handoff package for continuing the Backyard Upgrades website project inside a ChatGPT Project folder.

## What this project is

Backyard Upgrades is a static content website built to showcase outdoor living articles with a premium visual design. It currently includes:

- A styled homepage with featured sections, article search, and category filters
- A reusable article page that loads Markdown article content
- 10 publish-ready article drafts upgraded from the original Package 1 set
- Affiliate-tagged Amazon links already embedded in the article content
- Supporting trust pages for about, affiliate disclosure, privacy, and contact
- `robots.txt` and `sitemap.xml` already added to the site root

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

- Prepare a GitHub-ready repo wrapper if the project will be published there next
- Replace the placeholder contact wording with a real email or contact method
- Review `robots.txt` and `sitemap.xml` domain values before deployment
- Add favicon and brand assets
- Optionally improve internal links, schema, and richer SEO polish

## Local preview command

```bash
cd "/Users/AshleySkinner/Documents/00_Engineering/04_Code/53_Affliate Marketing/site"
python3 -m http.server 8000
```

Then open `http://localhost:8000`.
