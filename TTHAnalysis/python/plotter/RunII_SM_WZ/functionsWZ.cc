#include "TMath.h"
#include <assert.h>
#include <iostream>
#include "TH2F.h"
#include "TH1F.h"
#include "TFile.h"
#include "TSystem.h"
#include "TLorentzVector.h"
#include "TGraphAsymmErrors.h"

int nJB(int nJ, float nBJ) {
    int bin = 0;
    
    // Push SRs to make room for the new bins
    if (nJ==1) bin =  1+nBJ;
    if (nJ==2) bin =  3+nBJ;
    if (nJ==3) bin =  6+nBJ;
    if (nJ>=4) bin = 10+nBJ;
    
    return bin;
}

Float_t WZdeltaPhi(Float_t phi1, Float_t phi2)
{
  Float_t res(phi1 - phi2);
  while(res >   M_PI) res -= Float_t(2*M_PI);
  while(res <= -M_PI) res += Float_t(2*M_PI);
  return res;
}

Float_t baseDeltaR(Float_t eta1, Float_t phi1, Float_t eta2, Float_t phi2)
{
  Float_t res;
  Float_t dEta(std::abs(eta1-eta2));
  Float_t dPhi(WZdeltaPhi(phi1, phi2));
  res= std::sqrt(dEta*dEta + dPhi*dPhi);
  return res;
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

Bool_t lepMVACut(Float_t lep1mva, Float_t lep2mva, Float_t lep3mva, Int_t pdg1, Int_t pdg2, Int_t pdg3, Float_t elecut, Float_t mucut, Bool_t tightW){
  Bool_t pass1 = false;
  Bool_t pass2 = false;
  Bool_t pass3 = false;
  if (abs(pdg1) == 11 && lep1mva >= elecut) pass1 = true;
  if (abs(pdg1) == 13 && lep1mva >= mucut)  pass1 = true;
  if (abs(pdg2) == 11 && lep2mva >= elecut) pass2 = true;
  if (abs(pdg2) == 13 && lep2mva >= mucut)  pass2 = true;
  if (abs(pdg3) == 11 && lep3mva >= elecut) pass3 = true;
  if (abs(pdg3) == 13 && lep3mva >= mucut)  pass3 = true;
  return pass1 && pass2 && pass3 && tightW;
}

Int_t DiFakeRateBin(float pt1, float eta1, float pt2, float eta2, int pdgcode, int tightcode, int ptbin, int etabin)
{
 // First lepton is the one "in range", second lepton is "off range"
 // Returns flavorcode*4 + tightcode
 // Flavor code:
 // -1 == No lepton in range
 //   0 == ee
 //   1 == em
 //   2 == me
 //   3 == mm
 // Tight code:
 //   0 = Tight (in) Tight (out)
 //   1 = Loose (in) Tight (out)
 //   2 = Tight (in) Loose (out)
 //   3 = Loose (in) Loose (out)
  float ptmin; float ptmax; float etamax; float etamin;
 if (ptbin == 0){
   ptmax = 40;
   ptmin = 20;
 } 
 if (etabin == 0){
   etamax = 2.5;
   etamin = -2.5;
 }
 if (pt1 <= ptmax &&  pt1 >= ptmin && eta1 <= etamax && eta1 >= etamin && !( pt2 > ptmax ||  pt2 < ptmin || eta2 > etamax || eta2 < etamin )){
    // First one passes, second doesn't
    return pdgcode*4+tightcode;
 }
 if (pt2 <= ptmax &&  pt2 >= ptmin && eta2 <= etamax && eta2 >= etamin && !( pt1 > ptmax ||  pt1 < ptmin || eta1 > etamax || eta1 < etamin )){
    // Second one passes, first doesn't
    int newpdgcode;
    int newtightcode;
    if (pdgcode == 1) newpdgcode = 2;
    if (pdgcode == 2) newpdgcode = 1;
    if (tightcode == 1) newtightcode = 2;
    if (tightcode == 2) newtightcode = 1;
    return newpdgcode*4+newtightcode;
 }
 // If here, no candidate lepton
 return -1;   
}

//                balance = self.bestOSPair.l1.p4()
//                balance += self.bestOSPair.l2.p4()
//                self.ret["deltaR_WZ"] = deltaR(balance.Eta(), balance.Phi(), self.lepSelFO[i].p4().Eta(), self.lepSelFO[i].p4().Phi())
//                balance -= self.lepSelFO[i].p4()
//                metmom = ROOT.TLorentzVector()
//                metmom.SetPtEtaPhiM(self.met[0],0,self.metphi[0],0)
//                balance -= metmom
//                # Later do it with standalone function like makeMassMET
//                self.ret["wzBalance_pt"] = balance.Pt()
//                balance = self.bestOSPair.l1.p4(self.bestOSPair.l1.conePt)
//                balance += self.bestOSPair.l2.p4(self.bestOSPair.l2.conePt)
//                balance -= self.lepSelFO[i].p4(self.lepSelFO[i].conePt)
//                balance -= metmom
//                self.ret["wzBalance_conePt"] = balance.Pt()
//


// TBD: implement the same but with conePt
Float_t WZbalance(Float_t zpt, Float_t zeta, Float_t zphi, Float_t zm, Float_t wpt, Float_t weta, Float_t wphi, Float_t wm)
{
  TLorentzVector z; z.SetPtEtaPhiM(zpt, zeta, zphi, zm);
  TLorentzVector w; w.SetPtEtaPhiM(wpt, weta, wphi, wm);
  TLorentzVector balance = z + w;
  return balance.Pt();
}

Float_t WZdeltaR(Float_t zeta, Float_t zphi, Float_t weta, Float_t wphi)
{
  ///// save time //TLorentzVector  w; w.SetPtEtaPhiM(wpt ,  weta,  wphi,  wm);
  //
  //Float_t res(baseDeltaR(z.Eta(), z.Phi(), weta, wphi));
  Float_t res(baseDeltaR(zeta, zphi, weta, wphi));
  //std::cout << baseDeltaR(z.Eta(), z.Phi(), weta, wphi) << std::endl;
  // save time //return deltaR(z.Eta(), z.Phi(), w.Eta(), w.Phi());
  return res;
}

Int_t getWZRegion(Float_t met_pt, Float_t mll_3l, Float_t m3L, Int_t nBJetMedium30, Int_t nLepSel, Int_t LepSel4_isTight, Float_t LepSel4_pt){
  //Region index in the WZ analysis: SR->0; CRDY->1; CRTT->2; CRZZ->3; CRconv->4
  if (met_pt > 30    && nBJetMedium30 == 0 && abs(91.1876-mll_3l)<15  &&  nLepSel<4  && m3L > 100)                        return 1;
  else if (met_pt <= 30    && nBJetMedium30 == 0 && abs(91.1876-mll_3l)<15  &&  nLepSel<4  && m3L > 100)                  return 0;
  else if (met_pt > 30    && nBJetMedium30 > 0  && abs(91.1876-mll_3l)>5   &&  nLepSel<4  && m3L > 100)                   return 2;
  else if (met_pt > 30    && nBJetMedium30 == 0 && abs(91.1876-mll_3l)<15  &&  nLepSel==4 && m3L > 100  && LepSel4_isTight && LepSel4_pt > 10)     return 3;
  else if (met_pt <= 30   && nBJetMedium30 == 0 && abs(91.1876-mll_3l)>15  && m3L <= 100  &&  nLepSel<4)     return 4;
  else return -1;
}


/*Int_t getWWWRegion(Float_t met_pt, Float_t mllSFAS, Float_t mllSFOS, Int_t nOSSF, Float_t dPhi3lMet){
  //Region index in the WZ analysis: SR->0; CRDY->1; CRTT->2; CRZZ->3; CRconv->4
  if (met_pt > 30    && nBJetMedium30 == 0 && abs(91.1876-mll_3l)<15  &&  nLepSel<4  && m3L > 100)                        return 0;
  else if (met_pt <= 30    && nBJetMedium30 == 0 && abs(91.1876-mll_3l)<15  &&  nLepSel<4  && m3L > 100)                  return 1;
  else if (met_pt > 30    && nBJetMedium30 > 0  && abs(91.1876-mll_3l)>5   &&  nLepSel<4  && m3L > 100)                   return 2;
  else if (met_pt > 30    && nBJetMedium30 == 0 && abs(91.1876-mll_3l)<15  &&  nLepSel==4 && m3L > 100  && LepSel4_isTight && LepSel4_pt > 10)     return 3;
  else if (met_pt <= 30   && nBJetMedium30 == 0 && abs(91.1876-mll_3l)>15  && m3L <= 100  &&  nLepSel<4)     return 4;
  else return -1;
}*/




Float_t WZ_weight_W16(Float_t c, Int_t mode)
{
    Float_t fLSM = 0.481; Float_t fRSM = 0.272; Float_t fOSM = 0.247;
    Float_t den = 3./8. *( (1 -c)*(1-c)*fLSM + (1+c)*(1+c)*fRSM + 2*(1-c*c)*fOSM);
    if (mode ==  0) return 3./4.*(1-c*c)*fOSM/den;
    if (mode == -1) return 3./8.*(1-c)*(1-c)*fLSM/den;
    if (mode ==  1) return 3./8.*(1+c)*(1+c)*fRSM/den;
}

Float_t WZ_weight_Wp16(Float_t c, Int_t mode)
{
    Float_t fLSM = 0.538; Float_t fRSM = 0.233; Float_t fOSM = 0.229;
    Float_t den = 3./8. *( (1 -c)*(1-c)*fLSM + (1+c)*(1+c)*fRSM + 2*(1-c*c)*fOSM);
    if (mode ==  0) return 3./4.*(1-c*c)*fOSM/den;
    if (mode == -1) return 3./8.*(1-c)*(1-c)*fLSM/den;
    if (mode ==  1) return 3./8.*(1+c)*(1+c)*fRSM/den;
}


Float_t WZ_weight_Wm16(Float_t c, Int_t mode)
{
    Float_t fLSM = 0.389; Float_t fRSM = 0.333; Float_t fOSM = 0.278;
    Float_t den = 3./8. *( (1 -c)*(1-c)*fLSM + (1+c)*(1+c)*fRSM + 2*(1-c*c)*fOSM);
    if (mode ==  0) return 3./4.*(1-c*c)*fOSM/den;
    if (mode == -1) return 3./8.*(1-c)*(1-c)*fLSM/den;
    if (mode ==  1) return 3./8.*(1+c)*(1+c)*fRSM/den;
}


Float_t WZ_weight_Z16(Float_t c, Int_t mode)
{
    Float_t fLSM = 0.313; Float_t fRSM = 0.429; Float_t fOSM = 0.258;
    Float_t alpha = 0.213;
    Float_t den = 3./8. *( (1 -2*c*alpha + c*c)*fLSM + (1 +2*c*alpha + c*c)*fRSM + 2*(1-c*c)*fOSM);
    if (mode ==  0) return 3./4.*(1-c*c)*fOSM/den;
    if (mode == -1) return 3./8.*(1 -2*c*alpha + c*c)*fLSM/den;
    if (mode ==  1) return 3./8.*(1 +2*c*alpha + c*c)*fRSM/den;
}

Float_t WZ_weight_Zm16(Float_t c, Int_t mode)
{
    Float_t fLSM = 0.291; Float_t fRSM = 0.470; Float_t fOSM = 0.239;
    Float_t alpha = 0.213;
    Float_t den = 3./8. *( (1 -2*c*alpha + c*c)*fLSM + (1 +2*c*alpha + c*c)*fRSM + 2*(1-c*c)*fOSM);
    if (mode ==  0) return 3./4.*(1-c*c)*fOSM/den;
    if (mode == -1) return 3./8.*(1 -2*c*alpha + c*c)*fLSM/den;
    if (mode ==  1) return 3./8.*(1 +2*c*alpha + c*c)*fRSM/den;
}

Float_t WZ_weight_Zp16(Float_t c, Int_t mode)
{
    Float_t fLSM = 0.325; Float_t fRSM = 0.403; Float_t fOSM = 0.271;
    Float_t alpha = 0.213;
    Float_t den = 3./8. *( (1 -2*c*alpha + c*c)*fLSM + (1 +2*c*alpha + c*c)*fRSM + 2*(1-c*c)*fOSM);
    if (mode ==  0) return 3./4.*(1-c*c)*fOSM/den;
    if (mode == -1) return 3./8.*(1 -2*c*alpha + c*c)*fLSM/den;
    if (mode ==  1) return 3./8.*(1 +2*c*alpha + c*c)*fRSM/den;
}

Float_t WZ_weight_WZ(Float_t cW, Float_t cZ, Int_t mode){
    Float_t alpha = 0.213;
    Float_t fLL = 0.1853; 
    Float_t fLR = 0.0738;
    Float_t fLO = 0.0737;
    Float_t fRL = 0.1320;
    Float_t fRR = 0.1451;
    Float_t fRO = 0.1121;
    Float_t fOL = 0.1534;
    Float_t fOR = 0.0714;
    Float_t fOO = 0.0532;
    Float_t den = 3./8. * ( fLL*(1+cW)*(1+cW)*(1+2*alpha*cZ+cZ*cZ) + fLR*(1+cW)*(1+cW)*(1-2*alpha*cZ+cZ*cZ)+ 2*fLO*(1+cW)*(1+cW)*(1-cZ*cZ) + fRL*(1-cW)*(1-cW)*(1+2*alpha*cZ+cZ*cZ) + fRR*(1-cW)*(1-cW)*(1-2*alpha*cZ+cZ*cZ)+ 2*fRO*(1-cW)*(1-cW)*(1-cZ*cZ) + 2*fOL*(1+cW*cW)*(1+2*alpha*cZ+cZ*cZ) + 2*fOR*(1+cW*cW)*(1-2*alpha*cZ+cZ*cZ)+ 4*fOO*(1+cW*cW)*(1-cZ*cZ));
    if (mode == 0) return 3*fOO*(1+cW*cW)*(1-cZ*cZ)/(2*den); // This is component OO
    if (mode == 1) return 3*(fOL*(1+cW*cW)*(1+2*alpha*cZ+cZ*cZ) + fOR*(1+cW*cW)*(1-2*alpha*cZ+cZ*cZ))/(4*den); // This is component OT
    if (mode == 2) return 3*(fLO*(1+cW)*(1+cW)*(1-cZ*cZ)+fRO*(1-cW)*(1-cW)*(1-cZ*cZ))/(4*den); // This is component TO
    if (mode == 3) return 3*(fLL*(1+cW)*(1+cW)*(1+2*alpha*cZ+cZ*cZ) + fLR*(1+cW)*(1+cW)*(1-2*alpha*cZ+cZ*cZ)+fRL*(1-cW)*(1-cW)*(1+2*alpha*cZ+cZ*cZ) + fRR*(1-cW)*(1-cW)*(1-2*alpha*cZ+cZ*cZ))/(8*den); // This is component TT
}

Float_t bincWcZ(Float_t cW, Float_t cZ){
    return floor((cW+1)*5./2.) + floor((cZ + 1)*5/2.)*5.;
}

Float_t WZ_weight_WZ_all(Float_t cW, Float_t cZ, Int_t mode){
    Float_t alpha = 0.213;
    Float_t fLL = 0.1853;
    Float_t fLR = 0.0738;
    Float_t fLO = 0.0737;
    Float_t fRL = 0.1320;
    Float_t fRR = 0.1451;
    Float_t fRO = 0.1121;
    Float_t fOL = 0.1534;
    Float_t fOR = 0.0714;
    Float_t fOO = 0.0532;
    Float_t den = 3./8. * ( fLL*(1+cW)*(1+cW)*(1+2*alpha*cZ+cZ*cZ) + fLR*(1+cW)*(1+cW)*(1-2*alpha*cZ+cZ*cZ)+ 2*fLO*(1+cW)*(1+cW)*(1-cZ*cZ) + fRL*(1-cW)*(1-cW)*(1+2*alpha*cZ+cZ*cZ) + fRR*(1-cW)*(1-cW)*(1-2*alpha*cZ+cZ*cZ)+ 2*fRO*(1-cW)*(1-cW)*(1-cZ*cZ) + 2*fOL*(1+cW*cW)*(1+2*alpha*cZ+cZ*cZ) + 2*fOR*(1+cW*cW)*(1-2*alpha*cZ+cZ*cZ)+ 4*fOO*(1+cW*cW)*(1-cZ*cZ));
    if (mode == 0) return 4*fOO*(1+cW*cW)*(1-cZ*cZ)/(den); // This is component OO
    if (mode == 1) return 2*(fOL*(1+cW*cW)*(1+2*alpha*cZ+cZ*cZ))/(den); // This is component OL
    if (mode == 2) return 2*fOR*(1+cW*cW)*(1-2*alpha*cZ+cZ*cZ)/den; // This is component OR
    if (mode == 3) return 2*fRO*(1-cW)*(1-cW)*(1-cZ*cZ)/den; // This is component RO
    if (mode == 4) return fRR*(1-cW)*(1-cW)*(1-2*alpha*cZ+cZ*cZ)/den; // This is component OR
    if (mode == 5) return fRL*(1-cW)*(1-cW)*(1+2*alpha*cZ+cZ*cZ)/den; // This is component OR
    if (mode == 6) return 2*fLO*(1+cW)*(1+cW)*(1-cZ*cZ)/den; // This is component OR
    if (mode == 7) return fLR*(1+cW)*(1+cW)*(1-2*alpha*cZ+cZ*cZ)/den; // This is component OR
    if (mode == 8) return fLL*(1+cW)*(1+cW)*(1+2*alpha*cZ+cZ*cZ)/den; // This is component OR
}

/*Float_t WZ_weight_Z(Float_t c, Int_t mode)
{
    Float_t fLSM = 0.314; Float_t fRSM = 0.424; Float_t fOSM = 0.262;
    Float_t alpha = 0.213;
    Float_t den = 3./8. *( (1 -2*c*alpha + c*c)*fLSM + (1 +2*c*alpha + c*c)*fRSM + 2*(1-c*c)*fOSM);
    if (mode ==  0) return 3./4.*(1-c*c)*fOSM/den;
    if (mode == -1) return 3./8.*(1 -2*c*alpha + c*c)*fLSM/den;
    if (mode ==  1) return 3./8.*(1 +2*c*alpha + c*c)*fRSM/den;
}

Float_t WZ_weight_ZP(Float_t c, Int_t mode)
{
    Float_t fLSM = 0.335; Float_t fRSM = 0.389; Float_t fOSM = 0.275;
    Float_t alpha = 0.213;
    Float_t den = 3./8. *( (1 -2*c*alpha + c*c)*fLSM + (1 +2*c*alpha + c*c)*fRSM + 2*(1-c*c)*fOSM);
    if (mode ==  0) return 3./4.*(1-c*c)*fOSM/den;
    if (mode == -1) return 3./8.*(1 -2*c*alpha + c*c)*fLSM/den;
    if (mode ==  1) return 3./8.*(1 +2*c*alpha + c*c)*fRSM/den;
}


Float_t WZ_weight_ZM(Float_t c, Int_t mode)
{
    Float_t fLSM = 0.278; Float_t fRSM = 0.481; Float_t fOSM = 0.242;
    Float_t alpha = 0.213;
    Float_t den = 3./8. *( (1 -2*c*alpha + c*c)*fLSM + (1 +2*c*alpha + c*c)*fRSM + 2*(1-c*c)*fOSM);
    if (mode ==  0) return 3./4.*(1-c*c)*fOSM/den;
    if (mode == -1) return 3./8.*(1 -2*c*alpha + c*c)*fLSM/den;
    if (mode ==  1) return 3./8.*(1 +2*c*alpha + c*c)*fRSM/den;
}*/


float unrealnessW(Float_t ptl, Float_t etal, Float_t phil, Float_t ptnu, Float_t phinu){
   Float_t muVal = (80.385)*(80.385)/2. + ptl*ptnu*TMath::Cos(phil-phinu);
   Float_t disc  = (muVal*muVal*ptl*ptl*TMath::SinH(etal)*TMath::SinH(etal)/(ptl*ptl*ptl*ptl) - ((ptl*ptl*TMath::CosH(etal)*TMath::CosH(etal))*ptnu*ptnu - muVal*muVal)/ptl*ptl);        
   return disc;
}

float ISRUp(int nJet){
if (nJet <= 0) return 1.;
if (nJet == 1) return 0.98;
if (nJet == 2) return 1.02;
if (nJet == 3) return 1.06;
if (nJet == 4) return 1.08;
if (nJet == 5) return 1.10;
if (nJet == 6) return 1.12;
if (nJet >= 7) return 1.17;
}

float ISRDn(int nJet){
if (nJet <= 0) return 1.;
if (nJet == 1) return 1.02;
if (nJet == 2) return 0.98;
if (nJet == 3) return 0.95;
if (nJet == 4) return 0.93;
if (nJet == 5) return 0.91;
if (nJet == 6) return 0.88;
if (nJet >= 7) return 0.83;
}

float weight_mWZ(float mWZ){
 if (mWZ <= 200) return 1.03113;
 if (mWZ <= 300) return 0.994016;
 if (mWZ <= 400) return 1.00339;
 if (mWZ <= 500) return 0.999467;
 if (mWZ <= 1000) return 0.96045;
 if (mWZ <= 1500) return 0.822343;
 //if (mWZ <= 3000) return 0.740922;
 else return 1.;
}
void functionsWZ() {}
