#!/bin/sh
# Bundle the LaTeX template into a self-contained zip for the website.
set -e
cd "$(dirname "$0")"
tmp=$(mktemp -d)
mkdir "$tmp/cv-latex"
cp -r haupt-cv.cls cv.tex resume.tex build.py refs.bib README.md headshot.jpg generated "$tmp/cv-latex/"
rm -rf "$tmp/cv-latex/generated/__pycache__"
rm -f ../assets/portfolio/cv-latex.zip
(cd "$tmp" && zip -qrX "$OLDPWD/../assets/portfolio/cv-latex.zip" cv-latex)
rm -rf "$tmp"
echo "wrote assets/portfolio/cv-latex.zip"
