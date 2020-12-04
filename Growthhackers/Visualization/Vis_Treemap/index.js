
   
    d3.json('assignment.json').then(function (data) {
    console.log(data);
    var sales = data.map(function (d) { return d.sales; })
    var margin = data.map(function (d) { return d.margin; })
    var category = data.map(function (d) { return d.category; })

    
  var w = 400;
  var h = 400;
  var svg = d3.select('#chart').append('svg')
  .attr('width', w)
  .attr('height', h);
  var dataset1 = sales;
  var dataset2 = margin;
  var dataset3 = category;
      console.log(dataset1)
      console.log(dataset2)
  var bar = svg.selectAll('circle.bar')
  .data(dataset1)
  .enter().append('circle')
  .attr('class', 'bar')
  .attr('cx', function (d) { return d*(400/240)-25; })
  .data(dataset2)
//
  //var x = d3.scaleLinear()
  //. domain(d3.extent(dataset, function(d){
   // return d.sales}))
//이렇게 하고 나중에 
//.attr('x', function (d){return x(d.sales)})
//scale 사용법

.attr('cy', function (d) { return 400-d*(400/0.6)-10; })
  .attr('r', 4+'px')

  var label = svg.selectAll('text.label')
  .data(dataset1) 
  .enter().append('text')
  .attr('class', 'label')
  .attr('x', function (d) { return d * (400 / 240)-20 ; })
  .data(dataset2)
  .attr('y', function (d) { return 400 - d * (400 / 0.6)-20 ; })
  .data(dataset3)
  .text(function (d) { return d; })
   label.style("font-family", "sans-serif")
  .style("font-size", "11px")
  .style("fill", "black");
})     

  
  
  //일일이 가서 다 써주는거 가 text

