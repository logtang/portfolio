```
logtang.github.io/
├── index.html          ← landing page (intro, resume link)
├── about.html          ← About me
├── writeups.html       ← list linking to each write-up
├── style.css           ← shared look for the hand-written pages (empty for now)
├── resume.pdf
└── writeups/           ← rendered write-ups only; no .qmd lives here
    ├── statistics-for-normal-people.html
    └── new-perspective-on-an-old-lesson.html
```

## Publishing a write-up

Write-ups are written and rendered in `~/pers/projects/datablog`.
`datablog/.complete` is a symlink to this repo's `writeups/` folder.

1. In the `.qmd` front matter, under `format: html:`, make sure these are set:
   ```yaml
   embed-resources: true          # one self-contained .html, no _files/ folder
   include-before-body:
       text: |
           <p><a href="../index.html">← Logan Tang</a></p>
   ```
2. Render with the datablog venv:
   `QUARTO_PYTHON=../.venv/bin/python quarto render NN.qmd`
3. Copy under a descriptive name (the name becomes the URL):
   `cp "NN - Title/NN.html" .complete/some-descriptive-name.html`
4. Add an `<li>` for it on `writeups.html`.
5. Commit and push this repo.

## Progress ledger

Legend: `[x]` done · `[-]` skipped · `[ ]` to do

### Phase A — Self-contained write-ups (datablog side)
- [x] Removed accidental self-looping symlink `writeups/writeups`
- [x] A1. `01.qmd`: added `embed-resources: true`, re-rendered, copied over
- [x] A2. `02.qmd`: same; images now embedded
- [-] A3. `03.qmd` (Regression Done Right): not ready to publish
- [x] A4. Verified: no relative `src`/`href` left in either write-up
- [x] A5. Renamed to descriptive URLs:
  - `01.html` → `writeups/statistics-for-normal-people.html`
  - `02.html` → `writeups/new-perspective-on-an-old-lesson.html`
- [ ] Cleanup: delete unused `writeups/01_files/`, `02_files/`, `02_images/` (never committed; `*_files/` is gitignored)

### Phase B — Site skeleton (zero design)
- [x] B1. `<nav>` on `index.html` (Home · About · Write-ups)
- [x] B2. `about.html`
- [x] B3. `writeups.html`
- [-] B4. `apps.html` (created, later removed)
- [x] B5. Empty `style.css`, linked from all pages
- [x] B6. Intro line + Resume link on `index.html`
- [ ] B7. Add `resume.pdf`
- [x] B8. List write-ups on `writeups.html`
- [x] B9. "← Logan Tang" back-link inside each write-up (via Quarto `include-before-body`)
- [-] B10. Apps page removed
- [ ] B11. About content (hand-written, or from `00 - About Me/00.qmd`)

### Phase C — Repo hygiene
- [x] C1. Add `.DS_Store` to `.gitignore`
- [x] C2. Update the tree above to match reality, and document the `.complete` workflow
- [x] C3. Commits (one per step)

### Phase D — Deploy
- [x] D1. Confirm GitHub username: `logtang` (from `gh auth status`)
- [x] D2. Created `logtang/logtang.github.io` (public, via `gh repo create`)
- [x] D3. Add remote, push
- [x] D4. Enable Pages (main / root)
- [x] D5. Live at https://logtang.github.io — all pages 200 except `resume.pdf` (B7)

### Phase E — Later
- [ ] Design, favicon, 404 page, matching the Quarto look to the hand-written pages
