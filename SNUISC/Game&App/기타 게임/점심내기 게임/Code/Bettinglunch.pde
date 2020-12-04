float X = 550;
float Y = 500;
float A = 550;
float B = 500;
float C = 300;

void setup(){
  size(600,600);
}

void draw(){
background(55,232,155);
  //*play ground*//
  
  strokeWeight(5);
  stroke(255);
  fill(138,187,255);
  
  quad(200,100,400,100,450,500,150,500);
  
  fill(255,241,91);
  strokeWeight(2);
  ellipse(350,Y,30,30);
  ellipse(250,B,30,30);
  
strokeWeight(4);
fill(255);
rectMode(CORNER);
rect(500,350,70,200);
rect(30,350,70,200);
rectMode(CORNERS);
fill(255,190,196);
rect(500,550,570,X);
rect(30,550,100,A);

fill(232,121,0);
strokeWeight(4);
rect(500,200,570,250);
rect(500,270,570,320);

rect(30,200,100,250);
rect(30,270,100,320);

ellipse(65,225,40,30);
ellipse(535,225,40,30);
triangle(65,280,40,310,90,310);
triangle(535,280,510,310,560,310);

if(mouseX>30 && mouseX<100 && mouseY> 200 && mouseY<250)
{fill(random(100,200),20,20);
  ellipse(65,225,40,30);
}

if( mouseX>500 && mouseX<570 && mouseY> 200 && mouseY<250)
{fill(random(100,200),20,20);
  ellipse(535,225,40,30);
}



 if (mousePressed && mouseX>500 && mouseX<570 && mouseY> 200 && mouseY<250)
  {X=X-10;}
  if (X==350){X=550;}

if (mousePressed && mouseX>500 && mouseX<570 && mouseY> 270 && mouseY<320)
{Y=Y-3;}

if (Y==X*3-1150)
{Y=Y+3;}

if (Y<=70){Y=-100;}


 if (mousePressed && mouseX>30 && mouseX<100 && mouseY> 200 && mouseY<250)
  {A=A-10;}
  if (A==350)
{A=550;}

if (mousePressed && mouseX>30 && mouseX<100 && mouseY> 270 && mouseY<320)
{B=B-3;}
if (B==A*3-1150)
{B=B+3;}

if (B<=70)
{B=-100;}



stroke(0);
strokeWeight(1);
fill(255);
noStroke();
ellipse(280,60,10,20);
ellipse(275,65,12,15);
ellipse(285,65,12,15);

fill(232,105,47);
ellipse(280,30,30,50);

fill(255);
noStroke();
ellipse(320,60,10,20);
ellipse(315,65,12,15);
ellipse(325,65,12,15);
fill(232,105,47);
ellipse(320,30,30,50);

fill(255);
noStroke();
ellipse(C,60,10,20);
ellipse(C-5,65,12,15);
ellipse(C+5,65,12,15);
fill(232,105,47);
ellipse(C,30,30,50);


}

void mousePressed(){ if(mouseX>305 && mouseX<335 && mouseY>5 && mouseY<55) {
  C=C+40;}
if(mouseX<295 && mouseX>265 && mouseY>5 && mouseY<55) {C=C-40;}

}

void keyPressed(){
  A=550;
  B=500;
  X=550;
  Y=500;
  
  
}