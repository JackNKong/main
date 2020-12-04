class Card {
  PImage icon;
   String [] filenames = {
     "cucum_card1.png",
     "cucum_card2.png",
     "cucum_card3.png",
     "cucum_card4.png"
  };
  PImage backing;
  
  
  float x, y, w, h;
  int v;
  boolean face_up, hide; 
  
  
  
  Card(float ix, float iy, float iw, float ih,int value) {
    x=ix;
    y=iy;
    w=iw;
    h=ih;
    
    face_up=false;
    hide=false;
    
   backing = loadImage("backside.png");
    
    v= value;
    
   setImage(value); 
      
  }
  
  void setImage(int value){
    v = value;
    icon = loadImage(filenames[value]);
  }
 
  
  
  void draw() {
    if (!hide) {
      imageMode(CORNER);
      if (!face_up) {
  
        image(backing, x, y);
        w=backing.width;
        h=backing.height;
      } else {
        image(icon, x, y);
        w=icon.width;
        h=icon.height;
      }
      noFill();
      stroke(#353535);
      if (mouseOverCard()) stroke(#08B3FF);
      rectMode(CORNER);
      rect(x, y, w, h);
    }
  }
  
  
  boolean mouseOverCard() {
    return(!hide && mouseX >= x && mouseX < x+w && mouseY >= y && mouseY < y+h);
  }
 
  void clicked() {
    
      face_up = !face_up;
      
    }
    
    
    void reset(){
      face_up=false;
      hide = false;
    }
  }