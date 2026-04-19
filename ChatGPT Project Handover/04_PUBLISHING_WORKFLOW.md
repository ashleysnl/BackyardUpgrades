# Publishing Workflow

## Local workflow

1. Edit article Markdown files in `site/content/articles/`
2. Update article metadata in `site/content/articles.json` if titles, decks, or categories change
3. Run the local preview server:

```bash
cd "/Users/AshleySkinner/Documents/00_Engineering/04_Code/53_Affliate Marketing/site"
python3 -m http.server 8000
```

4. Check homepage and several article pages in the browser

## Before public launch

- Review copy for factual accuracy and consistency
- Add site icons and brand assets
- Confirm all internal links and article slugs work
- Replace the remaining `Garden Hose Timer` search link if an approved exact direct product URL becomes available
- Update `robots.txt`, `sitemap.xml`, and canonical URLs only if the final host changes away from the current GitHub Pages project URL
- Decide whether to keep the Google Fonts dependency or self-host fonts later

## GitHub preparation checklist

- Repository is already initialized and pushed to GitHub
- GitHub Pages project-path behavior is already working
- Keep relative URLs intact when editing content or templates
- If a custom domain is added later, update crawl files, canonicals, and any hardcoded host references in one pass

## Suggested next implementation phases

### Phase 1

Add favicon assets, tighten article-to-article internal links, and confirm the remaining unfinished product link decision.

### Phase 2

Improve launch polish with favicon assets, internal linking, and optional schema.

### Phase 3

If a custom domain is added, update host-sensitive files and confirm path behavior again.

### Phase 4

Expand the content library and add supporting navigation like category landing pages or featured collections.
