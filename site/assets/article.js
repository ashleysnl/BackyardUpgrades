const manifestUrl = "./content/articles.json";

const titleEl = document.querySelector("#article-title");
const deckEl = document.querySelector("#article-deck");
const categoryEl = document.querySelector("#article-category");
const readTimeEl = document.querySelector("#article-readtime");
const bodyEl = document.querySelector("#article-body");
const relatedEl = document.querySelector("#related-articles");
const metaDescriptionEl = document.querySelector("#meta-description");
const metaOgTitleEl = document.querySelector("#meta-og-title");
const metaOgDescriptionEl = document.querySelector("#meta-og-description");

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

  const response = await fetch(manifestUrl);
  const articles = (await response.json()).map((entry) => ({
    ...entry,
    categoryLabel: entry.categoryLabel || entry.category
  }));
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

  const markdownResponse = await fetch(`./content/articles/${article.slug}.md`);
  const markdown = stripFrontmatter(await markdownResponse.text());
  bodyEl.innerHTML = renderMarkdown(markdown);
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

function renderMarkdown(markdown) {
  const lines = markdown.split("\n");
  const blocks = [];
  let paragraph = [];
  let listItems = [];
  let orderedItems = [];
  let inRecommendedProducts = false;
  let productBlock = null;

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
    if (productBlock) {
      if (line.trim() === ":::") {
        flushParagraph();
        flushList();
        flushOrderedList();
        blocks.push(renderProductBlock(productBlock));
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

    if (!line.trim()) {
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

    if (line.trim() === ":::product") {
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
        blocks.push(renderRecommendedProduct(line.slice(2)));
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

function renderRecommendedProduct(text) {
  const match = text.match(/\*\*(.+?)\*\*\s+—\s+Affiliate link:\s+\[([^\]]+)\]\(([^)]+)\)/);
  if (!match) {
    return `<ul><li>${formatInline(text)}</li></ul>`;
  }
  const [, productName, linkLabel, href] = match;
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

function renderProductBlock(block) {
  const image = block.image ? renderProductImage(block.image, block.name || "Product image") : "";
  const note = block.note ? `<p>${formatInline(block.note)}</p>` : "";
  const name = block.name ? `<strong>${formatInline(block.name)}</strong>` : "";
  const ctaLabel = block.cta || "Check price on Amazon";
  const href = block.url || "#";

  return `
    <section class="product-card${image ? "" : " product-card--missing-image"}">
      <div class="product-card__media">
        ${image}
      </div>
      <div class="product-card__content">
        <p class="panel-label">Recommended Product</p>
        ${name}
        ${note}
        <a class="button primary" href="${escapeAttribute(href)}" target="_blank" rel="noopener noreferrer sponsored">
          ${formatInline(ctaLabel)}
        </a>
      </div>
    </section>
  `;
}

function renderProductImage(src, alt) {
  return `
    <img
      src="${escapeAttribute(src)}"
      alt="${escapeAttribute(alt)}"
      loading="lazy"
      decoding="async"
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
