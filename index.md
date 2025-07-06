---
layout: default
title: Andreas Haupt's Portfolio
---

Andreas Haupt is a Human-Centered AI Postdoctoral Fellow jointly appointed in [Stanford](https://www.stanford.edu/)'s [Economics](https://economics.stanford.edu/) and [Computer Science](https://www.cs.stanford.edu/) Departments, advised by Erik Brynjolfsson and Sanmi Koyejo. 

He earned a Ph.D. in Engineering-Economic Systems from MIT in February 2025. Prior to that, he completed two master degrees at the University of Bonn--first in Mathematics (2017) and then in Economics (2017). Throughout his graduate studies, he bridged Economics and Artificial intelligence, p

Before embarking on his doctoral 



<details>
  <summary>280-character bio</summary>This is the text that shows up when you click “Read more…”
</details>
<details>
  <summary>Tagline</summary>Andreas Haupt is 
</details>
<a class="button" href="/assets/media/">MEDIA ASSETS<a>

## Selected Publications

A more complete list of publications can be found on [Google Scholar]({{ site.social.google }}). <sup>‡</sup> indicates equal contribution or alphabetic author listing.

{% for paper in site.papers %}
<div class="paper">
    <h3 class="title"><b>{{ paper.title }}</b></h3>
    <p>{{ paper.authors }}</p>
    <p><i>{{ paper.venue }}</i></p>
    <div class="paper-buttons">
    {% assign keys = 'pdf,slides,poster,video,code,data' | split: ',' %}
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