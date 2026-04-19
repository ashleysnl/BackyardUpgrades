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
  Article-page logic for loading one Markdown file, stripping YAML frontmatter, rendering Markdown, showing related articles, and turning recommended products into affiliate callout cards.

- `content/articles.json`
  Manifest file containing article metadata such as slug, title, category, featured status, read time, deck text, description, meta title, and meta description.

- `content/articles/*.md`
  Article content files in Markdown format with YAML frontmatter and embedded affiliate-tagged product links.

- `about.html`
  Static about page using the shared design system.

- `affiliate-disclosure.html`
  Static affiliate disclosure page.

- `privacy.html`
  Static privacy page.

- `contact.html`
  Static contact page with placeholder launch guidance that still needs a real inbox.

- `robots.txt`
  Crawl rules file currently pointing at the intended production domain.

- `sitemap.xml`
  Static sitemap with homepage, legal pages, and article URLs.

## How content is loaded

The homepage loads article metadata from `content/articles.json`.

The article page:

1. Reads the `slug` query parameter
2. Matches the slug to an entry in `articles.json`
3. Fetches the corresponding Markdown file from `content/articles/<slug>.md`
4. Strips YAML frontmatter from the Markdown file
5. Converts the Markdown into HTML using the lightweight renderer in `assets/article.js`

## Important implementation note

The site should be previewed through a local HTTP server, not by opening the HTML files directly in the browser, because the JavaScript uses `fetch()` to load JSON and Markdown files.

## Suggested future additions

- `favicon` assets
- author or editorial page
- image assets for cards and social sharing
- category landing pages
