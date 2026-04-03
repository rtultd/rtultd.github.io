document.addEventListener('DOMContentLoaded', () => {
  const mobileToggle = document.querySelector('[data-mobile-toggle]');
  const navLinks = document.querySelector('[data-nav-links]');
  if (mobileToggle && navLinks) {
    mobileToggle.addEventListener('click', () => {
      navLinks.classList.toggle('show');
    });
  }

  document.querySelectorAll('.nav-item > .drop-toggle').forEach(button => {
    button.addEventListener('click', (event) => {
      if (window.innerWidth > 860) return;
      event.preventDefault();
      const item = button.parentElement;
      item.classList.toggle('open');
    });
  });

  const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) entry.target.classList.add('visible');
    });
  }, { threshold: 0.15 });

  document.querySelectorAll('.reveal').forEach((el) => observer.observe(el));

  const yearEls = document.querySelectorAll('[data-year]');
  yearEls.forEach(el => el.textContent = new Date().getFullYear());

  const formSuccess = document.querySelector('[data-form-success]');
  if (formSuccess) {
    const params = new URLSearchParams(window.location.search);
    if (params.get('sent') === '1') {
      formSuccess.hidden = false;
    }
  }
});

  const formSuccess = document.querySelector('[data-form-success]');
  if (formSuccess) {
    const params = new URLSearchParams(window.location.search);
    if (params.get('sent') === '1') {
      formSuccess.hidden = false;
    }
  }
