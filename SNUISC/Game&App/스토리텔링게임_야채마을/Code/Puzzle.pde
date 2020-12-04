class Puzzle{
  
  int value, xpos, ypos, w, h;
  PImage img;
 
 Puzzle(int xval, int yval, int wid_th, int heig_th, PImage _img){
  xpos = xval;
  ypos = yval;
  img = _img;
  w = wid_th; //width of a puzzle tile 
  h = heig_th;//height of a puzzle tile 
 }

  void storePos(int xval, int yval){
    xpos = xval;
    ypos = yval;
  }
  
  void create(){
    image(img, xpos, ypos);
  }
  
}