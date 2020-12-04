

class ScriptWindow{

  int x, y, w, h;
  int page;
  
  String[] script;
  

  PFont font;
  
  ScriptWindow(int xIn,int yIn, int wIn, int hIn, String[] scriptIn, PFont fontIn){
    x = xIn;
    y = yIn;
    w = wIn;
    h = hIn;
    
    script = scriptIn;
    
    page = 0;
    
    font = fontIn;
    


  
  }
  
  
  boolean isClicked(){
    if (mouseX > x && mouseX < x+w && mouseY > y && mouseY < y+h){
      return true;
    }
    else {
      return false;
    }
  }
  
  
  void inMousePressed(){

   if(isClicked()){
     page += 1;
   } 
   

  }
  
  
  
  
  void inDraw(){
    
     if(page >= script.length){
       stage += 1;     
     } else{
       
      rectMode(CORNER);
      fill(#6F4400,200);
      rect(x,y,w,h,20);
      

      textFont(font,30);
      
     
      textAlign(LEFT);
      fill(255);
      stroke(255);
      text(script[page], x+20,y+20,x+460,y+150);
       
     }
     

  }
  
  
   int getPage(){
    return page; 
   }
  
  void reset(){
    page = 0;
    
  }

}