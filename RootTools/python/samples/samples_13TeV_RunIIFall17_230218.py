import PhysicsTools.HeppyCore.framework.config as cfg
import os

#####COMPONENT CREATOR

from CMGTools.RootTools.samples.ComponentCreator import ComponentCreator
kreator = ComponentCreator()

### NB: Commented lines refer to samples available in RunIIFall15MiniAODv2 but not yet in RunIISpring16MiniAODv1

### ----------------------------- 25 ns ----------------------------------------

# TTbar cross section: NNLO, https://twiki.cern.ch/twiki/bin/view/LHCPhysics/TtbarNNLO (172.5)
TTJets = kreator.makeMCComponent("TTJets", "/TTJets_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIFall17MiniAOD-94X_mc2017_realistic_v10-v1/MINIAODSIM", "CMS", ".*root", 831.76)
#TTJets_ext = kreator.makeMCComponent("TTJets_ext", "/TTJets_13TeV-amcatnloFXFX-pythia8/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12_ext1-v1/MINIAODSIM", "CMS", ".*root", 831.76)
#TT_pow = kreator.makeMCComponent("TTbar", "/TT_TuneCUETP8M1_13TeV-powheg-pythia8/RunIISpring16MiniAODv2-PUSpring16_RECODEBUG_80X_mcRun2_asymptotic_2016_miniAODv2_v0_ext3-v1/MINIAODSIM", "CMS", ".*root", 831.762)
#TT_pow_ext3 = kreator.makeMCComponent("TT_pow_ext3", "/TT_TuneCUETP8M1_13TeV-powheg-pythia8/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_80X_mcRun2_asymptotic_2016_miniAODv2_v0_ext3-v1/MINIAODSIM", "CMS", ".*root", 831.76)
#TT_pow_ext4 = kreator.makeMCComponent("TT_pow_ext4", "/TT_TuneCUETP8M1_13TeV-powheg-pythia8/RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0_ext4-v1/MINIAODSIM", "CMS", ".*root", 831.76)

#TTJets_SingleLeptonFromTbar = kreator.makeMCComponent("TTJets_SingleLeptonFromTbar", "/TTJets_SingleLeptFromTbar_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/MINIAODSIM", "CMS", ".*root", 831.76*(3*0.108)*(1-3*0.108) )
#TTJets_SingleLeptonFromTbar_ext = kreator.makeMCComponent("TTJets_SingleLeptonFromTbar_ext", "/TTJets_SingleLeptFromTbar_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/MINIAODSIM", "CMS", ".*root", 831.76*(3*0.108)*(1-3*0.108) )
TTJets_SingleLeptonFromT = kreator.makeMCComponent("TTJets_SingleLeptonFromT", "/TTJets_SingleLeptFromT_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAOD-94X_mc2017_realistic_v10-v1/MINIAODSIM", "CMS", ".*root", 831.76*(3*0.108)*(1-3*0.108))
#TTJets_SingleLeptonFromT_ext = kreator.makeMCComponent("TTJets_SingleLeptonFromT_ext", "/TTJets_SingleLeptFromT_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAOD-94X_mc2017_realistic_v10-v1/MINIAODSIM", "CMS", ".*root", 831.76*(3*0.108)*(1-3*0.108))
#TTJets_DiLepton = kreator.makeMCComponent("TTJets_DiLepton", "/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM", "CMS", ".*root", 831.76*((3*0.108)**2) )
#TTJets_DiLepton_ext = kreator.makeMCComponent("TTJets_DiLepton_ext", "/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/MINIAODSIM", "CMS", ".*root", 831.76*((3*0.108)**2) )

TTs = [ 
TTJets,
#TTJets_ext, 
#TT_pow,
##TT_pow_ext3,
##TT_pow_ext4,
#TTJets_SingleLeptonFromTbar,
##TTJets_SingleLeptonFromTbar_ext,
TTJets_SingleLeptonFromT,
#TTJets_SingleLeptonFromT_ext,
#TTJets_DiLepton,
##TTJets_DiLepton_ext,
]


# Higgs
# TTH cross section from LHC Higgs XS WG: https://twiki.cern.ch/twiki/bin/view/LHCPhysics/CERNYellowReportPageAt1314TeV?rev=15
TTHnobb_pow = kreator.makeMCComponent("TTHnobb_pow", "/ttHToNonbb_M125_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAOD-94X_mc2017_realistic_v10-v1/MINIAODSIM", "CMS", ".*root",0.5085*(1-0.577))
TTHnobb = kreator.makeMCComponent("TTHnobb", "/ttHJetToNonbb_M125_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/RunIIFall17MiniAOD-94X_mc2017_realistic_v10-v1/MINIAODSIM", "CMS", ".*root", 0.5085*(1-0.577))
#TTHnobb_ext = kreator.makeMCComponent("TTHnobb_ext", "/ttHJetToNonbb_M125_13TeV_amcatnloFXFX_madspin_pythia8_mWCutfix/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_80X_mcRun2_asymptotic_2016_miniAODv2_v0_ext1-v2/MINIAODSIM", "CMS", ".*root",0.5085*(1-0.577))

# GGH cross section from LHC Higgs XS WG: https://twiki.cern.ch/twiki/bin/view/LHCPhysics/CERNYellowReportPageAt1314TeV?rev=15
GGHZZ4L = kreator.makeMCComponent("GGHZZ4L", "/GluGluHToZZTo4L_M125_13TeV_powheg2_JHUGenV7011_pythia8/RunIIFall17MiniAOD-94X_mc2017_realistic_v10-v1/MINIAODSIM", "CMS", ".*root", 0.01212)
GGHZZ4L_ext = kreator.makeMCComponent("GGHZZ4L_ext", "/GluGluHToZZTo4L_M125_13TeV_powheg2_JHUGenV7011_pythia8/RunIIFall17MiniAOD-94X_mc2017_realistic_v11_ext1-v1/MINIAODSIM", "CMS", ".*root", 0.01212)
#VHToNonbb = kreator.makeMCComponent("VHToNonbb", "/VHToNonbb_M125_13TeV_amcatnloFXFX_madspin_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM", "CMS", ".*root", 0.9561)

VBF_HToZZTo4L = kreator.makeMCComponent("VBF_HToZZTo4L","/VBF_HToZZTo4L_M125_13TeV_powheg2_JHUGenV7011_pythia8/RunIIFall17MiniAOD-94X_mc2017_realistic_v11_ext1-v1/MINIAODSIM","CMS",".*root", 0.001034)
GluGluToContinToZZTo2e2mu = kreator.makeMCComponent("GluGluToContinToZZTo2e2mu","/GluGluToContinToZZTo2e2mu_13TeV_MCFM701_pythia8/RunIIFall17MiniAOD-94X_mc2017_realistic_v10-v2/MINIAODSIM","CMS",".*root", 0.00734)
GluGluToContinToZZTo2e2nu = kreator.makeMCComponent("GluGluToContinToZZTo2e2nu","/GluGluToContinToZZTo2e2nu_13TeV_MCFM701_pythia8/RunIIFall17MiniAOD-94X_mc2017_realistic_v10-v1/MINIAODSIM","CMS",".*root", 0.003956)
GluGluToContinToZZTo2mu2nu = kreator.makeMCComponent("GluGluToContinToZZTo2mu2nu","/GluGluToContinToZZTo2mu2nu_13TeV_MCFM701_pythia8/RunIIFall17MiniAOD-94X_mc2017_realistic_v10-v2/MINIAODSIM","CMS",".*root", 0.003956)
GluGluToContinToZZTo2mu2tau = kreator.makeMCComponent("GluGluToContinToZZTo2mu2tau","/GluGluToContinToZZTo2mu2tau_13TeV_MCFM701_pythia8/RunIIFall17MiniAOD-94X_mc2017_realistic_v10-v2/MINIAODSIM","CMS",".*root", 0.00734)
GluGluToContinToZZTo2e2tau = kreator.makeMCComponent("GluGluToContinToZZTo2e2tau","/GluGluToContinToZZTo2e2tau_13TeV_MCFM701_pythia8/RunIIFall17MiniAOD-94X_mc2017_realistic_v10-v2/MINIAODSIM","CMS",".*root", 0.00734)

Higgs = [
TTHnobb,
##TTHnobb_ext,
TTHnobb_pow,
GGHZZ4L,
GGHZZ4L_ext,
#VHToNonbb,
VBF_HToZZTo4L,
#GluGluToContinToZZTo2e2mu,
GluGluToContinToZZTo2e2nu,
GluGluToContinToZZTo2mu2nu,
GluGluToContinToZZTo2mu2tau,
GluGluToContinToZZTo2e2tau
]


# These are the SM cross sections, i.e. cf = cv = 1.0 (see https://twiki.cern.ch/twiki/bin/viewauth/CMS/SingleTopHiggsGeneration13TeV)
#THQ = kreator.makeMCComponent("THQ", "/THQ_Hincl_13TeV-madgraph-pythia8_TuneCUETP8M1/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM", "CMS", ".*root",  0.7927)
#THW = kreator.makeMCComponent("THW", "/THW_Hincl_13TeV-madgraph-pythia8_TuneCUETP8M1/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM", "CMS", ".*root",  0.1472)

Higgs += [
#THQ,
#THW,
]

# Single top cross sections: https://twiki.cern.ch/twiki/bin/viewauth/CMS/SingleTopSigma
#TToLeptons_tch_amcatnlo = kreator.makeMCComponent("TToLeptons_tch_amcatnlo", "/ST_t-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1/RunIISpring16MiniAODv2-premix_withHLT_80X_mcRun2_asymptotic_v14_ext1-v1/MINIAODSIM", "CMS", ".*root", (136.05+80.97)*0.108*3)
#TToLeptons_tch_amcatnlo_ext = kreator.makeMCComponent("TToLeptons_tch_amcatnlo_ext", "/ST_t-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12_ext1-v1/MINIAODSIM", "CMS", ".*root", (136.05+80.97)*0.108*3) 
TToLeptons_sch_amcatnlo = kreator.makeMCComponent("TToLeptons_sch", "/ST_s-channel_4f_leptonDecays_TuneCP5_13TeV-amcatnlo-pythia8/RunIIFall17MiniAOD-94X_mc2017_realistic_v10-v1/MINIAODSIM", "CMS", ".*root", (7.20+4.16)*0.108*3)
T_tch_powheg = kreator.makeMCComponent("T_tch_powheg", "/ST_t-channel_top_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8/RunIIFall17MiniAOD-94X_mc2017_realistic_v10-v1/MINIAODSIM", "CMS", ".*root", 136.02) # inclusive sample
TBar_tch_powheg = kreator.makeMCComponent("TBar_tch_powheg", "/ST_t-channel_antitop_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8/RunIIFall17MiniAOD-94X_mc2017_realistic_v10-v1/MINIAODSIM", "CMS", ".*root", 136.02) # inclusive sample

#TBar_tWch = kreator.makeMCComponent("TBar_tWch", "/ST_tW_antitop_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAOD-94X_mc2017_realistic_v10-v1/MINIAODSIM", "CMS", ".*root",35.6)
#TBar_tWch_ext = kreator.makeMCComponent("TBar_tWch_ext", "/ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/MINIAODSIM", "CMS", ".*root",35.6)
#T_tWch= kreator.makeMCComponent("T_tWch", "/ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAOD-94X_mc2017_realistic_v10-v1/MINIAODSIM", "CMS", ".*root",35.6)
#T_tWch_ext= kreator.makeMCComponent("T_tWch_ext", "/ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/MINIAODSIM", "CMS", ".*root",35.6)
#TBar_tWch_noFullHad = kreator.makeMCComponent("TBar_tWch_noFullHad","/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAOD-94X_mc2017_realistic_v10-v1/MINIAODSIM","CMS",".*root", 34.91*0.53 )
#TBar_tWch_noFullHad_ext = kreator.makeMCComponent("TBar_tWch_noFullHad_ext","/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAOD-94X_mc2017_realistic_v10_ext1-v1/MINIAODSIM","CMS",".*root", 34.91*0.53 )
T_tWch_noFullHad = kreator.makeMCComponent("T_tWch_noFullHad","/ST_tW_top_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAOD-94X_mc2017_realistic_v10-v1/MINIAODSIM","CMS",".*root", 34.91*0.58 ) 
#x-sections*filter from McM

#/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAOD-94X_mc2017_realistic_v10-v1/MINIAODSIM
#/ST_tW_antitop_5f_inclusiveDecays_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAOD-94X_mc2017_realistic_v10-v2/MINIAODSIM
#/ST_tW_top_5f_NoFullyHadronicDecays_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAOD-94X_mc2017_realistic_v10-v1/MINIAODSIM
#/ST_tW_top_5f_inclusiveDecays_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAOD-94X_mc2017_realistic_v10-v1/MINIAODSIM

#TGJets = kreator.makeMCComponent("TGJets", "/TGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/RunIIFall17MiniAOD-94X_mc2017_realistic_v10-v1/MINIAODSIM", "CMS", ".*root", 2.967)

#tZW_ll = kreator.makeMCComponent("tZW_ll",        "/ST_tWll_5f_LO_13TeV-MadGraph-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM", "CMS", ".*root", 0.01123)
#tZW_ll_ext = kreator.makeMCComponent("tZW_ll_ext","/ST_tWll_5f_LO_13TeV_MadGraph_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM", "CMS", ".*root", 0.01123)
tZq_ll = kreator.makeMCComponent("tZq_ll","/tZq_ll_4f_ckm_NLO_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/RunIIFall17MiniAOD-94X_mc2017_realistic_v10-v1/MINIAODSIM", "CMS", ".*root", 0.0758)


#SingleTop = [
#TToLeptons_tch_amcatnlo,
##TToLeptons_tch_amcatnlo_ext,
#TToLeptons_sch_amcatnlo,
#T_tch_powheg,
#TBar_tch_powheg,
#TBar_tWch,
##TBar_tWch_ext,
#T_tWch,
##T_tWch_ext,
#TBar_tWch_noFullHad,
#TBar_tWch_noFullHad_ext,
#T_tWch_noFullHad,
#TGJets,
#tZW_ll,
##tZW_ll_ext,
#tZq_ll
#]

### V+jets inclusive (from https://twiki.cern.ch/twiki/bin/viewauth/CMS/StandardModelCrossSectionsat13TeV)
#WJetsToLNu = kreator.makeMCComponent("WJetsToLNu","/WJetsToLNu_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM", "CMS", ".*root", 3* 20508.9)
WJetsToLNu_LO = kreator.makeMCComponent("WJetsToLNu_LO","/WJetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAOD-94X_mc2017_realistic_v10-v1/MINIAODSIM", "CMS", ".*root", 3* 20508.9)


#DYJetsToLL_M10to50 = kreator.makeMCComponent("DYJetsToLL_M10to50", "/DYJetsToLL_M-10to50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/MINIAODSIM", "CMS", ".*root", 18610)
#DYJetsToLL_M10to50_ext1 = kreator.makeMCComponent("DYJetsToLL_M10to50_ext1", "/DYJetsToLL_M-10to50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/MINIAODSIM", "CMS", ".*root", 18610)
DYJetsToLL_M10to50_LO = kreator.makeMCComponent("DYJetsToLL_M10to50_LO", "/DYJetsToLL_M-10to50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAOD-94X_mc2017_realistic_v10-v2/MINIAODSIM", "CMS", ".*root", 18610)
#DYJetsToLL_M5to50_LO = kreator.makeMCComponent("DYJetsToLL_M5to50_LO", "/DYJetsToLL_M-5to50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM", "CMS", ".*root", 7.1310*10**4)
DYJetsToLL_M50 = kreator.makeMCComponent("DYJetsToLL_M50", "/DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIFall17MiniAOD-94X_mc2017_realistic_v10-v1/MINIAODSIM", "CMS", ".*root", 2008.*3)
DYJetsToLL_M50_ext = kreator.makeMCComponent("DYJetsToLL_M50_ext", "/DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIFall17MiniAOD-94X_mc2017_realistic_v10_ext1-v1/MINIAODSIM", "CMS", ".*root", 2008.*3)
DYJetsToLL_M50_LO =  kreator.makeMCComponent("DYJetsToLL_M50_LO", "/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAOD-RECOSIMstep_94X_mc2017_realistic_v10_ext1-v1/MINIAODSIM", "CMS", ".*root", 2008.*3)
DYJetsToLL_M50_LO_ext =  kreator.makeMCComponent("DYJetsToLL_M50_LO_ext", "/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAOD-RECOSIMstep_94X_mc2017_realistic_v10_ext1-v1/MINIAODSIM", "CMS", ".*root", 2008.*3)

VJets = [
#WJetsToLNu,
WJetsToLNu_LO,
#DYJetsToLL_M10to50,
DYJetsToLL_M10to50_LO,
#DYJetsToLL_M5to50_LO,
DYJetsToLL_M50,
DYJetsToLL_M50_ext,
DYJetsToLL_M50_LO,
DYJetsToLL_M50_LO_ext,
]




### QCD

# qcd muenr
QCD_Mu15 = kreator.makeMCComponent("QCD_Mu15", "/QCD_Pt-20toInf_MuEnrichedPt15_TuneCP5_13TeV_pythia8/RunIIFall17MiniAOD-RECOSIMstep_94X_mc2017_realistic_v10-v1/MINIAODSIM", "CMS", ".*root", 720.65e6*0.00042)
QCD_Pt15to20_Mu5    = kreator.makeMCComponent("QCD_Pt15to20_Mu5"    , "/QCD_Pt-15to20_MuEnrichedPt5_TuneCP5_13TeV_pythia8/RunIIFall17MiniAOD-94X_mc2017_realistic_v10-v1/MINIAODSIM"       , "CMS" , ".*root" , 1273190000*0.003)
QCD_Pt20to30_Mu5    = kreator.makeMCComponent("QCD_Pt20to30_Mu5"    , "/QCD_Pt-20to30_MuEnrichedPt5_TuneCP5_13TeV_pythia8/RunIIFall17MiniAOD-94X_mc2017_realistic_v10-v1/MINIAODSIM"      , "CMS" , ".*root" , 558528000*0.0053)
QCD_Pt30to50_Mu5    = kreator.makeMCComponent("QCD_Pt30to50_Mu5", "/QCD_Pt-30to50_MuEnrichedPt5_TuneCP5_13TeV_pythia8/RunIIFall17MiniAOD-94X_mc2017_realistic_v10-v1/MINIAODSIM", "CMS", ".*root", 139803000*0.01182)
QCD_Pt50to80_Mu5    = kreator.makeMCComponent("QCD_Pt50to80_Mu5"    , "/QCD_Pt-50to80_MuEnrichedPt5_TuneCP5_13TeV_pythia8/RunIIFall17MiniAOD-94X_mc2017_realistic_v10-v1/MINIAODSIM" , "CMS" , ".*root" , 19222500*0.02276)
QCD_Pt80to120_Mu5   = kreator.makeMCComponent("QCD_Pt80to120_Mu5"   , "/QCD_Pt-80to120_MuEnrichedPt5_TuneCP5_13TeV_pythia8/RunIIFall17MiniAOD-94X_mc2017_realistic_v10-v1/MINIAODSIM"     , "CMS" , ".*root" , 2758420*0.03844)
QCD_Pt120to170_Mu5  = kreator.makeMCComponent("QCD_Pt120to170_Mu5"  , "/QCD_Pt-120to170_MuEnrichedPt5_TuneCP5_13TeV_pythia8/RunIIFall17MiniAOD-94X_mc2017_realistic_v10-v1/MINIAODSIM", "CMS" , ".*root" , 469797*0.05362)
QCD_Pt170to300_Mu5  = kreator.makeMCComponent("QCD_Pt170to300_Mu5", "/QCD_Pt-170to300_MuEnrichedPt5_TuneCP5_13TeV_pythia8/RunIIFall17MiniAOD-94X_mc2017_realistic_v10-v1/MINIAODSIM", "CMS", ".*root", 117989*0.07335)
QCD_Pt300to470_Mu5  = kreator.makeMCComponent("QCD_Pt300to470_Mu5"  , "/QCD_Pt-300to470_MuEnrichedPt5_TuneCP5_13TeV_pythia8/RunIIFall17MiniAOD-94X_mc2017_realistic_v10-v1/MINIAODSIM"    , "CMS" , ".*root" , 7820.25*0.10196)
QCD_Pt300to470_Mu5_ext  = kreator.makeMCComponent("QCD_Pt300to470_Mu5_ext"  , "/QCD_Pt-300to470_MuEnrichedPt5_TuneCP5_13TeV_pythia8/RunIIFall17MiniAOD-94X_mc2017_realistic_v10-v1/MINIAODSIM"    , "CMS" , ".*root" , 7820.25*0.10196)
QCD_Pt470to600_Mu5  = kreator.makeMCComponent("QCD_Pt470to600_Mu5"  , "/QCD_Pt-470to600_MuEnrichedPt5_TuneCP5_13TeV_pythia8/RunIIFall17MiniAOD-94X_mc2017_realistic_v10-v1/MINIAODSIM"    , "CMS" , ".*root" , 645.528*0.12242)
QCD_Pt470to600_Mu5_ext  = kreator.makeMCComponent("QCD_Pt470to600_Mu5_ext"  , "/QCD_Pt-470to600_MuEnrichedPt5_TuneCP5_13TeV_pythia8/RunIIFall17MiniAOD-94X_mc2017_realistic_v10-v1/MINIAODSIM"    , "CMS" , ".*root" , 645.528*0.12242)
QCD_Pt600to800_Mu5  = kreator.makeMCComponent("QCD_Pt600to800_Mu5", "/QCD_Pt-600to800_MuEnrichedPt5_TuneCP5_13TeV_pythia8/RunIIFall17MiniAOD-94X_mc2017_realistic_v10-v1/MINIAODSIM", "CMS", ".*root", 187.109*0.13412)
QCD_Pt600to800_Mu5_ext  = kreator.makeMCComponent("QCD_Pt600to800_Mu5_ext", "/QCD_Pt-600to800_MuEnrichedPt5_TuneCP5_13TeV_pythia8/RunIIFall17MiniAOD-94X_mc2017_realistic_v10-v1/MINIAODSIM", "CMS", ".*root", 187.109*0.13412)
QCD_Pt800to1000_Mu5 = kreator.makeMCComponent("QCD_Pt800to1000_Mu5" , "/QCD_Pt-800to1000_MuEnrichedPt5_TuneCP5_13TeV_pythia8/RunIIFall17MiniAOD-94X_mc2017_realistic_v10-v1/MINIAODSIM"   , "CMS" , ".*root" , 32.3486*0.14552)
QCD_Pt800to1000_Mu5_ext = kreator.makeMCComponent("QCD_Pt800to1000_Mu5_ext" , "/QCD_Pt-800to1000_MuEnrichedPt5_TuneCP5_13TeV_pythia8/RunIIFall17MiniAOD-94X_mc2017_realistic_v10-v1/MINIAODSIM"   , "CMS" , ".*root" , 32.3486*0.14552)
QCD_Pt1000toInf_Mu5 = kreator.makeMCComponent("QCD_Pt1000toInf_Mu5" , "/QCD_Pt-1000toInf_MuEnrichedPt5_TuneCP5_13TeV_pythia8/RunIIFall17MiniAOD-94X_mc2017_realistic_v10-v1/MINIAODSIM"   , "CMS" , ".*root" , 10.4305*0.15544)

QCD_Mu5 = [
QCD_Pt15to20_Mu5,
QCD_Pt20to30_Mu5,
QCD_Pt30to50_Mu5,
QCD_Pt50to80_Mu5,
QCD_Pt80to120_Mu5,
QCD_Pt120to170_Mu5,
QCD_Pt170to300_Mu5,
QCD_Pt300to470_Mu5,
QCD_Pt300to470_Mu5_ext,
QCD_Pt470to600_Mu5,
QCD_Pt470to600_Mu5_ext,
QCD_Pt600to800_Mu5,
QCD_Pt600to800_Mu5_ext,
QCD_Pt800to1000_Mu5,
QCD_Pt800to1000_Mu5_ext,
QCD_Pt1000toInf_Mu5
]



# qcd emenr
QCD_Pt15to20_EMEnriched   = kreator.makeMCComponent("QCD_Pt15to20_EMEnriched"  ,"/QCD_Pt-15to20_EMEnriched_TuneCP5_13TeV_pythia8/RunIIFall17MiniAOD-94X_mc2017_realistic_v10-v1/MINIAODSIM"  , "CMS", ".*root", 1273000000*0.0002)
QCD_Pt20to30_EMEnriched   = kreator.makeMCComponent("QCD_Pt20to30_EMEnriched"  ,"/QCD_Pt-20to30_EMEnriched_TuneCP5_13TeV_pythia8/RunIIFall17MiniAOD-94X_mc2017_realistic_v10-v1/MINIAODSIM"  , "CMS", ".*root", 557600000*0.0096)
QCD_Pt30to50_EMEnriched   = kreator.makeMCComponent("QCD_Pt30to50_EMEnriched"  ,"/QCD_Pt-30to50_EMEnriched_TuneCP5_13TeV_pythia8/RunIIFall17MiniAOD-94X_mc2017_realistic_v10-v1/MINIAODSIM"  , "CMS", ".*root", 136000000*0.073)
QCD_Pt50to80_EMEnriched   = kreator.makeMCComponent("QCD_Pt50to80_EMEnriched", "/QCD_Pt-50to80_EMEnriched_TuneCP5_13TeV_pythia8/RunIIFall17MiniAOD-94X_mc2017_realistic_v10-v1/MINIAODSIM", "CMS", ".*root", 19800000*0.146)
QCD_Pt80to120_EMEnriched  = kreator.makeMCComponent("QCD_Pt80to120_EMEnriched" ,"/QCD_Pt-80to120_EMEnriched_TuneCP5_13TeV_pythia8/RunIIFall17MiniAOD-94X_mc2017_realistic_v10-v1/MINIAODSIM" , "CMS", ".*root", 2800000*0.125)
QCD_Pt120to170_EMEnriched = kreator.makeMCComponent("QCD_Pt120to170_EMEnriched","/QCD_Pt-120to170_EMEnriched_TuneCP5_13TeV_pythia8/RunIIFall17MiniAOD-94X_mc2017_realistic_v10-v1/MINIAODSIM", "CMS", ".*root", 477000*0.132)
QCD_Pt170to300_EMEnriched = kreator.makeMCComponent("QCD_Pt170to300_EMEnriched","/QCD_Pt-170to300_EMEnriched_TuneCP5_13TeV_pythia8/RunIIFall17MiniAOD-94X_mc2017_realistic_v10-v1/MINIAODSIM", "CMS", ".*root", 114000*0.165)
QCD_Pt300toInf_EMEnriched = kreator.makeMCComponent("QCD_Pt300toInf_EMEnriched","/QCD_Pt-300toInf_EMEnriched_TuneCP5_13TeV_pythia8/RunIIFall17MiniAOD-94X_mc2017_realistic_v10-v1/MINIAODSIM", "CMS", ".*root", 9000*0.15)

QCDPtEMEnriched = [
QCD_Pt15to20_EMEnriched,
QCD_Pt20to30_EMEnriched,
QCD_Pt30to50_EMEnriched,
QCD_Pt50to80_EMEnriched,
QCD_Pt80to120_EMEnriched,
QCD_Pt120to170_EMEnriched,
QCD_Pt170to300_EMEnriched,
QCD_Pt300toInf_EMEnriched
]

# qcd bctoe

QCD_Pt_15to20_bcToE   = kreator.makeMCComponent("QCD_Pt_15to20_bcToE"   , "/QCD_Pt_15to20_bcToE_TuneCP5_13TeV_pythia8/RunIIFall17MiniAOD-94X_mc2017_realistic_v11-v1/MINIAODSIM"  , "CMS" , ".*root" , 1272980000*0.0002)
QCD_Pt_20to30_bcToE   = kreator.makeMCComponent("QCD_Pt_20to30_bcToE"   , "/QCD_Pt_20to30_bcToE_TuneCP5_13TeV_pythia8/RunIIFall17MiniAOD-94X_mc2017_realistic_v11-v1/MINIAODSIM"  , "CMS" , ".*root" , 557627000*0.00059)
QCD_Pt_30to80_bcToE   = kreator.makeMCComponent("QCD_Pt_30to80_bcToE"   , "/QCD_Pt_30to80_bcToE_TuneCP5_13TeV_pythia8/RunIIFall17MiniAOD-94X_mc2017_realistic_v11-v1/MINIAODSIM"  , "CMS" , ".*root" , 159068000*0.00255)
QCD_Pt_80to170_bcToE  = kreator.makeMCComponent("QCD_Pt_80to170_bcToE"  , "/QCD_Pt_80to170_bcToE_TuneCP5_13TeV_pythia8/RunIIFall17MiniAOD-94X_mc2017_realistic_v11-v1/MINIAODSIM" , "CMS" , ".*root" , 3221000*0.01183)
QCD_Pt_170to250_bcToE = kreator.makeMCComponent("QCD_Pt_170to250_bcToE","/QCD_Pt_170to250_bcToE_TuneCP5_13TeV_pythia8/RunIIFall17MiniAOD-94X_mc2017_realistic_v11-v1/MINIAODSIM", "CMS", ".*root", 105771*0.02492)
QCD_Pt_250toInf_bcToE = kreator.makeMCComponent("QCD_Pt_250toInf_bcToE" , "/QCD_Pt_250toInf_bcToE_TuneCP5_13TeV_pythia8/RunIIFall17MiniAOD-94X_mc2017_realistic_v11-v1/MINIAODSIM", "CMS" , ".*root" , 21094.1*0.03375)

QCDPtbcToE = [
QCD_Pt_15to20_bcToE,
QCD_Pt_20to30_bcToE,
QCD_Pt_30to80_bcToE,
QCD_Pt_80to170_bcToE,
QCD_Pt_170to250_bcToE,
QCD_Pt_250toInf_bcToE
]


### DiBosons

# cross section from https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns#Diboson

WWTo2L2Nu = kreator.makeMCComponent("WWTo2L2Nu", "/WWTo2L2Nu_NNPDF31_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAOD-94X_mc2017_realistic_v10-v1/MINIAODSIM", "CMS", ".*root", 10.481 )
WWTo1L1Nu2Q = kreator.makeMCComponent("WWTo1L1Nu2Q", "/WWTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8/RunIIFall17MiniAOD-94X_mc2017_realistic_v10-v1/MINIAODSIM", "CMS", ".*root", 49.997 )
ZZTo2L2Nu = kreator.makeMCComponent("ZZTo2L2Nu", "/ZZTo2L2Nu_13TeV_powheg_pythia8/RunIIFall17MiniAOD-94X_mc2017_realistic_v10-v1/MINIAODSIM", "CMS", ".*root", 0.564)
ZZTo4L = kreator.makeMCComponent("ZZTo4L", "/ZZTo4L_13TeV_powheg_pythia8/RunIIFall17MiniAOD-94X_mc2017_realistic_v10-v2/MINIAODSIM", "CMS", ".*root", 1.256)
#WZTo3LNu = kreator.makeMCComponent("WZTo3LNu", "/WZTo3LNu_TuneCUETP8M1_13TeV-powheg-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM", "CMS", ".*root", 4.42965)
WZTo3LNu_amcatnlo = kreator.makeMCComponent("WZTo3LNu_amcatnlo", "/WZTo3LNu_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIFall17MiniAOD-94X_mc2017_realistic_v10-v2/MINIAODSIM", "CMS", ".*root", 4.666)
WZTo3LNu_powheg = kreator.makeMCComponent("WZTo3LNu_powheg", "/WZTo3LNu_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM", "CMS", ".*root", 4.666)

#WZTo3LNu_ext = kreator.makeMCComponent("WZTo3LNu_ext", "/WZTo3LNu_mllmin01_13TeV-powheg-pythia8_ext1/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/MINIAODSIM", "CMS", ".*root", 4.42965)
#WGToLNuG = kreator.makeMCComponent("WGToLNuG", "/WGToLNuG_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM", "CMS", ".*root", 585.8)
#WGToLNuG_amcatnlo_ext = kreator.makeMCComponent("WGToLNuG_amcatnlo_ext", "/WGToLNuG_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/MINIAODSIM", "CMS", ".*root", 585.8) # cross section copied from MLM sample above, to be checked
#WGToLNuG_amcatnlo_ext2 = kreator.makeMCComponent("WGToLNuG_amcatnlo_ext2", "/WGToLNuG_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1/MINIAODSIM", "CMS", ".*root", 585.8) # cross section copied from MLM sample above, to be checked
#ZGTo2LG = kreator.makeMCComponent("ZGTo2LG", "/ZGTo2LG_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/MINIAODSIM", "CMS", ".*root", 131.3)
#WW2L2NuDouble = kreator.makeMCComponent("WW2L2NuDouble", "/WWTo2L2Nu_DoubleScattering_13TeV-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM", "CMS", ".*root", 1.64*(3*0.108)*(3*.108))
#WpWpJJ = kreator.makeMCComponent("WpWpJJ", "/WpWpJJ_EWK-QCD_TuneCUETP8M1_13TeV-madgraph-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM", "CMS", ".*root", 0.03711)


TT_94_Dil    = kreator.makeMCComponent("TT_Dil"   ,        "/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM", "CMS", ".*root", 1)
TT_94_Sin    = kreator.makeMCComponent("TT_Single", "/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM", "CMS", ".*root", 1)
TT_94_Had    = kreator.makeMCComponent("TT_Had"   ,     "/TTToHadronic_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM", "CMS", ".*root", 1)



DiBosons = [
WWTo2L2Nu,
WWTo1L1Nu2Q,
ZZTo2L2Nu,
ZZTo4L,
#WZTo3LNu,
WZTo3LNu_amcatnlo,
##WZTo3LNu_ext,
#WGToLNuG,
##WGToLNuG_amcatnlo_ext,
###WGToLNuG_amcatnlo_ext2,
#ZGTo2LG,
#WW2L2NuDouble,
#WpWpJJ,
]

### TriBosons
# cross section from https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns#Triboson

WWW_4F = kreator.makeMCComponent("WWW_4F", "/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/RunIIFall17MiniAOD-94X_mc2017_realistic_v11-v1/MINIAODSIM", "CMS", ".*root", 0.2086, fracNegWeights=0.053)        
WZG    = kreator.makeMCComponent("WZG",    "/WZG_TuneCP5_13TeV-amcatnlo-pythia8/RunIIFall17MiniAOD-94X_mc2017_realistic_v10-v1/MINIAODSIM", "CMS", ".*root", 0.04345, fracNegWeights=0.078)          
WZZ    = kreator.makeMCComponent("WZZ",    "/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/RunIIFall17MiniAOD-94X_mc2017_realistic_v11-v1/MINIAODSIM", "CMS", ".*root", 0.05565, fracNegWeights=0.060)          
ZZZ    = kreator.makeMCComponent("ZZZ",    "/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/RunIIFall17MiniAOD-94X_mc2017_realistic_v11-v1/MINIAODSIM", "CMS", ".*root", 0.01398, fracNegWeights=0.060)  
#tZW    = kreator.makeMCComponent("tZW",    "/ST_tWll_5f_LO_TuneCP5_PSweights_13TeV-madgraph-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM", "CMS", ".*root",  0.01123 )


#WWG = kreator.makeMCComponent("WWG", "/WWG_TuneCUETP8M1_13TeV-amcatnlo-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/MINIAODSIM", "CMS", ".*root", 0.2147 )
#WZG = kreator.makeMCComponent("WZG", "/WZG_TuneCUETP8M1_13TeV-amcatnlo-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM", "CMS", ".*root", 0.04123 )

TriBosons = [
#WWW,
#WZZ,
#WWZ,
#ZZZ,
#WWG,
#WZG,
]

### TTV
TTWToLNu = kreator.makeMCComponent("TTWToLNu", "/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/RunIIFall17MiniAOD-94X_mc2017_realistic_v10-v2/MINIAODSIM", "CMS", ".*root", 0.2043)
#TTWToLNu_ext1 = kreator.makeMCComponent("TTWToLNu_ext1", "/TTWJetsToLNu_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v3/MINIAODSIM", "CMS", ".*root", 0.2043)
#TTWToLNu_ext2 = kreator.makeMCComponent("TTWToLNu_ext2", "/TTWJetsToLNu_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1/MINIAODSIM", "CMS", ".*root", 0.2043)
TTW_LO = kreator.makeMCComponent("TTW_LO", "/ttWJets_TuneCP5_13TeV_madgraphMLM_pythia8/RunIIFall17MiniAOD-94X_mc2017_realistic_v10-v1/MINIAODSIM", "CMS", ".*root",  0.6105 )
TTZToLLNuNu = kreator.makeMCComponent("TTZToLLNuNu","/TTZToLLNuNu_M-10_TuneCP5_13TeV-amcatnlo-pythia8/RunIIFall17MiniAOD-94X_mc2017_realistic_v10-v1/MINIAODSIM", "CMS", ".*root", 0.2529)
#TTZToLLNuNu_ext2 = kreator.makeMCComponent("TTZToLLNuNu_ext2","/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1/MINIAODSIM", "CMS", ".*root", 0.2529)
# https://twiki.cern.ch/twiki/bin/view/CMS/SameSignDilepton2016
#TTZ_LO = kreator.makeMCComponent("TTZ_LO", "/ttZJets_TuneCP5_13TeV_madgraphMLM_pythia8/RunIIFall17MiniAOD-94X_mc2017_realistic_v10-v2/MINIAODSIM", "CMS", ".*root",  0.5297/0.692)
TTLLJets_m1to10 = kreator.makeMCComponent("TTLLJets_m1to10", "/TTZToLL_M-1to10_TuneCP5_13TeV-amcatnlo-pythia8/RunIIFall17MiniAOD-94X_mc2017_realistic_v10-v1/MINIAODSIM", "CMS", ".*root",  0.0283)
TTGJets = kreator.makeMCComponent("TTGJets","/TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/RunIIFall17MiniAOD-94X_mc2017_realistic_v10-v1/MINIAODSIM", "CMS", ".*root", 3.697)

TTWW = kreator.makeMCComponent("TTWW","/TTWW_TuneCP5_13TeV-madgraph-pythia8/RunIIFall17MiniAOD-94X_mc2017_realistic_v10_ext1-v1/MINIAODSIM", "CMS", ".*root", 0.007883)
TTWZ = kreator.makeMCComponent("TTWZ","/TTWZ_TuneCP5_13TeV-madgraph-pythia8/RunIIFall17MiniAOD-94X_mc2017_realistic_v10-v2/MINIAODSIM", "CMS", ".*root", 0.002974)
TTZH = kreator.makeMCComponent("TTZH","/TTZH_TuneCP5_13TeV-madgraph-pythia8/RunIIFall17MiniAOD-94X_mc2017_realistic_v10-v2/MINIAODSIM", "CMS", ".*root", 0.001253)
TTZZ = kreator.makeMCComponent("TTZZ","/TTZZ_TuneCP5_13TeV-madgraph-pythia8/RunIIFall17MiniAOD-94X_mc2017_realistic_v10-v2/MINIAODSIM", "CMS", ".*root", 0.001572)

#/TTWJetsToLNu_TuneCP5_PSweights_13TeV-amcatnloFXFX-madspin-pythia8/RunIIFall17MiniAOD-94X_mc2017_realistic_v10-v1/MINIAODSIM
#/TTZToLLNuNu_M-10_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/RunIIFall17MiniAOD-94X_mc2017_realistic_v10-v1/MINIAODSIM


SingleTop = []

TTV = [
TTWToLNu,
#TTWToLNu_ext1,
#TTWToLNu_ext2,
TTW_LO,
TTZToLLNuNu,
##TTZToLLNuNu_ext2,
TTLLJets_m1to10,
TTGJets,
TTWW,
TTWZ,
TTZH,
TTZZ

]

### Rares
TTTT = kreator.makeMCComponent("TTTT", "/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/RunIIFall17MiniAOD-94X_mc2017_realistic_v10-v2/MINIAODSIM", "CMS", ".*root", 0.009103)
TTTT_ext = kreator.makeMCComponent("TTTT_ext", "/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/RunIIFall17MiniAOD-94X_mc2017_realistic_v10-v2/MINIAODSIM", "CMS", ".*root", 0.009103)

Rares = [
TTTT,
TTTT_ext,
]

### ----------------------------- summary ----------------------------------------

mcSamples = TTs + SingleTop + VJets + QCDPtbcToE + QCDPtEMEnriched + [QCD_Mu15] + QCD_Mu5 +  DiBosons + TriBosons + TTV + Higgs + Rares

samples = mcSamples

### ---------------------------------------------------------------------

from CMGTools.TTHAnalysis.setup.Efficiencies import *
dataDir = "$CMSSW_BASE/src/CMGTools/TTHAnalysis/data"

#Define splitting
for comp in mcSamples:
    comp.isMC = True
    comp.isData = False
    comp.splitFactor = 200
 #  if comp.name in [ "WJets", "DY3JetsM50", "DY4JetsM50","W1Jets","W2Jets","W3Jets","W4Jets","TTJetsHad" ] else 100
    comp.puFileMC=dataDir+"/puProfile_Summer12_53X.root"
    comp.puFileData=dataDir+"/puProfile_Data12.root"
    comp.efficiency = eff2012

if __name__ == "__main__":
    from CMGTools.RootTools.samples.tools import runMain
    runMain(samples)
