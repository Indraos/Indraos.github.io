# CV and résumé

LaTeX sources for `assets/portfolio/CV.pdf` and `assets/portfolio/Resume.pdf`,
styled after the website (Lato body, Palatino headings, cardinal `#8C1515`
accents, round headshot, timeline-style entries). Jekyll ignores this folder
because its name starts with an underscore.

Publications, events, art and ongoing interests come from `../_config.yml`, so
editing the website also updates the CV:

```sh
python3 build.py            # regenerates generated/*.tex and refs.bib
latexmk -pdf cv.tex resume.tex
cp cv.pdf ../assets/portfolio/CV.pdf
cp resume.pdf ../assets/portfolio/Resume.pdf
./package.sh                # refreshes ../assets/portfolio/cv-latex.zip
```

Everything else (appointments, education, honors, talks, references) lives in
`cv.tex` and `resume.tex`. The résumé picks publications by BibTeX key with
`\selectedpub[optional short title]{key}`; `build.py` prints all keys.

The class (`haupt-cv.cls`) compiles with pdflatex, lualatex or xelatex, so the
zip also works on Overleaf. Options: `compact` (one-page résumé spacing) and
`nophoto`.
