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
- Replace the placeholder contact wording with a real email or contact path
- Review Amazon search-link URLs and upgrade them to exact product pages where possible
- Update `robots.txt` and `sitemap.xml` if the final host is not `https://www.backyardupgrades.com/`
- Decide whether to keep the Google Fonts dependency or self-host fonts later

## GitHub preparation checklist

- Create a Git repository at the workspace root or around the `site/` folder
- Add a top-level `README.md`
- Add a `.gitignore`
- Decide whether GitHub Pages should publish from the repo root or a dedicated branch/folder
- If using a project site path on GitHub Pages, verify relative URLs still behave as expected

## Suggested next implementation phases

### Phase 1

Prepare the repo for GitHub, add a root README, and decide the final deployment target.

### Phase 2

Improve launch polish with favicon assets, real contact details, internal linking, and optional schema.

### Phase 3

Deploy to GitHub Pages or another static host and confirm path behavior.

### Phase 4

Expand the content library and add supporting navigation like category landing pages or featured collections.
