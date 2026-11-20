/* Scotus pauperum — two-column reader with marginal apparatus.
   Data: text/manifest.json, text/{latin,english}/NNN.md, notes/notes.json.
   No build step; plain ES2017. */
(function () {
  "use strict";
  const $ = (s, el = document) => el.querySelector(s);
  const esc = s => s.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");

  async function get(url, json) {
    const r = await fetch(url, { cache: "no-cache" });
    if (!r.ok) throw new Error(url + ": " + r.status);
    return json ? r.json() : r.text();
  }

  /* Parse one section file: optional front matter, paragraphs separated by
     blank lines, each beginning {#id .class}. */
  function parseMd(src) {
    let meta = {};
    src = src.replace(/^---\n([\s\S]*?)\n---\n/, (_, fm) => {
      fm.split("\n").forEach(l => { const m = l.match(/^(\w+):\s*"?(.*?)"?\s*$/); if (m) meta[m[1]] = m[2]; });
      return "";
    });
    const paras = [];
    src.split(/\n\s*\n/).map(s => s.trim()).filter(Boolean).forEach(block => {
      const m = block.match(/^\{#([\w-]+)((?:\s+\.[\w-]+)*)\}\s*([\s\S]*)$/);
      if (!m) { console.warn("Unlabelled paragraph", block.slice(0, 40)); return; }
      paras.push({ id: m[1], cls: (m[2].match(/[\w-]+/g) || []), text: m[3].replace(/\s*\n\s*/g, " ") });
    });
    return { meta, paras };
  }

  function inline(s) {
    s = esc(s);
    s = s.replace(/\[\[p\.\s*(\d+)\|([^\]]+)\]\]/g,
      (_, p, sig) => `<span class="pb" title="page ${p}; leaf side and printed mark: ${sig}">‖ <b>p. ${p}</b> · ${sig}</span>`);
    s = s.replace(/\*([^*]+)\*/g, "<em>$1</em>");
    s = s.replace(/⟨([^⟩]+)⟩/g, '<span class="unc">⟨$1⟩</span>');
    return s;
  }

  /* Wrap the first occurrence of `lemma` (plain text) inside element el. */
  function wrapLemma(el, lemma) {
    const norm = t => t.replace(/[⟨⟩]/g, "");
    const walker = document.createTreeWalker(el, NodeFilter.SHOW_TEXT, {
      acceptNode: n => n.parentElement.closest(".pb,.pid,.anchor") ? NodeFilter.FILTER_REJECT : NodeFilter.FILTER_ACCEPT
    });
    // Collect text nodes and build a flat string to allow lemmas spanning markup.
    const nodes = []; let flat = "";
    while (walker.nextNode()) { nodes.push({ n: walker.currentNode, start: flat.length }); flat += walker.currentNode.nodeValue; }
    let idx = flat.indexOf(lemma);
    if (idx < 0) idx = norm(flat).indexOf(norm(lemma)) >= 0 ? flat.indexOf(norm(lemma)) : -1;
    if (idx < 0) return null;
    const end = idx + lemma.length;
    const range = document.createRange();
    const locate = pos => { for (let i = nodes.length - 1; i >= 0; i--) if (pos >= nodes[i].start) return [nodes[i].n, pos - nodes[i].start]; };
    range.setStart(...locate(idx));
    range.setEnd(...locate(end));
    const span = document.createElement("span");
    span.className = "anchor";
    try { range.surroundContents(span); }
    catch (e) { span.appendChild(range.extractContents()); range.insertNode(span); }
    return span;
  }

  function noteHtml(n) {
    const status = n.status && n.status !== "certain" ? `<span class="status">${esc(n.status)}</span>` : "";
    return `<span class="num">${n.num}</span><span class="lemma">${inline(n.anchor.lemma)}</span> ` +
      `${inline(n.text)}<span class="tag">${n.type}</span>${status}`;
  }

  function link(a, notes) {
    const on = v => () => { a.classList.toggle("hl", v); notes.forEach(x => x.classList.toggle("hl", v)); };
    [a, ...notes].forEach(el => { el.addEventListener("mouseenter", on(true)); el.addEventListener("mouseleave", on(false)); });
    a.addEventListener("click", () => notes[0] && notes[0].scrollIntoView({ behavior: "smooth", block: "center" }));
  }

  /* Position margin notes beside their anchors, pushing down on collision. */
  function layout() {
    document.querySelectorAll(".row").forEach(row => {
      ["left", "right"].forEach(side => {
        const m = row.querySelector(".margin." + side); if (!m || !m.offsetParent) return;
        let y = 0;
        [...m.children].forEach(note => {
          const a = document.getElementById(note.dataset.anchor);
          const top = a ? a.getBoundingClientRect().top - m.getBoundingClientRect().top : 0;
          const t = Math.max(top - 2, y);
          note.style.top = t + "px";
          y = t + note.offsetHeight + 6;
        });
        m.style.minHeight = y + "px";
      });
    });
  }

  async function main() {
    const ed = $("#edition");
    const manifest = await get("text/manifest.json", true);
    const notesData = await get("notes/notes.json", true);
    const byPara = {};
    notesData.notes.forEach(n => (byPara[n.anchor.para] = byPara[n.anchor.para] || []).push(n));
    ed.innerHTML = "";
    const toc = $("#toc");
    /* Note labels: Latin notes are numbered 1, 2, 3 …; English notes are lettered
       a … z, aa, ab … (bijective base 26). Both series restart in every section. */
    const letters = k => { let s = ""; while (k > 0) { k--; s = String.fromCharCode(97 + k % 26) + s; k = Math.floor(k / 26); } return s; };

    for (const sec of manifest.sections) {
      const [la, en] = await Promise.all([get(`text/latin/${sec.id}.md`), get(`text/english/${sec.id}.md`)]).then(x => x.map(parseMd));
      let laN = 0, enN = 0;
      const enById = Object.fromEntries(en.paras.map(p => [p.id, p]));
      toc.insertAdjacentHTML("beforeend", `<a href="#sec-${sec.id}">${esc(sec.en)}</a>`);
      ed.insertAdjacentHTML("beforeend",
        `<div class="section-head" id="sec-${sec.id}"><div class="spacer"></div>` +
        `<h2 lang="la">${esc(sec.la)}<span class="pp">pp. ${esc(sec.pages)}</span></h2>` +
        `<h2 lang="en">${esc(sec.en)}${sec.partial ? " <span class=\"pp\">(specimen)</span>" : ""}</h2><div class="spacer"></div></div>`);

      for (const p of la.paras) {
        const q = enById[p.id];
        if (!q) console.warn("No English for", p.id);
        const row = document.createElement("div");
        row.className = "row " + p.cls.join(" ");
        row.id = p.id;
        row.innerHTML =
          `<aside class="margin left" aria-label="Notes to Latin"></aside>` +
          `<p class="p la" lang="la"><span class="pid">${p.id.replace(/^s/, "")}</span>${inline(p.text)}</p>` +
          `<p class="p en" lang="en"><span class="pid">${p.id.replace(/^s/, "")}</span>${q ? inline(q.text) : "<em>[translation pending]</em>"}</p>` +
          `<aside class="margin right" aria-label="Notes to translation"></aside>` +
          `<div class="foot"></div>`;
        ed.appendChild(row);

        // Order notes by position of their lemma in the paragraph (Latin first, then English).
        const list = (byPara[p.id] || []).map(n => {
          const side = n.anchor.side === "en" ? "en" : "la";
          const txt = (side === "en" ? (q ? q.text : "") : p.text).replace(/\*/g, "");
          return { n, side, pos: txt.indexOf(n.anchor.lemma) };
        }).sort((a, b) => (a.side === b.side ? a.pos - b.pos : a.side === "la" ? -1 : 1));

        for (const { n, side } of list) {
          n.num = side === "la" ? String(++laN) : letters(++enN);
          n.side = side;
          const host = row.querySelector(".p." + side);
          let a = wrapLemma(host, n.anchor.lemma);
          if (!a) { console.warn("Lemma not found", n.id, n.anchor.lemma); a = document.createElement("span"); a.className = "anchor"; host.prepend(a); }
          a.id = "a-" + n.id;
          a.insertAdjacentHTML("beforeend", `<sup class="${side}">${n.num}</sup>`);
          const mk = () => { const d = document.createElement("div"); d.className = "note " + n.type + " " + side; d.dataset.anchor = a.id; d.innerHTML = noteHtml(n); return d; };
          const mNote = mk(); mNote.id = n.id;
          row.querySelector(side === "la" ? ".margin.left" : ".margin.right").appendChild(mNote);
          const fNote = mk(); row.querySelector(".foot").appendChild(fNote);
          link(a, [mNote, fNote]);
        }
        if (!list.length) row.querySelector(".foot").remove();
      }
    }
    layout();
    if (document.fonts) document.fonts.ready.then(layout);
    let t; window.addEventListener("resize", () => { clearTimeout(t); t = setTimeout(layout, 80); });
    document.body.dataset.ready = "1";
  }

  main().catch(e => { $("#edition").innerHTML = `<p class="loading">Error loading edition: ${esc(String(e))}</p>`; console.error(e); });
})();
