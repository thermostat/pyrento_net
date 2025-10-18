
  window.addEventListener("load", () => {
    document.querySelectorAll("details.code-fold").forEach((fold) => {
      const summary = fold.querySelector("summary");
      if (!summary) return;

      summary.hidden = true;

      const toggle = document.createElement("button");
      toggle.type = "button";
      toggle.className = "code-toggle btn btn-link p-0";
      toggle.textContent = fold.hasAttribute("open") ? "Hide Code" : "Show Code";

      const container = document.createElement("div");
      container.className = "code-toggle-container";
      container.appendChild(toggle);

      fold.insertBefore(container, summary.nextElementSibling);

      toggle.addEventListener("click", () => {
        const isOpen = fold.hasAttribute("open");
        fold.toggleAttribute("open", !isOpen);
        toggle.textContent = isOpen ? "Show Code" : "Hide Code";
      });
    });
  });
