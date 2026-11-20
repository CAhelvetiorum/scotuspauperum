# Editorial principles — *Scotus pauperum* (Toulouse 1486)

Status: **conventions approved** (punctuation approved by the editor); text established for PDF pp. 1–13 (dedication, preface, Prologue qq. 1–4).

## Copy-text
Guillermus Gorris, *Scotus pauperum*, Toulouse: Henricus Mayer, after 10 May 1486; 4°, [256] leaves.
Copy: Lisbon, Biblioteca Nacional de Portugal, INC. 535 (digitised at purl.pt/32008), read from the
supplied PDF (150 dpi page images). The PDF's OCR layer is ignored.

Images are read at their native resolution (150 dpi, extracted losslessly from the PDF with `pdfimages`).

## Sigla and collation
- **A** = Toulouse: Henricus Mayer, after 10 May 1486. Lisbon, Biblioteca Nacional de Portugal, INC. 535. **Copy-text.**
- **B** = [Speyer: Peter Drach, c. 1492]. Munich, Bayerische Staatsbibliothek, 4 Inc.s.a. 910 a
  (GW 10961; Goff G325; H/C 6456; BSB-Ink G-230; IGI 4351), digitised as `bsb00042670`
  (digitale-sammlungen.de, read through the IIIF image API). Title: *Scotus pauperum vel abbreuiatus …*;
  Rebdorf ownership inscription. Two columns. B is a reprint of A (or of a common ancestor): it shares
  A's errors in several places (e.g. *Citacorum*), but corrects many misprints and occasionally fills
  lacunae; it also omits a few passages (e.g. the dating clause of the dedication).
- Collation records **substantive** variants only (wording, word order, omissions/additions, numerals,
  references). Orthographic variants (*e/ae*, *u/v*, *c/t*, single/double consonants), abbreviation
  differences, trivial changes of mood or word form that leave the sense unchanged (*sit/est*,
  *quereret/querat*, *Primum/Primo*, *incipere/incipit*) and interchanges of simple connectives
  (*et/quia*, *et/vel*, *sed/et*) are not recorded.
- A is printed as it stands, misprints included; where A gives no sense and B (or the source, chiefly the
  *Ordinatio*) gives the correct reading, the translation follows the correct reading and a lettered
  English note says so, while a numbered Latin note gives the A/B evidence.
- **Extent of collation.** For pp. 1–97 (sections 001–061, Prologue to Book I d. 23; B images up to b-0080 of the
  MDZ copy) B was read in full against A, and every substantive variant is recorded; throughout this stretch
  silence of the apparatus means that A and B agree. Notes say *B checked* when they rest on B.
- Not yet consulted: manuscript copy, c. 1490, Edinburgh, National Library of Scotland (ex Carmelites of Baccarat) — *to verify*.

## Transcription
1. **Abbreviations** are expanded silently (e.g. *xpo* → *Christo*, *qꝛ* → *quia*, *-ꝝ* → *-rum*, *ꝯ* → *con-*,
   *p̄* → *pre-*, *ꝑ* → *per-*, *⁊* → *et*, nasal bars → *m/n*). Expansions follow the
   printer's own spelling where it is attested in full elsewhere; doubtful expansions get a textual note.
2. **Orthography** is kept as printed: *e* for *ae/oe* (*prefatio*, *celestis*), *-ci-* for *-ti-* (*gracia*),
   *h* present or absent as printed (*habundas*, *ortor*), *u/v* and *i/j* exactly as printed
   (initial *v*, medial *u*: *vtilitas*, *deuotissima*; *Johanni*).
3. **Long s** is rendered *s*. Ligatures are resolved.
4. **Punctuation** follows the print, minimally normalised: the punctus is rendered as a full stop and the
   printed colon (*punctus elevatus*-like mark) as a colon, even where modern usage would put a comma, so that
   the print's sentence-rhythm is preserved; a virgula, where it occurs, becomes a comma. Question marks are
   supplied editorially, with a note. Round brackets ( ) are the printer's. The translation is punctuated in modern style.
5. **Capitalisation**: proper names (persons, places, books of Scripture) are capitalised; otherwise the print's
   capitals are retained. *deus, filius, spiritus sanctus* are left lower-case as printed.
6. **Paragraphing** is editorial, by sense; each paragraph has a stable id (see below).
7. **Page breaks** are marked inline as `[[p. N|label]]`, displayed as ‖ p. N · label, where N is the page of the
   supplied PDF and *label* gives the side of the leaf (r°/v°) followed, where present, by the printed mark in
   the headline of the recto. These marks are **running headlines**, not signatures: the Gothic capital
   formerly read *D* (or *B*) is a *Q* (= *Questio*), so the Prologue rectos carry *Q.ii* (p. 7), *Q.iii* (p. 9),
   *Q.iiii* (p. 11), *Q.iiiii* (p. 13), *Q.v* (p. 15), and from p. 17 the rectos carry *Di.* + numeral (*Distinctio*);
   Prologue versos carry no printed headline. From p. 18 the versos also carry a headline (*Di.i. Q.ii*, *Di.i. Q.iii*: distinction + question in progress). The manuscript *Liber 1* on p. 17 is a later hand. The first true signature
   seen so far stands at the foot of p. 15 (*b. i.*); signatures are given as *sig.* in the label when present. The foot of p. 19 reads *b. 2* (arabic 2 in the *z*-form). If p. 15 is *b. i*, then p. 17 would be expected as *b. ii*, so the sequence is anomalous; it is recorded as printed.
   (The *D.ii* etc. of the first two batches have been corrected accordingly.) The modern pencil foliation
   of the Lisbon copy is ignored.
8. **Uncertain readings** are enclosed in ⟨ ⟩ and always carry a textual note.
   **Illegible** text is marked […] (number of letters estimated in the note where possible).
   Nothing is supplied silently; no text is invented. Obvious misprints are kept and noted (no *[sic]* in the text).
9. Copy-specific features (rubrication, ownership marks, stamps) are recorded in notes, not in the text.

## Translation
- Aims at an accurate, scholarly English register, aligned paragraph by paragraph with the Latin.
- Standard Scotist terminology: *ens inquantum ens* = being *qua* being; *pro statu isto* = in the present state;
  *obiectum primum* = first object; *doctor subtilis* = the Subtle Doctor; *scotizare* = to “scotize”.
- Editorial supplements in the English are in [square brackets]; titles of works in italics.
- Translation choices that are interpretative get a `translation` note anchored in the English.

## Apparatus (notes)
Kept separate from the text in `docs/notes/notes.json`. Each note:

```json
{ "id": "n042",
  "anchor": { "para": "s002-09", "lemma": "prout maximo legum latori", "side": "la" },
  "type": "textual | source | historical | translation",
  "status": "certain | verified | to-verify | conjecture | uncertain",
  "text": "Markdown-light text (*italic* only)" }
```

- `lemma` must occur verbatim (ignoring ⟨ ⟩ and *italics*) in paragraph `para` of the Latin (`side: "la"`) or
  English (`side: "en"`); the first occurrence is anchored.
- `verified`: checked against a source this session; `to-verify`: plausible, needs checking;
  `conjecture`: the editor's hypothesis; `uncertain`: the reading itself is doubtful.
- Note ids are permanent; display labels are assigned automatically in reading order.
- **Two series of labels** distinguish the two levels of apparatus: notes anchored in the **Latin** are
  **numbered** (1, 2, 3 …) and print beside the Latin column; notes anchored in the **English** are
  **lettered in italics** (*a, b, c … z, aa, ab …*) and print beside the translation. Both series
  **restart at 1 / a in every section** (dedication, preface, each question), so a reference takes the form
  “§ Prologue q. 2, n. 7” or “q. 2, n. *c*”. The note id (n001 …) remains the stable identifier for citation
  within the project.
- On narrow screens the margins collapse and the notes appear as footnotes after each paragraph pair,
  Latin (numbered) first, then English (lettered).

## File layout
- `docs/text/manifest.json` — ordered list of sections.
- `docs/text/latin/NNN.md`, `docs/text/english/NNN.md` — one file per section; optional front matter; paragraphs
  separated by blank lines, each beginning `{#sNNN-PP}` (headings `{#sNNN-h .heading}`). Matching ids pair the columns.
- New chunks are added by appending sections to the manifest and new NNN files.
