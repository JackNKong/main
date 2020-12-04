

class OneStroke{
  
  int y_xpos = 0;
  int y_ypos = 0;
  
  int y_w, y_h;
  
  int y_gridX, y_gridY;
  
  int[] y_goal;

  boolean y_gameOn = true;
 
  
  boolean[][] y_grid = new boolean[4][4];
  boolean[][] y_obstacle = new boolean[4][4];

  PImage mirrorClean;
PImage mirrorDirty;
PImage cleaner;

  HelpButton helpB;
  
  
  OneStroke(int y_wIn, int y_hIn){
    
    y_w = y_wIn;
    y_h = y_hIn;
    
    y_gridX = (width-y_w)/2;
    y_gridY = (height- y_h)/2;
    
    y_goal = new int[2];
    
    for(int i = 0; i <y_grid.length; i++){
      for(int j = 0; j< y_grid[0].length; j++){
        y_grid[i][j] = false;
        y_obstacle[i][j] = false;
      }
      
  }
  
  
  y_grid[1][1] = true;
  y_grid[2][1] = true;
  
  y_obstacle[1][1] = true;
  y_obstacle[2][1] = true;
  
  y_goal[0] = 0;
  y_goal[1] = 1;


mirrorClean = loadImage("mirror_c.png");
mirrorDirty = loadImage("mirror_d.png");
cleaner=loadImage("cleaningCloth.png");


      PImage helpImage = loadImage("HelpStroke.png");
    helpB = new HelpButton(helpImage);


  }
  
  
  void inDraw(){
      
  noStroke();
    
 if (y_gameOn){
   
   
  background(#744600); 
  
  fill(100);
  rectMode(CORNER);
  rect(y_gridX,y_gridY,y_w,y_h);
  
  
  imageMode(CORNER);
    for(int i = 0; i <y_grid.length; i++){
    for(int j = 0; j< y_grid[0].length; j++){
          image(mirrorDirty,y_gridX+i*y_w/4, y_gridY+j*y_h/4);
        } 
    }
  
  
 
  y_display();
  
  if(y_checkVictory()){
    y_gameOn = false;
    stage++;
  }
  
  }
  else{
   background(#794F00);
   fill(0,255,0); //light green
   rectMode(CENTER);
   rect(y_w/2, y_h/2, y_w/2, y_h/3);
    
  } 
  
  helpB.inDraw();
  }
  
  
  
  
  void y_translate(int xM, int yM){
  
  int y_intermX = y_xpos + xM;
  int y_intermY = y_ypos + yM;

  
  
  y_intermX = constrain(y_intermX, 0,3);
  y_intermY = constrain(y_intermY, 0, 3);
  
  if (!y_obstacle[y_intermX][y_intermY] &&(y_xpos != y_intermX || y_ypos != y_intermY)){
    y_grid[y_xpos][y_ypos] = true;
    
    y_xpos = y_intermX;
    y_ypos = y_intermY;
    
    if(y_grid[y_xpos][y_ypos]){
      y_reset();
    }
    
  }

}


void y_reset(){
  y_xpos = 0;
  y_ypos = 0;
  
   for(int i = 0; i <y_grid.length; i++){
    for(int j = 0; j< y_grid[0].length; j++){
      y_grid[i][j] = false;
    }
  }
  
  y_grid[1][1] = true;
  y_grid[2][1] = true;
  
  y_obstacle[1][1] = true;
  y_obstacle[2][1] = true;
  
}



void y_display(){
 
  
  
  imageMode(CORNER);
  image(mirrorDirty,y_gridX + y_goal[0]*y_w/4, y_gridY + y_goal[1]*y_h/4);
  textSize(40);
  fill(#33FF15);
  textAlign(CENTER,CENTER);
  text("FINISH",y_gridX + y_goal[0]*y_w/4, y_gridY + y_goal[1]*y_h/4,150,150);
  
  
  imageMode(CORNER);
  for(int i = 0; i <y_grid.length; i++){
    for(int j = 0; j< y_grid[0].length; j++){
      if(y_grid[i][j]){
        if(y_obstacle[i][j]){
          image(mirrorClean,y_gridX+i*y_w/4, y_gridY+j*y_h/4);
        } else{
          image(mirrorClean,y_gridX + i*y_w/4, y_gridY + j*y_h/4);
        }
        
       
        
      }
    }
  }
  
  
  imageMode(CENTER);
  image(cleaner,y_gridX+ y_w/8 + y_xpos*y_w/4, y_gridY + y_h/8+y_ypos*y_h/4);
   
}



void inKeyPressed(int keyIn){
 if(keyIn == UP){
   y_translate(0,-1);
 }
 
 if(keyIn == DOWN){
   y_translate(0,1);
 }
 
 if(keyIn == LEFT){
   y_translate(-1,0);
 }
 
 if(keyIn == RIGHT){
   y_translate(1,0);
 }
 
 if(keyIn == ENTER){
   y_gameOn = true;
   y_reset(); 
 }
   
}

 boolean y_checkVictory(){
  
  int y_victoryC =0;
  
  
  for(int i = 0; i <y_grid.length; i++){
    for(int j = 0; j< y_grid[0].length; j++){
      if(!y_grid[i][j]){
        y_victoryC += 1;
      }
    }
  }
  
  if(y_victoryC <= 1 && y_xpos == y_goal[0] && y_ypos == y_goal[1]){
    return true;
  } else{
   return false; 
  }
  
}
  
  void reset(){
    y_reset();
    y_gameOn = true;
  }
  
}