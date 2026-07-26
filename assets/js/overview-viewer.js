(function () {
  const params = new URLSearchParams(window.location.search);
  const src = params.get("src");
  const titleEl = document.getElementById("doc-title");
  const headingEl = document.getElementById("overview-heading");
  const blurbEl = document.getElementById("overview-blurb");
  const content = document.getElementById("content");

  const META = {
    "rental_market_report.md": {
      label: "SFR / 2–4 rental",
      blurb:
        "Cash-flow–balanced screen for single-family houses and 2–4 unit multifamily. Overview shows Top 10 actionable markets; open the full report for every state deep dive.",
    },
    "apartment_market_report.md": {
      label: "Apartments (5+)",
      blurb:
        "Conventional multifamily / apartment investment lens (5+ units). Overview shows Top 10 actionable apartment markets; open the full report for NOI screens and all-state detail.",
    },
    "sfh_appreciation_report.md": {
      label: "SFH appreciation",
      blurb:
        "Single-family equity / appreciation path (5–10+ year hold). Overview shows Top 10 appreciation markets; open the full report for FHFA-driven deep dives and squatting overlays.",
    },
  };

  if (!src || !META[src]) {
    content.innerHTML =
      '<p class="status error">Missing or invalid <code>?src=</code>. Use a known report file.</p>';
    return;
  }

  const meta = META[src];
  const fullHref = "view.html?src=" + encodeURIComponent(src);
  const fullTop10Href = fullHref + "#3-top-10-actionable-markets";

  titleEl.textContent = meta.label + " · Overview";
  headingEl.textContent = meta.label;
  blurbEl.textContent = meta.blurb;
  document.title = meta.label + " · Overview · Market";

  ["full-report-top", "full-report-cta", "full-report-bottom"].forEach(function (id) {
    var el = document.getElementById(id);
    if (el) el.setAttribute("href", fullHref);
  });
  var jump = document.getElementById("full-report-top10");
  if (jump) jump.setAttribute("href", fullTop10Href);

  fetch(src, { cache: "no-cache" })
    .then(function (res) {
      if (!res.ok) throw new Error("HTTP " + res.status);
      return res.text();
    })
    .then(function (md) {
      var slice = extractTop10Section(md);
      if (!slice) throw new Error("Could not find §3 Top 10 in " + src);

      // Drop Back-to-Index crumbs — overview is not the full report
      slice = slice.replace(/\[↑ Back to Index\]\(#index\)\s*/g, "");

      marked.setOptions({ gfm: true, breaks: false });
      content.innerHTML = marked.parse(slice);
      assignHeadingIds(content);
      rewriteLinks(content, fullHref);
      openExternalInNewTab(content);
      wrapTables(content);
      markWideTables(content);
    })
    .catch(function (err) {
      content.innerHTML =
        '<p class="status error">Could not build overview: ' +
        String(err.message || err) +
        "</p>";
    });

  function extractTop10Section(md) {
    var start = md.search(/^## 3\. Top 10 actionable markets\s*$/m);
    if (start < 0) return null;
    var rest = md.slice(start);
    var endRel = rest.search(/\n## 4\. All-state ranking matrix\s*$/m);
    if (endRel < 0) return rest;
    return rest.slice(0, endRel).trim() + "\n";
  }

  function githubSlug(text) {
    return String(text || "")
      .trim()
      .toLowerCase()
      .replace(/[^\p{L}\p{N}\s-]/gu, "")
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
      while (used[id]) {
        id = base + "-" + n;
        n += 1;
      }
      used[id] = true;
      h.id = id;
    });
  }

  function rewriteLinks(root, fullReportHref) {
    root.querySelectorAll("a[href]").forEach(function (a) {
      var href = (a.getAttribute("href") || "").trim();
      if (!href) return;

      // Point report-internal hashes at the full detail viewer
      if (href.charAt(0) === "#") {
        a.setAttribute("href", fullReportHref + href);
        return;
      }

      var file = href.split("#")[0];
      var hash = href.includes("#") ? href.slice(href.indexOf("#")) : "";
      if (Object.keys(META).indexOf(file) !== -1) {
        a.setAttribute(
          "href",
          "overview.html?src=" + encodeURIComponent(file) + (hash ? "" : "")
        );
        // Prefer full report if they linked a deep section
        if (hash) {
          a.setAttribute("href", "view.html?src=" + encodeURIComponent(file) + hash);
        }
      }
    });
  }

  function openExternalInNewTab(root) {
    root.querySelectorAll("a[href]").forEach(function (a) {
      var href = (a.getAttribute("href") || "").trim();
      if (!/^(https?:)?\/\//i.test(href) && !/^https?:/i.test(href)) {
        a.removeAttribute("target");
        a.removeAttribute("rel");
        return;
      }
      try {
        var url = new URL(href, window.location.href);
        if (url.origin === window.location.origin) {
          a.removeAttribute("target");
          a.removeAttribute("rel");
          return;
        }
      } catch (_) {}
      a.setAttribute("target", "_blank");
      a.setAttribute("rel", "noopener noreferrer");
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
        wrap.classList.toggle("is-wide", wrap.scrollWidth > wrap.clientWidth + 4);
      });
    }
    update();
    window.addEventListener("resize", update, { passive: true });
  }
})();
