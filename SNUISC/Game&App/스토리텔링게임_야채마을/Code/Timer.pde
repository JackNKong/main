
class Timer {
 int savedTime;
 int totalTime;
 
 Timer(int temp){
  savedTime = temp;
  totalTime = temp;
 }
 
 void startTimer(){
  savedTime = millis(); 
 }
 
 boolean isFinished(){
   int timePassed = millis() - savedTime;
   if(timePassed >totalTime){
    return true; 
   }
   else{
    return false; 
   }
 }
  
}