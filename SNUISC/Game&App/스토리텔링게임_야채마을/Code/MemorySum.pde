

class MemorySum{
  
  Timer timer;

  Card[] cards;
  

  int firstCard=-1, secondCard=-1;
  int checkpoint = 0;
  
  HelpButton helpB;
   
  MemorySum(){

    cards = new Card[8];
    
    int count = 0;
    for (int i=0; i<2; i++) {
    for (int j=0; j<4; j++) {
      cards[count] = new Card (10+200*j, 20+290*i, 180, 270, 0);
      count += 1;
    }
    
    timer = new Timer(200);
    
    PImage helpImage = loadImage("HelpMemory.png");
    helpB = new HelpButton(helpImage);

    
    //println(count);
  }


   
   shuffle();
  }
  
  
   void shuffle(){
    int[] values = new int[8];
      
   for (int i=0; i<values.length/2; i++) {
    values[2*i] = i;
    values[2*i+1] = i;
   }
     
  for (int i=0; i<values.length; i++) {
    int r = int(random(values.length));
    int t = values[i];
    values[i] = values[r];
    values[r] = t;
  }
 
 for(int i = 0; i<cards.length; i++){
   cards[i].setImage(values[i]);
 }
  
    
  }
  
  
  void inDraw(){

   background(#FDFF8E);
    
   for (int t=0; t<cards.length;t++){ 
     cards[t].draw ();
   };
   
   if(firstCard>=0 && secondCard>=0){
   if(timer.isFinished()){
     checkMatch();
   }}
  
  if (checkpoint == 4) {
    background(0);
    text("clear!", width/2, height/2);
    stage ++;
    
  }
  
  helpB.inDraw();
  
  }
  
void inMousePressed(){
  
  if(timer.isFinished()){
  if(firstCard >= 0 && secondCard >= 0){
    checkMatch();
    println("bothup");
     for(int i = 0; i<cards.length; i++){
       cards[i].face_up = false;
     }
     
     firstCard = -1;
     secondCard = -1;
   
  }
 else{
 for(int i = 0; i<cards.length; i++){
   if(cards[i].mouseOverCard()){
    if(i != firstCard){
     cards[i].clicked();
     
     if(firstCard < 0){
       firstCard = i;
     }
     else{
       secondCard = i;

       //checkMatch();
       if(cards[firstCard].v == cards[secondCard].v){
         timer.startTimer();
       }

     }
     
    }
     
   }
 }}}
 
 }
 
 
 void checkMatch(){
   
   if(cards[firstCard].v == cards[secondCard].v){
     cards[firstCard].hide =true;
     cards[secondCard].hide = true;
     
     firstCard = -1;
     secondCard = -1;
     
     checkpoint++;
     
     
   }
   
   
  
 }
 
 
 void reset(){
   checkpoint = 0;
   firstCard = -1;
   secondCard = -1;
   
   shuffle();
   
   for(int i = 0 ; i< cards.length; i++){
     cards[i].reset();
   }
 }
  
}