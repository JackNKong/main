Boat boat = new Boat();
land land1 = new land(80,420);
land land2 = new land(200,400);
land land3 = new land(330,440);
land land4 = new land(250,300);
land land5 = new land(120,270);
land land6 = new land(50,170);
land land7 = new land(200,180);
land land8 = new land(320,200);
 





void setup() {
  size(400,600);
PFont font;

font = loadFont("NanumPen-30.vlw");
textFont(font,30);
}

void draw(){
  imageMode(CORNER);
  //island//

  //island//
noStroke();
boat.move();

if (boat.touched(80,420) ||
boat.touched(200,400) ||
boat.touched(330,440) ||
boat.touched(250,300) ||
boat.touched(120,270) ||
boat.touched(50,170) ||
boat.touched(200,180) ||
boat.touched(320,200) ||
boat.touched(50,250))
{background(53,149,208);}  
else { background(53,149,208);
text("섬들을 모험하여 보물섬을 찾아라!" , 70,70);}

land1.display();
land2.display();
land3.display();
land4.display();
land5.display();
land6.display();
land7.display();

land1.wave(330,350);
land1.wave(50,250);
land1.wave(270,400);
land1.wave(190,280);
if (boat.touched(350,350)){boat.restart();}

if (boat.touched(270,400)){boat.restart();}
if (boat.touched(190,280)){boat.restart();}




strokeWeight(1);
 boat.display();
fill(255);
text("방향키이동", 280,520);
text("멈춤 >'S'", 280,550);

if (boat.touched(80,420)){land1.message("섬에 있는 할아버지를 만나다!",100);
land1.message2("목적지는 아직 보이지 않아. 허허",100);
fill(255);
rect(25,25,60,60);
PImage img1;
img1 = loadImage("granpa.png"); 
image(img1,25,25,60,60);
}
else{text("" , 120,50);}

//////////////

if (boat.touched(200,400)){land2.message("인디언을 만나다!?",100);
land2.message2("파도 근처에는 얼씬도 말게나!!",100);
fill(255);
rect(25,25,60,60);
PImage img2;
img2 = loadImage("indian.jpg"); 
image(img2,10,25,75,60);
}
//////////////

if (boat.touched(330,440)){land3.message("비석에 뭐라고 써져있다!",100);
land3.message2("파도도 높은데 뭐하러 왔어ㅋ",100);
fill(255);
rect(25,25,60,60);
PImage img3;
img3 = loadImage("stone.jpg"); 
image(img3,10,25,75,60);

}
else{text("" , 120,50);}

///////////////////////

if (boat.touched(250,300)){
land4.message("비석에 의미심장한 말이!?",100);
land4.message2("결과보다는 과정이 중요하다네..",100);
fill(255);
rect(25,25,60,60);
PImage img4;
img4 = loadImage("stone.jpg"); 
image(img4,10,25,75,60);}
else{text("" , 120,50);}


///////////////////////////////////
if (boat.touched(120,270)){
land5.message("여긴 아무도 없는건가??",100);
land5.message2("무인도 인듯 하다 ㅠㅠ",100);
fill(255);
rect(25,25,60,60);
PImage img5;
img5 = loadImage("island.jpg"); 
image(img5,10,25,75,60);}
else{text("" , 120,50);}


if (boat.touched(50,170)){land6.message("외딴 섬에 스위치가?",100);
land6.message2("스위치를 누를때만 드러나는 섬이?! ",100);
fill(255);
rect(25,25,60,60);
fill(125);
  ellipse(55,55,55,55);
  fill(217,121,65);
  ellipse(55,55,40,40);
  land8.display();
  

}
else{text("" , 120,50);}
if (boat.touched(200,180)){
land7.message("야호! 등대를 발견하였다!!",100);
land7.message2("왼쪽방향을 가르키는거 같다.. ",100);
fill(255);
rect(20,25,65,75);
PImage img7;
img7 = loadImage("lighthouse.png"); 
image(img7,22,25,60,75);}
  

else{text("" , 120,50);}
if (boat.touched(320,200)){
  land8.message("아까 그 할아버지?!",100);
land8.message2("가장 왼쪽 파도에는 보물이 있다네~",100);
fill(255);
rect(25,25,60,60);
PImage img8;
img8 = loadImage("granpa.png"); 
image(img8,25,25,60,60);}
else{text("" , 120,50);}

if (boat.touched(50,250)){
  fill(255);
 land5.message("자네가 헤쳐온 과정이 모두 보물이라네",80);
land5.message2(" - 낚시꾼 할아버지가..",180);
fill(255);

PImage img5;
img5 = loadImage("last.png"); 
image(img5,10,25,60,50);}
else{text("" , 120,50);}

fill(255);
noStroke();
rect(20,530,90,40);
fill(0);
text("다시하기",30,560);
fill(255);  
}

void mousePressed(){
  if(mouseX >=20 && mouseX <=110 &&
  mouseY >=530 && mouseY <=570) {boat.restart();}
}