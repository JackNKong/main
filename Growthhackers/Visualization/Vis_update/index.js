d3.json('assignment.json').then(function (data) {
  console.log(data);
  var w = 400;
  var h = 400;
  var mar = { top: 20, right: 20, bottom: 20, left: 20 };
  var innerW = w - mar.left - mar.right,
      innerH = h - mar.top - mar.bottom;
  var xRange = [0, innerW];
  var yRange = [innerH, 0];

  function randDataset() {
    var rand1 = d3.randomUniform(0,innerW); // 기존 도메인 사이 값만 나오도록 랜덤값 생성
    var rand2 = d3.randomUniform(0,innerH);
    d3.select(this).selectAll('.bar').each(function (d) { // svg.selectAll('.bar')나  bar 와 같음
      d.sales = Math.round(rand1()); //sales 값을 바꿔본다
      d.margin = Math.round(rand2());
    
    })
  }
 // var cate = data.map(function (d) {return d.category;})
  
 

  var xDomain = data.map(function (d) { return d.sales; })
  var x = d3.scaleBand()
    .domain(xDomain)
    .range(xRange)
    .padding(0.1)
  var yDomain = data.map(function (d) { return d.margin; })
  var y = d3.scaleBand()
    .domain(yDomain)
    .range(yRange)
    .padding(0.1)
  var zDomain =data.map(function (d) { return d.category; })
  var z = d3.scaleBand()
    .domain(zDomain)
    .padding(0.1)
  var xAxis = d3.axisBottom(x); //함수를 전달 받는 거임./x축을 그릴 아래방향 axis에 x 스케일을 전달한다. 결과값인 xAxis는 g를 받아 축을 그려주는 함수(axis 
  xAxis.tickSize(innerW) //xAxis의 tickSize를 없애고
    .tickPadding(6)
    
  var yAxis = d3.axisRight(y);
  yAxis.tickSize(innerH)
    .tickPadding(5);  

var xtick = [50,100,150,200,250,300]

  var svg = d3.select('#vertical').append('svg')
    .attr('width', w)
    .attr('height', h)
    .append('g') //�실제 차트가 그려질 공간은 별도로 설정
    .attr('transform', 'translate(' + [mar.top, mar.right] + ')'); 
  
    svg.append('g') //g를 먼저 추가하고
    .attr('class', 'x axis')
    .call(xAxis)
    .attr('text', xtick)
    .attr('transform', 'translate(' + [0, innerH] + ')');

    svg.append('g')
    .attr('class','y axis')
    .call(yAxis)
    .attr('transform', 'translate(' + [innerW,0]+ ')');
  
  //  console.log(data)

  var xy = d3.local();
  var bar = svg.selectAll('.bar')
    .data(data)
    .enter().append('g')
    .attr('class', 'bar')
    .each(function(d){
      xy.set(this,[(d.sales),y(d.margin)])
    })
    .attr('transform', function(d){
      var pos = xy.get(this);
      console.log(pos)
      return 'translate(' + pos + ')'
    });
    var circle = bar.append('circle')
    .attr('cx',x)
    .attr('cy',y)
    .attr('r', 4 + 'px')
    .attr('fill', function(d) { 
    if(d.category == 'R'){
    return 'red'}
    if(d.category =='B')
    return 'blue'
    if(d.category == 'G')
    return 'green'
  
  });
  //if (d.category == R){ return 'red'}
  //if (d.category == B){return 'blue'}
  //if (d.category == G){return 'green'}
    
    
    var text = bar.append('text')
    .attr('x',x)
    .attr('y',y)
    .text(function(d) {return d.category})
    .style("font-family", "sans-serif")
    .style("font-size", "11px")
    .style("fill", "black");  


  svg.on('click', function (d) {
    randDataset.apply(this); //�bar 마다 데이터를 변화
    bar.each(function (d) {
    xy.set(this, [(d.sales), (d.margin)]); // d3.local을 업데이트 
  })
    .attr('transform', function (d) { //재이동
      return 'translate(' + xy.get(this) + ')'
    });
  bar.select('circle') // 다시 높이와 색상을 그려준다.
    .attr('cx', x)
    .attr('cy', y)
    .attr('r', 4 + 'px')


  })
})

  //일일이 가서 다 써주는거 가 text
//filter() 이거는 특정 조건만 통과 시키는게 있음 저번주 과제 확인
