

class HelpButton{
  int cx, cy;
  int r;
  PImage img;
  
  color backC = color(255,255,0);
  color textC = color(#008AFF);
  
  HelpButton(PImage imgIn){
    img = imgIn;
    
    cx = 760;
    cy = 40;
    r=18;
    
    img = imgIn;
  }
  
  
  void inDraw(){
    
    noStroke();
    
        
    if(mouseOn()){
      imageMode(CORNER);
      image(img, 400,0,400,300);
    }
    
    
    ellipseMode(CENTER);
    fill(backC);
    ellipse(cx,cy,r*2,r*2);
    
    textAlign(CENTER,CENTER);
    fill(textC);
    textSize(30);
    text("?",cx,cy);
    

  }


  boolean mouseOn(){
    if(dist(mouseX,mouseY,cx,cy) < r){
      return true;
    }  else{
      return false;
    }
  }

}