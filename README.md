# Indraos.github.io

Personal academic website for Andreas Haupt ([andyhaupt.com](https://andyhaupt.com)),
built with Jekyll and deployed by GitHub Actions.

## Layout

```
_config.yml         site settings and identity (name, positions, links, research sentence)
_data/              content: publications, experiences, honors, service, talks,
                    references, interests, and the CV/résumé layout (cv.yml)
_includes/          header, footer, publication card and filters, Vita timeline
_layouts/           page layout
index.md            the home page
assets/css/         styles
assets/js/          publication filters
assets/img/         press photos (offered as media assets), art, thumbnail
assets/pdf/         theses
cv/                 LaTeX CV and résumé, generated from _config.yml and _data/
.github/workflows/  builds the CV, then the site, and deploys to GitHub Pages
```

Edit `_data/` to change content: the website and the CV/résumé both read it.
On every push to `master`, `.github/workflows/pages.yml` builds the CV and
résumé into `assets/cv/` (not committed), builds the site and deploys it.
Pages must be set to deploy from GitHub Actions (Settings → Pages → Source).

To preview locally: `bundle exec jekyll serve`. To build the CV locally, see
[`cv/README.md`](cv/README.md).

## Acknowledgments

I found the (CC0) CSS code for the biographical timeline on [Martin Saveski's site](http://martinsaveski.com/).
