const baseBurger = document.getElementById('base-burger');
const basePanel = document.getElementById('base-mobilePanel');

const baseOpenPanel = () => {
  basePanel.hidden = false;
  basePanel.classList.add('active');
  baseBurger.setAttribute('aria-expanded', 'true');
  document.documentElement.style.overflow = 'hidden';
};
const baseClosePanel = () => {
  basePanel.classList.remove('active');
  baseBurger.setAttribute('aria-expanded', 'false');
  document.documentElement.style.overflow = '';
  requestAnimationFrame(() => { basePanel.hidden = true; });
};

baseBurger.addEventListener('click', () => {
  if(basePanel.classList.contains('active')) baseClosePanel();
  else baseOpenPanel();
});

basePanel.addEventListener('click', (e) => {
  if(e.target.matches('[data-close]')) baseClosePanel();
});
window.addEventListener('keydown', (e)=>{
  if(e.key === 'Escape' && basePanel.classList.contains('active')) baseClosePanel();
});
basePanel.querySelectorAll('a').forEach(a =>
  a.addEventListener('click', baseClosePanel)
);
