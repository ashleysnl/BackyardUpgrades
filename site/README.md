# Backyard Upgrades Site

Static publish-ready article site for the Backyard Upgrades project.

## Current status

This site now includes:

- a styled homepage with article search and category filters
- a reusable article page that loads Markdown content by slug
- 10 publish-ready article files
- affiliate-tagged Amazon links embedded in article content
- supporting pages for about, affiliate disclosure, privacy, and contact
- `robots.txt` and `sitemap.xml`

## Run locally

From the workspace root:

```bash
cd "/Users/AshleySkinner/Documents/00_Engineering/04_Code/53_Affliate Marketing/site"
python3 -m http.server 8000
```

Then open:

- `http://localhost:8000`

Important:

- open the site through a local web server
- do not open `index.html` directly from the filesystem
- the site uses `fetch()` for JSON and Markdown content, so direct file opening will not load the articles

## Structure

- `index.html`
  Homepage with featured content, search, filters, and article cards.

- `article.html`
  Reusable article template that loads article content from the query-string slug.

- `about.html`
  Static about page.

- `affiliate-disclosure.html`
  Static affiliate disclosure page.

- `privacy.html`
  Static privacy page.

- `contact.html`
  Static contact page. Still needs a final real contact email or destination before public launch.

- `assets/styles.css`
  Main visual system and layout styles.

- `assets/app.js`
  Homepage logic for loading and filtering article metadata.

- `assets/article.js`
  Article-page logic for loading Markdown, stripping frontmatter, rendering content, and displaying affiliate product cards.

- `content/articles.json`
  Shared article metadata manifest.

- `content/articles/*.md`
  Markdown article files with YAML frontmatter and embedded affiliate-tagged product links.

- `robots.txt`
  Crawl rules file. Review before launch if the final host is not `https://www.backyardupgrades.com/`.

- `sitemap.xml`
  Static sitemap. Review before launch if the final host is not `https://www.backyardupgrades.com/`.

## Launch notes

Before publishing publicly:

- replace the placeholder contact wording in `contact.html`
- review Amazon search-based affiliate links and upgrade to exact product pages where possible
- confirm `robots.txt` and `sitemap.xml` match the final production domain
- add favicon and brand assets

## Product image authoring

Product images live in:

- `assets/images/products/`
- `content/product-images.json`
- `content/image-sources.json`

Recommended authoring pattern for article product sections:

```text
:::product
name: Product Name
image: ./assets/images/products/category/example-product.jpg
note: One short sentence explaining why this product fits the guide.
cta: Check price on Amazon.ca
url: https://example.com/affiliate-link
:::
```

Notes:

- the renderer supports this block inside article Markdown
- the site also supports standalone Markdown images like `![Alt text](./assets/images/products/...)`
- `content/product-images.json` can override card images, alt text, and support copy without rewriting article Markdown
- `content/image-sources.json` tracks the stock-photo source page for each downloaded image
- if an image file is missing, the article now falls back to the configured product-type image before collapsing the card
- existing list-style recommended-product blocks still work, so older articles do not need to be rewritten immediately

## Deployment

This is a plain static site, so it can be uploaded directly to GitHub and served with GitHub Pages or any static host.
