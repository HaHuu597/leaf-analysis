// Footer year
document.querySelector('#year')?.textContent = new Date().getFullYear();

// Toast
const toast = document.querySelector('#toast');
function showToast(msg, type="success") {
  if (!toast) return;
  let color = "rgba(34,197,94,.95)";
  if (type === "error") color = "rgba(239,68,68,.95)";
  if (type === "info") color = "rgba(59,130,246,.95)";
  toast.textContent = msg;
  toast.style.background = color;
  toast.classList.add("show");
  setTimeout(() => toast.classList.remove("show"), 3000);
}
document.addEventListener("DOMContentLoaded", () => {
  document.querySelectorAll(".django-msg").forEach(msg => {
    showToast(msg.textContent.trim(), msg.dataset.level || "info");
  });
});


