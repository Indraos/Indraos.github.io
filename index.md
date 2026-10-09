---
layout: default
title: Andreas Haupt's Portfolio
---

Andreas Haupt is an AI Institute Fellow-in-Residence at [Schmidt Sciences](https://www.schmidtsciences.org/person/andreas-haupt/), a Digital Fellow at the [Stanford Digital Economy Lab](https://digitaleconomy.stanford.edu/person/andreas-alexander-haupt/), and a Technology and Human Rights Fellow at the [Harvard Kennedy School](https://www.hks.harvard.edu/about/andreas-haupt). He studies {{ site.research }}. His work has been published in AI venues such as NeurIPS and ICML, in computer science venues such as ACM EC, ACM RecSys, and ACM FAccT, and as a lead article in the [American Economic Review](https://www.aeaweb.org/articles?id=10.1257/aer.20240576). He earned a Ph.D. in Engineering-Economic Systems from MIT in February 2025 with a committee evenly split between Economics and Computer Science. Prior to that, he completed two master's degrees at the [University of Bonn](https://www.uni-bonn.de/en)—first in Mathematics (2017) and then in Economics (2018), with distinction. He has worked on competition enforcement for the [European Commission's Directorate-General for Competition](https://op.europa.eu/en/web/who-is-who/organization/-/organization/COMP/COM_CRF_1273) and the [U.S. Federal Trade Commission](https://www.ftc.gov/about-ftc/bureaus-offices/office-international-affairs), and [taught](https://www.bsgg.net/news/artikel/erster-schulentscheid-jugend-debattiert-an-den-bsgg/) [high school](https://www.bsgg.net/news/artikel/klickwinkel/) [mathematics](https://www.bsgg.net/news/artikel/abschluss-des-lernvideoprojekts-deine-bildung-dein-film/) and [computer science](https://www.bsgg.net/news/artikel/hour-of-code-in-der-berufsfachschule/) in Germany before his Ph.D. He remains committed to education and scholarship, most recently as a co-author of a textbook on [Machine Learning from Human Preferences](https://mlhp.stanford.edu), forthcoming with Princeton University Press.

<details>
  <summary>280-character bio</summary>
  Andreas Haupt is an AI Institute Fellow-in-Residence at Schmidt Sciences and a fellow at Stanford's Digital Economy Lab and Harvard Kennedy School. He studies how AI systems represent and are evaluated against diverse human preferences, publishing in NeurIPS, ACM EC, and the AER.
</details>
<details>
  <summary>Tagline</summary>
  Use AI to Learn about People's Preferences
</details>
<details>
  <summary>Media Assets</summary>
  {% assign media_files = site.static_files | where: "media", true %}
  {% for file in media_files %}
    <a class="button" href="{{ file.path }}" target="_blank">{{ file.basename | replace: "_", " " | upcase }}</a>
  {% endfor %}
</details>

## Publications

A more complete list of publications can be found on [Google Scholar]({{ site.social.google }}). <sup>‡</sup> indicates equal contribution or alphabetic author listing. Only published work is shown by default; select another type, or *All* types, to see the rest.

{% assign default_type = site.paper_types | first %}
{% include publication-filters.html %}

{% for paper in site.data.publications %}
{% include publication.html paper=paper default_type=default_type %}
{% endfor %}

## Ongoing Interests

{% for interest in site.data.interests %}
<div class="interest" data-tags="{{ interest.tags | join: ',' }}">
    <h3 class="title"><b>{{ interest.title }}</b></h3>
    <p>{{ interest.description }}</p>
    <div class="paper-buttons">
    {% if interest.tags %}
    {% for tag in interest.tags %}
    <span class="paper-tag">{{ tag }}</span>
    {% endfor %}
    {% endif %}
    </div>
</div>
{% endfor %}

## Vita

Full [Resume]({{ site.resume }}) and [CV]({{ site.cv }}) are available as `pdf`; their [LaTeX source]({{ site.cv_source }}) uses this site's style.

{% include vita.html %}
