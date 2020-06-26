#include <iostream>

int SRcorr(float mll, float mT, float met, float ht, int offset = 0) {

    if(              mll <  75 && ht >=  0 && ht < 200) {
        if(mT >=   0 && mT < 100 && met >=   0 && met < 100) return offset +  1;
        if(mT >=   0 && mT < 100 && met >= 100 && met < 150) return offset +  2;
        if(mT >=   0 && mT < 100 && met >= 150 && met < 200) return offset +  3;
        if(mT >=   0 && mT < 100 && met >= 200             ) return offset +  4;
        if(mT >= 100 && mT < 160 && met >=   0 && met < 100) return offset +  5;
        if(mT >= 100 && mT < 160 && met >= 100 && met < 150) return offset +  6;
        if(mT >= 100 && mT < 160 && met >= 150             ) return offset +  7;
        if(mT >= 160 &&             met >=   0 && met < 100) return offset +  8;
        if(mT >= 160 &&             met >= 100 && met < 150) return offset +  9;
        if(mT >= 160 &&             met >= 150 && met < 200) return offset + 10;
        if(mT >= 160 &&             met >= 200             ) return offset + 11;
    }
    if(              mll <  75 && ht >= 200            ) {
        if(mT >=   0 && mT < 100                           ) return offset + 12;
        if(mT >= 100 && mT < 160                           ) return offset + 13;
        if(mT >= 160                                       ) return offset + 14;
    }
    if(mll >=  75 && mll < 105 && ht >=  0 && ht < 100) {
        if(mT >=   0 && mT < 100 && met >=   0 && met < 100) return 0          ; // this is the WZ CR !
        if(mT >=   0 && mT < 100 && met >= 100 && met < 150) return offset + 15;
        if(mT >=   0 && mT < 100 && met >= 150 && met < 200) return offset + 16;
        if(mT >=   0 && mT < 100 && met >= 200 && met < 250) return offset + 17;
        if(mT >=   0 && mT < 100 && met >= 250             ) return offset + 18;
        if(mT >= 100 && mT < 160 && met >=   0 && met < 100) return offset + 19;
        if(mT >= 100 && mT < 160 && met >= 100 && met < 150) return offset + 20;
        if(mT >= 100 && mT < 160 && met >= 150 && met < 200) return offset + 21;
        if(mT >= 100 && mT < 160 && met >= 200             ) return offset + 22;
        if(mT >= 160 &&             met >=   0 && met < 100) return offset + 23;
        if(mT >= 160 &&             met >= 100 && met < 150) return offset + 24;
        if(mT >= 160 &&             met >= 150 && met < 200) return offset + 25;
        if(mT >= 160 &&             met >= 200             ) return offset + 26;
    }
    if(mll >=  75 && mll < 105 && ht >= 100 && ht < 200) {
        if(mT >=   0 && mT < 100 && met >=   0 && met < 100) return offset + 27;
        if(mT >=   0 && mT < 100 && met >= 100 && met < 150) return offset + 28;
        if(mT >=   0 && mT < 100 && met >= 150 && met < 200) return offset + 29;
        if(mT >=   0 && mT < 100 && met >= 200 && met < 250) return offset + 30;
        if(mT >=   0 && mT < 100 && met >= 250             ) return offset + 31;
        if(mT >= 100 && mT < 160 && met >=   0 && met < 100) return offset + 32;
        if(mT >= 100 && mT < 160 && met >= 100 && met < 150) return offset + 33;
        if(mT >= 100 && mT < 160 && met >= 150 && met < 200) return offset + 34;
        if(mT >= 100 && mT < 160 && met >= 200             ) return offset + 35;
        if(mT >= 160 &&             met >=   0 && met < 100) return offset + 36;
        if(mT >= 160 &&             met >= 100 && met < 150) return offset + 37;
        if(mT >= 160 &&             met >= 150 && met < 200) return offset + 38;
        if(mT >= 160 &&             met >= 200             ) return offset + 39;
    }
    if(mll >=  75 && mll < 105 && ht >= 200            ) {
        if(mT >=   0 && mT < 100 && met >=   0 && met < 150) return offset + 40;
        if(mT >=   0 && mT < 100 && met >= 150 && met < 250) return offset + 41;
        if(mT >=   0 && mT < 100 && met >= 250 && met < 350) return offset + 42;
        if(mT >=   0 && mT < 100 && met >= 350             ) return offset + 43;
        if(mT >= 100 && mT < 160 && met >=   0 && met < 100) return offset + 44;
        if(mT >= 100 && mT < 160 && met >= 100 && met < 150) return offset + 45;
        if(mT >= 100 && mT < 160 && met >= 150 && met < 200) return offset + 46;
        if(mT >= 100 && mT < 160 && met >= 200 && met < 250) return offset + 47;
        if(mT >= 100 && mT < 160 && met >= 250 && met < 300) return offset + 48;
        if(mT >= 100 && mT < 160 && met >= 300             ) return offset + 49;
        if(mT >= 160 &&             met >=   0 && met < 100) return offset + 50;
        if(mT >= 160 &&             met >= 100 && met < 150) return offset + 51;
        if(mT >= 160 &&             met >= 150 && met < 200) return offset + 52;
        if(mT >= 160 &&             met >= 200 && met < 250) return offset + 53;
        if(mT >= 160 &&             met >= 250 && met < 300) return offset + 54;
        if(mT >= 160 &&             met >= 300             ) return offset + 55;
    }
    if(mll >= 105                                      ) {
        if(mT >=   0 && mT < 100                           ) return offset + 56;
        if(mT >= 100 && mT < 160                           ) return offset + 57;
        if(mT >= 160                                       ) return offset + 58;
    } 
    return 0;
}


int unused4(int id1, int id2, int ord){
    int idx = 0;
    for (int i = 0; i< 4; i ++){
        if (i == id1 || i == id2){continue;}
        else idx++;
        if (idx == ord) return i;
    }
    return -1;
}

bool isFake(int mcTag, int pdgId, bool requireid = false, int requiredpdgId = 0){
  if (pdgId != requiredpdgId && requireid) return false;
  else if(mcTag%10 == 2 || mcTag%10 == 3 || mcTag%10 == 9 || mcTag%-1 == 0) return true;
  else return false;
}


int SR_ewk_ss2l_v6_plot(float mt2, float met, float ptll, float ptdil, float mtW, float charge){
  int SR = 1;
  if (mt2 == 0){
      if (ptll < 70){
          if (met < 100) SR =  2;
          else if (met < 150 && charge > 0) SR =  3;
          else if (met < 150 && charge < 0) SR =  4;
          else if (charge > 0) SR =  5;
          else if (charge < 0) SR = 6;
      }
  }
  else if (mt2 < 80){
      if (ptdil < 30){
          if (met < 200 && charge > 0) SR = 7;
          else if (met < 200 && charge < 0) SR = 8;
          else if (charge > 0) SR = 9;
          else if (charge < 0) SR = 8;
      }
      else {
          SR=10;
      }
  }
  else if (mt2 >= 80){
      if (met < 100 && ptll < 200) SR = 11;
      else if (met < 200 && ptll < 200 && charge > 0) SR = 12;
      else if (met < 200 && ptll < 200 && charge < 0) SR = 13;
      else if (ptll < 200 && charge > 0) SR = 14;
      else if (ptll < 200 && charge < 0) SR = 15;
      if (ptll > 200){
          if (met < 100) SR =  16;
          else if (met < 200 && charge > 0) SR =  17;
          else if (met < 200 && charge < 0) SR =  18;
          else if (met < 900 && charge > 0) SR =  19;
          else if (met < 900 && charge < 0) SR =  20;
          else SR = 20;
      }
  }
  return SR;   
}


float WZunc(float met, float mt, int var = 0){
  if (mt>=  0 && mt<100 && met>= 50 && met<100) return (1 + var*0.05);
  if (mt>=  0 && mt<100 && met>=100 && met<150) return (1 + var*0.10);
  if (mt>=  0 && mt<100 && met>=150 && met<200) return (1 + var*0.20);
  if (mt>=  0 && mt<100 && met>=200           ) return (1 + var*0.20);
  if (mt>=100 && mt<160 && met>= 50 && met<100) return (1 + var*0.05);
  if (mt>=100 && mt<160 && met>=100 && met<150) return (1 + var*0.25);
  if (mt>=100 && mt<160 && met>=150 && met<200) return (1 + var*0.45);
  if (mt>=100 && mt<160 && met>=200           ) return (1 + var*0.45);
  if (mt>=160           && met>= 50 && met<100) return (1 + var*0.30);
  if (mt>=160           && met>=100 && met<150) return (1 + var*0.50);
  if (mt>=160           && met>=150 && met<200) return (1 + var*0.40);
  if (mt>=160           && met>=200           ) return (1 + var*0.45);
  return 0;
}

int tauIdx1(int lep1pdg, int lep2pdg, int lep3pdg, int lep4pdg = 0){
    if(abs(lep1pdg)==15) return 0;
    if(abs(lep2pdg)==15) return 1;
    if(abs(lep3pdg)==15) return 2;
    if(abs(lep4pdg)==15) return 3;
    return -1;
}

int tauIdx2(int lep1pdg, int lep2pdg, int lep3pdg, int lep4pdg = 0){
    int firstTau = tauIdx1(lep1pdg, lep2pdg, lep3pdg, lep4pdg);
    if(firstTau == -1) return -1;
    if(abs(lep2pdg)==15 && firstTau<1) return 1;
    if(abs(lep3pdg)==15 && firstTau<2) return 2;
    if(abs(lep4pdg)==15 && firstTau<3) return 3;
    return -1;
}

int isConv(int nLep, int lep1mcUCSX, int lep2mcUCSX, int lep3mcUCSX, int lep4mcUCSX = 0) {
    if(nLep == 2) return (lep1mcUCSX==4 || lep2mcUCSX==4);
    if(nLep == 3) return (lep1mcUCSX==4 || lep2mcUCSX==4 || lep3mcUCSX==4);
    return (lep1mcUCSX==4 || lep2mcUCSX==4 || lep3mcUCSX==4 || lep4mcUCSX==4);
}

int isFake(int nLep, int lep1mcUCSX, int lep2mcUCSX, int lep3mcUCSX = 0, int lep4mcUCSX = 0) {
    if(nLep == 2) return ((lep1mcUCSX==2 || lep1mcUCSX==3) || (lep2mcUCSX==2 || lep2mcUCSX==3));
    if(nLep == 3) return ((lep1mcUCSX==2 || lep1mcUCSX==3) || (lep2mcUCSX==2 || lep2mcUCSX==3) || (lep3mcUCSX==2 || lep3mcUCSX==3));
    return ((lep1mcUCSX==2 || lep1mcUCSX==3) || (lep2mcUCSX==2 || lep2mcUCSX==3) || (lep3mcUCSX==2 || lep3mcUCSX==3) || (lep4mcUCSX==2 || lep4mcUCSX==3));
}

int isFakeHeppy(int nLep, int lep1mcHeppy, int lep2mcHeppy, int lep3mcHeppy = 1, int lep4mcHeppy = 1) {
    if(nLep == 2) return (lep1mcHeppy==0 || lep2mcHeppy==0);
    if(nLep == 3) return (lep1mcHeppy==0 || lep2mcHeppy==0 || lep3mcHeppy==0);
    return (lep1mcHeppy==0 || lep2mcHeppy==0 || lep3mcHeppy==0 || lep4mcHeppy==0);
}

int isFakeHF(int nLep, int lep1mcUCSX, int lep2mcUCSX, int lep3mcUCSX = 0, int lep4mcUCSX = 0) {
    if(nLep == 2) return (lep1mcUCSX==3 || lep2mcUCSX==3);
    if(nLep == 3) return (lep1mcUCSX==3 || lep2mcUCSX==3 || lep3mcUCSX==3);
    return (lep1mcUCSX==3 || lep2mcUCSX==3 || lep3mcUCSX==3 || lep4mcUCSX==3);
}

int isFakeLF(int nLep, int lep1mcUCSX, int lep2mcUCSX, int lep3mcUCSX = 0, int lep4mcUCSX = 0) {
    if(nLep == 2) return (lep1mcUCSX==2 || lep2mcUCSX==2);
    if(nLep == 3) return (lep1mcUCSX==2 || lep2mcUCSX==2 || lep3mcUCSX==2);
    return (lep1mcUCSX==2 || lep2mcUCSX==2 || lep3mcUCSX==2 || lep4mcUCSX==2);
}

int isPrompt(int nLep, int lep1mcUCSX, int lep2mcUCSX, int lep3mcUCSX = 0, int lep4mcUCSX = 0) {
    if(nLep == 2) return ((lep1mcUCSX==0 || lep1mcUCSX==1) && (lep2mcUCSX==0 || lep2mcUCSX==1));
    if(nLep == 3) return ((lep1mcUCSX==0 || lep1mcUCSX==1) && (lep2mcUCSX==0 || lep2mcUCSX==1) && (lep3mcUCSX==0 || lep3mcUCSX==1));
    return ((lep1mcUCSX==0 || lep1mcUCSX==1) && (lep2mcUCSX==0 || lep2mcUCSX==1) && (lep3mcUCSX==0 || lep3mcUCSX==1) && (lep4mcUCSX==0 || lep4mcUCSX==1));
}

int isPromptRightCharge(int nLep, int lep1mcUCSX, int lep2mcUCSX, int lep3mcUCSX = 0, int lep4mcUCSX = 0) {
    if(nLep == 2) return (lep1mcUCSX==0 && lep2mcUCSX==0);
    if(nLep == 3) return (lep1mcUCSX==0 && lep2mcUCSX==0 && lep3mcUCSX==0);
    return (lep1mcUCSX==0 && lep2mcUCSX==0 && lep3mcUCSX==0 && lep4mcUCSX==0);
}

int hasPromptLight(int nLep, int lep1pdgId, int lep1mcUCSX, int lep2pdgId, int lep2mcUCSX, int lep3pdgId = 0, int lep3mcUCSX = 0, int lep4pdgId = 0, int lep4mcUCSX = 0) {
    if(abs(lep1pdgId)<15 && !(lep1mcUCSX==0 || lep1mcUCSX==1)) return 0;
    if(abs(lep2pdgId)<15 && !(lep2mcUCSX==0 || lep2mcUCSX==1)) return 0;
    if(nLep == 2                                             ) return 1;
    if(abs(lep3pdgId)<15 && !(lep3mcUCSX==0 || lep3mcUCSX==1)) return 0;
    if(nLep == 3                                             ) return 1;
    if(abs(lep4pdgId)<15 && !(lep4mcUCSX==0 || lep4mcUCSX==1)) return 0;
    return 0;
}

int hasPromptTau(int nLep, int lep1pdgId, int lep1mcUCSX, int lep2pdgId, int lep2mcUCSX, int lep3pdgId = 0, int lep3mcUCSX = 0, int lep4pdgId = 0, int lep4mcUCSX = 0) {
    if(abs(lep1pdgId)==15 && !(lep1mcUCSX==0 || lep1mcUCSX==1)) return 0;
    if(abs(lep2pdgId)==15 && !(lep2mcUCSX==0 || lep2mcUCSX==1)) return 0;
    if(nLep == 2                                              ) return 1;
    if(abs(lep3pdgId)==15 && !(lep3mcUCSX==0 || lep3mcUCSX==1)) return 0;
    if(nLep == 3                                              ) return 1;
    if(abs(lep4pdgId)==15 && !(lep4mcUCSX==0 || lep4mcUCSX==1)) return 0;
    return 0;
}

int isGoodFake(float pt, int isTight) {
    if(pt == 0) return 0;
    if(isTight) return 0;
    return 1;
}

float getTau(int lep1pdgId, float lep1value, int lep2pdgId, float lep2value, int lep3pdgId, float lep3value, float down=0, float up=0) {
	float val = 0;
    if(abs(lep1pdgId)==15) val = lep1value;
    if(abs(lep2pdgId)==15) val = lep2value;
    if(abs(lep3pdgId)==15) val = lep3value;
    if(up  >0) val = std::min(up, val);
    if(down>0) val = std::max(down, val);
    return val;
}

int allTightLight(int nLep, int l1pdgId, int l1isTight, int l2pdgId, int l2isTight, int l3pdgId = 0, int l3isTight = 0, int l4pdgId = 0, int l4isTight = 0){
    if(abs(l1pdgId)<15 && !l1isTight) return 0;
    if(abs(l2pdgId)<15 && !l2isTight) return 0;
    if(nLep == 2                    ) return 1;
    if(abs(l3pdgId)<15 && !l3isTight) return 0;
    if(nLep == 3                    ) return 1;
    if(abs(l4pdgId)<15 && !l4isTight) return 0;
    return 1;
}

int allTightTau(int nLep, int l1pdgId, int l1isTight, int l2pdgId, int l2isTight, int l3pdgId = 0, int l3isTight = 0, int l4pdgId = 0, int l4isTight = 0){
    if(abs(l1pdgId)==15 && !l1isTight) return 0;
    if(abs(l2pdgId)==15 && !l2isTight) return 0;
    if(nLep == 2                     ) return 1;
    if(abs(l3pdgId)==15 && !l3isTight) return 0;
    if(nLep == 3                     ) return 1;
    if(abs(l4pdgId)==15 && !l4isTight) return 0;
    return 1;
}

int tightChargeCut(int nLep, int l1pdgId, int l1tightCharge, int l2pdgId, int l2tightCharge, int l3pdgId = 0, int l3tightCharge = 0, int l4pdgId = 0, int l4tightCharge = 0) { 
    if((abs(l1pdgId)==11 && l1tightCharge<2) || (abs(l1pdgId)==13 && l1tightCharge<2)) return 0;
    if((abs(l2pdgId)==11 && l2tightCharge<2) || (abs(l2pdgId)==13 && l2tightCharge<2)) return 0;
    if(nLep == 2                                                                     ) return 1;
    if((abs(l3pdgId)==11 && l3tightCharge<2) || (abs(l3pdgId)==13 && l3tightCharge<2)) return 0;
    if(nLep == 3                                                                     ) return 1;
    if((abs(l4pdgId)==11 && l4tightCharge<2) || (abs(l4pdgId)==13 && l4tightCharge<2)) return 0;
    return 1;
}
/*
int allTight(int nLep, int l1isTight, int l2isTight, int l3isTight = 0, int l4isTight = 0){
    if(nLep == 2) return ((l1isTight+l2isTight)==2);
    if(nLep == 3) return ((l1isTight+l2isTight+l3isTight)==3);
    return ((l1isTight+l2isTight+l3isTight+l4isTight)==4);
}
*/

Bool_t samesign(int pdg1, int pdg2){
  return pdg1*pdg2 > 0;
}


Bool_t allTight(Bool_t isT1, Bool_t isT2){
  return isT1 && isT2;
}

Bool_t allTight(Bool_t isT1, Bool_t isT2, Bool_t isT3){
  return isT1 && isT2 && isT3;
}

Bool_t allTight(Bool_t isT1, Bool_t isT2, Bool_t isT3, Bool_t isT4){
  return isT1 && isT2 && isT3 && isT4;
}

int countTaus(int nLep, int l1pdgId, int l2pdgId, int l3pdgId, int l4pdgId = 0){
    if(nLep == 3) return (abs(l1pdgId)==15)+(abs(l2pdgId)==15)+(abs(l3pdgId)==15);
    return (abs(l1pdgId)==15)+(abs(l2pdgId)==15)+(abs(l3pdgId)==15)+(abs(l4pdgId)==15);
}

float srMll(int nLep, float mllAllFlavors, float mllOnlyLight, float mllOnlyTaus) {
    if(nLep==3) return mllOnlyLight;
    return mllAllFlavors;
}

float srMt(int nLep, float mtAllFlavors, float mtOnlyLight, float mtOnlyTaus) {
    if(nLep==3) return mtOnlyLight;
    return mtAllFlavors;
}

int nLepFlavor(int nTau, int is4l, int is5l){

    if(!is4l && !is5l) return 0;
    if(is5l          ) return 6;
    if(nTau == 0     ) return 1;
    if(nTau == 1     ) return 2;
    if(nTau == 2     ) return 3;
    if(nTau == 3     ) return 4; 
    if(nTau == 4     ) return 5; 

    return 0;
}

int BR(int nLep, int nTau, int nOSSF, int nOSLF, int nOSTF){

    if(nLep == 3 && nTau == 0 && nOSSF >= 1              ) return  1;
    if(nLep == 3 && nTau == 0 && nOSSF <  1              ) return  2;
    if(nLep == 3 && nTau == 1 && nOSSF >= 1              ) return  3;
    if(nLep == 3 && nTau == 1 && nOSSF <  1 && nOSLF >= 1) return  4;
    if(nLep == 3 && nTau == 1 && nOSLF <  1              ) return  5;
    if(nLep == 3 && nTau == 2                            ) return  6;
    if(nLep == 4 && nTau == 0 && nOSSF >= 2              ) return  7;
    if(nLep == 4 && nTau == 0 && nOSSF <= 1              ) return  8;
    if(nLep == 4 && nTau == 1                            ) return  9;
    if(nLep == 4 && nTau == 2 && nOSSF >= 2              ) return 10;
    if(nLep == 4 && nTau == 2 && nOSSF <= 1              ) return 11;

    return 0;
}

int BRos(int nLep, int nTau, int nOSSF, int nOSLF, int nOSTF){

    int br = BR(nLep, nTau, nOSSF, nOSLF, nOSTF);
    if(br == 3 || br == 4) return 5; // mimicking BR = 5 event
	return 0;
}

int SR3lA(float mT2L, float mT2T, float mll, float mT, float met, int offset = 0) {

    if(mll >= 0 && mll < 75) {
        if (mT >=   0 && mT < 100 && met >=   0 && met < 100) return offset +  1;
        if (mT >=   0 && mT < 100 && met >= 100 && met < 150) return offset +  2;
        if (mT >=   0 && mT < 100 && met >= 150 && met < 200) return offset +  3;
        if (mT >=   0 && mT < 100 && met >= 200 && met < 250) return offset +  4;
        if (mT >=   0 && mT < 100 && met >= 250             ) return offset +  5;
        if (mT >= 100 && mT < 160 && met >=   0 && met < 100) return offset +  6;
        if (mT >= 100 && mT < 160 && met >= 100 && met < 150) return offset +  7;
        if (mT >= 100 && mT < 160 && met >= 150 && met < 200) return offset +  8;
        if (mT >= 100 && mT < 160 && met >= 200             ) return offset +  9;
        if (mT >= 160 &&             met >=   0 && met < 100) return offset + 10;
        if (mT >= 160 &&             met >= 100 && met < 150) return offset + 11;
        if (mT >= 160 &&             met >= 150 && met < 200) return offset + 12;
        if (mT >= 160 &&             met >= 200 && met < 250) return offset + 13;
        if (mT >= 160 &&             met >= 250             ) return offset + 14;
    }
    if(mll >= 75 && mll < 105) {
        if (mT >=   0 && mT < 100 && met >=   0 && met < 100) return offset + 15;
        if (mT >=   0 && mT < 100 && met >= 100 && met < 150) return offset + 16;
        if (mT >=   0 && mT < 100 && met >= 150 && met < 200) return offset + 17;
        if (mT >=   0 && mT < 100 && met >= 200 && met < 250) return offset + 18;
        if (mT >=   0 && mT < 100 && met >= 250 && met < 400) return offset + 19;
        if (mT >=   0 && mT < 100 && met >= 400 && met < 550) return offset + 20;
        if (mT >=   0 && mT < 100 && met >= 550             ) return offset + 21;
        if (mT >= 100 && mT < 160 && met >=   0 && met < 100) return offset + 22;
        if (mT >= 100 && mT < 160 && met >= 100 && met < 150) return offset + 23;
        if (mT >= 100 && mT < 160 && met >= 150 && met < 200) return offset + 24;
        if (mT >= 100 && mT < 160 && met >= 200             ) return offset + 25;
        if (mT >= 160 &&             met >=   0 && met < 100) return offset + 26;
        if (mT >= 160 &&             met >= 100 && met < 150) return offset + 27;
        if (mT >= 160 &&             met >= 150 && met < 200) return offset + 28;
        if (mT >= 160 &&             met >= 200 && met < 250) return offset + 29;
        if (mT >= 160 &&             met >= 250 && met < 400) return offset + 30;
        if (mT >= 160 &&             met >= 400             ) return offset + 31;
    }
    if(mll >= 105) {
        if (mT >=   0 && mT < 100 && met >=   0 && met < 100) return offset + 32;
        if (mT >=   0 && mT < 100 && met >= 100 && met < 150) return offset + 33;
        if (mT >=   0 && mT < 100 && met >= 150 && met < 200) return offset + 34;
        if (mT >=   0 && mT < 100 && met >= 200 && met < 250) return offset + 35;
        if (mT >=   0 && mT < 100 && met >= 250             ) return offset + 36;
        if (mT >= 100 && mT < 160 && met >=   0 && met < 100) return offset + 37;
        if (mT >= 100 && mT < 160 && met >= 100 && met < 150) return offset + 38;
        if (mT >= 100 && mT < 160 && met >= 150 && met < 200) return offset + 39;
        if (mT >= 100 && mT < 160 && met >= 200             ) return offset + 40;
        if (mT >= 160 &&             met >=   0 && met < 100) return offset + 41;
        if (mT >= 160 &&             met >= 100 && met < 150) return offset + 42;
        if (mT >= 160 &&             met >= 150 && met < 200) return offset + 43;
        if (mT >= 160 &&             met >= 200             ) return offset + 44;
    }
    return 0;
}

int SR3lB(float mT2L, float mT2T, float mll, float mT, float met, int offset = 0) {

    if(mll < 100){
        if(mT <  120 && met >=   0 && met < 100) return offset + 1;
        if(mT <  120 && met >= 100             ) return offset + 2;
        if(mT >= 120 && met >=   0             ) return offset + 3;
    }
    if(mll >= 100) {
        if(mT <  120 && met >=   0 && met < 100) return offset + 4;
        if(mT <  120 && met >= 100             ) return offset + 5;
        if(mT >= 120 && met >=   0             ) return offset + 6;
    }

    return 0;
}

int SR3lC(float mT2L, float mT2T, float mll, float mT, float met, int offset = 0) {

    if(mT2L < 100  && mll >=   0 && mll <  75 && met >=   0 && met < 100) return offset +  1;
    if(mT2L < 100  && mll >=   0 && mll <  75 && met >= 100 && met < 150) return offset +  2;
    if(mT2L < 100  && mll >=   0 && mll <  75 && met >= 150 && met < 200) return offset +  3;
    if(mT2L < 100  && mll >=   0 && mll <  75 && met >= 200 && met < 250) return offset +  4;
    if(mT2L < 100  && mll >=   0 && mll <  75 && met >= 250             ) return offset +  5;
    if(               mll >=  75 && mll < 105 && met >=   0 && met < 100) return offset +  6;
    if(               mll >=  75 && mll < 105 && met >= 100 && met < 150) return offset +  7;
    if(               mll >=  75 && mll < 105 && met >= 150 && met < 200) return offset +  8;
    if(               mll >=  75 && mll < 105 && met >= 200 && met < 300) return offset +  9;
    if(               mll >=  75 && mll < 105 && met >= 300 && met < 400) return offset + 10;
    if(               mll >=  75 && mll < 105 && met >= 400             ) return offset + 11;
    if(mT2L < 100  && mll >= 105 &&              met >=   0 && met < 100) return offset + 12;
    if(mT2L < 100  && mll >= 105 &&              met >= 100 && met < 150) return offset + 13;
    if(mT2L < 100  && mll >= 105 &&              met >= 150 && met < 200) return offset + 14;
    if(mT2L < 100  && mll >= 105 &&              met >= 200 && met < 250) return offset + 15;
    if(mT2L < 100  && mll >= 105 &&              met >= 250             ) return offset + 16;
    if(mT2L >= 100 && (mll < 75 || mll >= 105) && met >=  0 && met < 200) return offset + 17;
    if(mT2L >= 100 && (mll < 75 || mll >= 105) && met >= 200            ) return offset + 18;
    return 0;
}

int SR3lD(float mT2L, float mT2T, float mll, float mT, float met, int offset = 0) {

    if(mT2L >= 0 && mT2L < 100){
        if(mll >=   0 && mll <  60 && met >=   0 && met < 100) return offset +  1;
        if(mll >=   0 && mll <  60 && met >= 100 && met < 150) return offset +  2;
        if(mll >=   0 && mll <  60 && met >= 150 && met < 200) return offset +  3;
        if(mll >=   0 && mll <  60 && met >= 200 && met < 250) return offset +  4;
        if(mll >=   0 && mll <  60 && met >= 250             ) return offset +  5;
        if(mll >=  60 && mll < 100 && met >=   0 && met < 100) return offset +  6;
        if(mll >=  60 && mll < 100 && met >= 100 && met < 150) return offset +  7;
        if(mll >=  60 && mll < 100 && met >= 150 && met < 200) return offset +  8;
        if(mll >=  60 && mll < 100 && met >= 200 && met < 250) return offset +  9;
        if(mll >=  60 && mll < 100 && met >= 250             ) return offset + 10;
        if(mll >= 100 &&              met >=   0 && met < 100) return offset + 11;
        if(mll >= 100 &&              met >= 100 && met < 150) return offset + 12;
        if(mll >= 100 &&              met >= 150 && met < 200) return offset + 13;
        if(mll >= 100 &&              met >= 200             ) return offset + 14;
    }
    if(mT2L >= 100) {
        if(met >=  0 && met < 200                            ) return offset + 15;
        if(met >= 200                                        ) return offset + 16;
    }

    return 0;
}


float SR3lD_weight(float mT2L, float mT2T, float mll, float mT, float met, int offset = 0){

    if(mT2L >= 0 && mT2L < 100){
        if(mll >=   0 && mll <  60 && met >=   0 && met < 100) return 0.15;
        if(mll >=   0 && mll <  60 && met >= 100 && met < 150) return 0.15;
        if(mll >=   0 && mll <  60 && met >= 150 && met < 200) return 0.15;
        if(mll >=   0 && mll <  60 && met >= 200 && met < 250) return 0.20;
        if(mll >=   0 && mll <  60 && met >= 250             ) return 0.20;
        if(mll >=  60 && mll < 100 && met >=   0 && met < 100) return 0.20;
        if(mll >=  60 && mll < 100 && met >= 100 && met < 150) return 0.20;
        if(mll >=  60 && mll < 100 && met >= 150 && met < 200) return 0.20;
        if(mll >=  60 && mll < 100 && met >= 200 && met < 250) return 0.25;
        if(mll >=  60 && mll < 100 && met >= 250             ) return 0.25;
        if(mll >= 100 &&              met >=   0 && met < 100) return 0.20;
        if(mll >= 100 &&              met >= 100 && met < 150) return 0.25;
        if(mll >= 100 &&              met >= 150 && met < 200) return 0.25;
        if(mll >= 100 &&              met >= 200             ) return 0.25;
    }
    if(mT2L >= 100) {
        if(met >=  0 && met < 200                            ) return 0.30;
        if(met >= 200                                        ) return 0.30;
    }

    return 0;
}
int SR3lE(float mT2L, float mT2T, float mll, float mT, float met, int offset = 0) {

    if(mT2T >= 0 && mT2T < 100){
        if(mll >=  -1 && mll <  60 && met >=   0 && met < 100) return offset +  1;
        if(mll >=  -1 && mll <  60 && met >= 100 && met < 150) return offset +  2;
        if(mll >=  -1 && mll <  60 && met >= 150 && met < 200) return offset +  3;
        if(mll >=  -1 && mll <  60 && met >= 200 && met < 250) return offset +  4;
        if(mll >=  -1 && mll <  60 && met >= 250             ) return offset +  5;
        if(mll >=  60 && mll < 100 && met >=   0 && met < 100) return offset +  6;
        if(mll >=  60 && mll < 100 && met >= 100 && met < 150) return offset +  7;
        if(mll >=  60 && mll < 100 && met >= 150 && met < 200) return offset +  8;
        if(mll >=  60 && mll < 100 && met >= 200 && met < 250) return offset +  9;
        if(mll >=  60 && mll < 100 && met >= 250             ) return offset + 10;
        if(mll >= 100 &&              met >=   0             ) return offset + 11;
    }
    if(mT2T >= 100) {
        if(met >=  0                                         ) return offset + 12;
    }
    return 0;
}

int SR3lF(float mT2L, float mT2T, float mll, float mT, float met, int offset = 0) {

    if(mT2T >= 0 && mT2T < 100){
        if(mll >=   0 && mll < 100 && met >=   0 && met < 100) return offset +  1;
        if(mll >=   0 && mll < 100 && met >= 100 && met < 150) return offset +  2;
        if(mll >=   0 && mll < 100 && met >= 150 && met < 200) return offset +  3;
        if(mll >=   0 && mll < 100 && met >= 200 && met < 250) return offset +  4;
        if(mll >=   0 && mll < 100 && met >= 250 && met < 300) return offset +  5;
        if(mll >=   0 && mll < 100 && met >= 300             ) return offset +  6;
        if(mll >= 100 &&              met >=   0 && met < 100) return offset +  7;
        if(mll >= 100 &&              met >= 100 && met < 150) return offset +  8;
        if(mll >= 100 &&              met >= 150 && met < 200) return offset +  9;
        if(mll >= 100 &&              met >= 200             ) return offset + 10;
    }
    if(mT2T >= 100) {
        if(met >=  0 && met < 200                            ) return offset + 11;
        if(met >= 200                                        ) return offset + 12;
    }

    return 0;
}

int SR4lG(float mT2L, float mT2T, float mll, float mT, float met, int offset = 0) {

    if(met >=   0 && met <  50) return offset + 1;
    if(met >=  50 && met < 100) return offset + 2;
    if(met >= 100 && met < 150) return offset + 3;
    if(met >= 150 && met < 200) return offset + 4;
    if(met >= 200             ) return offset + 5;

    return 0;
}

int SR4lH(float mT2L, float mT2T, float mll, float mT, float met, int offset = 0) {

    if(met >=   0 && met <  50) return offset + 1;
    if(met >=  50 && met < 100) return offset + 2;
    if(met >= 100 && met < 150) return offset + 3;
    if(met >= 150             ) return offset + 4;

    return 0;
}

int SR4lK(float mT2L, float mT2T, float mll, float mT, float met, int offset = 0) {

    if(met >=   0 && met < 100) return offset + 1;
    if(met >= 100 && met < 150) return offset + 2;
    if(met >= 150             ) return offset + 3;

    return 0;
}

int SR3l(int nTau, int nOSSF, int nOSLF, float mT2L, float mT2T, float mll, float mT, float met){

    // 3 light
    if(nTau == 0 && nOSSF >= 1              ) return SR3lA(mT2L, mT2T, mll, mT, met,  0);
    if(nTau == 0 && nOSSF <  1              ) return SR3lB(mT2L, mT2T, mll, mT, met, 44);
    // 2 light + 1 tau
    if(nTau == 1 && nOSSF >= 1              ) return SR3lC(mT2L, mT2T, mll, mT, met, 50);
    if(nTau == 1 && nOSSF <  1 && nOSLF >= 1) return SR3lD(mT2L, mT2T, mll, mT, met, 68);
    if(nTau == 1 && nOSLF <  1              ) return SR3lE(mT2L, mT2T, mll, mT, met, 84);
    // 1 light + 2 tau
    if(nTau == 2                            ) return SR3lF(mT2L, mT2T, mll, mT, met, 96);
    return 0;
}

int SR4l(int nTau, int nOSSF, int nOSLF, float mT2L, float mT2T, float mll, float mT, float met){

    // 4 light
    if(nTau == 0 && nOSSF >= 2              ) return SR4lG(mT2L, mT2T, mll, mT, met, 108);
    if(nTau == 0 && nOSSF <= 1              ) return SR4lH(mT2L, mT2T, mll, mT, met, 113);
    // 3light + 1tau
    if(nTau == 1                            ) return SR4lH(mT2L, mT2T, mll, mT, met, 117);
    // 2light + 2tau
    if(nTau == 2 && nOSSF >= 2              ) return SR4lH(mT2L, mT2T, mll, mT, met, 121);
    if(nTau == 2 && nOSSF <= 1              ) return SR4lK(mT2L, mT2T, mll, mT, met, 125);
    return 0;
}

int SR(int nLep, int nTau, int nOSSF, int nOSLF, float mT2L, float mT2T, float mll, float mT, float met) {

  if(nLep == 3)
    return SR3l(nTau, nOSSF, nOSLF, mT2L, mT2T, mll, mT, met);
  if(nLep == 4)
    return SR4l(nTau, nOSSF, nOSLF, mT2L, mT2T, mll, mT, met);
  return 0;
}

int SRos(int nLep, int nTau, int nOSSF, int nOSLF, float mT2L, float mT2T, float mll, float mT, float met) {
    if(nLep != 3 || nTau != 1) return 0;
    if(nOSSF >= 1 || (nOSSF <  1 && nOSLF >= 1)) return SR3lE(mT2L, mT2T, mll, mT, met, 84);
    return 0;
}

int SuperSig3L1(int nTau, float mT, float met) {
    if(nTau==0 && (mT   >= 120 && met >= 200)) return 1;
    return 0;
}

int SuperSig3L2(int nTau, float met) {
    if(nTau==0 &&                 met >= 200)  return 1;
    return 0;
}

int SuperSig3L3(int nTau, float mT2L, float met) {
    if(nTau==1 && (mT2L >=  50 && met >= 200)) return 1;
    return 0;
}

int SuperSig3L4(int nTau, float mT2T, float met) {
    if(nTau==2 && (mT2T >=  50 && met >= 200)) return 1;
    return 0;
}

int SuperSig3L5(int nTau, float met) {
    if(nTau==2 && met >=  75 ) return 1;
    return 0;
}

int SuperSig4L1(float met) {
    if(met >= 200) return 1;
    return 0;
}


int SuperSig(int nLep, int nTau, int nOSSF, int nOSLF, float mT2L, float mT2T, float mll, float mT, float met) {

    if(nLep == 3){
        if(nTau==0 && (mT   >= 120 && met >= 200)) return 1;
        if(nTau==0 &&                 met >= 250 ) return 2;
        if(nTau==1 && (mT2L >=  50 && met >= 200)) return 3;
        if(nTau==2 && (mT2T >=  50 && met >= 200)) return 4;
        if(nTau==2 &&                 met >=  75 ) return 5;
    }
    if(nLep == 4){
        if(met >= 200                            ) return 6;
    }
    return 0;
}


int SRA_new(float mll, float mT, float met, int offset = 0) {

    if(mll >= 0 && mll < 75) {
        if (mT >=   0 && mT < 100 && met >=   0 && met < 100) return offset +  1;
        if (mT >=   0 && mT < 100 && met >= 100 && met < 150) return offset +  2;
        if (mT >=   0 && mT < 100 && met >= 150 && met < 200) return offset +  3;
        if (mT >=   0 && mT < 100 && met >= 200 && met < 250) return offset +  4;
        if (mT >=   0 && mT < 100 && met >= 250             ) return offset +  5;
        if (mT >= 100 && mT < 160 && met >=   0 && met < 100) return offset +  6;
        if (mT >= 100 && mT < 160 && met >= 100 && met < 150) return offset +  7;
        if (mT >= 100 && mT < 160 && met >= 150 && met < 200) return offset +  8;
        if (mT >= 100 && mT < 160 && met >= 200             ) return offset +  9;
        if (mT >= 160 &&             met >=   0 && met < 100) return offset + 10;
        if (mT >= 160 &&             met >= 100 && met < 150) return offset + 11;
        if (mT >= 160 &&             met >= 150 && met < 200) return offset + 12;
        if (mT >= 160 &&             met >= 200 && met < 250) return offset + 13;
        if (mT >= 160 &&             met >= 250             ) return offset + 14;
    }
    if(mll >= 75 && mll < 105) {
        if (mT >=   0 && mT < 100 && met >=   0 && met < 100) return offset + 15;
        if (mT >=   0 && mT < 100 && met >= 100 && met < 150) return offset + 16;
        if (mT >=   0 && mT < 100 && met >= 150 && met < 200) return offset + 17;
        if (mT >=   0 && mT < 100 && met >= 200 && met < 250) return offset + 18;
        if (mT >=   0 && mT < 100 && met >= 250 && met < 400) return offset + 19;
        if (mT >=   0 && mT < 100 && met >= 400 && met < 550) return offset + 20;
        if (mT >=   0 && mT < 100 && met >= 550             ) return offset + 21;
        if (mT >= 100 && mT < 160 && met >=   0 && met < 100) return offset + 22;
        if (mT >= 100 && mT < 160 && met >= 100 && met < 150) return offset + 23;
        if (mT >= 100 && mT < 160 && met >= 150 && met < 200) return offset + 24;
        if (mT >= 100 && mT < 160 && met >= 200             ) return offset + 25;
        if (mT >= 160 &&             met >=   0 && met < 100) return offset + 26;
        if (mT >= 160 &&             met >= 100 && met < 150) return offset + 27;
        if (mT >= 160 &&             met >= 150 && met < 200) return offset + 28;
        if (mT >= 160 &&             met >= 200 && met < 250) return offset + 29;
        if (mT >= 160 &&             met >= 250 && met < 400) return offset + 30;
        if (mT >= 160 &&             met >= 400             ) return offset + 31;
    }
    if(mll >= 105) {
        if (mT >=   0 && mT < 100 && met >=   0 && met < 100) return offset + 32;
        if (mT >=   0 && mT < 100 && met >= 100 && met < 150) return offset + 33;
        if (mT >=   0 && mT < 100 && met >= 150 && met < 200) return offset + 34;
        if (mT >=   0 && mT < 100 && met >= 200 && met < 250) return offset + 35;
        if (mT >=   0 && mT < 100 && met >= 250             ) return offset + 36;
        if (mT >= 100 && mT < 160 && met >=   0 && met < 100) return offset + 37;
        if (mT >= 100 && mT < 160 && met >= 100 && met < 150) return offset + 38;
        if (mT >= 100 && mT < 160 && met >= 150 && met < 200) return offset + 39;
        if (mT >= 100 && mT < 160 && met >= 200             ) return offset + 40;
        if (mT >= 160 &&             met >=   0 && met < 100) return offset + 41;
        if (mT >= 160 &&             met >= 100 && met < 150) return offset + 42;
        if (mT >= 160 &&             met >= 150 && met < 200) return offset + 43;
        if (mT >= 160 &&             met >= 200             ) return offset + 44;
    }
    return 0+offset;
}

int SRB_new(float dR3l, int offset=0){
  if (dR3l < 0.4) return 1 + offset;
  if (dR3l < 1.) return 2 + offset;
  return 3+offset;
}

int SRC_new(float met, float mtZprime, float mt2ll, int offset = 0){
    if (met < 200){
        if (mt2ll < 80) return 1 + offset;
        if (mt2ll < 120) return 2 + offset;
        else return 3 + offset;
    }
    else if (met > 200 && met < 300){
        if (mt2ll < 80) return 4 + offset;
        if (mt2ll < 120) return 5 + offset;
        return 6 + offset;
    }
    else if (met > 300){
        if (mtZprime < 250) return 7 + offset;
        if (mtZprime < 500) return 8 + offset;
        return 9 + offset;
    }
}


int SRD_new(float mT2L, float met, float mll, int offset = 0){
    if(mT2L >= 0 && mT2L < 100){
        if(mll >=   0 && mll <  60 && met >=   0 && met < 100) return offset +  1;
        if(mll >=   0 && mll <  60 && met >= 100 && met < 150) return offset +  2;
        if(mll >=   0 && mll <  60 && met >= 150 && met < 200) return offset +  3;
        if(mll >=   0 && mll <  60 && met >= 200 && met < 250) return offset +  4;
        if(mll >=   0 && mll <  60 && met >= 250             ) return offset +  5;
        if(mll >=  60 && mll < 100 && met >=   0 && met < 100) return offset +  6;
        if(mll >=  60 && mll < 100 && met >= 100 && met < 150) return offset +  7;
        if(mll >=  60 && mll < 100 && met >= 150 && met < 200) return offset +  8;
        if(mll >=  60 && mll < 100 && met >= 200 && met < 250) return offset +  9;
        if(mll >=  60 && mll < 100 && met >= 250             ) return offset + 10;
        if(mll >= 100 &&              met >=   0 && met < 100) return offset + 11;
        if(mll >= 100 &&              met >= 100 && met < 150) return offset + 12;
        if(mll >= 100 &&              met >= 150 && met < 200) return offset + 13;
        if(mll >= 100 &&              met >= 200             ) return offset + 14;
    }
    if(mT2L >= 100) {
        if(met >=  0 && met < 200                            ) return offset + 15;
        if(met >= 200                                        ) return offset + 16;
    }

}



int SRE_new(float mt2, float mll, float met, int offset = 0){
    if (mt2 < 80){
        if (mll < 50){
            if (met < 100) return 1 + offset;
            if (met < 250) return 2 + offset;
            else return 3 + offset;
        }
        else{
            if (met < 100) return 4 + offset;
            if (met < 250) return 5 + offset;
            else return 5 + offset;
        }
    }
    else{
        if (mll < 100){
            if (met < 150) return 6 + offset;
            else return 7 + offset;
        }       
        else{
            if (met < 200) return 8 + offset;
            else return 9 + offset;
        }       
    }
}

int SRF_new(float mT2T, float mll, float met, int offset = 0) {

    if(mT2T >= 0 && mT2T < 100){
        if(mll >=   0 && mll < 100 && met >=   0 && met < 100) return offset +  1;
        if(mll >=   0 && mll < 100 && met >= 100 && met < 150) return offset +  2;
        if(mll >=   0 && mll < 100 && met >= 150 && met < 200) return offset +  3;
        if(mll >=   0 && mll < 100 && met >= 200 && met < 250) return offset +  4;
        if(mll >=   0 && mll < 100 && met >= 250 && met < 300) return offset +  5;
        if(mll >=   0 && mll < 100 && met >= 300             ) return offset +  6;
        if(mll >= 100 &&              met >=   0 && met < 100) return offset +  7;
        if(mll >= 100 &&              met >= 100 && met < 150) return offset +  8;
        if(mll >= 100 &&              met >= 150 && met < 200) return offset +  9;
        if(mll >= 100 &&              met >= 200             ) return offset + 10;
    }
    if(mT2T >= 100) {
        if(met >=  0 && met < 200                            ) return offset + 11;
        if(met >= 200                                        ) return offset + 12;
    }

    return offset+13;
}

float chooseMll(int cat, float mllL, float mllT, float mllAll){
  if(cat == 1) return mllL;
  if(cat == 3) return mllL;
  if(cat == 5) return mllT;
  if(cat == 6) return mllT;
  else return mllAll;
}

int SR3l_new(int cat, float mT2L, float mT2T, float mll, float mT, float ptlll, float met, float dR3l, float mtZprime){
    // 3 light
    if(cat == 1              ) return SRA_new(mll, mT, met,  0);
    if(cat == 2              ) return SRB_new(dR3l, 44);
    // 2 light + 1 tau
    if(cat == 3              ) return SRC_new(met, mtZprime, mT2L, 47);
    if(cat == 4              ) return SRD_new(mT2L,  met,  mll, 57);
    if(cat == 5              ) return SRE_new(mT2T,  mll, met, 73);
    // 1 light + 2 tau
    if(cat == 6) return SRF_new(mT2T, mll, met, 82);
    return 0;
}

int CRSR3l(int nb, float m3l, float met, int cat, int offset=0){
    if (nb == 0 && abs(m3l -91.16) > 15 && met > 50) return 0;
    if (nb > 0 && met > 50 && cat == 1)  return offset + 1;
    if (nb == 0 && abs(m3l -91.16) < 15 && met < 50 && cat == 1) return offset + 2;
}


int SSRB_new(float dR3l, int offset=0){
  if (dR3l < 0.4) return 1 + offset;
  return -1 -offset;
}

int SSRC_new(float mll, float ptlll, float met, float mtZprime, float mt2ll, int offset = 0){
    //if (ptlll < 125) return 1 + offset;
    if (abs(mll - 91.186) < 25){
        return -1 - offset;
    }
    else if (met < 200){
        if (mt2ll < 80) return -1 - offset;
        if (mt2ll < 120) return -1 - offset;
        else return 4 + offset;
    }
    else if (met > 200 && met < 300){
        if (mt2ll < 80) return -1 - offset;
        if (mt2ll < 120) return 1 + offset;
        return 1 + offset;
    }
    else if (met > 300){
        if (mtZprime < 250) return -1 - offset;
        if (mtZprime < 500) return 2 + offset;
        return 2 + offset;
    }
}


int SSRD_new(float mT2L, float met, float mll, int offset = 0){
    if(mT2L >= 50 && met > 200){ return offset +1;}
    return -1-offset;
}



int SSRE_new(float mt2, float mll, float met, int offset = 0){
    if (mt2 > 80 && met > 150){
        return 1 + offset;
    }
    return -1 - offset;
}

int SSRF_new(float mT2T, float mll, float met, int offset = 0) {
    if (met > 200 && mT2T > 50) return offset +1;
    return -offset -1;
}

int SSR_3l(int cat, float mT2L, float mT2T, float mll, float mT, float ptlll, float met, float dR3l, float mtZprime){
    // 3 light
    //cat = cat -1;

    //std::cout << "Cat: " << cat << std::endl;
    if(cat == 1              ){ return -1;}
    else if(cat == 2              ){ return SSRB_new(dR3l, 0);}
    // 2 light + 1 tau
    else if(cat == 3              ){return SSRC_new(mll, ptlll, met, mtZprime, mT2L, 1);}
    else if(cat == 4              ){return SSRD_new(mT2L,  met,  mll, 3);}
    else if(cat == 5              ){return SSRE_new(mT2T,  mll, met, 4);}
    // 1 light + 2 tau
    else if(cat == 6){return SSRF_new(mT2T, mll, met, 5);}
    return -1;
}



int SR4lGplot(float mT2Z, float met, float mZ2, int offset=0) {
    if(mT2Z > 400) return 5+offset;
    if(mT2Z > 250) return 4+offset;
    if(mT2Z > 150 && mZ2 < 60) return 3+offset;
    if(mT2Z > 150 && mZ2 >= 60) return 2+offset;
    if(mT2Z < 150) return 1+offset;
    return -1;
}


int SR4lHplot(float dRllH, float bestZ, int offset=0) {//Low MET CUT
    if(dRllH < 0.8) return 3+offset;
    if(dRllH > 0.8 && bestZ < 60) return 2+offset;
    if(dRllH > 0.8 && bestZ > 60) return 1+offset;
    return -1;
}


int SR4lIplot(float dRllH, float bestZ, int offset=0) {//Low MET CUT
    if(dRllH < 0.8) return 3+offset;
    if(dRllH > 0.8 && bestZ < 60) return 2+offset;
    if(dRllH > 0.8 && bestZ > 60) return 1+offset;
    return -1;
}

int SR4lJplot(float ptH, float bestZ, int offset=0) {//Low MET CUT
    if(bestZ < 60) return 3+offset;
    if(ptH > 100 && bestZ > 60) return 2+offset;
    if(ptH < 100 && bestZ > 60) return 1+offset;
    return -1;
}

int SR4lKplot(float met, float bestZ, int offset=0) {//Low MET CUT
    if(bestZ < 60 && met > 100) return 3+offset;
    if(bestZ < 60 && met < 100) return 2+offset;
    if(bestZ > 60) return 1+offset;
    return -1;
}


int SR4lplot(int BR, float mT2Z, float met, float mZ2, float mZ1, float dRllH, float ptH){
    // 4 light
    if(met < 50) return 0;
    if(BR==7) return SR4lGplot(mT2Z, met, mZ2, 0);
    if(BR==8) return SR4lHplot(dRllH, mZ1, 5);
    // 3light + 1tau
    if(BR==9) return SR4lIplot(dRllH, mZ1, 8);
    // 2light + 2tau
    if(BR==10) return SR4lJplot(ptH, mZ1, 11);
    if(BR==11) return SR4lKplot(met, mZ1, 14);
    return -1;
}



int SR4lplot_Alt(int BR, float mT2Z, float met, float mZ2, float mZ1, float dRllH, float ptH){
    // 4 light
    if(met < 50) return 0;
    if(BR==7) return SR4lGplot(mT2Z, met, mZ2, 0);
    if(mZ1 > 60) return 6;
    if(BR==8) return SR4lHplot(dRllH, mZ1, 6);
    // 3light + 1tau
    if(BR==9) return SR4lIplot(dRllH, mZ1, 9);
    // 2light + 2tau
    if(BR==10) return SR4lJplot(ptH, mZ1, 12);
    if(BR==11) return SR4lKplot(met, mZ1, 15);
    return 0;
}


int SR4lplot_v2(int BR, float mT2Z, float met, float mZ2, float mZ1, float dRllH, float ptH){
    // 4 light
    if(met < 50) return 0;
    if(BR==7) return SR4lGplot(mT2Z, met, mZ2, 0);
    if(BR==8) return SR4lHplot(dRllH, mZ1, 5);
    // 3light + 1tau
    if(BR==9) return SR4lHplot(dRllH, mZ1, 8);
    // 2light + 2tau
    if(BR==10) return SR4lHplot(dRllH, mZ1, 11);
    if(BR==11) return SR4lHplot(dRllH, mZ1, 14);
    return -1;
}

int SR4lplot_v3(int BR, float mT2Z, float met, float mZ2, float mZ1, float dRllH, float ptH){
    // 4 light
    if(met < 50) return 0;
    if(BR==7) return SR4lGplot(mT2Z, met, mZ2, 0);
    if(BR>7) return SR4lHplot(dRllH, mZ1, 5);
    return -1;
}

int SSR_4l_new(int BR, float met, float mZ1){
    // 4 light
    if((BR==7 || BR==10) && met > 150) return 1;
    else if ((BR==6 || BR==8 || BR==9 || BR==11) && met > 50 &&  mZ1 < 60) return 2;
    return -1;
}

void functionsEWK() {}
