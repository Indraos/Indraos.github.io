---
layout: default
title: Arts
---

[← Back to Home](/)

## Arts

{% for art in site.arts %}
<div class="art-piece">
    <div class="art-content">
        <img src="{{ art.thumbnail }}" alt="{{ art.title }}" class="art-thumbnail">
        <div class="art-info">
            <h3 class="title"><b>{{ art.title }}</b></h3>
            <p>{{ art.authors }}</p>
            <p>
            {% for venue in art.venues %}
                <a href="{{ venue.url }}" target="_blank"><i>{{ venue.name }}</i></a>{% unless forloop.last %}, {% endunless %}
            {% endfor %}
            </p>
            <p>{{ art.description }}</p>
        </div>
    </div>
</div>
{% endfor %}
