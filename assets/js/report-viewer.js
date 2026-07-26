(function () {
  const params = new URLSearchParams(window.location.search);
  const src = params.get("src");
  const titleEl = document.getElementById("doc-title");
  const content = document.getElementById("content");

  const labels = {
    "rental_market_report.md": "SFR / 2–4 rental",
    "apartment_market_report.md": "Apartments (5+)",
    "sfh_appreciation_report.md": "SFH appreciation",
  };

  if (!src || !/^[a-z0-9_\-]+\.md$/i.test(src)) {
    content.innerHTML = '<p class="status error">Missing or invalid <code>?src=</code> report file.</p>';
    return;
  }

  titleEl.textContent = labels[src] || src;

  content.innerHTML = '<p class="status">Loading report…</p>';

  fetch(src, { cache: "no-cache" })
    .then(function (res) {
      if (!res.ok) throw new Error("HTTP " + res.status);
      return res.text();
    })
    .then(function (md) {
      marked.setOptions({ gfm: true, breaks: false });
      content.innerHTML = marked.parse(md);
      wrapTables(content);
      markWideTables(content);
      document.title = (labels[src] || src) + " · Market";
    })
    .catch(function (err) {
      content.innerHTML =
        '<p class="status error">Could not load <code>' +
        src +
        "</code>: " +
        String(err.message || err) +
        "</p>";
    });

  function wrapTables(root) {
    root.querySelectorAll("table").forEach(function (table) {
      if (table.parentElement && table.parentElement.classList.contains("table-wrap")) return;
      const wrap = document.createElement("div");
      wrap.className = "table-wrap";
      table.parentNode.insertBefore(wrap, table);
      wrap.appendChild(table);
    });
  }

  function markWideTables(root) {
    function update() {
      root.querySelectorAll(".table-wrap").forEach(function (wrap) {
        var wide = wrap.scrollWidth > wrap.clientWidth + 4;
        wrap.classList.toggle("is-wide", wide);
      });
    }
    update();
    window.addEventListener("resize", update, { passive: true });
    if (window.visualViewport) {
      window.visualViewport.addEventListener("resize", update, { passive: true });
    }
  }
})();
