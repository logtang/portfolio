```
logatang.github.io/
├── index.html          ← landing page (intro, resume link)
├── about.html          ← About me
├── writeups.html       ← cards linking to each write-up
├── apps.html           ← cards linking to each Streamlit app
├── style.css           ← shared look for your hand-written pages
├── resume.pdf
└── writeups/
    ├── anscombe.qmd    ← what you write
    ├── anscombe.html   ← what Quarto produces (what visitors see)
    ├── kaggle.qmd
    └── kaggle.html
```

## Progress ledger

Legend: `[x]` done · `[-]` skipped · `[ ]` to do

### Phase A — Self-contained write-ups (datablog side)
- [x] Removed accidental self-looping symlink `writeups/writeups` (staged, not committed)
- [x] A1. `01.qmd`: added `embed-resources: true`, re-rendered, copied over
- [x] A2. `02.qmd`: same; images now embedded
- [-] A3. `03.qmd` (Regression Done Right): not ready to publish
- [x] A4. Verified: no relative `src`/`href` left in either write-up
- [x] A5. Renamed to descriptive URLs:
  - `01.html` → `writeups/statistics-for-normal-people.html`
  - `02.html` → `writeups/new-perspective-on-an-old-lesson.html`
- [ ] Cleanup: delete unused `writeups/01_files/`, `02_files/`, `02_images/`

### Phase B — Site skeleton (zero design)
- [x] B1. `<nav>` on `index.html` (Home · About · Write-ups · Apps)
- [x] B2. `about.html`
- [x] B3. `writeups.html`
- [x] B4. `apps.html`
- [x] B5. Empty `style.css`, linked from all pages
- [x] B6. Intro line + Resume link on `index.html`
- [ ] B7. Add `resume.pdf`
- [x] B8. List write-ups on `writeups.html`
- [x] B9. "← Logan Tang" back-link inside each write-up (via Quarto `include-before-body`)
- [ ] B10. List Streamlit apps on `apps.html`
- [ ] B11. About content (hand-written, or from `00 - About Me/00.qmd`)

### Phase C — Repo hygiene
- [ ] C1. Add `.DS_Store` to `.gitignore`
- [ ] C2. Update the tree above to match reality, and document the `.complete` workflow
- [ ] C3. Commits

### Phase D — Deploy
- [ ] D1. Confirm GitHub username (`logatang` vs `logtang`)
- [ ] D2. Create `<username>.github.io` repo
- [ ] D3. Add remote, push
- [ ] D4. Enable Pages (main / root)
- [ ] D5. Click through the live site

### Phase E — Later
- [ ] Design, favicon, 404 page, matching the Quarto look to the hand-written pages
