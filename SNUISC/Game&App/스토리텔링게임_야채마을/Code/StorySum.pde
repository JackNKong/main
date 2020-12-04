


class StorySum {

  PImage[] loadbacks;
  PImage[] backs;
  
  PFont font;

  String[][] scripts =


    {
    //case 0. tomato
    {"나는 누구일까?", "(야채도 과일도 아닌 토마토, 정체성에 혼란을 느껴 모험을 떠나게 되는데... 함께 해볼까요?)"}, 

    //case 1. tomato is at two-way
    {"흠.. 과일마을과 야채마을... 도대체 난 어느 마을로 가야하지?" }, 

    //case 2. tomato & orange
    {"넌 뭐야!! 여기 왜 알짱거려..\n야채마을로 어서 들어가!!" }, 

    //case 3. tomato @ veggie town
    {"어머머머, 쟤는 왜 여기 있는거야?", "힝... 난 뭐야 과일도 아니고 야채도 아니고 \n난 도대체 뭐냐구!!!"}, 

    //case 4. tomato runs away
    { "(텅빈 공터로 도망친다.)" }, 

    //case 5 (same as back 4) tomato & sweetp
    {"어? 너는 왜 여기 혼자 있니?", "어...어어.. 아아아년녕 나는 고구마야 사아 라암 드을이 내가 다압다압하다고 좋아하지 않아..", 
    "(크흠.. 좀 답답하긴 하군.) \n아.. 아니야. 해결할 수 있어", 
    "부우모오 님이 이이 사아라암을 만나라고 주우시긴 했는데에. 무어어인지 모오르겠어.", "오? 내가 도와줄게!!."}, 

    //case 6. SLIDE PUZZLE
    {"d"}, 

    //case 7. (same as back 4) tomato & sweetp
    {"맞췄다!! 김치인데?? 그래 고구마야 누구나 혼자서 살아갈 수는 없어.. 김치와 함께 한다면 최고의 간식이 될 수 있어!!", 
    "그으러엏구나. 아하하 고오마아워 \n아아 차암 이거 오오이 하안테 전해 줄래?", "그래 다음에 봐! 꼭 김치 만나구!!"}, 

    //case 8. tomato going to cucumber
    {"(오이 만나러 가는 중)"}, 

    //case 9. (same as back0) tomato & cucumber
    {"넌 왜 울고 있니?", "저는 맛이 없고 인기가 없어요. 사람들은 음식을 먹을 때 저만 빼고 먹어요", "아니야. 나는 그렇지 않은데?"
    , "거짓말.. 심지어 오이를 싫어하는 모임도 있다구요...", "그러지말고 이거 고구마한테 받은건데 \n같이 해보자!!"}, 

    //case 10. MEMORY GAME
    {"d"}, 

    //case 11. (same as back0) tomato & cucumber
    {"맞췄다!","제가 이렇게 인기가 많은지 몰랐어요!", "너를 싫어하는 사람보다 너를 좋아하는 사람이 훠~얼씬 많단다.", 
    "감사해요! 싫어하는 사람들의 시선만 보아서 좋아하는 사람들의 시선을 느끼지 못했어요. 저기 실의에 빠져있는 호박도 도와 주세용!"}, 

    //case 12 (same as back8) tomato going to pumpkin
    {"(호박 만나러 가는 중)"}, 

    //case 13. tomato & pumkin
    {"왜 계속 거울을 보고 있니?", "사람들이 제 표정이 안 좋대요. 웃으면서 다니 라고 하는데.. 거울을 보니 웃어도 웃는 게 아닌 거 같아요", "무슨 소리야 너 잘 웃고 있어! 거울이 문제야. 내가 닦아 줄게."},
    
    //case 14. tomato& pumpkin
    {"호박아 너는 웃는 모습이 정말 예뻐 거울이 잘못 되어 있던거야.","와~! 이게 제 웃는 얼굴이군요. 제 얼굴인데 새롭네요.","이제 사람들 앞에서도 방긋 웃으며 다니렴!!"},
    //case 15. tomato & others
    {"토마토야 고마워. 우리 모두 마을로 돌아가자.","음... 난 야채마을로 돌아갈 수 없어. 난 야채도 아니고 과일도 아닌걸... ",
  "그게 뭐가 중요해... 넌 이미 야채마을에서 빼놓을 수 없는 소중한 존재야!! 야채마을로 가자~", "..."},
  //case 16. tomato alone
    {"맞아! 내가 야채인지 과일인지는 중요하지 않아.", "난 어디든 잘 어울릴 수 있어.", "다 함게 행복하게 살자!!"}
  };



  ScriptWindow[] scriptModules;
  Characts[] chs;
  
  
  HelpButton helpB;


  StorySum() {
    scriptModules = new ScriptWindow[scripts.length];

  font = createFont("THEnamuM",48);

    loadbacks = new PImage[8];
    for (int i=0; i< loadbacks.length; i++) {
      loadbacks[i]=new PImage();
      loadbacks[i]=loadImage("back"+i+".png");
    }


backs=new PImage[scripts.length];
for (int i=0; i<backs.length; i++){
      if (i>=0 && i<=4) {
      backs[i]=loadbacks[i];
    } else if (i>=5 && i<=7) {
      backs[i]=loadbacks[4];

    } else if (i==8 || i==12) {
      backs[i]=loadbacks[5];

    } else if (i>=9 && i<=11) {
      backs[i]=loadbacks[0];

    } else if (i==13) {
      backs[i]=loadbacks[6];
    }else if (i==14){
backs[i]=loadbacks[7];

    } else{
    backs[i]=loadbacks[0];
    }
 
    PImage helpImage = loadImage("HelpStory.png");
    helpB = new HelpButton(helpImage);

 
}




    for ( int i = 0; i<scripts.length; i++) {
      scriptModules[i] = new ScriptWindow(100, 400, 600, 170, scripts[i],font);
    }


    characGenerate();
  }

  void characGenerate() {
    chs = new Characts[15];

    String[] str1 = {"ccucumber_2.png"};
    String[] str2 = {"csweetp1.png"};

    String[] str3 = {"cpumpkin3.png"};
    String[] str4 = {"ctom4.png"};

    String[] str5 = {"ccarrot.png"};
    String[] str6 = {"corange.png"};
    String[] str7 = {"ctom1.png"};
   String[] str8 = {"ctom2.png"};
      String[] str9 = {"ctom3.png"};
      String[] str10 = {"ctom5.png"};
      String[] str11 = {"ctom6.png"};  
      String[] str12 = {"ccucumber_3.png"}; 
      //
      String[] str13={"csweetp2.png"};
      String[] str14={"cpumpkin2.png"};
      String[] str15={"cveggies.png"};
      
    chs[0] = new Characts(str1);
    chs[1] = new Characts(str2);
    chs[2] = new Characts(str3);
    chs[3] = new Characts(str4);
    chs[4] = new Characts(str5);
    chs[5] = new Characts(str6);
    chs[6] = new Characts(str7);
    chs[7] = new Characts(str8);
    chs[8] = new Characts(str9);
    chs[9] = new Characts(str10);
    chs[10] = new Characts(str11);  
    chs[11] = new Characts(str12);       
    chs[12]=new Characts(str13);
    chs[13]=new Characts(str14);
    chs[14]=new Characts(str15);
  }


  void inDraw(int index, int left, int right ) {
    //background(255);
    imageMode(CENTER);
    image(backs[index],400,300);
    

    if (left>=0) {
      chs[left].left = true;
      if(scriptModules[index].page % 2 == 0){
        chs[left].jump2();
      } else{
        chs[left].inDraw();
      }
    }    

    if (right>=0) {
      chs[right].left = false;
      if(scriptModules[index].page%2 == 0){
        chs[right].inDraw();
      } else{
         chs[right].jump2(); 
      }
    }

    scriptModules[index].inDraw();
    
    helpB.inDraw();
  }

  void centerDraw(int index, int center) {
    chs[center].cenDraw();
    scriptModules[index].inDraw();
    
    helpB.inDraw();
  }

  void jumping(int index, int center) { 
    imageMode(CENTER);
    image(backs[index], 400, 300);
    chs[center].jump();
    scriptModules[index].inDraw();
    helpB.inDraw();

  }

  void inMousePressed(int index) {
    scriptModules[index].inMousePressed();
  }


 
  void reset(){
    for(int i = 0; i<scriptModules.length; i ++){
      scriptModules[i].reset();
    }
  }
}