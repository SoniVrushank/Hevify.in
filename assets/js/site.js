const WHATSAPP_URL = "https://wa.me/+919429428370";
const WHATSAPP_TEXT = "Hi Hevify Labs, I want to discuss my requirements.";
const DOCK_INTERVAL = 10000;
const DOCK_ITEMS = [
  {
    category: "Featured Blog",
    title: "5 AI Tools Every Marketer Should Be Using in 2025",
    copy: "Discover practical tools that save time, improve productivity, and make marketing workflows lighter.",
    reading: "4 min read",
    href: "/blogs/performance-marketing-guide/",
    image: "/favicon.webp"
  },
  {
    category: "Case Study",
    title: "Case Study: 4x ROAS with a Cleaner Funnel",
    copy: "A tighter offer, faster landing page, and stronger retargeting can unlock better efficiency without wasted spend.",
    reading: "5 min read",
    href: "/case-studies/",
    image: "/favicon.webp"
  },
  {
    category: "Marketing Insight",
    title: "Why Ads Stop Scaling",
    copy: "When creative, landing pages, and follow-up drift apart, performance plateaus even if spend increases.",
    reading: "3 min read",
    href: "/blog/",
    image: "/favicon.webp"
  },
  {
    category: "AI Tip",
    title: "Build Faster With Small AI Workflows",
    copy: "Use focused automations for follow-ups, reporting, and research instead of trying to automate everything at once.",
    reading: "3 min read",
    href: "/blog/",
    image: "/favicon.webp"
  },
  {
    category: "Free Resource",
    title: "Landing Page Checklist for Better Conversions",
    copy: "A simple structure that keeps the page focused, fast, and easy to scan on mobile.",
    reading: "2 min read",
    href: "/blog/",
    image: "/favicon.webp"
  },
  {
    category: "Client Success",
    title: "How a Local Brand Turned Content Into Inquiries",
    copy: "A sharper message and more consistent posts made it easier for people to understand the offer and act.",
    reading: "4 min read",
    href: "/case-studies/",
    image: "/favicon.webp"
  },
  {
    category: "SEO Tip",
    title: "Make One Page Answer One Intent",
    copy: "Matching a page to one search intent usually improves clarity, engagement, and rankings at the same time.",
    reading: "3 min read",
    href: "/seo-services/",
    image: "/favicon.webp"
  },
  {
    category: "Content Strategy",
    title: "Plan Content Around Buying Signals",
    copy: "Create posts that help people move from curiosity to action with fewer jumps and less friction.",
    reading: "4 min read",
    href: "/blog/",
    image: "/favicon.webp"
  }
];

const nav = document.querySelector(".site-nav");
const navLinks = document.querySelector(".nav-links");
const themeToggle = document.querySelector(".theme-toggle");
const body = document.body;
const onScroll = () => {
  nav?.classList.toggle("scrolled", window.scrollY > 24);
};

onScroll();
addEventListener("scroll", onScroll, { passive: true });

document.addEventListener("click", (event) => {
  if (navLinks?.classList.contains("open") && !navLinks.contains(event.target)) {
    navLinks.classList.remove("open");
  }
});

document.addEventListener("keydown", (event) => {
  if (event.key === "Escape") {
    closeMenu();
    document.querySelectorAll(".modal-layer.open").forEach((modal) => {
      modal.classList.remove("open");
      modal.setAttribute("aria-hidden", "true");
    });
  }
});

const io = "IntersectionObserver" in window
  ? new IntersectionObserver((entries) => entries.forEach((entry) => {
      if (entry.isIntersecting) {
        entry.target.classList.add("in");
        io.unobserve(entry.target);
      }
    }), { threshold: 0.12 })
  : null;

document.querySelectorAll(".reveal").forEach((el) => io ? io.observe(el) : el.classList.add("in"));

const savedTheme = localStorage.getItem("hevify-theme");
if (savedTheme === "dark") body.classList.add("theme-dark");
themeToggle?.addEventListener("click", () => {
  body.classList.toggle("theme-dark");
  localStorage.setItem("hevify-theme", body.classList.contains("theme-dark") ? "dark" : "light");
});

function whatsappHref(text = WHATSAPP_TEXT) {
  return `${WHATSAPP_URL}?text=${encodeURIComponent(text)}`;
}

function hydrateDetailFromCard(card) {
  document.getElementById("detail-kicker").textContent = card.dataset.kicker || "Details";
  document.getElementById("detail-title").textContent = card.dataset.title || "Details";
  document.getElementById("detail-copy").textContent = card.dataset.copy || "";
  const source = card.dataset.packages || card.dataset.list || "";
  document.getElementById("detail-list").innerHTML = source
    .split(card.dataset.packages ? "||" : "|")
    .filter(Boolean)
    .map((x) => {
      const parts = x.split("|");
      return parts.length > 1
        ? `<li><strong>${parts[0]}</strong><br><span>${parts[1]} plan</span><p>${parts[2]}</p><small>${parts[3] || ""}</small></li>`
        : `<li>${x}</li>`;
    })
    .join("");
  document.getElementById("detail-mail").href = card.dataset.mail || whatsappHref();
}

document.addEventListener("click", (event) => {
  const teamBtn = event.target.closest("[data-toggle-team]");
  if (teamBtn) {
    const card = teamBtn.closest(".team-card");
    document.querySelectorAll(".team-card.open").forEach((item) => {
      if (item !== card) item.classList.remove("open");
    });
    card.classList.toggle("open");
  }

  const contactOpen = event.target.closest("[data-open-contact]");
  if (contactOpen) {
    const modal = document.getElementById("contact-modal");
    modal.classList.add("open");
    modal.setAttribute("aria-hidden", "false");
  }

  if (event.target.matches("[data-close-contact]") || event.target.id === "contact-modal") {
    const modal = document.getElementById("contact-modal");
    modal.classList.remove("open");
    modal.setAttribute("aria-hidden", "true");
  }

  if (event.target.matches("[data-close-modal]") || event.target.id === "detail-modal") {
    const modal = document.getElementById("detail-modal");
    modal.classList.remove("open");
    modal.setAttribute("aria-hidden", "true");
  }

  const detailBtn = event.target.closest("[data-open-detail]");
  if (detailBtn) {
    const modal = document.getElementById("detail-modal");
    const cats = document.getElementById("detail-cats");
    const current = detailBtn.closest("[data-title]");
    const folderCards = [...document.querySelectorAll(".folder-card[data-title]")];
    cats.innerHTML = folderCards.length > 1
      ? folderCards.map((card, i) => `<button type="button" data-folder-index="${i}" class="${card === current ? "active" : ""}">${card.dataset.title}</button>`).join("")
      : "";
    hydrateDetailFromCard(current);
    modal.classList.add("open");
    modal.setAttribute("aria-hidden", "false");
  }

  const cat = event.target.closest("[data-folder-index]");
  if (cat) {
    const cards = [...document.querySelectorAll(".folder-card[data-title]")];
    const card = cards[Number(cat.dataset.folderIndex)];
    if (card) {
      hydrateDetailFromCard(card);
      document.querySelectorAll(".modal-cats button").forEach((b) => b.classList.remove("active"));
      cat.classList.add("active");
    }
  }

  const blogOpen = event.target.closest("[data-open-blog-dock]");
  if (blogOpen) openDockSheet("blog");
  const waOpen = event.target.closest("[data-open-wa-dock]");
  if (waOpen) openDockSheet("wa");
  if (event.target.closest("[data-close-blog-dock]")) closeDockSheet("blog");
  if (event.target.closest("[data-close-wa-dock]")) closeDockSheet("wa");
});

window.addEventListener("resize", () => {
  document.querySelectorAll(".pkg-panel").forEach((panel) => {
    if (panel.style.maxHeight) panel.style.maxHeight = `${panel.scrollHeight}px`;
  });
});

document.querySelectorAll(".pkg-toggle").forEach((btn) => {
  btn.addEventListener("click", () => {
    const panel = btn.nextElementSibling;
    const isOpen = panel.style.maxHeight;
    document.querySelectorAll(".pkg-panel").forEach((p) => {
      p.style.maxHeight = null;
      p.style.opacity = "0";
    });
    document.querySelectorAll(".pkg-toggle").forEach((b) => {
      b.querySelector(".chevron").style.transform = "rotate(0deg)";
      b.setAttribute("aria-expanded", "false");
    });
    if (!isOpen) {
      panel.style.maxHeight = `${panel.scrollHeight}px`;
      panel.style.opacity = "1";
      btn.querySelector(".chevron").style.transform = "rotate(90deg)";
      btn.setAttribute("aria-expanded", "true");
    }
  });
});

document.querySelectorAll("img").forEach((img) => {
  if (!img.hasAttribute("width")) img.setAttribute("width", img.naturalWidth || "1");
  if (!img.hasAttribute("height")) img.setAttribute("height", img.naturalHeight || "1");
});

document.getElementById("mail-form")?.addEventListener("submit", (event) => {
  event.preventDefault();
  const name = document.getElementById("mail-name").value.trim();
  const brand = document.getElementById("mail-brand").value.trim();
  const email = document.getElementById("mail-email").value.trim();
  const phone = document.getElementById("mail-phone").value.trim();
  const service = document.getElementById("mail-service").value;
  const message = document.getElementById("mail-message").value.trim();
  const msg = [
    "Hi Hevify Labs,",
    "",
    `Name: ${name}`,
    `Brand: ${brand}`,
    `Phone: ${phone}`,
    `Email: ${email}`,
    `Service: ${service}`,
    `Message: ${message}`
  ].join("\n");
  window.open(whatsappHref(msg), "_blank", "noopener");
});

const dock = {
  index: 0,
  timer: null,
  progressTimer: null
};

const dockTitle = document.querySelector("[data-dock-title]");
const dockMeta = document.querySelector("[data-dock-meta]");
const dockProgress = document.querySelector("[data-dock-progress]");
const blogSheet = document.getElementById("blog-sheet");
const waSheet = document.getElementById("wa-sheet");
const blogSheetImage = document.querySelector("[data-sheet-image]");
const blogSheetCategory = document.querySelector("[data-sheet-category]");
const blogSheetTitle = document.querySelector("[data-sheet-title]");
const blogSheetCopy = document.querySelector("[data-sheet-copy]");
const blogSheetReading = document.querySelector("[data-sheet-reading]");
const blogSheetCta = document.querySelector("[data-sheet-cta]");
const waForm = document.getElementById("wa-sheet-form");

function renderDockItem(index = dock.index) {
  if (!dockTitle || !dockMeta || !blogSheetImage || !blogSheetCategory || !blogSheetTitle || !blogSheetCopy || !blogSheetReading || !blogSheetCta) return;
  const item = DOCK_ITEMS[index % DOCK_ITEMS.length];
  dockTitle.textContent = item.title;
  dockMeta.textContent = `${item.category} · ${item.reading}`;
  blogSheetImage.src = item.image;
  blogSheetImage.alt = item.title;
  blogSheetCategory.textContent = item.category;
  blogSheetTitle.textContent = item.title;
  blogSheetCopy.textContent = item.copy;
  blogSheetReading.textContent = item.reading;
  blogSheetCta.href = item.href;
}

function animateDockProgress() {
  if (!dockProgress) return;
  dockProgress.style.transition = "none";
  dockProgress.style.width = "0%";
  requestAnimationFrame(() => {
    dockProgress.style.transition = `width ${DOCK_INTERVAL}ms linear`;
    dockProgress.style.width = "100%";
  });
}

function startDockRotation() {
  stopDockRotation();
  renderDockItem();
  animateDockProgress();
  dock.timer = window.setInterval(() => {
    dock.index = (dock.index + 1) % DOCK_ITEMS.length;
    renderDockItem(dock.index);
    animateDockProgress();
  }, DOCK_INTERVAL);
}

function stopDockRotation() {
  if (dock.timer) clearInterval(dock.timer);
  dock.timer = null;
}

function openDockSheet(kind) {
  const sheet = kind === "blog" ? blogSheet : waSheet;
  if (!sheet) return;
  sheet?.classList.add("open");
  sheet?.setAttribute("aria-hidden", "false");
  stopDockRotation();
}

function closeDockSheet(kind) {
  const sheet = kind === "blog" ? blogSheet : waSheet;
  if (!sheet) return;
  sheet?.classList.remove("open");
  sheet?.setAttribute("aria-hidden", "true");
  if (!blogSheet?.classList.contains("open") && !waSheet?.classList.contains("open")) startDockRotation();
}

waForm?.addEventListener("submit", (event) => {
  event.preventDefault();
  const name = document.getElementById("wa-name").value.trim();
  const company = document.getElementById("wa-company").value.trim();
  const message = document.getElementById("wa-message").value.trim();
  const msg = [
    "Hi Hevify,",
    "",
    name ? `Name: ${name}` : null,
    company ? `Company: ${company}` : null,
    `Message: ${message}`
  ].filter(Boolean).join("\n");
  window.open(whatsappHref(msg), "_blank", "noopener");
});

if (dockTitle && dockMeta && blogSheetImage && blogSheetCategory && blogSheetTitle && blogSheetCopy && blogSheetReading && blogSheetCta) {
  startDockRotation();
}

document.querySelectorAll(".pkg-wrap").forEach((wrap) => {
  if (!wrap.closest(".featured-card")) return;
  const btn = wrap.querySelector(".pkg-toggle");
  const panel = wrap.querySelector(".pkg-panel");
  const chevron = wrap.querySelector(".chevron");
  if (!btn || !panel) return;
  btn.setAttribute("aria-expanded", "true");
  panel.classList.add("open");
  panel.style.maxHeight = `${panel.scrollHeight}px`;
  panel.style.opacity = "1";
  if (chevron) chevron.style.transform = "rotate(90deg)";
});
