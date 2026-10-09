#!/bin/sh
# Bundle the LaTeX template into a self-contained zip for the website.
# Run after build.py so that generated/ exists.
set -e
cd "$(dirname "$0")"
tmp=$(mktemp -d)
mkdir "$tmp/cv-latex"
cp -r haupt-cv.cls cv.tex resume.tex build.py README.md generated "$tmp/cv-latex/"
mkdir -p ../assets/cv
rm -f ../assets/cv/cv-latex.zip
(cd "$tmp" && zip -qrX "$OLDPWD/../assets/cv/cv-latex.zip" cv-latex)
rm -rf "$tmp"
echo "wrote assets/cv/cv-latex.zip"
