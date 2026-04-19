const manifestUrl = "./content/articles.json";

const categoryOrder = [
  { value: "all", label: "All" },
  { value: "lighting", label: "Lighting" },
  { value: "fire-pits", label: "Fire Pits" },
  { value: "gardening", label: "Gardening" },
  { value: "smart-backyard", label: "Smart Backyard" },
  { value: "comfort", label: "Comfort" }
];

const articleGrid = document.querySelector("#article-grid");
const filterRow = document.querySelector("#filter-row");
const searchInput = document.querySelector("#search-input");
const articleCount = document.querySelector("#article-count");

let articles = [];
let activeCategory = "all";
let activeSearch = "";

async function init() {
  if (window.location.protocol === "file:") {
    articleGrid.innerHTML = `
      <div class="empty-state">
        <p class="eyebrow">Local preview required</p>
        <h3>This site needs to be opened through a local web server.</h3>
        <p>Open the <code>site</code> folder in Terminal and run <code>python3 -m http.server 8000</code>, then visit <code>http://localhost:8000</code>.</p>
      </div>
    `;
    return;
  }

  const response = await fetch(manifestUrl);
  articles = (await response.json()).map((article) => ({
    ...article,
    categoryLabel: article.categoryLabel || article.category
  }));
  articleCount.textContent = String(articles.length);
  renderFilters();
  renderArticles();
  searchInput.addEventListener("input", (event) => {
    activeSearch = event.target.value.toLowerCase().trim();
    renderArticles();
  });
}

function renderFilters() {
  filterRow.innerHTML = "";
  categoryOrder.forEach((category) => {
    const button = document.createElement("button");
    button.type = "button";
    button.className = `filter-chip${category.value === activeCategory ? " active" : ""}`;
    button.textContent = category.label;
    button.addEventListener("click", () => {
      activeCategory = category.value;
      renderFilters();
      renderArticles();
    });
    filterRow.appendChild(button);
  });
}

function renderArticles() {
  const filtered = articles.filter((article) => {
    const categoryValue = normalizeCategory(article.category);
    const matchesCategory =
      activeCategory === "all" || categoryValue === activeCategory;
    const haystack = `${article.title} ${article.deck} ${article.categoryLabel || article.category}`.toLowerCase();
    const matchesSearch = haystack.includes(activeSearch);
    return matchesCategory && matchesSearch;
  });

  articleGrid.innerHTML = "";

  if (!filtered.length) {
    const empty = document.createElement("div");
    empty.className = "empty-state";
    empty.innerHTML = `
      <p class="eyebrow">No matches</p>
      <h3>Try a different search or category.</h3>
      <p>Your full article library is still available, but nothing matches the current filter.</p>
    `;
    articleGrid.appendChild(empty);
    return;
  }

  filtered.forEach((article, index) => {
    const card = document.createElement("article");
    card.className = `article-card${article.featured ? " featured" : ""}`;
    card.style.animationDelay = `${index * 60}ms`;
    card.innerHTML = `
      <p class="card-tag">${article.categoryLabel}</p>
      <h3>${article.title}</h3>
      <p>${article.deck}</p>
      <div class="card-meta">
        <span>${article.readTime}</span>
        <span>${article.featured ? "Featured" : "Evergreen"}</span>
      </div>
      <a class="text-link" href="./article.html?slug=${encodeURIComponent(article.slug)}">Read article</a>
    `;
    articleGrid.appendChild(card);
  });
}

function normalizeCategory(category) {
  return String(category || "")
    .trim()
    .toLowerCase()
    .replace(/&/g, "and")
    .replace(/\s+/g, "-");
}

init().catch((error) => {
  articleGrid.innerHTML = `
    <div class="empty-state">
      <p class="eyebrow">Site data unavailable</p>
      <h3>Could not load the article manifest.</h3>
      <p>${error.message}</p>
    </div>
  `;
});
