#!/usr/bin/env python3
"""Generate CV/resume inputs from the website's _config.yml.

The website is the single source of truth for publications and events.
Nothing this script writes is committed; the GitHub Pages workflow runs it
before compiling cv.tex and resume.tex. Locally:

    python3 _cv/build.py [path/to/_config.yml] && cd _cv && latexmk -pdf cv.tex resume.tex

Writes into _cv/generated/:
    pubs-<type>.tex   one \\cvpub per entry, grouped by website type
    pubdefs.tex       \\pub@<key> macros for selected entries in the resume
    refs.bib          a BibTeX entry for every item (events as @misc)
    headshot.jpg      the website headshot, downscaled for the PDFs
"""
import html
import re
import sys
from pathlib import Path

import yaml
from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
HEADSHOT = ROOT / "assets" / "media" / "informal_headshot.jpg"
OUT = Path(__file__).resolve().parent / "generated"
LINK_LABELS = ["pdf", "html", "code", "data", "video", "slides", "poster"]
JOURNAL_HINTS = ["Journal", "Review", "Behavior", "Systems 38", "Research Part"]

SHORT_VENUES = [  # resume one-liners use the names people say out loud
    ("Advances in Neural Information Processing Systems", "NeurIPS"),
    ("ICML Workshop on AI for Science", "ICML AI for Science Workshop"),
    ("International Conference on Machine Learning", "ICML"),
    ("ACM Conference on Fairness, Accountability, and Transparency", "ACM FAccT"),
    ("ACM Conference on Economics and Computation", "ACM EC"),
    ("ACM Conference on Recommender Systems", "ACM RecSys"),
    ("ACM Symposium on Computer Science and Law", "ACM CSLAW"),
    ("American Economic Review", "AER"),
    ("Journal of the American Statistical Association", "JASA"),
    ("Autonomous Agents and Multi-Agent Systems", "JAAMAS"),
    ("Journal of Online Trust and Safety", "JOTS"),
    ("Symposium on the Foundations of Responsible Computing", "FORC"),
    ("Web and Internet Economics", "WINE"),
    ("Allied Social Science Associations Meeting", "ASSA"),
    ("Princeton University Press", "Princeton UP"),
]

LATEX_ESCAPES = {"&": r"\&", "%": r"\%", "$": r"\$", "#": r"\#", "_": r"\_",
                 "~": r"\textasciitilde{}", "^": r"\textasciicircum{}"}


def escape(text):
    return "".join(LATEX_ESCAPES.get(c, c) for c in text)


def quotes(text):
    """Turn straight double quotes into TeX quotes."""
    return re.sub(r'"([^"]*)"', r"``\1''", text)


def html_to_latex(text):
    """Convert the small HTML subset used in _config.yml to LaTeX."""
    text = html.unescape(text or "")
    links = []

    def stash(m):
        links.append((m.group(1), m.group(2)))
        return f"\x00{len(links) - 1}\x00"

    text = re.sub(r'<a href="([^"]*)"[^>]*>(.*?)</a>', stash, text)
    text = text.replace("<b>", "\x01").replace("</b>", "\x02")
    text = text.replace("<sup>‡</sup>", "\x03").replace("<br>", "\x04")
    text = re.sub(r"<[^>]+>", "", text)
    text = quotes(escape(text))
    text = (text.replace("\x01", r"\me{").replace("\x02", "}")
                .replace("\x03", r"\eq{}").replace("\x04", r"\newline "))
    for i, (url, label) in enumerate(links):
        text = text.replace(f"\x00{i}\x00", rf"\href{{{url}}}{{{escape(label)}}}")
    return text.replace("‡", r"\eq{}")


def plain(text):
    """Strip HTML and equal-contribution markers (for BibTeX)."""
    return re.sub(r"<[^>]+>", "", html.unescape(text or "")).replace("‡", "").strip()


def surname(name):
    return name.strip().split()[-1].replace(".", "")


def bib_key(paper, used):
    people = plain(paper.get("authors") or paper.get("organizers") or "Haupt")
    first = surname(people.split(",")[0]).lower()
    first = re.sub(r"[^a-z]", "", first) or "haupt"
    word = next((w for w in re.findall(r"[A-Za-z]+", paper["title"].lower())
                 if w not in {"a", "an", "the", "of", "on", "for", "and",
                              "position", "to", "in", "by"}), "untitled")
    key = f"{first}{str(paper['date'])[:4]}{word}"
    base, n = key, 1
    while key in used:
        n += 1
        key = f"{base}{n}"
    used.add(key)
    return key


def coauthors(paper):
    """'with Hitzig' / 'with Gemp et al.' for one-line resume entries."""
    people = [p.strip() for p in plain(paper.get("authors", "")).split(",")]
    others = [surname(p) for p in people if p and "Haupt" not in p and p != "et al."]
    if not others:
        return ""
    if len(others) <= 2:
        return "with " + " and ".join(others)
    return f"with {others[0]} et al."


def buttons(paper):
    out = []
    for label in LINK_LABELS:
        url = paper.get(label)
        if url:
            if url.startswith("/"):
                url = "https://andyhaupt.com" + url
            out.append(rf"\cvbutton{{{label.upper()}}}{{{escape(url)}}}")
    return "".join(out)


def pills(paper):
    return "".join(rf"\cvtag{{{escape(t)}}}" for t in paper.get("tags", []))


def cvpub(paper):
    people = paper.get("authors")
    if people is None:
        people = "Organizers: " + paper.get("organizers", "")
    return (rf"\cvpub{{{quotes(escape(paper['title']))}}}"
            rf"{{{html_to_latex(people)}}}"
            rf"{{{html_to_latex(paper['venue'])}}}"
            rf"{{{escape(paper['type'])}}}{{{pills(paper)}}}{{{buttons(paper)}}}")


def split_venue(venue):
    """'Advances in NeurIPS (Position Paper), 2026.' -> (name, note)."""
    v = re.sub(r",?\s*(?:\w+\s)?\d{4}\.?$", "", plain(venue)).rstrip(". ")
    note = ""
    m = re.search(r"\s*\(([^)]*[A-Za-z][^)]*)\)\s*$", v)
    if m:
        note, v = m.group(1), v[: m.start()]
    return v.strip(), note


def short_venue(venue, note):
    """'Games and Economic Behavior 148, p. 415-426' -> 'Games and Economic Behavior'."""
    venue = re.sub(r"^SSRN Preprint \d+$", "SSRN", venue)
    venue = re.sub(r" \d+(?: \(\d+\))?(?:, p\. [\d-]+)?$", "", venue)
    for long, short in SHORT_VENUES:
        if venue.startswith(long):
            venue = short
            break
    note = note.replace("Evaluations and Datasets Track", "E&D Track")
    return f"{venue} ({note})" if note else venue


def bibtex(paper, key):
    year = str(paper["date"])[:4]
    people = paper.get("authors") or paper.get("organizers", "")
    authors = [a.strip() for a in plain(people).split(",") if a.strip()]
    authors = ["others" if a == "et al." else a for a in authors]
    fields = {"title": "{" + paper["title"] + "}",
              "author": " and ".join(authors), "year": year}
    venue, note = split_venue(paper["venue"])
    kind = "misc"
    if paper["type"] == "Thesis":
        kind = "phdthesis" if "Ph.D." in venue else "mastersthesis"
        degree, _, school = venue.partition(", ")
        fields["school"] = school
        if kind == "mastersthesis":
            fields["type"] = degree
    elif "Press" in venue:
        kind = "book"
        fields["publisher"] = venue
        note = note or "forthcoming"
    elif paper["type"] in ("Published", "Preprint") and not venue.startswith(("Preprint", "SSRN")):
        if any(h in venue for h in JOURNAL_HINTS):
            kind = "article"
            m = re.match(r"(.+?) (\d+)(?: \((\d+)\))?(?:, p\. ([\d-]+))?$", venue)
            if m:
                fields["journal"] = m.group(1)
                fields["volume"] = m.group(2)
                if m.group(3):
                    fields["number"] = m.group(3)
                if m.group(4):
                    fields["pages"] = m.group(4).replace("-", "--")
            else:
                fields["journal"] = venue
        else:
            kind = "inproceedings"
            fields["booktitle"] = venue
    else:
        fields["howpublished"] = venue or paper["type"]
        if paper["type"] == "Event":
            note = "Organized event"
    if note:
        fields["note"] = note
    url = paper.get("html") or paper.get("pdf")
    if url and not url.startswith("/"):
        fields["url"] = url
    doi = re.search(r"(10\.\d{4,}/[^\s\"]+)", url or "")
    if doi and "arxiv" not in url:
        fields["doi"] = doi.group(1).split("?")[0]
    body = ",\n".join(f"  {k} = {{{v}}}" for k, v in fields.items() if v)
    return f"@{kind}{{{key},\n{body}\n}}\n"


def main():
    source = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / "_config.yml"
    if not source.exists():
        sys.exit(f"{source} not found; pass the website's _config.yml as an argument")
    config = yaml.safe_load(source.read_text())
    OUT.mkdir(exist_ok=True)
    papers = config["papers"]
    used = set()
    by_type, defs, bib = {}, [], []
    for paper in papers:
        key = bib_key(paper, used)
        by_type.setdefault(paper["type"], []).append(cvpub(paper))
        url = paper.get("html") or paper.get("pdf") or ""
        if url.startswith("/"):
            url = "https://andyhaupt.com" + url
        venue, note = split_venue(paper["venue"])
        defs.append(
            rf"\expandafter\def\csname pub@{key}\endcsname#1{{\cvpubline"
            rf"{{{str(paper['date'])[:4]}}}{{\ifx\relax#1\relax "
            rf"{quotes(escape(paper['title']))}\else#1\fi}}"
            rf"{{{escape(short_venue(venue, note))}}}"
            rf"{{{coauthors(paper)}}}{{{escape(url)}}}}}")
        entry = bibtex(paper, key)
        if entry:
            bib.append(entry)
    header = "% Generated by _cv/build.py from _config.yml -- do not edit.\n"
    for kind, entries in by_type.items():
        (OUT / f"pubs-{kind.lower()}.tex").write_text(header + "\n".join(entries) + "\n")
    (OUT / "pubdefs.tex").write_text(header + "\n".join(defs) + "\n")
    (OUT / "refs.bib").write_text(
        "% Generated by _cv/build.py from _config.yml -- do not edit.\n\n" + "\n".join(bib))
    if HEADSHOT.exists():
        with Image.open(HEADSHOT) as im:
            im.convert("RGB").resize((500, 500), Image.LANCZOS).save(
                OUT / "headshot.jpg", quality=88, optimize=True)
    keys = sorted(used)
    print(f"{len(papers)} entries, {len(bib)} BibTeX records; keys:", ", ".join(keys),
          file=sys.stderr)


if __name__ == "__main__":
    main()
