const manifestUrl = "./content/articles.json";
const productManifestUrl = "./content/product-images.json";

const titleEl = document.querySelector("#article-title");
const deckEl = document.querySelector("#article-deck");
const categoryEl = document.querySelector("#article-category");
const readTimeEl = document.querySelector("#article-readtime");
const bodyEl = document.querySelector("#article-body");
const relatedEl = document.querySelector("#related-articles");
const metaDescriptionEl = document.querySelector("#meta-description");
const metaOgTitleEl = document.querySelector("#meta-og-title");
const metaOgDescriptionEl = document.querySelector("#meta-og-description");
const metaOgUrlEl = document.querySelector("#meta-og-url");
const canonicalLinkEl = document.querySelector("#canonical-link");

const params = new URLSearchParams(window.location.search);
const slug = params.get("slug");

async function init() {
  if (window.location.protocol === "file:") {
    bodyEl.innerHTML = `
      <div class="empty-state">
        <p class="eyebrow">Local preview required</p>
        <h3>This article needs to be opened through a local web server.</h3>
        <p>Open the <code>site</code> folder in Terminal and run <code>python3 -m http.server 8000</code>, then visit <code>http://localhost:8000</code>.</p>
      </div>
    `;
    return;
  }

  const [articlesResponse, productManifestResponse] = await Promise.all([
    fetch(manifestUrl),
    fetch(productManifestUrl)
  ]);
  const articles = (await articlesResponse.json()).map((entry) => ({
    ...entry,
    categoryLabel: entry.categoryLabel || entry.category
  }));
  const productImageIndex = buildProductImageIndex(await productManifestResponse.json());
  const article = articles.find((entry) => entry.slug === slug) || articles[0];

  titleEl.textContent = article.title;
  deckEl.textContent = article.deck;
  categoryEl.textContent = article.categoryLabel;
  readTimeEl.textContent = article.readTime;
  document.title = article.metaTitle || `${article.title} | Backyard Upgrades`;
  if (metaDescriptionEl) {
    metaDescriptionEl.content = article.metaDescription || article.description || article.deck;
  }
  if (metaOgTitleEl) {
    metaOgTitleEl.content = article.metaTitle || `${article.title} | Backyard Upgrades`;
  }
  if (metaOgDescriptionEl) {
    metaOgDescriptionEl.content = article.metaDescription || article.description || article.deck;
  }
  const canonicalUrl = new URL(`./article.html?slug=${encodeURIComponent(article.slug)}`, window.location.href).toString();
  if (metaOgUrlEl) {
    metaOgUrlEl.content = canonicalUrl;
  }
  if (canonicalLinkEl) {
    canonicalLinkEl.href = canonicalUrl;
  }

  const markdownResponse = await fetch(`./content/articles/${article.slug}.md`);
  const markdown = stripFrontmatter(await markdownResponse.text());
  bodyEl.innerHTML = renderMarkdown(markdown, article.slug, productImageIndex);
  attachImageFallbacks(bodyEl);

  const related = articles
    .filter((entry) => entry.slug !== article.slug && entry.category === article.category)
    .slice(0, 3);

  relatedEl.innerHTML = related
    .map(
      (entry) => `
        <a class="related-item" href="./article.html?slug=${encodeURIComponent(entry.slug)}">
          <span>${entry.categoryLabel}</span>
          <strong>${entry.title}</strong>
        </a>
      `
    )
    .join("");
}

function renderMarkdown(markdown, articleSlug, productImageIndex) {
  const lines = markdown.split("\n");
  const blocks = [];
  let paragraph = [];
  let listItems = [];
  let orderedItems = [];
  let inRecommendedProducts = false;
  let productBlock = null;
  let inHtmlComment = false;

  const flushParagraph = () => {
    if (!paragraph.length) {
      return;
    }
    blocks.push(`<p>${formatInline(paragraph.join(" "))}</p>`);
    paragraph = [];
  };

  const flushList = () => {
    if (!listItems.length) {
      return;
    }
    blocks.push(
      `<ul>${listItems.map((item) => `<li>${formatInline(item)}</li>`).join("")}</ul>`
    );
    listItems = [];
  };

  const flushOrderedList = () => {
    if (!orderedItems.length) {
      return;
    }
    blocks.push(
      `<ol>${orderedItems.map((item) => `<li>${formatInline(item)}</li>`).join("")}</ol>`
    );
    orderedItems = [];
  };

  for (const line of lines) {
    const trimmedLine = line.trim();

    if (inHtmlComment) {
      if (trimmedLine.includes("-->")) {
        inHtmlComment = false;
      }
      continue;
    }

    if (trimmedLine.startsWith("<!--")) {
      if (!trimmedLine.includes("-->")) {
        inHtmlComment = true;
      }
      continue;
    }

    if (productBlock) {
      if (trimmedLine === ":::") {
        flushParagraph();
        flushList();
        flushOrderedList();
        blocks.push(renderProductBlock(productBlock, articleSlug, productImageIndex));
        productBlock = null;
        continue;
      }

      const separatorIndex = line.indexOf(":");
      if (separatorIndex !== -1) {
        const key = line.slice(0, separatorIndex).trim().toLowerCase();
        const value = line.slice(separatorIndex + 1).trim();
        if (key && value) {
          productBlock[key] = value;
        }
      }
      continue;
    }

    if (!trimmedLine) {
      flushParagraph();
      flushList();
      flushOrderedList();
      continue;
    }

    if (line.startsWith("# ")) {
      flushParagraph();
      flushList();
      flushOrderedList();
      continue;
    }

    if (line.startsWith("## ")) {
      flushParagraph();
      flushList();
      flushOrderedList();
      const heading = line.replace("## ", "");
      inRecommendedProducts = heading.toLowerCase() === "recommended products";
      blocks.push(`<h2>${formatInline(heading)}</h2>`);
      continue;
    }

    if (line.startsWith("### ")) {
      flushParagraph();
      flushList();
      flushOrderedList();
      blocks.push(`<h3>${formatInline(line.replace("### ", ""))}</h3>`);
      continue;
    }

    if (trimmedLine === ":::product") {
      flushParagraph();
      flushList();
      flushOrderedList();
      productBlock = {};
      continue;
    }

    if (line.startsWith("![")) {
      flushParagraph();
      flushList();
      flushOrderedList();
      blocks.push(renderStandaloneImage(line));
      continue;
    }

    if (line.startsWith("- ")) {
      flushParagraph();
      flushOrderedList();
      if (inRecommendedProducts) {
        blocks.push(renderRecommendedProduct(line.slice(2), articleSlug, productImageIndex));
        continue;
      }
      listItems.push(line.slice(2));
      continue;
    }

    if (/^\d+\.\s/.test(line)) {
      flushParagraph();
      flushList();
      orderedItems.push(line.replace(/^\d+\.\s/, ""));
      continue;
    }

    if (line === "Best for:" || line === "Pros:" || line === "Cons:" || line === "Potential downside:" || line === "Why beginners like it:" || line === "Why they help:" || line === "Why they fit a tight budget:" || line === "Best for:" || line === "The most effective cozy-backyard setups usually include three layers:") {
      flushParagraph();
      flushList();
      flushOrderedList();
      blocks.push(`<p class="label">${formatInline(line)}</p>`);
      continue;
    }

    paragraph.push(line.trim());
  }

  flushParagraph();
  flushList();
  flushOrderedList();
  return blocks.join("");
}

function renderRecommendedProduct(text, articleSlug, productImageIndex) {
  const match = text.match(/\*\*(.+?)\*\*\s+—\s+Affiliate link:\s+\[([^\]]+)\]\(([^)]+)\)/);
  if (!match) {
    return `<ul><li>${formatInline(text)}</li></ul>`;
  }
  const [, productName, linkLabel, href] = match;
  const product = resolveProductEntry(productImageIndex, articleSlug, productName);
  if (product) {
    return renderProductCard({
      productName,
      href,
      ctaLabel: linkLabel,
      note: product.supportingCopy,
      image: product.image,
      alt: product.alt,
      fallback: resolveFallbackEntry(productImageIndex, product.fallbackKey)
    });
  }

  return `
    <div class="affiliate-card">
      <div>
        <p class="panel-label">Product Pick</p>
        <strong>${productName}</strong>
        <p>Affiliate-supported recommendation selected for this guide.</p>
      </div>
      <a class="button primary" href="${href}" target="_blank" rel="noopener noreferrer sponsored">
        ${linkLabel}
      </a>
    </div>
  `;
}

function renderProductBlock(block, articleSlug, productImageIndex) {
  const product = block.name ? resolveProductEntry(productImageIndex, articleSlug, block.name) : null;
  return renderProductCard({
    productName: block.name || product?.productName || "Recommended Product",
    href: block.url || product?.affiliateUrl || "#",
    ctaLabel: block.cta || "Check price on Amazon",
    note: block.note || product?.supportingCopy,
    image: product?.image || block.image,
    alt: block.alt || product?.alt || `${block.name || "Product"} lifestyle photo`,
    fallback: resolveFallbackEntry(productImageIndex, product?.fallbackKey || block.fallback)
  });
}

function renderProductCard({ productName, href, ctaLabel, note, image, alt, fallback }) {
  const imageMarkup = image ? renderProductImage(image, alt || productName || "Product image", fallback) : "";
  const noteMarkup = note ? `<p>${formatInline(note)}</p>` : "";
  const nameMarkup = productName ? `<strong>${formatInline(productName)}</strong>` : "";

  return `
    <section class="product-card${imageMarkup ? "" : " product-card--missing-image"}">
      <div class="product-card__media">
        ${imageMarkup}
      </div>
      <div class="product-card__content">
        <p class="panel-label">Recommended Product</p>
        ${nameMarkup}
        ${noteMarkup}
        <a class="button primary" href="${escapeAttribute(href)}" target="_blank" rel="noopener noreferrer sponsored">
          ${formatInline(ctaLabel)}
        </a>
      </div>
    </section>
  `;
}

function renderProductImage(src, alt, fallback) {
  const fallbackAttributes = fallback
    ? ` data-fallback-src="${escapeAttribute(fallback.image)}" data-fallback-alt="${escapeAttribute(
        fallback.alt || alt
      )}"`
    : "";
  return `
    <img
      src="${escapeAttribute(src)}"
      alt="${escapeAttribute(alt)}"
      loading="lazy"
      decoding="async"${fallbackAttributes}
    />
  `;
}

function renderStandaloneImage(line) {
  const match = line.match(/^!\[([^\]]*)\]\(([^)]+)\)$/);
  if (!match) {
    return `<p>${formatInline(line)}</p>`;
  }

  const [, alt, src] = match;
  return `
    <figure class="prose-image">
      <img
        src="${escapeAttribute(src)}"
        alt="${escapeAttribute(alt)}"
        loading="lazy"
        decoding="async"
      />
      ${alt ? `<figcaption>${formatInline(alt)}</figcaption>` : ""}
    </figure>
  `;
}

function formatInline(text) {
  return text
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/\*\*(.+?)\*\*/g, "<strong>$1</strong>")
    .replace(/\[([^\]]+)\]\(([^)]+)\)/g, '<a href="$2">$1</a>');
}

function escapeAttribute(text) {
  return String(text)
    .replace(/&/g, "&amp;")
    .replace(/"/g, "&quot;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;");
}

function normalizeLookupKey(text) {
  return String(text || "")
    .trim()
    .toLowerCase();
}

function buildProductImageIndex(manifest) {
  const exact = new Map();
  const byName = new Map();
  const fallbacks = new Map();

  (manifest.products || []).forEach((entry) => {
    const normalizedName = normalizeLookupKey(entry.productName);
    exact.set(`${entry.articleSlug}::${normalizedName}`, entry);
    if (!byName.has(normalizedName)) {
      byName.set(normalizedName, entry);
    }
  });

  (manifest.fallbacks || []).forEach((entry) => {
    fallbacks.set(entry.fallbackKey, entry);
  });

  return { exact, byName, fallbacks };
}

function resolveProductEntry(productImageIndex, articleSlug, productName) {
  const normalizedName = normalizeLookupKey(productName);
  return (
    productImageIndex.exact.get(`${articleSlug}::${normalizedName}`) ||
    productImageIndex.byName.get(normalizedName) ||
    null
  );
}

function resolveFallbackEntry(productImageIndex, fallbackKey) {
  if (!fallbackKey) {
    return null;
  }
  return productImageIndex.fallbacks.get(fallbackKey) || null;
}

function stripFrontmatter(markdown) {
  if (!markdown.startsWith("---")) {
    return markdown;
  }
  const endIndex = markdown.indexOf("\n---", 3);
  if (endIndex === -1) {
    return markdown;
  }
  return markdown.slice(endIndex + 4).trimStart();
}

function attachImageFallbacks(root) {
  root.querySelectorAll("img").forEach((image) => {
    const handleMissing = () => {
      if (image.dataset.fallbackSrc && image.getAttribute("src") !== image.dataset.fallbackSrc) {
        image.src = image.dataset.fallbackSrc;
        if (image.dataset.fallbackAlt) {
          image.alt = image.dataset.fallbackAlt;
        }
        image.removeAttribute("data-fallback-src");
        image.removeAttribute("data-fallback-alt");
        return;
      }

      const figure = image.closest(".prose-image");
      if (figure) {
        figure.classList.add("prose-image--missing");
      }

      const productCard = image.closest(".product-card");
      if (productCard) {
        productCard.classList.add("product-card--missing-image");
      }

      image.remove();
    };

    image.addEventListener("error", handleMissing, { once: true });

    if (image.complete && image.naturalWidth === 0) {
      handleMissing();
    }
  });
}

init().catch((error) => {
  bodyEl.innerHTML = `
    <div class="empty-state">
      <p class="eyebrow">Article unavailable</p>
      <h3>Could not load this article.</h3>
      <p>${error.message}</p>
    </div>
  `;
});
