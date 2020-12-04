    float centerA=150;
  float centerB=150;
  float centerC=150;
  float centerD=50;
  float centerE=10;

float angleA=0;
float angleB=0.5;
float angleC=1;
float angleD=0;
float angleE=1;

float snailX=-350;
float snailY=430;
void setup(){
  size(600,600);

}
void draw(){
  background(144,120,255);
  
//*cloud*//
noStroke();
fill(44,255,232);
ellipse(80,110,70,50);
ellipse(100,95,50,60);
ellipse(130,100,50,70);
ellipse(160,110,60,50);
ellipse(130,130,50,40);
ellipse(100,130,50,40);

ellipse(420,60,70,50);
ellipse(440,45,50,60);
ellipse(470,50,50,70);
ellipse(500,60,60,50);
ellipse(470,80,50,40);
ellipse(440,80,50,40);

ellipse(260,150,70,50);
ellipse(280,135,50,60);
ellipse(310,140,50,70);
ellipse(340,150,60,50);
ellipse(310,170,50,40);
ellipse(280,170,50,40);




//*mountain*//
noStroke();




    fill(70,200,1);
  triangle(600,100,570,125,600,125);
    fill(73,203,4);
  quad(570,125,540,150,600,150,600,125);
    fill(76,206,7);
  quad(540,150,510,175,600,175,600,150);
    fill(80,210,10);
  quad(510,175,480,200,600,200,600,175);
    fill(83,213,1);
  quad(480,200,450,225,600,225,600,200);
    fill(86,216,1);
  quad(450,225,420,250,600,250,600,225);
    fill(90,220,1);
  quad(420,250,390,275,600,275,600,250);
      fill(93,223,1);
  quad(390,275,360,300,600,300,600,275);
      fill(96,226,1);
  quad(360,300,330,325,600,325,600,300);
      fill(100,230,1);
  quad(330,325,300,350,600,350,600,325);
      fill(103,233,1);
  quad(300,350,270,375,600,375,600,350);
      fill(106,236,1);
  quad(270,375,240,400,600,400,600,375);
      fill(110,240,1);
  quad(240,400,210,425,600,425,600,400);
      fill(113,243,1);
  quad(210,425,180,450,600,450,600,425);
      fill(116,246,1);
  quad(180,450,150,475,600,475,600,450);  
      fill(120,250,1);
  quad(150,475,120,500,600,500,600,475);
      fill(123,253,1);
  quad(120,500,90,525,600,525,600,500);
      fill(126,255,1);
  quad(90,525,60,550,600,550,600,525);
      fill(130,255,1);
  quad(60,550,30,575,600,575,600,550);
      fill(133,255,1);
  quad(30,575,00,600,600,600,600,575);


stroke(0);
noFill();

//*circles*//

  centerA=centerA+8*sin(angleA);
  centerB=centerB+10*sin(angleB);
  centerC=centerC+9*sin(angleC);
  centerD=centerD+5*sin(angleD);
  centerE=centerE+11*sin(angleE);
  angleA=angleA+0.01;
  angleB=angleB+0.03;
  angleC=angleC+0.04;
  angleD=angleD+0.01;
  angleE=angleE+0.02;
  
  
  noStroke();
  fill(255,255,150);
  ellipse(100,centerA,25,35);
  ellipse(200,centerB,25,35);
    ellipse(350,centerC,25,35);
    ellipse(400,centerD,25,35);
    ellipse(500,centerE,25,35);
stroke(0);
noFill();

//*snail*//

rotate(radians(-40));

noStroke();
fill(228,255,107);
ellipse(snailX,snailY-50,100,25);
quad(snailX+40,snailY-50,snailX+30,snailY+30,snailX+35,snailY+30,snailX+45,snailY-50);




strokeWeight(0.2);
fill(250,148,250);
ellipse(snailX-5,snailY,45,55);

strokeWeight(6);
stroke(232,100,97);
fill(242,148,217);
ellipse(snailX-5,snailY,24,40);

strokeWeight(0.2);
fill(217,85,109);
ellipse(snailX-5,snailY,10,18);


noStroke();
fill(97,232,205);
quad(snailX+18,snailY+28,snailX+16,snailY-10,snailX+20,snailY-10,snailX+23,snailY+28);
quad(snailX+24,snailY+28,snailX+26,snailY-10,snailX+30,snailY-10,snailX+29,snailY+28);
ellipse(snailX-5,snailY+30,70,10);

fill(242,229,189);
ellipse(snailX+28,snailY-18,15,15);
ellipse(snailX+17,snailY-18,15,15);
fill(11,15,38);
ellipse(snailX+28,snailY-18,6,6);
ellipse(snailX+17,snailY-18,6,6);

}




void keyPressed() {
  snailX=snailX+15;
}

 