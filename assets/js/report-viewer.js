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

  const REPORT_MD = Object.keys(labels);

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
      assignHeadingIds(content);
      rewriteLocalLinks(content);
      openLinksInNewTab(content);
      wrapTables(content);
      markWideTables(content);
      document.title = (labels[src] || src) + " · Market";
      // Hash is often applied before async HTML exists — scroll after IDs are ready
      scrollToHash();
    })
    .catch(function (err) {
      content.innerHTML =
        '<p class="status error">Could not load <code>' +
        src +
        "</code>: " +
        String(err.message || err) +
        "</p>";
    });

  window.addEventListener("hashchange", scrollToHash);

  content.addEventListener("click", function (ev) {
    var a = ev.target.closest && ev.target.closest("a[href^='#']");
    if (!a) return;
    var hash = a.getAttribute("href");
    if (!hash || hash === "#") return;
    var el = findAnchor(hash);
    if (!el) return;
    ev.preventDefault();
    history.pushState(null, "", hash);
    el.scrollIntoView({ behavior: "smooth", block: "start" });
  });

  /** Match GitHub / GFM heading anchors used in the report Index links. */
  function githubSlug(text) {
    return String(text || "")
      .trim()
      .toLowerCase()
      .replace(/[^\p{L}\p{N}\s-]/gu, "") // drop punctuation (., (), –, etc.)
      .replace(/[\s_]+/g, "-")
      .replace(/-+/g, "-")
      .replace(/^-|-$/g, "");
  }

  function assignHeadingIds(root) {
    var used = Object.create(null);
    root.querySelectorAll("h1, h2, h3, h4, h5, h6").forEach(function (h) {
      var base = githubSlug(h.textContent);
      if (!base) return;
      var id = base;
      var n = 1;
      while (used[id] || document.getElementById(id)) {
        id = base + "-" + n;
        n += 1;
      }
      used[id] = true;
      h.id = id;
    });
  }

  function rewriteLocalLinks(root) {
    root.querySelectorAll("a[href]").forEach(function (a) {
      var href = a.getAttribute("href") || "";
      // Sibling report .md -> sticky viewer
      var file = href.split("#")[0];
      var hash = href.includes("#") ? href.slice(href.indexOf("#")) : "";
      if (REPORT_MD.indexOf(file) !== -1) {
        a.setAttribute("href", "view.html?src=" + encodeURIComponent(file) + hash);
        return;
      }
      // Bare same-doc anchors sometimes written without leading path
      if (href.charAt(0) === "#" && href.length > 1) {
        a.setAttribute("href", href);
      }
    });
  }

  /** External / file links open in a new tab. Same-page #anchors stay in-page for Index nav. */
  function openLinksInNewTab(root) {
    root.querySelectorAll("a[href]").forEach(function (a) {
      var href = (a.getAttribute("href") || "").trim();
      if (!href || href === "#") return;
      // In-page section jumps (Index, Back to Index, state deep dives)
      if (href.charAt(0) === "#") return;

      a.setAttribute("target", "_blank");
      a.setAttribute("rel", "noopener noreferrer");
    });
  }

  function findAnchor(hash) {
    if (!hash) return null;
    var raw = decodeURIComponent(String(hash).replace(/^#/, ""));
    if (!raw) return null;
    try {
      var byId = document.getElementById(raw);
      if (byId) return byId;
    } catch (_) { /* invalid id selector chars */ }
    // Fallback: query [id="..."] for ids that need CSS.escape
    if (window.CSS && CSS.escape) {
      return document.querySelector('[id="' + CSS.escape(raw) + '"]');
    }
    return null;
  }

  function scrollToHash() {
    var hash = location.hash;
    if (!hash || hash === "#") return;
    // Wait a frame so layout + sticky topbar scroll-margin apply
    requestAnimationFrame(function () {
      var el = findAnchor(hash);
      if (el) el.scrollIntoView({ behavior: "auto", block: "start" });
    });
  }

  function wrapTables(root) {
    root.querySelectorAll("table").forEach(function (table) {
      if (table.parentElement && table.parentElement.classList.contains("table-wrap")) return;
      var wrap = document.createElement("div");
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
