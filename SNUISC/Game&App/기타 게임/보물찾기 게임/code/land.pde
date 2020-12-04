class land {
  float x, y;
  float z;
  
  land(float _x, float _y){
    x = _x;
    y = _y;

}
  
  void display(){
     fill(46,109,31);
  strokeWeight(1);
ellipse(x,y,35,30);

}

void message(String S , float z){
text(S , z ,50);}
void message2(String S , float z){
text(S , z ,80);}

void wave(float a, float b) {
fill(53,149,208);
strokeWeight(2);
stroke(255);
ellipse(a-10,b-15,10,8);
ellipse(a,b-15,10,8);
ellipse(a+10,b-15,10,8);
fill(53,149,208);
stroke(53,149,208);
rect(a-15,b-21,30,5);


fill(53,149,208);
strokeWeight(2);
stroke(255);
ellipse(a-10,b,10,8);
ellipse(a,b,10,8);
ellipse(a+10,b,10,8);
fill(53,149,208);
stroke(53,149,208);
rect(a-15,b-6,30,5);

fill(53,149,208);
strokeWeight(2);
stroke(255);
ellipse(a-10,b+15,10,8);
ellipse(a,b+15,10,8);
ellipse(a+10,b+15,10,8);
fill(53,149,208);
stroke(53,149,208);
rect(a-15,b+9,30,5);
}



}