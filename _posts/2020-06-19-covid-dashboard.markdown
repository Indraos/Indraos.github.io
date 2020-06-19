---
layout: post
title:  "A COVID-19 Visualizer, Created with MIT IDSS ISOLAT"
date:   2020-06-19 08:00:00 +0100
categories: decide
---
The following is a visualization using `js`, merely for exploratory purposes. Credit to [Adrian](https://github.com/adrianxdev) who worked on this.
<script type="text/javascript" src="{{site.baseurl}}/assets/d3/d3.min.js"></script>
<div id="my_dataviz"></div>
<script>

// set the dimensions and margins of the graph
var margin = {top: 10, right: 30, bottom: 30, left: 60},
    width = 650 - margin.left - margin.right,
    height = 400 - margin.top - margin.bottom;

// append the svg object to the body of the page
var svg = d3.select("#my_dataviz")
  .append("svg")
    .attr("width", width + margin.left + margin.right)
    .attr("height", height + margin.top + margin.bottom)
  .append("g")
    .attr("transform",
          "translate(" + margin.left + "," + margin.top + ")");

//Read the data (the d3 v5+ way)
d3.csv("{{site.baseurl}}/assets/data/2020-06-19-data.csv",function(d){
    return { date : d3.timeParse("%Y-%m-%d")(d.date), value : d.value }
  })

  // Now I can use this dataset:

  //Note that this code is for d3 v5+ .... the .then uses a promise to load data which was introduced in v5
  .then(function(data) {

    // Add X axis --> it is a date format
    var x = d3.scaleTime()
      .domain(d3.extent(data, function(d) { return d.date; }))
      .range([ 0, width ]);
    svg.append("g")
      .attr("transform", "translate(0," + height + ")")
      .call(d3.axisBottom(x));

    // Add Y axis
    var y = d3.scaleLinear()
      .domain([0, d3.max(data, function(d) { return +d.value; })])
      .range([ height, 0 ]);
    svg.append("g")
      .call(d3.axisLeft(y));

    // Add the line
    svg.append("path")
      .datum(data)
      .attr("fill", "none")
      .attr("stroke", "steelblue")
      .attr("stroke-width", 1.5)
      .attr("d", d3.line()
        .x(function(d) { return x(d.date) })
        .y(function(d) { return y(d.value) })
        )

})
.catch(function(error){
     // handle error   
  })

</script>
