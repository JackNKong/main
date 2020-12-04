
int stage;

StorySum storyModule;
PuzzleSum puzzleModule;
MemorySum memoryModule;
OneStroke stroke;
ResetWindow resetModule;
import processing.sound.*;
SoundFile sample;


PImage startImg;
PImage endImg;





void setup() {
  size(800, 600);
  


  memoryModule = new MemorySum();
  storyModule = new StorySum();
  puzzleModule = new PuzzleSum();
  stroke = new OneStroke(600, 600);
  
  resetModule = new ResetWindow();
  
  startImg = loadImage("START.png");
  endImg = loadImage("END.png");
  
  stage = -1;
  
  
  sample = new SoundFile(this, "cute.mp3");
  sample.loop();

}


void draw() {
  
  if(resetModule.isOn()){
    resetModule.inDraw();
  }
  
  else{

  switch(stage) {
  
    case -1:
      imageMode(CENTER);
      image(startImg,width/2,height/2);
      break;
   
  case 0: //Tomato Alone
    storyModule.jumping(0, 7);

    
    break;

  case 1: //Tomato at Two-Way
    storyModule.jumping(1, 9);
    break;

  case 2: //Tomato & Orange @ FruitTown
    storyModule.inDraw(2, 5, 8);
    
    break;

  case 3: //Tomato @ VeggieTown
    storyModule.inDraw(3, 4, 8);
    break;

  case 4: //Tomato runs away
    storyModule.jumping(4, 10);
    break;


  case 5: //Tomato & SweetPotato
    storyModule.inDraw(5, 9, 1);
    break;

  case 6: //SlidePuzzle
    puzzleModule.inDraw();
    break;

  case 7: //Tomato & SweetPotato
    storyModule.inDraw(7, 3, 12);
    break;


  case 8: //Tomato going to cucumber
    storyModule.jumping(8,3);
    break;

  case 9: //Tomato & Cucumber

    storyModule.inDraw(9, 3, 0);
    break;      

  case 10:
    memoryModule.inDraw();
    break;  

  case 11: //Tomato & Cucumber
    storyModule.inDraw(11, 3, 11);
    break; 

  case 12: //Tomato going to pumpkin

    storyModule.jumping(12, 3);
    break;


  case 13: //Tomato & Pumpkin
    storyModule.inDraw(13, 3, 2);
    break;


  case 14:
         stroke.inDraw();
    break; 
    
  case 15:
   storyModule.inDraw(14, 3, 13);
  break;

  case 16:
       storyModule.inDraw(15, 14, 8);
    break; 
  case 17:
       storyModule.jumping(16, 3);
    break;  
    
  case 18:
       imageMode(CENTER);
     image(endImg,width/2,height/2);
     break;



  default:
  }
  
  }
}



void mousePressed() {
  if(resetModule.isOn()){
    resetModule.inMousePressed();
  }
  
  else{
  
  switch(stage) {
  case 0 :
    //storyModule.switchOn(0);
    storyModule.inMousePressed(0);
    break;

  case 1:
    //storyModule.switchOn(1);
    storyModule.inMousePressed(1);
    break;

  case 2:
    //storyModule.switchOn(2);
    storyModule.inMousePressed(2);
    break;

  case 3:
    //storyModule.switchOn(3);
    storyModule.inMousePressed(3);
    break;   

  case 4:
    //storyModule.switchOn(4);
    storyModule.inMousePressed(4);
    break;   

  case 5:
    //storyModule.switchOn(5);
    storyModule.inMousePressed(5);
    break;   
    
  case 6:
    //storyModule.switchOn(6);
    storyModule.inMousePressed(6);
    break;        

  case 7:
    //storyModule.switchOn(7);
    storyModule.inMousePressed(7);
    break; 

  case 8:
    //storyModule.switchOn(8);
    storyModule.inMousePressed(8);
    break;  


  case 9:
    //storyModule.switchOn(9);
    storyModule.inMousePressed(9);
    break; 

  default:
  case 10:
    memoryModule.inMousePressed();
    //storyModule.switchOn(10);
    storyModule.inMousePressed(10);
    break;

  case 11:
    //storyModule.switchOn(11);
    storyModule.inMousePressed(11);
    break;

  case 12:
    //storyModule.switchOn(12);
    storyModule.inMousePressed(12);
    break;

  case 13:
    //storyModule.switchOn(13);
    storyModule.inMousePressed(13);
    break;

  case 14:
    break;
  
  case 15:
   storyModule.inMousePressed(14);
  break;
  
  case 16:
    storyModule.inMousePressed(15);
    break;
  case 17:
    storyModule.inMousePressed(16);
    break;  
   case 18:
    resetModule.reset();
    
   break;
    

}
  }

}


void keyPressed() {
  
  if(!resetModule.isOn()){
  switch(stage) {
    case -1:
      if(keyCode == RETURN || keyCode == ENTER){
        stage++;
      }
      break;
  case 14:
    stroke.inKeyPressed(keyCode);
    break;
    
   case 18:
      if(keyCode == RETURN || keyCode == ENTER){
        resetModule.reset();
      }
     break;
  }
  
  }
  
  resetModule.inKeyPressed(keyCode);
 
}