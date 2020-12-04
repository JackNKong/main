class Boat {
  float x, y;
  
  Boat(){
    x = 200;
    y = 520;
  }
  
  void display(){
    fill(255);
    rect(x-11,y+10,22,24);
fill(255,242,0);
quad(x-10,y,x+10,y,x+5,y+10,x-5,y+10);

quad(x-10,y,x-5,y+10,x-11,y+17,x-22,y+11);
quad(x-11,y+17,x-22,y+11,x-22,y+32,x-11,y+27);
quad(x-22,y+32,x-11,y+27,x-6,y+33,x-11,y+43);

quad(x+10,y,x+5,y+10,x+11,y+17,x+22,y+11);
quad(x+11,y+17,x+22,y+11,x+22,y+32,x+11,y+27);
quad(x+22,y+32,x+11,y+27,x+6,y+33,x+11,y+43);
quad(x-6,y+33,x-11,y+43,x+11,y+43,x+6,y+33);


fill(125);
ellipse(x,y+22,17,17);
line(x+7.5,y+22,x+30,y+22);
line(x-7.5,y+22,x-30,y+22);
quad(x+30,y+19,x+30,y+25,x+38,y+27,x+38,y+17);
quad(x-30,y+19,x-30,y+25,x-38,y+27,x-38,y+17);
}


void move()
{ if(keyPressed) {
  if (keyCode == UP) {y = y-1.5;
background(255);}
  if (keyCode == LEFT) {x = x -1.5; 
  background(255);}
  if (keyCode == RIGHT) {x = x+1.5;
  background(255);}
  if (keyCode == DOWN) {y = y+1.5;}
}
}

boolean touched(float x1,float y1){
 
  if ( dist(x,y+22, x1, y1)< 42){
  return true;}
  else return false;
}
void restart(){
  x = 200; y = 520;}
}