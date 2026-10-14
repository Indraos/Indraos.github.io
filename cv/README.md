# CV, résumé and list of publications

The CV, résumé and list of publications linked from the website are generated
entirely from the site's `../_config.yml` and `../_data/`, styled after the
site (Lato body, Palatino headings, cardinal `#8C1515` accents, round
headshot, timeline-style entries). `_config.yml` excludes this folder from
the site.

| Source | Used for |
|---|---|
| `_config.yml`: `name`, `positions`, `email`, `url`, `social`, `profile_pic` | header |
| `_config.yml`: `research` | the opening sentence (also the website bio) |
| `_data/experiences.yml` (`cv_section`, `degree`, `cv_description`, `cv_details`, `resume`) | appointments, education, policy, teaching |
| `_data/honors.yml`, `service.yml`, `talks.yml`, `references.yml` | the corresponding sections |
| `_data/publications.yml` | publications, preprints, theses, organized events, `refs.bib`, the list of publications |
| `_data/cv.yml` (`cv`, `resume`, `publications`) | section order, titles, contacts, and which entries the résumé selects |

Mark an entry with `resume: true` (publications, honors, service) or a `resume:`
block of shorter wording (experiences) to put it on the résumé; résumé
sections with `selected: true` show only those entries.

## List of publications

`publications.tex` is a numbered list of publications in the format the
[Max Planck Research Group](https://www.mpg.de/career/max-planck-research-groups/applications)
calls ask for, in the site's style:

- the three most important publications are identified: marked with a star,
  listed first with the applicant's quantified `contribution` (mark them
  `important: true` in `_data/publications.yml`; the calls require the
  contribution where the applicant is not first author);
- only peer-reviewed and in-press work counts as published: preprints,
  submitted work (`status: "Submitted to ..."`) and theses are listed in
  separate sections and marked;
- open-access publications are marked (inferred from links to arXiv,
  OpenReview, PMLR, SSRN, ..., or set with `open_access`);
- every entry links to the publisher's version or a preprint, and the
  opening line counts the entries as of the build date.

`build.py` also writes the same list as `generated/publications.md`, which
cites the records of `generated/refs.bib` by key (Pandoc:
`pandoc --citeproc generated/publications.md`).

## Building

`cv.tex`, `resume.tex` and `publications.tex` only choose the document class
and include the generated files. Only sources are committed: on every push to
`master`, the GitHub Pages workflow (`.github/workflows/pages.yml`) runs
`build.py`, compiles the three documents, writes `assets/cv/cv.pdf`,
`resume.pdf`, `publications.pdf` (with `publications.md` and `refs.bib`) and
`cv-latex.zip`, and deploys the site with them. To build locally (needs
PyYAML, Pillow and TeX Live):

```sh
python3 build.py            # writes generated/ (CV, résumé, list of publications, refs.bib, headshot)
latexmk -pdf cv.tex resume.tex publications.tex
./package.sh                # writes ../assets/cv/cv-latex.zip
```

The class (`haupt-cv.cls`) compiles with pdflatex, lualatex or xelatex, so the
zip also works on Overleaf. Options: `compact` (one-page résumé spacing) and
`nophoto`.
