#include "TH2F.h"
#include "TMath.h"
#include "TGraphAsymmErrors.h"
#include "TFile.h"
#include "TSystem.h"
#include <iostream>

using namespace std;

TString CMSSW_BASE_SF = gSystem->ExpandPathName("${CMSSW_BASE}");
TString DATA_SF = CMSSW_BASE_SF+"/src/CMGTools/TTHAnalysis/data";

float getSF(TH2F* hist, float pt, float eta){
    int xbin = std::max(1, std::min(hist->GetNbinsX(), hist->GetXaxis()->FindBin(pt)));
    int ybin = std::max(1, std::min(hist->GetNbinsY(), hist->GetYaxis()->FindBin(eta)));
    return hist->GetBinContent(xbin,ybin);
}

float getSF(TH2D* hist, float pt, float eta){
    int xbin = std::max(1, std::min(hist->GetNbinsX(), hist->GetXaxis()->FindBin(pt)));
    int ybin = std::max(1, std::min(hist->GetNbinsY(), hist->GetYaxis()->FindBin(eta)));
    return hist->GetBinContent(xbin,ybin);
}

float getUnc(TH2F* hist, float pt, float eta){
    int xbin = std::max(1, std::min(hist->GetNbinsX(), hist->GetXaxis()->FindBin(pt)));
    int ybin = std::max(1, std::min(hist->GetNbinsY(), hist->GetYaxis()->FindBin(eta)));
    return hist->GetBinError(xbin,ybin);
}


// TRIGGER SCALE FACTORS FULLSIM
// -------------------------------------------------------------

// files
TFile* f_trigEff_0tau = new TFile(DATA_SF+"/triggerSF/triggerSF_0tau_EWKino_fastsim_M17_36p5fb.root", "read");
TFile* f_trigEff_1tau = new TFile(DATA_SF+"/triggerSF/triggerSF_1tau_EWKino_fastsim_M17_36p5fb.root", "read");
TFile* f_trigSF_1lep  = new TFile(DATA_SF+"/triggerSF/triggerSF_1lep_EWKino_M17_36p5fb.root"        , "read");

// fullsim
TH2F* h_trigSF_1el   = (TH2F*) f_trigSF_1lep -> Get("ele27_sf");
TH2F* h_trigSF_1mu   = (TH2F*) f_trigSF_1lep -> Get("isomu24_sf");

float triggerSFfullsim(float pt1  , float eta1  , int pdg1  ,
                       float pt2  , float eta2  , int pdg2  ,
                       float pt3=0, float eta3=0, int pdg3=0) {

    int nTaus = (abs(pdg1)==15)+(abs(pdg2)==15)+(abs(pdg3)==15);

    // 2lss or 3l 1tau region
    if(pdg3==0 || nTaus==1) {
        float lpt1 = pt1; float lpt2 = pt2; int lpdg1 = pdg1; int lpdg2 = pdg2;
        if(abs(pdg1)==15) {lpt1 = pt2; lpdg1 = pdg2; lpt2 = pt3; lpdg2 = pdg3; } 
        if(abs(pdg2)==15) {lpt1 = pt1; lpdg1 = pdg1; lpt2 = pt3; lpdg2 = pdg3; } 
        if(abs(lpdg1)+abs(lpdg2)!=22) return 1.0;
        if(lpt1>30 || lpt2>20       ) return 1.0;
        return 0.95;
    }

    // 3l 2tau
    if(nTaus==2){ 
        float lpt = pt1; float leta = eta1; int lpdg = pdg1;
        if(abs(pdg2)!=15) {lpt = pt2; leta = eta2; lpdg = pdg2; } 
        if(abs(pdg3)!=15) {lpt = pt3; leta = eta3; lpdg = pdg3; } 
        TH2F* hist = (abs(lpdg)==13)?h_trigSF_1mu:h_trigSF_1el;
        return getSF(hist, lpt, abs(leta));
    }

    return 1.0;
}

// fastsim
TH2F* h_trigEff_0tau = (TH2F*) f_trigEff_0tau -> Get("h_0tau_num");
TH2F* h_trigEff_1tau = (TH2F*) f_trigEff_1tau -> Get("h_1tau_num");
TH2F* h_trigEff_1el  = (TH2F*) f_trigSF_1lep  -> Get("hist2dnum_Ele27_WPTight_Gsf_fromemu__HLT_Ele27_WPTight_Gsfpt");
TH2F* h_trigEff_1mu  = (TH2F*) f_trigSF_1lep  -> Get("hist2dnum_IsoMu24orIsoTkMu24_fromemu__HLT_IsoMu24orIsoTkMu24pt");


float triggerSFfastsim(float pt1  , float eta1  , int pdg1  ,
                       float pt2  , float eta2  , int pdg2  ,
                       float pt3=0, float eta3=0, int pdg3=0) {

    int nTaus = (abs(pdg1)==15)+(abs(pdg2)==15)+(abs(pdg3)==15);

    // 2lss or 3l 1tau region
    if(pdg3==0 || nTaus==1) {
        float lpt1 = pt1; float lpt2 = pt2;
        if(abs(pdg1)==15) {lpt1 = pt2; lpt2 = pt3; } 
        if(abs(pdg2)==15) {lpt1 = pt1; lpt2 = pt3; } 
        return getSF(h_trigEff_1tau, lpt1, lpt2);
    }

    // 3l 2tau
    if(nTaus==2){ 
        float lpt = pt1; float leta = eta1; int lpdg = pdg1;
        if(abs(pdg2)!=15) {lpt = pt2; leta = eta2; lpdg = pdg2; } 
        if(abs(pdg3)!=15) {lpt = pt3; leta = eta3; lpdg = pdg3; } 
        TH2F* hist = (abs(lpdg)==13)?h_trigEff_1mu:h_trigEff_1el;
        return getSF(hist, lpt, abs(leta));
    }

    // 3l 0tau
    if(nTaus==0){
        return getSF(h_trigEff_0tau, pt2, pt3);
    } 
    return 1.0;
}



// LEPTON SCALE FACTORS FULLSIM
// -------------------------------------------------------------


// electrons
TFile* f_elSF_id   = new TFile(DATA_SF+"/leptonSF/electronSF_id_EWKino_fullsim_M17_36p5fb.root"    , "read");
TFile* f_elSF_eff  = new TFile(DATA_SF+"/leptonSF/electronSF_trkEff_EWKino_fullsim_M17_36p5fb.root", "read");
TH2F* h_elSF_mvaVT = (TH2F*) f_elSF_id ->Get("GsfElectronToLeptonMvaVTIDEmuTightIP2DSIP3D8mini04");
TH2F* h_elSF_mvaM  = (TH2F*) f_elSF_id ->Get("GsfElectronToLeptonMvaMIDEmuTightIP2DSIP3D8mini04");
TH2F* h_elSF_id    = (TH2F*) f_elSF_id ->Get("GsfElectronToMVAVLooseTightIP2D");
TH2F* h_elSF_trk   = (TH2F*) f_elSF_eff->Get("EGamma_SF2D");

// muons
TFile* f_muSF_mvaVT = new TFile(DATA_SF+"/leptonSF/muonSF_mvaVT_EWKino_fullsim_M17_36p5fb.root", "read");
TFile* f_muSF_mvaM  = new TFile(DATA_SF+"/leptonSF/muonSF_mvaM_EWKino_fullsim_M17_36p5fb.root" , "read");
TFile* f_muSF_id    = new TFile(DATA_SF+"/leptonSF/muonSF_id_EWKino_fullsim_M17_36p5fb.root"   , "read");
TFile* f_muSF_eff   = new TFile(DATA_SF+"/leptonSF/muonSF_trk_EWKino_fullsim_M17_36p5fb.root"  , "read"); 
TH2F* h_muSF_mvaVT = (TH2F*) f_muSF_mvaVT->Get("SF" );
TH2F* h_muSF_mvaM  = (TH2F*) f_muSF_mvaM ->Get("SF" );
TH2F* h_muSF_id    = (TH2F*) f_muSF_id   ->Get("SF" );
TGraphAsymmErrors* h_muSF_trk = (TGraphAsymmErrors*) f_muSF_eff->Get("ratio_eff_eta3_dr030e030_corr");


float getElectronSF(float pt, float eta, int wp = 0){
    TH2F* hist = (wp == 1)?h_elSF_mvaVT:h_elSF_mvaM;
    return getSF(hist, pt, abs(eta))*getSF(h_elSF_id, pt, abs(eta))*getSF(h_elSF_trk, eta, pt);
}


float getElectronUnc(float pt, float eta, int wp = 0, int var = 0){
    TH2F* hist = (wp == 1)?h_elSF_mvaVT:h_elSF_mvaM;
    float error1 = getUnc(hist      , pt , abs(eta));
    float error2 = getUnc(h_elSF_id , pt , abs(eta));
    float error3 = getUnc(h_elSF_trk, eta, pt);
    return TMath::Sqrt(error1*error1 + error2*error2 + error3*error3);
}


float getMuonSF(float pt, float eta, int wp = 0){
    TH2F* hist = (wp == 1)?h_muSF_mvaVT:h_muSF_mvaM;
    return h_muSF_trk->Eval(eta)*getSF(hist, pt, abs(eta))*getSF(h_muSF_id, pt, abs(eta)); 
}

float getMuonUnc(float pt, int var = 0) {
    if (pt<20)  //FIXME: check uncertainty on tracking efficiency once it is available
         return TMath::Sqrt(0.03*0.03+0.01*0.01+0.01*0.01);
    return TMath::Sqrt(0.02*0.02+0.01*0.01);  
}




float getLepSF(float pt, float eta, int pdgId, int isTight, int wp = 0, int var = 0){
    if(!isTight) return 1.0;
    float sf  = 1.0; 
    float err = 0.0;
    if(abs(pdgId) == 11) { sf = getElectronSF(pt, eta, wp);}
    if(abs(pdgId) == 13) { sf = getMuonSF(pt, eta, wp);} // only relative error
    if(abs(pdgId) == 15) { sf = 0.95                      ; err = 0.05;                             };
    return (var==0)?sf:(sf+var*err)/sf;

}


// electrons
//TFile* f_elSF_id   = new TFile(DATA_SF+"/leptonSF/electronSF_id_EWKino_fullsim_M17_36p5fb.root"    , "read");
TFile* f_elSF_Loose2018  = new TFile(DATA_SF+"/leptonSF/egamma2017_Loose.root", "read"); //Loose ID + ISO SF
TH2F* h_elSF_Loose2018   = (TH2F*) f_elSF_Loose2018->Get("EGamma_SF2D");
TFile* f_elSF_Tight2018  = new TFile(DATA_SF+"/leptonSF/egamma2017_Tight_Old.root", "read"); //Loose to Tight ID + ISO SF
TH2F* h_elSF_Tight2018   = (TH2F*) f_elSF_Tight2018->Get("EGamma_SF2D");

// muons
TFile* f_muSF_id2018    = new TFile(DATA_SF+"/leptonSF/muon_SF_ID_2018.root"   , "read");
TH2F* h_muSF_id2018    = (TH2F*) f_muSF_id2018->Get("NUM_LooseID_DEN_genTracks_pt_abseta" );

TFile* f_muSF_id2018_T    = new TFile(DATA_SF+"/leptonSF/EfficienciesAndSF_Tight_EWKino_2017Cut_NUM_Tight_EWKino_2017Cut_DEN_Loose_EWKino_2017Cut_PAR_pt_eta.root"   , "read");
TH2F* h_muSF_id2018_T    = (TH2F*) f_muSF_id2018_T->Get("EfficiencyLOOSEMVA_TightMVA_Final/pt_abseta_ratio");


float getElectronSF2018(float pt, float eta, int wp = 0){
    //TH2F* hist1 = (wp == 1)?h_elSF_mvaVT:h_elSF_mvaM;
    //return getSF(hist, pt, abs(eta))*getSF(h_elSF_id, pt, abs(eta))*getSF(h_elSF_trk, eta, pt);
    return getSF(h_elSF_Loose2018, eta, pt)*getSF(h_elSF_Tight2018, eta, pt);
}

float getMuonSF2018(float pt, float eta, int wp = 0){
    return getSF(h_muSF_id2018_T, pt, abs(eta))*getSF(h_muSF_id2018, pt, abs(eta)); 
    //return getSF(h_muSF_id2018, abs(eta), pt)*getSF(hist, pt, abs(eta));
}


float getLepSF2018(float pt, float eta, int pdgId, int isTight, int wp = 0, int var = 0){
    if(!isTight) return 1.0;
    float sf  = 1.0; 
    float err = 0.0;
    if(abs(pdgId) == 11) { sf = getElectronSF2018(pt, eta, wp);}
    if(abs(pdgId) == 13) { sf = getMuonSF2018    (pt, eta, wp);} // only relative error
    if(abs(pdgId) == 15) { sf = 0.95                      ; err = 0.05;                             };
    return (var==0)?sf:(sf+var*err)/sf;

}


float getLepSF2018Loose(float pt, float eta, int pdgId, int isTight, int wp = 0, int var = 0){
    if(!isTight) return 1.0;
    float sf  = 1.0; 
    float err = 0.0;
    if(abs(pdgId) == 11) { sf = getSF(h_elSF_Loose2018, eta, pt);}
    if(abs(pdgId) == 13) { sf = h_muSF_trk->Eval(eta)*getSF(h_muSF_id2018, pt, abs(eta));} // only relative error
    if(abs(pdgId) == 15) { sf = 0.95                      ; err = 0.05;                             };
    return (var==0)?sf:(sf+var*err)/sf;

}






float leptonSF(float lepSF1, float lepSF2, float lepSF3 = 1, float lepSF4 = 1){
    return lepSF1*lepSF2*lepSF3*lepSF4;
}



// LEPTON SCALE FACTORS FASTSIM SPRING16
// -------------------------------------------------------------

// electrons
TFile* f_elSF_FS_mvaVT = new TFile(DATA_SF+"/leptonSF/electronSF_mvaVT_EWKino_fastsim_M17_36p5fb.root", "read");
TFile* f_elSF_FS_mvaM  = new TFile(DATA_SF+"/leptonSF/electronSF_mvaM_EWKino_fastsim_M17_36p5fb.root" , "read");
TFile* f_elSF_FS_id    = new TFile(DATA_SF+"/leptonSF/electronSF_id_EWKino_fastsim_M17_36p5fb.root"   , "read");
TH2F* h_elSF_FS_mvaVT  = (TH2F*) f_elSF_FS_mvaVT->Get("histo2D");
TH2F* h_elSF_FS_mvaM   = (TH2F*) f_elSF_FS_mvaM ->Get("histo2D");
TH2F* h_elSF_FS_id     = (TH2F*) f_elSF_FS_id   ->Get("histo2D");

// muons
TFile* f_muSF_FS_mvaVT = new TFile(DATA_SF+"/leptonSF/muonSF_mvaVT_EWKino_fastsim_M17_36p5fb.root", "read");
TFile* f_muSF_FS_mvaM  = new TFile(DATA_SF+"/leptonSF/muonSF_mvaM_EWKino_fastsim_M17_36p5fb.root" , "read");
TFile* f_muSF_FS_id    = new TFile(DATA_SF+"/leptonSF/muonSF_id_EWKino_fastsim_M17_36p5fb.root"   , "read");
TH2F* h_muSF_FS_mvaVT  = (TH2F*) f_muSF_FS_mvaVT->Get("histo2D");
TH2F* h_muSF_FS_mvaM   = (TH2F*) f_muSF_FS_mvaM ->Get("histo2D");
TH2F* h_muSF_FS_id     = (TH2F*) f_muSF_FS_id   ->Get("histo2D");

// taus
TFile* f_tauSF_FS_id = new TFile(DATA_SF+"/leptonSF/tauSF_id_EWKino_fastsim_M17_36p5fb.root", "read");
TH2F* h_tauSF_FS_id  = (TH2F*) f_tauSF_FS_id->Get("histo2D" );

float getElectronSFFS(float pt, float eta, int wp = 0){
    TH2F* hist = (wp == 1)?h_elSF_FS_mvaVT:h_elSF_FS_mvaM;
    return getSF(hist, pt, abs(eta))*getSF(h_elSF_FS_id, pt, abs(eta));
}

float getElectronUncFS(int var = 0){
	return 0.02;
}

float getMuonSFFS(float pt, float eta, int wp = 0){
    TH2F* hist = (wp == 1)?h_muSF_FS_mvaVT:h_muSF_FS_mvaM;
    return getSF(hist, pt, abs(eta))*getSF(h_muSF_FS_id, pt, abs(eta)); 
}

float getMuonUncFS(float pt, int var = 0) {
	return 0.02;
}

float getTauSFFS(float pt, float eta){
    return getSF(h_tauSF_FS_id, pt, abs(eta));
}

float getTauUncFS(float pt, float eta, int var = 0) {
	return getUnc(h_tauSF_FS_id, pt, abs(eta));
}

float getLepSFFS(float pt, float eta, int pdgId, int isTight, int wp = 0, int var = 0){
    if(!isTight) return 1.0;
    float sf  = 1.0; 
    float err = 0.0;
    if(abs(pdgId) == 11) { sf = getElectronSFFS(pt, eta, wp); err = sf*getElectronUncFS(var); } // relative uncertainty
    if(abs(pdgId) == 13) { sf = getMuonSFFS    (pt, eta, wp); err = sf*getMuonUncFS    (var); } // relative uncertainty
    if(abs(pdgId) == 15) { sf = getTauSFFS     (pt, eta    ); err = getTauUncFS(pt, eta, var);}
    return (var==0)?sf:(sf+var*err)/sf;
}

float leptonSFFS(float lepSF1, float lepSF2, float lepSF3 = 1.0, float lepSF4 = 1.0){
    return lepSF1*lepSF2*lepSF3*lepSF4;
}



// LEPTON SCALE FACTORS FASTSIM SUMMER16
// -------------------------------------------------------------

// electrons
TFile* f_elSF_FS16_mvaVT = new TFile(DATA_SF+"/leptonSF/electronSF_mvaVT_EWKino_fastsim_Summer16_M17_36p5fb.root", "read");
TFile* f_elSF_FS16_mvaM  = new TFile(DATA_SF+"/leptonSF/electronSF_mvaM_EWKino_fastsim_Summer16_M17_36p5fb.root" , "read");
TH2F* h_elSF_FS16_mvaVT  = (TH2F*) f_elSF_FS16_mvaVT->Get("histo2D");
TH2F* h_elSF_FS16_mvaM   = (TH2F*) f_elSF_FS16_mvaM ->Get("histo2D");

// muons
TFile* f_muSF_FS16_mvaVT = new TFile(DATA_SF+"/leptonSF/muonSF_mvaVT_EWKino_fastsim_Summer16_M17_36p5fb.root", "read");
TFile* f_muSF_FS16_mvaM  = new TFile(DATA_SF+"/leptonSF/muonSF_mvaM_EWKino_fastsim_Summer16_M17_36p5fb.root" , "read");
TH2F* h_muSF_FS16_mvaVT  = (TH2F*) f_muSF_FS16_mvaVT->Get("histo2D");
TH2F* h_muSF_FS16_mvaM   = (TH2F*) f_muSF_FS16_mvaM ->Get("histo2D");

float getElectronSFFS16(float pt, float eta, int wp = 0){
    TH2F* hist = (wp == 1)?h_elSF_FS16_mvaVT:h_elSF_FS16_mvaM;
    return getSF(hist, pt, abs(eta));
}

float getElectronUncFS16(int var = 0){
	return 0.02;
}

float getMuonSFFS16(float pt, float eta, int wp = 0){
    TH2F* hist = (wp == 1)?h_muSF_FS16_mvaVT:h_muSF_FS16_mvaM;
    return getSF(hist, pt, abs(eta));
}

float getMuonUncFS16(float pt, int var = 0) {
	return 0.02;
}

float getTauSFFS16(float pt, float eta){
	return 1.0;
}

float getTauUncFS16(float pt, float eta, int var = 0) {
	return 0.02;
}

float getLepSFFS16(float pt, float eta, int pdgId, int isTight, int wp = 0, int var = 0){
    if(!isTight) return 1.0;
    float sf  = 1.0; 
    float err = 0.0;
    if(abs(pdgId) == 11) { sf = getElectronSFFS16(pt, eta, wp); err = sf*getElectronUncFS16(var); } // relative uncertainty
    if(abs(pdgId) == 13) { sf = getMuonSFFS16    (pt, eta, wp); err = sf*getMuonUncFS16    (var); } // relative uncertainty
    if(abs(pdgId) == 15) { sf = getTauSFFS16     (pt, eta    ); err = sf*getTauUncFS16(pt, eta, var);} // relative uncertainty
    return (var==0)?sf:(sf+var*err)/sf;
}

float leptonSFFS16(float lepSF1, float lepSF2, float lepSF3 = 1.0, float lepSF4 = 1.0){
    return lepSF1*lepSF2*lepSF3*lepSF4;
}

float AdHoc(Int_t Trigee, Int_t Trige, Int_t Trigem){
    float SF = 1;
    if (Trige > 0) SF *= 1./1.139;
    else SF *= 1./0.82;
    return SF;
}

///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//Lepton SF for the first set of legacy Data/MC (nanoAODv5), 17Jul2018 (2016) + 17Nov2017 (2017) + 17Sep2018 (2018) data reprocessing//
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

///////////
// EL SF //
///////////
TFile* f_elSF_v5_2016_2lss  = new TFile(DATA_SF+"/EWKino/SF/SFElectronGlobal16_2lsstight.root", "read");
TH2F*  h_elSF_v5_2016_2lss  = (TH2F*) f_elSF_v5_2016_2lss->Get("SFglobal");
TFile* f_elSF_v5_2017_2lss  = new TFile(DATA_SF+"/EWKino/SF/SFElectronGlobal17_2lsstight.root", "read");
TH2F*  h_elSF_v5_2017_2lss  = (TH2F*) f_elSF_v5_2017_2lss->Get("SFglobal");
TFile* f_elSF_v5_2018_2lss  = new TFile(DATA_SF+"/EWKino/SF/SFElectronGlobal18_2lsstight.root", "read");
TH2F*  h_elSF_v5_2018_2lss  = (TH2F*) f_elSF_v5_2018_2lss->Get("SFglobal");

TFile* f_elSF_v5_2016_3l  = new TFile(DATA_SF+"/EWKino/SF/SFElectronGlobal16_3ltight.root", "read");
TH2F*  h_elSF_v5_2016_3l  = (TH2F*) f_elSF_v5_2016_3l->Get("SFglobal");
TFile* f_elSF_v5_2017_3l  = new TFile(DATA_SF+"/EWKino/SF/SFElectronGlobal17_3ltight.root", "read");
TH2F*  h_elSF_v5_2017_3l  = (TH2F*) f_elSF_v5_2017_3l->Get("SFglobal");
TFile* f_elSF_v5_2018_3l  = new TFile(DATA_SF+"/EWKino/SF/SFElectronGlobal18_3ltight.root", "read");
TH2F*  h_elSF_v5_2018_3l  = (TH2F*) f_elSF_v5_2018_3l->Get("SFglobal");

TFile* f_elSF_v5_2016_FO  = new TFile(DATA_SF+"/EWKino/SF/SFElectronGlobal16_FO.root", "read");
TH2F*  h_elSF_v5_2016_FO  = (TH2F*) f_elSF_v5_2016_FO->Get("SFglobal");
TFile* f_elSF_v5_2017_FO  = new TFile(DATA_SF+"/EWKino/SF/SFElectronGlobal17_FO.root", "read");
TH2F*  h_elSF_v5_2017_FO  = (TH2F*) f_elSF_v5_2017_FO->Get("SFglobal");
TFile* f_elSF_v5_2018_FO  = new TFile(DATA_SF+"/EWKino/SF/SFElectronGlobal18_FO.root", "read");
TH2F*  h_elSF_v5_2018_FO  = (TH2F*) f_elSF_v5_2018_FO->Get("SFglobal");


float getElSF_v5_2016(int wp, int unc, float pt, float eta){
  float sf;
  float sfcorr;
  if (wp == 1){
    sf     = getSF(h_elSF_v5_2016_2lss, eta, pt);
    sfcorr = getUnc(h_elSF_v5_2016_2lss, eta, pt);
  }
  if (wp == 2){
    sf     = getSF(h_elSF_v5_2016_3l, eta, pt);
    sfcorr = getUnc(h_elSF_v5_2016_3l, eta, pt);
  }
  if (wp == 3){
    sf     = getSF(h_elSF_v5_2016_FO, eta, pt);
    sfcorr = getUnc(h_elSF_v5_2016_FO, eta, pt);
  }
  return sf*(1+unc*sfcorr);
}

float getElSF_v5_2017(int wp, int unc, float pt, float eta){
  float sf;
  float sfcorr;
  if (wp == 1){
    sf     = getSF(h_elSF_v5_2017_2lss, eta, pt);
    sfcorr = getUnc(h_elSF_v5_2017_2lss, eta, pt);
  }
  if (wp == 2){
    sf     = getSF(h_elSF_v5_2017_3l, eta, pt);
    sfcorr = getUnc(h_elSF_v5_2017_3l, eta, pt);
  }
  if (wp == 3){
    sf     = getSF(h_elSF_v5_2017_FO, eta, pt);
    sfcorr = getUnc(h_elSF_v5_2017_FO, eta, pt);
  }
  return sf*(1+unc*sfcorr);
}

float getElSF_v5_2018(int wp, int unc, float pt, float eta){
  float sf;
  float sfcorr;
  if (wp == 1){
    sf     = getSF(h_elSF_v5_2018_2lss, eta, pt);
    sfcorr = getUnc(h_elSF_v5_2018_2lss, eta, pt);
  }
  if (wp == 2){
    sf     = getSF(h_elSF_v5_2018_3l, eta, pt);
    sfcorr = getUnc(h_elSF_v5_2018_3l, eta, pt);
  }
  if (wp == 3){
    sf     = getSF(h_elSF_v5_2018_FO, eta, pt);
    sfcorr = getUnc(h_elSF_v5_2018_FO, eta, pt);
  }
  return sf*(1+unc*sfcorr);
}

float getElSF_v5(int wp, int unc, int year, float pt, float eta){
  //El SF
  if (year==2016) return getElSF_v5_2016(wp, unc, pt, eta);
  if (year==2017) return getElSF_v5_2017(wp, unc, pt, eta);
  if (year==2018) return getElSF_v5_2018(wp, unc, pt, eta);
  else std::cout << "Wrong year for electron SF!!" << std::endl;
  return -1.;
}


///////////
// MU SF //
///////////

TFile* f_muSF_v5_2016_2lss  = new TFile(DATA_SF+"/EWKino/SF/SFMuonGlobal16_2lsstight.root", "read");
TH2F*  h_muSF_v5_2016_2lss  = (TH2F*) f_muSF_v5_2016_2lss->Get("SFglobal");
TFile* f_muSF_v5_2017_2lss  = new TFile(DATA_SF+"/EWKino/SF/SFMuonGlobal17_2lsstight.root", "read");
TH2F*  h_muSF_v5_2017_2lss  = (TH2F*) f_muSF_v5_2017_2lss->Get("SFglobal");
TFile* f_muSF_v5_2018_2lss  = new TFile(DATA_SF+"/EWKino/SF/SFMuonGlobal18_2lsstight.root", "read");
TH2F*  h_muSF_v5_2018_2lss  = (TH2F*) f_muSF_v5_2018_2lss->Get("SFglobal");

TFile* f_muSF_v5_2016_3l  = new TFile(DATA_SF+"/EWKino/SF/SFMuonGlobal16_3ltight.root", "read");
TH2F*  h_muSF_v5_2016_3l  = (TH2F*) f_muSF_v5_2016_3l->Get("SFglobal");
TFile* f_muSF_v5_2017_3l  = new TFile(DATA_SF+"/EWKino/SF/SFMuonGlobal17_3ltight.root", "read");
TH2F*  h_muSF_v5_2017_3l  = (TH2F*) f_muSF_v5_2017_3l->Get("SFglobal");
TFile* f_muSF_v5_2018_3l  = new TFile(DATA_SF+"/EWKino/SF/SFMuonGlobal18_3ltight.root", "read");
TH2F*  h_muSF_v5_2018_3l  = (TH2F*) f_muSF_v5_2018_3l->Get("SFglobal");

TFile* f_muSF_v5_2016_FO  = new TFile(DATA_SF+"/EWKino/SF/SFMuonGlobal16_FO.root", "read");
TH2F*  h_muSF_v5_2016_FO  = (TH2F*) f_muSF_v5_2016_FO->Get("SFglobal");
TFile* f_muSF_v5_2017_FO  = new TFile(DATA_SF+"/EWKino/SF/SFMuonGlobal17_FO.root", "read");
TH2F*  h_muSF_v5_2017_FO  = (TH2F*) f_muSF_v5_2017_FO->Get("SFglobal");
TFile* f_muSF_v5_2018_FO  = new TFile(DATA_SF+"/EWKino/SF/SFMuonGlobal18_FO.root", "read");
TH2F*  h_muSF_v5_2018_FO  = (TH2F*) f_muSF_v5_2018_FO->Get("SFglobal");


float getMuSF_v5_2016(int wp, int unc, float pt, float eta){
  float sf;
  float sfcorr;
  if (wp == 1){
    sf     = getSF(h_muSF_v5_2016_2lss, abs(eta), pt);
    sfcorr = getUnc(h_muSF_v5_2016_2lss, abs(eta), pt);
  }
  if (wp == 2){
    sf     = getSF(h_muSF_v5_2016_3l, abs(eta), pt);
    sfcorr = getUnc(h_muSF_v5_2016_3l, abs(eta), pt);
  }
  if (wp == 3){
    sf     = getSF(h_muSF_v5_2016_FO, abs(eta), pt);
    sfcorr = getUnc(h_muSF_v5_2016_FO, abs(eta), pt);
  }
  return sf*(1+unc*sfcorr);
}

float getMuSF_v5_2017(int wp, int unc, float pt, float eta){
  float sf;
  float sfcorr;
  if (wp == 1){
    sf     = getSF(h_muSF_v5_2017_2lss, abs(eta), pt);
    sfcorr = getUnc(h_muSF_v5_2017_2lss, abs(eta), pt);
  }
  if (wp == 2){
    sf     = getSF(h_muSF_v5_2017_3l, abs(eta), pt);
    sfcorr = getUnc(h_muSF_v5_2017_3l, abs(eta), pt);
  }
  if (wp == 3){
    sf     = getSF(h_muSF_v5_2017_FO, abs(eta), pt);
    sfcorr = getUnc(h_muSF_v5_2017_FO, abs(eta), pt);
  }
  return sf*(1+unc*sfcorr);
}

float getMuSF_v5_2018(int wp, int unc, float pt, float eta){
  float sf;
  float sfcorr;
  if (wp == 1){
    sf     = getSF(h_muSF_v5_2018_2lss, abs(eta), pt);
    sfcorr = getUnc(h_muSF_v5_2018_2lss, abs(eta), pt);
  }
  if (wp == 2){
    sf     = getSF(h_muSF_v5_2018_3l, abs(eta), pt);
    sfcorr = getUnc(h_muSF_v5_2018_3l, abs(eta), pt);
  }
  if (wp == 3){
    sf     = getSF(h_muSF_v5_2018_FO, abs(eta), pt);
    sfcorr = getUnc(h_muSF_v5_2018_FO, abs(eta), pt);
  }
  return sf*(1+unc*sfcorr);
}

float getMuSF_v5(int wp, int unc, int year, float pt, float eta){
  //El SF
  if (year==2016) return getMuSF_v5_2016(wp, unc, pt, eta);
  if (year==2017) return getMuSF_v5_2017(wp, unc, pt, eta);
  if (year==2018) return getMuSF_v5_2018(wp, unc, pt, eta);
  else std::cout << "Wrong year for electron SF!!" << std::endl;
  return -1.;
}
  
  
  
////////////
// TAU SF //
////////////


float getTauSF_v5_2016(int wp, int unc){
  //From here https://twiki.cern.ch/twiki/bin/view/CMS/TauIDRecommendation13TeV#Performance_in_data_and_recommen
  float sf; float corr;
  switch (wp){
  case 0:
    sf=0.90; corr=0.03;

  case 1:
    sf=0.90; corr=0.03;

  case 2:
    sf=0.86; corr=0.02;

  case 3:
    sf=0.88; corr=0.02;

  case 4:
    sf=0.87; corr=0.02;

  case 5:
    sf=0.86; corr=0.02;

  case 6:
    sf=0.86; corr=0.02;

  return sf*(1+corr*unc);
  }
}

float getTauSF_v5_2017(int wp, int unc){
  //From here https://twiki.cern.ch/twiki/bin/view/CMS/TauIDRecommendation13TeV#Performance_in_data_and_recommen
  float sf; float corr;
  switch (wp){
  case 0:
    sf=0.89; corr=0.03;

  case 1:
    sf=0.88; corr=0.03;

  case 2:
    sf=0.89; corr=0.03;

  case 3:
    sf=0.89; corr=0.03;

  case 4:
    sf=0.89; corr=0.03;

  case 5:
    sf=0.86; corr=0.03;

  case 6:
    sf=0.84; corr=0.03;

  return sf*(1+corr*unc);
  }
}

float getTauSF_v5_2018(int wp, int unc){
  //From here https://twiki.cern.ch/twiki/bin/view/CMS/TauIDRecommendation13TeV#Performance_in_data_and_recommen
  float sf; float corr;
  switch (wp){
  case 0:
    sf=0.86; corr=0.04;

  case 1:
    sf=0.90; corr=0.03;

  case 2:
    sf=0.90; corr=0.03;

  case 3:
    sf=0.90; corr=0.02;

  case 4:
    sf=0.90; corr=0.02;

  case 5:
    sf=0.89; corr=0.02;

  case 6:
    sf=0.89; corr=0.02;

  return sf*(1+corr*unc);
  }
}

float getTauSF_v5(int wp, int unc, int year){
  //Tau SF are flat in p_T
  if (year==2016) return getTauSF_v5_2016(4, unc);
  if (year==2017) return getTauSF_v5_2017(4, unc);
  if (year==2018) return getTauSF_v5_2018(4, unc);
  else std::cout << "Wrong year for tau SF!!" << std::endl;
  return -1.;
}

float getLeptonSF_v5(int wp, int unc, int year, float pt, float eta, int pdgId){
    if (pdgId == 0) pdgId =15; 
    if (abs(pdgId) == 15) return getTauSF_v5(4, unc, year); //We use tight
    if (abs(pdgId) == 13) return getMuSF_v5(wp, unc, year, pt, eta);
    if (abs(pdgId) == 11) return getElSF_v5(wp, unc, year, pt, eta);
    else if(abs(pdgId) != 0) std::cout << "Wrong pdg Id for lepton SF!!" << std::endl;
    return -1.;
}

float getLeptonSF_v5_var(int wp, int unc, int year, float pt, float eta, int pdgId, int target){
    float trueVar = 1;
    if (abs(pdgId) == target) trueVar = 1 + unc*0.008;
    if (abs(pdgId) == 15) return trueVar*getTauSF_v5(4, 0, year); //We use tight
    if (abs(pdgId) == 13) return trueVar*getMuSF_v5(wp, 0, year, pt, eta);
    if (abs(pdgId) == 11) return trueVar*getElSF_v5(wp, 0, year, pt, eta);
    else if(abs(pdgId) != 0) std::cout << "Wrong pdg Id for lepton SF!!" << std::endl;
    return -1.;
}


float extraTauSFs_2016(float eta, int mcMatch, int var){
    float sf = 1.; float unc= 0.;
    if (mcMatch == 1 || mcMatch == 3){ //Matched to electron
        if      (abs(eta) < 1.460){ sf = 1.32; unc = 0.03;}
        else if (abs(eta) > 1.558){ sf = 1.38; unc = 0.04;}
        else                      { sf = 1   ; unc = 0.00;}
    }
    if (mcMatch == 2 || mcMatch == 4){ //Matched to electron
        if      (abs(eta) < 0.400) { sf = 1.22; unc = 0.04;}
        else if (abs(eta) < 0.800) { sf = 1.12; unc = 0.04;}
        else if (abs(eta) < 1.200) { sf = 1.26; unc = 0.04;}
        else if (abs(eta) < 1.700) { sf = 1.22; unc = 0.15;}
        else if (abs(eta) < 2.300) { sf = 2.39; unc = 0.16;}
        else                       { sf = 1.00; unc = 0.00;}
    }
    return sf + var*unc;
}

float extraTauSFs_2017(float eta, int mcMatch, int var){
    float sf = 1.; float unc= 0.;
    if (mcMatch == 1 || mcMatch == 3){ //Matched to electron
        if      (abs(eta) < 1.460){ sf = 1.17; unc = 0.04;}
        else if (abs(eta) > 1.558){ sf = 1.25; unc = 0.06;}
        else                      { sf = 1   ; unc = 0.00;}
    }
    if (mcMatch == 2 || mcMatch == 4){ //Matched to electron
        if      (abs(eta) < 0.400) { sf = 1.06; unc = 0.05;}
        else if (abs(eta) < 0.800) { sf = 1.02; unc = 0.04;}
        else if (abs(eta) < 1.200) { sf = 1.10; unc = 0.04;}
        else if (abs(eta) < 1.700) { sf = 1.03; unc = 0.18;}
        else if (abs(eta) < 2.300) { sf = 1.94; unc = 0.35;}
        else                       { sf = 1.00; unc = 0.00;}
    }
    return sf + var*unc;
}

float extraTauSFs_2018(float eta, int mcMatch, int var){
    float sf = 1.; float unc= 0.;
    //Warning! Dummy values from 2017!
    if (mcMatch == 1 || mcMatch == 3){ //Matched to electron
        if      (abs(eta) < 1.460){ sf = 1.17; unc = 0.04;}
        else if (abs(eta) > 1.558){ sf = 1.25; unc = 0.06;}
        else                      { sf = 1   ; unc = 0.00;}
    }
    if (mcMatch == 2 || mcMatch == 4){ //Matched to electron
        if      (abs(eta) < 0.400) { sf = 1.06; unc = 0.05;}
        else if (abs(eta) < 0.800) { sf = 1.02; unc = 0.04;}
        else if (abs(eta) < 1.200) { sf = 1.10; unc = 0.04;}
        else if (abs(eta) < 1.700) { sf = 1.03; unc = 0.18;}
        else if (abs(eta) < 2.300) { sf = 1.94; unc = 0.35;}
        else                       { sf = 1.00; unc = 0.00;}
    }
    return sf + var*unc;
}

float extraTauSFs(float eta, int mcMatch, int year, int var){
    if (year==2016) return extraTauSFs_2016(eta, mcMatch, var);
    if (year==2017) return extraTauSFs_2017(eta, mcMatch, var);
    if (year==2018) return extraTauSFs_2018(eta, mcMatch, var);
}

Float_t scaleLepton(Float_t pt, Int_t pdgId, Float_t var, Int_t refId){
  if (not(pdgId == refId)) return pt;
  else{
    return var*pt;
  }
}

void functionsSF() {}
