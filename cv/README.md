# CV and résumé

The CV and résumé linked from the website are generated entirely from the
site's `../_config.yml` and `../_data/`, styled after the site (Lato body,
Palatino headings, cardinal `#8C1515` accents, round headshot,
timeline-style entries). `_config.yml` excludes this folder from the site.

| Source | Used for |
|---|---|
| `_config.yml`: `name`, `positions`, `email`, `url`, `social`, `profile_pic` | header |
| `_config.yml`: `research` | the opening sentence (also the website bio) |
| `_data/experiences.yml` (`cv_section`, `degree`, `cv_description`, `cv_details`, `resume`) | appointments, education, policy, teaching |
| `_data/honors.yml`, `service.yml`, `talks.yml`, `references.yml` | the corresponding sections |
| `_data/publications.yml` | publications, preprints, theses, organized events, `refs.bib` |
| `_data/cv.yml` (`cv`, `resume`) | section order, titles, contacts, and which entries the résumé selects |

Mark an entry with `resume: true` (publications, honors, service) or a `resume:`
block of shorter wording (experiences) to put it on the résumé; résumé
sections with `selected: true` show only those entries.

`cv.tex` and `resume.tex` only choose the document class and include the
generated files. Only sources are committed: on every push to `master`, the
GitHub Pages workflow (`.github/workflows/pages.yml`) runs `build.py`, compiles
both documents, writes `assets/cv/cv.pdf`, `resume.pdf` and
`cv-latex.zip`, and deploys the site with them. To build locally (needs
PyYAML, Pillow and TeX Live):

```sh
python3 build.py            # writes generated/ (CV, résumé, refs.bib, headshot)
latexmk -pdf cv.tex resume.tex
./package.sh                # writes ../assets/cv/cv-latex.zip
```

The class (`haupt-cv.cls`) compiles with pdflatex, lualatex or xelatex, so the
zip also works on Overleaf. Options: `compact` (one-page résumé spacing) and
`nophoto`.
