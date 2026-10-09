# CV and résumé

The CV and résumé linked from the website are generated entirely from
`../_config.yml`, styled after the site (Lato body, Palatino headings,
cardinal `#8C1515` accents, round headshot, timeline-style entries). Jekyll
ignores this folder because its name starts with an underscore.

| In `_config.yml` | Used for |
|---|---|
| `name`, `positions`, `email`, `url`, `social`, `profile_pic` | header |
| `research` | the opening sentence (also the website bio) |
| `experiences` (`cv_section`, `degree`, `cv_description`, `cv_details`, `resume`) | appointments, education, policy, teaching |
| `honors`, `service`, `talks`, `references` | the corresponding sections |
| `papers` | publications, preprints, theses, organized events, `refs.bib` |
| `cv_layout`, `resume_layout` | section order, titles, contacts, and which entries the résumé selects |

Mark an entry with `resume: true` (papers, honors, service) or a `resume:`
block of shorter wording (experiences) to put it on the résumé; résumé
sections with `selected: true` show only those entries.

`cv.tex` and `resume.tex` only choose the document class and include the
generated files. Only sources are committed: on every push to `master`, the
GitHub Pages workflow (`.github/workflows/pages.yml`) runs `build.py`, compiles
both documents, writes `assets/portfolio/CV.pdf`, `Resume.pdf` and
`cv-latex.zip`, and deploys the site with them. To build locally (needs
PyYAML, Pillow and TeX Live):

```sh
python3 build.py            # writes generated/ (CV, résumé, refs.bib, headshot)
latexmk -pdf cv.tex resume.tex
./package.sh                # writes ../assets/portfolio/cv-latex.zip
```

The class (`haupt-cv.cls`) compiles with pdflatex, lualatex or xelatex, so the
zip also works on Overleaf. Options: `compact` (one-page résumé spacing) and
`nophoto`.
