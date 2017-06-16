let bandName = '';

//Start with selecting the body and creating svg and axes
var graphTwo = d3.select('div.graphTwo');

//Set variables for height and width of svg
var width = parseInt(d3.select('div.graphTwo').style("width"));
var height = 600;

//Create SVG
var svg = graphTwo.append('svg')
  .attr("width", width)
  .attr("height", height);


//Variables for number of albums within each year.
var songs = [];

function getRandomColor() {
    var letters = '0123456789ABCDEF';
    var color = '#';
    for (var i = 0; i < 6; i++ ) {
        color += letters[Math.floor(Math.random() * 16)];
    }
    return color;
};

function convertToSeconds(orgLength) {
  var hms = orgLength;
  var a = hms.split(':');

  var seconds = (+a[0]) * 60 + (+a[1]);
  return seconds;
};

function convertToMinutes(length) {
  var minutes = Math.floor(length / 60);
  var seconds = length % 60;
  if(seconds < 10){
    seconds = '0' + seconds;
  };
  var output = minutes + ":" + seconds;
  return output;
};



//Now let's call our data and get to work.
d3.json('static/json/albums.json', function(err,data){
  if (err) throw error;

  bandName = data[0].artistName.toUpperCase();
  document.getElementById("title").innerHTML = bandName + " MADE SOME MUSIC";

  //Here's where we actually count the albums in each year for the vars above.
  for(var i = 0; i < data.length; i++){
    var color = getRandomColor();
    var songList = data[i].songs;
    var albumId = i + '-';
    for(var s = 0; s < songList.length; s++){
      var orgLength = songList[s].songLength;
      var trueLength = convertToSeconds(orgLength);
      var title = songList[s].songTitle;
      var songId = albumId + s;

      song = {};
      song ["value"] = trueLength;
      song ["songTitle"] = title;
      song ["color"] = color;
      song ["id"] = songId;

      songs.push(song);
    }
  };

  console.log(songs);

  var songData = {children: songs};

  var pack = d3.pack()
    .size([width, height])
    .padding(1.5);

  var root = d3.hierarchy(songData)
  .sum(function(d) {return d.value})
  .each(function(d) {
    d.color = d.data.color;
    d.title = d.data.songTitle;
    d.id = d.data.id;
  });
  console.log(root);

  var node = svg.selectAll(".node")
    .data(pack(root).leaves())
    .enter().append("g")
      .attr("class", "node")
      .attr("transform", function(d) { return "translate(" + d.x + "," + (d.y + 20) + ")"; });

  node.append("circle")
    .attr("id", function(d) { return d.id; })
    .attr("r", function(d) { return d.r; })
    .style("fill", function(d) { return d.color; })
    .attr("class", "circle");


  node.append("text")
    .attr("x", function(d){return 0 - d.x + width/2 - 10})
    .attr("y", function(d){return 0 - d.y - 20})
    .attr("text-anchor", "middle")
    .attr("class", "bubbleText")
    .attr("id", function(d){return "text" + d.id;})
    .text(function(d){return d.title + ' ' + '(' + convertToMinutes(d.value) + ')'})
    .style("fill", "white")
    .style("font-family", "sans-serif")
    .style("font-size", "20px");

  $(".circle").mouseenter(function(){
    var num = this.id;
    $("#text" + num).show();
  });
  $(".circle").mouseleave(function(){
    var num = this.id;
    $("#text" + num).hide();
  });


});
