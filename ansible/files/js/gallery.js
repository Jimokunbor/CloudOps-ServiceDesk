
/*
 * CloudOps ServiceDesk
 * Randomized Image Gallery
 */

document.addEventListener("DOMContentLoaded", () => {
  const gallery = document.getElementById("cloudops-gallery");

  if (!gallery) return;

  const slides = Array.from(
    gallery.querySelectorAll(".gallery-slide")
  );

  const indicators = Array.from(
    document.querySelectorAll(".gallery-indicator")
  );

  if (slides.length === 0) return;

  const reducedMotion = window.matchMedia(
    "(prefers-reduced-motion: reduce)"
  );

  let currentIndex = 0;
  let timer = null;

  function showSlide(index) {
    slides.forEach((slide, i) => {
      const active = i === index;

      slide.classList.toggle("active", active);
      slide.setAttribute("aria-hidden", String(!active));
    });

    indicators.forEach((indicator, i) => {
      const active = i === index;

      indicator.classList.toggle("active", active);
      indicator.setAttribute("aria-pressed", String(active));
    });

    currentIndex = index;
  }

  function showRandomSlide() {
    if (slides.length < 2) return;

    // Choose a random slide different from the current one.
    const offset =
      1 + Math.floor(Math.random() * (slides.length - 1));

    const nextIndex = (currentIndex + offset) % slides.length;

    showSlide(nextIndex);
  }

  function stopGallery() {
    if (timer !== null) {
      window.clearInterval(timer);
      timer = null;
    }
  }

  function startGallery() {
    stopGallery();

    if (reducedMotion.matches || slides.length < 2) return;

    // Change image every 5 seconds.
    timer = window.setInterval(showRandomSlide, 5000);
  }

  indicators.forEach((indicator, index) => {
    indicator.addEventListener("click", () => {
      if (index >= slides.length) return;

      showSlide(index);
      startGallery();
    });
  });

  gallery.addEventListener("mouseenter", stopGallery);
  gallery.addEventListener("mouseleave", startGallery);

  document.addEventListener("visibilitychange", () => {
    if (document.hidden) {
      stopGallery();
    } else {
      startGallery();
    }
  });

  reducedMotion.addEventListener("change", startGallery);

  showSlide(0);
  startGallery();
});
