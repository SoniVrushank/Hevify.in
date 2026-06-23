const WHATSAPP_URL = "https://wa.me/+919429428370";
const WHATSAPP_TEXT = "Hi Hevify Labs, I want to discuss my requirements.";

const navToggle = document.querySelector(".nav-toggle");
const navLinks = document.querySelector(".nav-links");

function closeMenu() {
  navLinks?.classList.remove("open");
  navToggle?.setAttribute("aria-expanded", "false");
}

navToggle?.addEventListener("click", function () {
  const open = navLinks.classList.toggle("open");
  this.setAttribute("aria-expanded", String(open));
});

const nav = document.querySelector(".site-nav");
const onScroll = () => {
  nav?.classList.toggle("scrolled", window.scrollY > 24);
  if (navLinks?.classList.contains("open")) closeMenu();
};

onScroll();
addEventListener("scroll", onScroll, { passive: true });

document.addEventListener("click", (event) => {
  if (
    navLinks?.classList.contains("open") &&
    !navLinks.contains(event.target) &&
    !navToggle?.contains(event.target)
  ) {
    closeMenu();
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
