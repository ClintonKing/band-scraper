//Start with selecting the body and creating svg and axes
var graphOne = d3.select('div.graphOne');

//Set variables for height and width of svg
var width = parseInt(d3.select('div.graphOne').style("width"));
var height = 400;

//Create SVG
var svg = graphOne.append('svg')
  .attr("width", width)
  .attr("height", height);

//Variables for number of albums within each year.
var allYears = [];
var yearSpan = [];
var countArray = [];
var counts = [];
let maxInYear = 0;

//Now let's call our data
d3.json('static/json/albums.json', function(err,data){
  if (err) throw error;

  //Here's where we actually count the albums in each year for the vars above.
  for(var i = 0; i < data.length; ++i){
    var release = data[i].release;
    var year = release.substring(0,4);
    yearInt = Number(year);
    allYears.push(yearInt);
  };
  allYears.sort();

  //Finds largest and smallest year of release for any album in list, then creates an array with span of all years, and one that will hold count for albums released that year.
  var largestYear = Math.max.apply(Math, allYears);
  var smallestYear = Math.min.apply(Math, allYears);
  for (var i = smallestYear; i <= largestYear; i++) {
      yearSpan.push(i);
  }
  for(var i = 0; i < yearSpan.length; i++){
  	countArray[i] = 0;
  }

  //Now counts number of albums with any particular release year...
  for(var i = 0; i < allYears.length; i++){
        var count = yearSpan.indexOf(allYears[i]);
        countArray[count]++
  }

  //...and make object array
  for(var i = 0; i < yearSpan.length; i++){
    var yearValue = yearSpan[i];
    var countValue = countArray[i];
    if (countValue > maxInYear){
      maxInYear = countValue;
    };

    item = {};
    item ["year"] = yearValue;
    item ["albums"] = countValue;

    counts.push(item);
  }

  //Let's see if those final counts look right...
  console.log(counts);

  function round5(x){
    return Math.ceil(x/5)*5;
  };

  var x = d3.scaleBand()
    .domain(counts.map(function(d){return d.year}))
    .rangeRound([0, width])
    .padding(0.4);

  //Time to make some axes
  var y = d3.scaleLinear()
    .domain([0, round5(maxInYear)])
    .range([0, height]);

  var yInv = d3.scaleLinear()
    .domain([round5(maxInYear), 0])
    .range([0, height]);

  var xAxis = d3.axisBottom()
    .scale(x);

  var yAxis = d3.axisLeft()
    .scale(yInv)
    .ticks(5)
    .tickSize(10);

  //Add and position the xAxis
  svg.append('g')
    .attr('class', 'x axis')
    .attr('transform', 'translate(0, ' + height + ')')
    .call(xAxis);
  //Add and position the yAxis
  svg.append('g')
    .attr('class', 'y axis')
    .call(yAxis);

  //Onto our bars
  var yearGraph = svg.append("g");

  var yearBars = yearGraph
    .selectAll("rect")
    .data(counts)
    .enter()
    .append("rect");

  yearBars
    .attr("x", function(d){return x(d.year)})
    .attr("y", function(d){return height - y(d.albums)})
    .attr("height", function(d){return y(d.albums)})
    .attr("width", x.bandwidth())
    .attr("class", "shape yearBar")
    .attr("id", function(d){return d.year});

    // Informational text for bars
    var yearBarText = yearGraph.selectAll("text")
        .data(counts)
        .enter()
        .append("text");

     yearBarText
      .attr("x", function(d){return x(d.year) + (x.bandwidth()/2)}) //Needs extra padding of half the bar width to center text
      .attr("y", function(d){return height -y(d.albums) - 10}) //-10 to float
      .attr("text-anchor", "middle")
      .attr("class", "barText")
      .attr("id", function(d){return "text" + d.year})
      .text(function(d){return d.albums.toFixed(0)})
      .style("fill", "white")
      .style("font-family", "sans-serif")
      .style("font-size", "16px");

    //Let's make info for a specific bar appear on hovering on that bar.
    $(".shape").mouseenter(function(){
      var num = this.id;
      $("#text" + num).show();
    });
    $(".shape").mouseleave(function(){
      var num = this.id;
      $("#text" + num).hide();
    });


});
