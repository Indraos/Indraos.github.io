---
layout: default
title: Andreas Haupt's Portfolio
---

Andreas Haupt is a Human-Centered AI Postdoctoral Fellow jointly appointed in Stanford's Economics and Computer Science Departments, where he is advised by [Erik Brynjolfsson](https://www.digitaleconomy.stanford.edu/people/erik-brynjolfsson/) and [Sanmi Koyejo](https://cs.stanford.edu/people/sanmi/). He studies the elicitation and aggregation of human preferences in machine learning systems, including questions of [privacy](https://dl.acm.org/doi/10.1145/3490486.3538259), [competition](https://papers.ssrn.com/abstract=5338793), and [consumer protection](). He develops and applies methods of [microeconomic theory](https://dl.acm.org/doi/10.1145/3670865.3673593), [structural econometrics](https://papers.ssrn.com/abstract_id=5126918), and [reinforcement learning](https://link.springer.com/article/10.1007/s10458-024-09682-5) to these domains. He earned a Ph.D. in Engineering-Economic Systems from MIT in February 2025 with a committee evenly split between Economics and Computer Science. Prior to that, he completed two master's degrees at the [University of Bonn](https://www.uni-bonn.de/en)—first in Mathematics (2017) and then in Economics (2018), with distinction. He has worked on competition enforcement for the [European Commission's Directorate-General for Competition](https://op.europa.eu/en/web/who-is-who/organization/-/organization/COMP/COM_CRF_1273) and the [U.S. Federal Trade Commission](https://www.ftc.gov/about-ftc/bureaus-offices/office-international-affairs), and [taught](https://www.bsgg.net/news/artikel/erster-schulentscheid-jugend-debattiert-an-den-bsgg/) [high school](https://www.bsgg.net/news/artikel/klickwinkel/) [mathematics](https://www.bsgg.net/news/artikel/abschluss-des-lernvideoprojekts-deine-bildung-dein-film/) and [computer science](https://www.bsgg.net/news/artikel/hour-of-code-in-der-berufsfachschule/) in Germany before his Ph.D. He remains committed to education and scholarship, most recently as a co-author of an upcoming textbook on [Machine Learning from Human Preferences](https://mlhp.stanford.edu).

<details>
  <summary>280-character bio</summary>
  Andreas Haupt is a Human-Centered AI Postdoctoral Fellow at Stanford Economics and CS. He studies human preferences in ML, drawing on economics and RL. He earned his Ph.D. at MIT and has worked with the EU and FTC. Before academia, he taught high school math and CS in Germany.
</details>
<details>
  <summary>Tagline</summary>
  Federal Trade Commission meets AI alignment.
</details>
<details>
  <summary>Media Assets</summary>
  {% assign media_files = site.static_files | where: "media", true %}
  {% for file in media_files %}
    <a class="button" href="{{ file.path }}" target="_blank">{{ file.basename | replace: "_", " " | upcase }}</a>
  {% endfor %}
</details>


## Selected Publications

A more complete list of publications can be found on [Google Scholar]({{ site.social.google }}). <sup>‡</sup> indicates equal contribution or alphabetic author listing.

{% for paper in site.papers %}
<div class="paper">
    <h3 class="title"><b>{{ paper.title }}</b></h3>
    <p>{{ paper.authors }}</p>
    <p><i>{{ paper.venue }}</i></p>
    <div class="paper-buttons">
    {% assign keys = 'pdf,slides,poster,video,code,data,html' | split: ',' %}
    {% for item in paper %}
        {% if keys contains item[0] %}
            <a class="button" href="{{ item[1] }}" target="_blank">{{ item[0] | upcase }}</a>
        {% endif %}
    {% endfor %}

    </div>
</div>
{% endfor %}

## Vita

Full [Resume]({{ site.resume }}) and [CV]({{ site.cv }}) are available as `pdf`.

<ul class="timeline">
{% for exp in site.experiences %}
<li>
    {% if exp.category == "work" %}
    <div class="direction-l">
    {% else %}
    <div class="direction-r">
    {% endif %}
    <div class="flag-wrapper">
        <span class="flag">{{ exp.place }}</span>
        <span class="time-wrapper"><span class="time">{{ exp.time }}</span></span>
    </div>
    <div class="desc"><b>{{ exp.title }}</b> <br/> {{ exp.description }}</div>
    </div>
</li>
{% endfor %}
</ul>