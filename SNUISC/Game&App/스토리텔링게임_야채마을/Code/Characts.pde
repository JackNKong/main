

class Characts {

  PImage[] imgs;
  boolean left;
  int index;
  
  float hc_ypos;
  float angle1;
  float scalar=50;


  Characts(String[] fileNames) {

    imgs = new PImage[fileNames.length];

    for (int i = 0; i<imgs.length; i++) {
      imgs[i] = new PImage();
      imgs[i] = loadImage(fileNames[i]);
    }

    index = 0;

    left = true;
  }

  void changeIndex(int iIn) {
    index = iIn;
  }

  void inDraw() {

    imageMode(CENTER);
    hc_ypos=250;
    if (left) {
      image(imgs[index], 200, hc_ypos);
    } else {
      image(imgs[index], 600, hc_ypos);
    }
  }

  void cenDraw() {
    imageMode(CENTER);
    hc_ypos=250;
    image(imgs[index], 400, hc_ypos);
  }

  void jump() {
    imageMode(CENTER);
    float ang1 = radians(angle1);
    hc_ypos = 250 + (0.5*scalar * sin(ang1*2));
    angle1 += 2;
    image(imgs[index],400,hc_ypos);

  }
  

  
  void jump2() {
    imageMode(CENTER);
    float ang1 = radians(angle1);
    hc_ypos = 250 + (0.5*scalar * sin(ang1*2));
    angle1 += 2;
    
    if(left == true){
    image(imgs[index],200,hc_ypos);
    } else{
     image(imgs[index],600, hc_ypos); 
    }

  }
}