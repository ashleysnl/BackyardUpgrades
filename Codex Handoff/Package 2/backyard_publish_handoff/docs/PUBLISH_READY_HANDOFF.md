# Backyard Upgrades Publish-Ready Handoff

This package is designed to help Codex or a developer take the current Backyard Upgrades project from draft status to launch-ready status.

## Included in this package

- 10 rewritten publish-ready article markdown files
- Enriched `articles.json` metadata file
- Product mapping CSV with affiliate-tagged Amazon Canada URLs
- Draft legal/trust page copy
- Launch checklist and implementation notes

## Important note on affiliate links

The product map includes two affiliate URL types:

1. `direct_product` — exact Amazon Canada product pages where a retrievable product URL was available.
2. `search_link` — Amazon Canada affiliate-tagged search URLs where the exact Canada product page could not be verified cleanly from the browsing environment.

Search links are usable for handoff and staging, but exact product-page replacements should be made during final QA where possible.

## Required Codex tasks

1. Replace existing article markdown files with the versions in `content/articles/`.
2. Merge the supplied `data/articles.json` fields into the live `content/articles.json`.
3. Replace affiliate placeholders with product callout blocks using `data/article_product_map.csv`.
4. Add supporting pages:
   - about
   - affiliate disclosure
   - privacy
   - contact
5. Add `robots.txt` and `sitemap.xml`.
6. Check all article slugs and internal links.
7. Confirm relative paths work for GitHub Pages.

## Suggested article callout pattern

Use a clean card block with:
- product name
- 1-sentence why-it-fits note
- button label such as “Check price on Amazon”
- disclosure line near the CTA or in page chrome

## Minimum launch QA

- no placeholder affiliate links remain
- article filenames match metadata slugs
- legal pages are linked in header or footer
- homepage cards show clean decks/excerpts
- pages load from static hosting with no build step
- search and filters still work
