---
layout: default
title: Andreas Haupt's Portfolio
---

Andreas Haupt is an AI Institute Fellow-in-Residence at [Schmidt Sciences](https://www.schmidtsciences.org/person/andreas-haupt/), a Digital Fellow at the [Stanford Digital Economy Lab](https://digitaleconomy.stanford.edu/person/andreas-alexander-haupt/), and a Technology and Human Rights Fellow at the [Harvard Kennedy School](https://www.hks.harvard.edu/about/andreas-haupt). He studies how algorithmic systems represent diverse human preferences, including questions of [privacy](https://www.aeaweb.org/articles?id=10.1257/aer.20240576), [competition](https://papers.ssrn.com/abstract=5338793), and [consumer protection](). He develops and applies methods of [microeconomic theory](https://dl.acm.org/doi/10.1145/3670865.3673593), [structural econometrics](https://papers.ssrn.com/abstract_id=5126918), and [reinforcement learning](https://link.springer.com/article/10.1007/s10458-024-09682-5) to these domains; his work has been published in AI venues such as NeurIPS and ICML, in computer science venues such as ACM EC, ACM RecSys, and ACM FAccT, and in the [American Economic Review](https://www.aeaweb.org/articles?id=10.1257/aer.20240576). He earned a Ph.D. in Engineering-Economic Systems from MIT in February 2025 with a committee evenly split between Economics and Computer Science. Prior to that, he completed two master's degrees at the [University of Bonn](https://www.uni-bonn.de/en)—first in Mathematics (2017) and then in Economics (2018), with distinction. He has worked on competition enforcement for the [European Commission's Directorate-General for Competition](https://op.europa.eu/en/web/who-is-who/organization/-/organization/COMP/COM_CRF_1273) and the [U.S. Federal Trade Commission](https://www.ftc.gov/about-ftc/bureaus-offices/office-international-affairs), and [taught](https://www.bsgg.net/news/artikel/erster-schulentscheid-jugend-debattiert-an-den-bsgg/) [high school](https://www.bsgg.net/news/artikel/klickwinkel/) [mathematics](https://www.bsgg.net/news/artikel/abschluss-des-lernvideoprojekts-deine-bildung-dein-film/) and [computer science](https://www.bsgg.net/news/artikel/hour-of-code-in-der-berufsfachschule/) in Germany before his Ph.D. He remains committed to education and scholarship, most recently as a co-author of a textbook on [Machine Learning from Human Preferences](https://mlhp.stanford.edu), forthcoming with Princeton University Press.

<details>
  <summary>280-character bio</summary>
  Andreas Haupt is an AI Institute Fellow-in-Residence at Schmidt Sciences and a fellow at Stanford's Digital Economy Lab and the Harvard Kennedy School. He studies how algorithmic systems represent diverse human preferences, publishing in NeurIPS, ICML, ACM EC, and the AER.
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
<div class="tag-filters">
{% for type in site.paper_types %}
<button class="tag-btn tag-btn-type{% if type == default_type %} tag-btn-active{% endif %}" data-type="{{ type }}">{{ type }}</button>
{% endfor %}
<button class="tag-btn tag-btn-type tag-btn-clear tag-btn-type-last" data-type="all">All</button>
{% assign paper_tags = "" | split: "" %}{% for paper in site.papers %}{% if paper.tags %}{% assign paper_tags = paper_tags | concat: paper.tags %}{% endif %}{% endfor %}{% assign paper_tags = paper_tags | uniq %}
{% for tag in paper_tags %}
<button class="tag-btn" data-tag="{{ tag }}">{{ tag }}</button>
{% endfor %}
<button class="tag-btn tag-btn-clear tag-btn-active" data-tag="all">All</button>
</div>

{% for paper in site.papers %}
<div class="paper" data-type="{{ paper.type }}" data-tags="{{ paper.tags | join: ',' }}"{% if paper.type != default_type %} style="display:none"{% endif %}>
    <h3 class="title"><b>{{ paper.title }}</b></h3>
    <p>{{ paper.authors }}</p>
    <p><i>{{ paper.venue }}</i></p>
    <div class="paper-buttons">
    {% if paper.type %}
    <span class="paper-tag paper-type">{{ paper.type }}</span>
    {% endif %}
    {% for tag in paper.tags %}
    <span class="paper-tag">{{ tag }}</span>
    {% endfor %}
    {% assign keys = 'pdf,slides,poster,video,code,data,html,img' | split: ',' %}
    {% for item in paper %}
        {% if keys contains item[0] %}
            <a class="button" href="{{ item[1] }}" target="_blank">{{ item[0] | upcase }}</a>
        {% endif %}
    {% endfor %}

    </div>
</div>
{% endfor %}

## Ongoing Interests

{% for interest in site.ongoing_interests %}
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
        <span class="flag">{% if exp.url %}<a href="{{ exp.url }}" target="_blank">{{ exp.place }}</a>{% else %}{{ exp.place }}{% endif %}</span>
        <span class="time-wrapper"><span class="time">{{ exp.time }}</span></span>
    </div>
    <div class="desc"><b>{{ exp.title }}</b> <br/> {{ exp.description }}</div>
    </div>
</li>
{% endfor %}
</ul>

<script>
document.addEventListener('DOMContentLoaded', function() {
  var activeType = {{ default_type | jsonify }};
  var activeTag = null;
  var typeButtons = document.querySelectorAll('.tag-btn[data-type]');
  var tagButtons = document.querySelectorAll('.tag-btn[data-tag]');
  var papers = document.querySelectorAll('.paper[data-tags]');
  var interests = document.querySelectorAll('.interest[data-tags]');

  function hasTag(el) {
    return !activeTag || el.getAttribute('data-tags').split(',').indexOf(activeTag) !== -1;
  }

  function apply() {
    papers.forEach(function(p) {
      var typeMatch = !activeType || p.getAttribute('data-type') === activeType;
      p.style.display = typeMatch && hasTag(p) ? '' : 'none';
    });
    interests.forEach(function(p) { p.style.display = hasTag(p) ? '' : 'none'; });
    typeButtons.forEach(function(b) {
      var type = b.getAttribute('data-type');
      b.classList.toggle('tag-btn-active', type === 'all' ? !activeType : type === activeType);
    });
    tagButtons.forEach(function(b) {
      var tag = b.getAttribute('data-tag');
      b.classList.toggle('tag-btn-active', tag === 'all' ? !activeTag : tag === activeTag);
    });
  }

  typeButtons.forEach(function(btn) {
    btn.addEventListener('click', function() {
      var type = this.getAttribute('data-type');
      activeType = type === 'all' || activeType === type ? null : type;
      apply();
    });
  });

  tagButtons.forEach(function(btn) {
    btn.addEventListener('click', function() {
      var tag = this.getAttribute('data-tag');
      activeTag = tag === 'all' || activeTag === tag ? null : tag;
      apply();
    });
  });
});
</script>
