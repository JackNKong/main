

class ResetWindow{
  
  int cx;
  boolean on;
  PImage backImg;
  
  PImage yesImg;
  PImage noImg;

  ResetWindow(){
    
    cx = width/2;
    on = false;
    
    backImg = loadImage("restartBack.png");
    yesImg = loadImage("YesButton.png");
    noImg = loadImage("NoButton.png");
    
  }
  
  
  void inDraw(){

    
    imageMode(CENTER);
    image(backImg,width/2,height/2);
    
    
    rectMode(CENTER);
    fill(175);
    noStroke();
    
    
    imageMode(CENTER);
    image(noImg,width/3,height*2/3);
    image(yesImg,width*2/3,height*2/3);
    
    if((mouseX<width/3+100 && mouseX > width/3-100 && mouseY <height*2/3 + 50 && mouseY > height*2/3-50) || (mouseX<width*2/3+100 && mouseX > width*2/3-100 && mouseY <height*2/3 + 50 && mouseY > height*2/3-50)){
     cursor(HAND);
    } else{
     cursor(ARROW); 
    }
  
    
  }
  
  
  void inMousePressed(){
    if(mouseX<width/3+100 && mouseX > width/3-100 && mouseY <height*2/3 + 50 && mouseY > height*2/3-50){
      switchOnoff();
      cursor(ARROW);
    }
    if(mouseX<width*2/3+100 && mouseX > width*2/3-100 && mouseY <height*2/3 + 50 && mouseY > height*2/3-50){
      reset();
      switchOnoff();
      cursor(ARROW);
    }
  }
  
  
  void switchOnoff(){
    on = !on;
  }
  
  
  void reset(){
  stage = -1;
  
  memoryModule.reset();
  storyModule.reset();
  puzzleModule.reset();
  stroke.reset();
  
}


  void inKeyPressed(int keyIn){
    if(keyIn == TAB){
      switchOnoff();
      cursor(ARROW);
    }
  }
  
  boolean isOn(){
    return on;
  }
}