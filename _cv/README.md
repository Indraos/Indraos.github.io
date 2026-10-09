# CV and résumé

LaTeX sources for the CV and résumé linked from the website, styled after the
site (Lato body, Palatino headings, cardinal `#8C1515` accents, round headshot,
timeline-style entries). Jekyll ignores this folder because its name starts
with an underscore.

Only sources are committed. On every push to `master`, the GitHub Pages
workflow (`.github/workflows/pages.yml`) runs `build.py`, compiles both
documents, writes `assets/portfolio/CV.pdf`, `Resume.pdf` and `cv-latex.zip`,
and deploys the site with them.

Publications and organized events come from `../_config.yml`, so editing the
website updates the CV. To build locally (needs PyYAML, Pillow and TeX Live):

```sh
python3 build.py            # writes generated/ (fragments, refs.bib, headshot)
latexmk -pdf cv.tex resume.tex
./package.sh                # writes ../assets/portfolio/cv-latex.zip
```

Everything else (appointments, education, honors, talks, references) lives in
`cv.tex` and `resume.tex`. The résumé picks publications by BibTeX key with
`\selectedpub[optional short title]{key}`; `build.py` prints all keys.

The class (`haupt-cv.cls`) compiles with pdflatex, lualatex or xelatex, so the
zip also works on Overleaf. Options: `compact` (one-page résumé spacing) and
`nophoto`.
