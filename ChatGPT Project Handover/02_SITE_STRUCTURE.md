# Site Structure

## Root working folder

- `/Users/AshleySkinner/Documents/00_Engineering/04_Code/53_Affliate Marketing/site`

## File map

- `index.html`
  Homepage with hero section, featured cards, article search, category filters, and article grid.

- `article.html`
  Reusable article template page. Loads an article by `slug` from the query string and applies per-article metadata in the page head.

- `assets/styles.css`
  Main design system and page styling.

- `assets/app.js`
  Homepage logic for loading `content/articles.json`, rendering cards, search, and category filtering.

- `assets/article.js`
  Article-page logic for loading one Markdown file, stripping YAML frontmatter, rendering Markdown, showing related articles, turning recommended products into affiliate callout cards, and resolving product-image fallbacks.

- `content/articles.json`
  Manifest file containing article metadata such as slug, title, category, featured status, read time, deck text, description, meta title, and meta description.

- `content/articles/*.md`
  Article content files in Markdown format with YAML frontmatter and embedded affiliate-tagged product links.

- `content/product-images.json`
  Product manifest used to map article product names to local images, affiliate URLs, supporting copy, and fallback keys. The current system supports both generic category fallbacks and product-specific image overrides.

- `content/image-sources.json`
  Source log for the reuse-safe product-type photography stored locally in the site.

- `about.html`
  Static about page using the shared design system.

- `affiliate-disclosure.html`
  Static affiliate disclosure page.

- `privacy.html`
  Static privacy page.

- `robots.txt`
  Crawl rules file currently aligned to the GitHub Pages project URL.

- `sitemap.xml`
  Static sitemap with homepage, legal pages, and article URLs for the current GitHub Pages deployment.

## How content is loaded

The homepage loads article metadata from `content/articles.json`.

The article page:

1. Reads the `slug` query parameter
2. Matches the slug to an entry in `articles.json`
3. Fetches the corresponding Markdown file from `content/articles/<slug>.md`
4. Strips YAML frontmatter from the Markdown file
5. Converts the Markdown into HTML using the lightweight renderer in `assets/article.js`
6. Resolves product-card imagery and fallback assets from `content/product-images.json`

## Product image note

The site now has a mixed image strategy:

- product-specific images for key affiliate recommendations
- category-level fallback images when a product-specific image is unavailable

That means future content updates should prefer adding a dedicated product image first, then fall back to the broader category image only when necessary.

## Important implementation note

The site should be previewed through a local HTTP server, not by opening the HTML files directly in the browser, because the JavaScript uses `fetch()` to load JSON and Markdown files.

## Suggested future additions

- `favicon` assets
- author or editorial page
- custom social-sharing assets
- category landing pages
