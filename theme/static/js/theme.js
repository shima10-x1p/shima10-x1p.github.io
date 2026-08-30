(function () {
  "use strict";

  var root = document.documentElement;
  var toggle = document.querySelector("[data-theme-toggle]");
  var themeColor = document.querySelector("[data-theme-color]");

  if (!toggle) return;

  function applyTheme(theme, persist) {
    var dark = theme === "dark";
    root.dataset.theme = theme;
    root.style.colorScheme = theme;
    toggle.setAttribute("aria-pressed", String(dark));
    toggle.setAttribute(
      "aria-label",
      dark ? "ライトテーマに切り替える" : "ダークテーマに切り替える"
    );
    toggle.querySelector("[data-theme-label]").textContent = dark ? "Light" : "Dark";
    if (themeColor) themeColor.setAttribute("content", dark ? "#181c20" : "#f8f9fa");
    if (persist) {
      try { localStorage.setItem("theme", theme); } catch (error) {}
    }
  }

  applyTheme(root.dataset.theme === "dark" ? "dark" : "light", false);
  toggle.addEventListener("click", function () {
    applyTheme(root.dataset.theme === "dark" ? "light" : "dark", true);
  });
}());

