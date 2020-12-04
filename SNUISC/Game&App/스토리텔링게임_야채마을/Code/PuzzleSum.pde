class PuzzleSum {
  Puzzle[] pieces = new Puzzle[9];
  PImage[] imgs = new PImage[9];
  PImage kimchi;
  boolean[] numSolved = {false, false, false, false, false, false, false, false, false};
  int[] location = {0, 0, 0, 0, 0, 0, 0, 0, 0};
  int[] locX = {110, 310, 510, 110, 310, 510, 110, 310, 510};
  int[] locY = {100, 100, 100, 300, 300, 300, 500, 500, 500};

  int i, u, o, tempX, tempY;
  int buX, buY, buW, buH;
  int buX2, buY2, buW2, buH2;
  
  PImage backImg;
  
  Timer timer;
  boolean timerActivated;
  
  HelpButton helpB;
  

  PuzzleSum() {
    
    for (int i = 0; i<imgs.length; i++) {
      imgs[i] = loadImage("cab"+i+".png");
    }
    kimchi = loadImage("kimchi.png");
    textAlign(CENTER);
    background(255);
    imageMode(CENTER);
    
    backImg = loadImage("back4.png");
    
    timer = new Timer(500);
    timerActivated = false;
    
    
    PImage helpImage = loadImage("HelpSlide.png");
    helpB = new HelpButton(helpImage);

    i = 0;
    while (i<9) {
      u = int(random(0, 9));
      if (location[u]==0) {
        pieces[i] = new Puzzle(locX[u], locY[u], 72, 72, imgs[i]);
        location[u] = 1;
        i++;
      }
      
    }

    for (i=0; i<9; i++) {
      //pieces[i].create();
    }
    buX = 650;
    buY = 500;
    buW = 130;
    buH = 60;
    
    buX2 = 650;
    buY2 = 400;
    buW2 = 130;
    buH2 = 60;
    
  }


  void inDraw() {
    imageMode(CENTER);
    image(backImg,400,300);

    fill(0);
    rectMode(CORNER);
    rect(buX, buY, buW, buH);
    fill(255);
    textSize(20);
    textAlign(CENTER);
    text("NEW GAME", buX+buW/2, buY+buH/2);
    
    fill(0);
    rectMode(CORNER);
    rect(buX2, buY2, buW2, buH2);
    fill(255);
    textSize(20);
    textAlign(CENTER);
    text("SKIP", buX2+buW2/2, buY2+buH2/2);
    
    if (mousePressed==true && mouseX>=buX && mouseX<=buX+buW && mouseY>=buY && mouseY<=buY+buH) {
      newPuzzle();
    }
    
      if (mousePressed==true && mouseX>=buX2 && mouseX<=buX2+buW2 && mouseY>=buY2 && mouseY<=buY2+buH2) {
      stage ++;
    }

    if ( checkSolved()==false ) {
      for (int i=0; i<9; i++) {
        if (mousePressed==true && mouseX>=(pieces[i].xpos)-85 && mouseX<=(pieces[i].xpos)+85 && mouseY>=(pieces[i].ypos)-85 && mouseY<=(pieces[i].ypos)+85 && imgs[i] != imgs[8]) {
          if (checkMove(pieces[8].xpos, pieces[8].ypos, pieces[i].xpos, pieces[i].ypos) ) {
            tempX = pieces[8].xpos;
            tempY = pieces[8].ypos;
            pieces[8].storePos(pieces[i].xpos, pieces[i].ypos);
            pieces[i].storePos(tempX, tempY);

          }
        }
        
            pieces[i].create();
    
  }
    } else {
      background(255);
      image(kimchi, width/2, height/2);
      
      if(!timerActivated){
        timer.startTimer();
        timerActivated = true;
      }
      else if(timer.isFinished()){
        stage++;
      }
      
    }
    
    helpB.inDraw();
  }

  boolean checkMove(int x8, int y8, int xi, int yi) {
    if (dist(x8, y8, xi, yi)<220 ) {
      return true;
    } else {
      return false;
    }
  }



  boolean checkSolved() {
    int u=0;
    for (int i=0; i<9; i++) {
      if ( pieces[i].xpos==locX[i] && pieces[i].ypos==locY[i] ) {
        numSolved[i]=true;
        u++;
      }
    }
    if (u==9) {
      return true;
    } else {
      return false;
    }
  }



  void newPuzzle() {
    u = 0;

    for (i=0; i<9; i++) {
      location[i] = 0;
    }

    i=0;

    while (i<9) {
      u = int(random(0, 9));
      if (location[u]==0) {
        pieces[i].storePos(locX[u], locY[u]);
        location[u] = 1;
        i++;
      }
    }

    for (i=0; i<9; i++) {
      pieces[i].create();
    }
  }
  
  
  void reset(){
    timerActivated = false;
    newPuzzle();
  }
}