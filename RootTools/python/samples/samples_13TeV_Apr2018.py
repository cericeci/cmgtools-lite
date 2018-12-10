import PhysicsTools.HeppyCore.framework.config as cfg
import os

#####COMPONENT CREATOR

from CMGTools.RootTools.samples.ComponentCreator import ComponentCreator
kreator = ComponentCreator()


### DiBosons

# cross section from https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns#Diboson

WZTo3LNu_amcatnlo = kreator.makeMCComponent("WZTo3LNu_amcatnlo", "/WZTo3LNu_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM", "CMS", ".*root", 4.666)
WZTo3LNu_powheg   = kreator.makeMCComponent("WZTo3LNu_powheg"  , "/WZTo3LNu_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM", "CMS", ".*root", 4.459)

TT_94_Dil    = kreator.makeMCComponent("TT_Dil_Powheg"      ,        "/TTTo2L2Nu_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM", "CMS", ".*root", 831.76*(3*0.108)*(3*0.108))
TT_94_Semi   = kreator.makeMCComponent("TT_SingleLep_Powheg", "/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM", "CMS", ".*root", 831.76*(3*0.108)*(1-3*0.108))
TT_94_Had    = kreator.makeMCComponent("TT_Had_Powheg"      ,     "/TTToHadronic_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM", "CMS", ".*root", 831.76*(1-3*0.108)*(1-3*0.108))

TT_94_SemT    = kreator.makeMCComponent("TT_SingleLepFromT_madgraph"      ,        "/TTJets_SingleLeptFromT_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM", "CMS", ".*root", 831.76*(1-3*0.108)*(3*0.108))
TT_94_SemTb    = kreator.makeMCComponent("TT_SingleLepFromTbar_madgraph"      ,        "/TTJets_SingleLeptFromTbar_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM", "CMS", ".*root", 831.76*(1-3*0.108)*(3*0.108))
TT_94_DilM    = kreator.makeMCComponent("TT_Dil_madgraph"      ,     "/TTJets_DiLept_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM", "CMS", ".*root", 831.76*(3*0.108)*(3*0.108))


WJets_MLM     = kreator.makeMCComponent("WJets_MLM"      ,        "/WJetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM", "CMS", ".*root",3* 20508.9)
DYJets_aMC    = kreator.makeMCComponent("DYJets_M-50_aMCatNLO"      ,        "/DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM", "CMS", ".*root", 2008.*3)
DYJets_aMC_ext    = kreator.makeMCComponent("DYJets_M-50_aMCatNLO_ext"      ,        "/DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/MINIAODSIM", "CMS", ".*root", 2008.*3)





TTH_nobb     = kreator.makeMCComponent("TTHnobb_Powheg"      ,        "/ttHToNonbb_M125_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM", "CMS", ".*root", 0.5085*(1-0.577))
TTH_incl     = kreator.makeMCComponent("TTHincl_Powheg"      ,        "/ttH_M125_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM", "CMS", ".*root", 0.5085)
TTZ          = kreator.makeMCComponent("TTZToLLNuNu_amcatnlo",        "/TTZToLLNuNu_M-10_TuneCP5_13TeV-amcatnlo-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM", "CMS", ".*root", 0.2529)





### ----------------------------- summary ----------------------------------------

mcSamples = [WZTo3LNu_amcatnlo, WZTo3LNu_powheg, TT_94_Dil, TT_94_Semi, TT_94_Had, TTH_nobb, TTH_incl, TTZ]

samples = mcSamples

### ---------------------------------------------------------------------

from CMGTools.TTHAnalysis.setup.Efficiencies import *
dataDir = "$CMSSW_BASE/src/CMGTools/TTHAnalysis/data"

#Define splitting
for comp in mcSamples:
    comp.isMC = True
    comp.isData = False
    comp.splitFactor = 500
 #  if comp.name in [ "WJets", "DY3JetsM50", "DY4JetsM50","W1Jets","W2Jets","W3Jets","W4Jets","TTJetsHad" ] else 100
    comp.puFileMC=dataDir+"/puProfile_Summer12_53X.root"
    comp.puFileData=dataDir+"/puProfile_Data12.root"
    comp.efficiency = eff2012

if __name__ == "__main__":
    from CMGTools.RootTools.samples.tools import runMain
    runMain(samples)
