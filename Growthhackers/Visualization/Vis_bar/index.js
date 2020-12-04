//d3.select("div.container").append("p").text("새 문단 추가");

//위랑 아래가 똑같은소리 컨테이널르 가져오고 거기에 p를 추가
//var container = d3.select("div.container");
//var p = container.append("p");
//p.text("새 문단 추가");

var dataset = [200, 300, 400, 500, 100];

d3.select("div.container")
  .selectAll("p") //
  .data(dataset) //데이터 연결
  .enter().append('p') //엔터는 가상의 자리를 만들어놔라 그리고 피추가
  .text(function(d,i){
      return d;
  })
  .attr("class", function(d,i){
      return 'h'+(i+1)
  })
var dataset = [200, 300, 400, 500, 100];

  
  //일일이 가서 다 써주는거 가 text

