#Minimodule to get polarization coefficients for W and Z from fTrees
import ROOT
from coeffsHelper import*

#Config options, likely not worth to add a proper parser
fileName = ["/pool/ciencias/HeppyTrees/RA7/nanoAODv5_2017_unSkimmed_estructure/bosonPolarizationGEN/*pow*root"]
varTags   = ["Pol_Z_17", "Pol_W_17" , "Pol_ZP_17", "Pol_ZM_17" , "Pol_WP_17", "Pol_WM_17"]
lumi = "41.3 fb^{-1}"

treeName = "sf/t"
treeVars  = ["genThetaZ_CS","charge*genThetaW_CS", "genThetaZ_CS","genThetaZ_CS","charge*genThetaW_CS", "charge*genThetaW_CS"]#,"charge*cos(genThetaWDn_HE_CM)","cos(genThetaZDn_HE_CM)","cos(genThetaZDn_HE_CM)"]
#treeVars  = ["cos_genThetaWDn_CS", "cos_genThetaZDn_CS","cos_genThetaWDn_CS","cos_genThetaWDn_CS","cos_genThetaZDn_CS","cos_genThetaZDn_CS"]
baseCut   = "status == -1 && mll_3l_gen >= 60 &&  mll_3l_gen <= 120"
fiducialCut = "status == -1 && mll_3l_gen >= 75 &&  mll_3l_gen <= 105 && genLepZ1_eta <= 2.4  && genLepZ2_eta <= 2.4 && genLepW_eta <= 2.4 && genLepZ2_pt >= 10 && genLepZ1_pt >= 25 && genLepW_pt >= 25" 
extracuts = ["", ""," && charge==1", " && charge==-1", " && charge==1", " && charge==-1"]
mode     = "quad"
drawControlPlots = True
doReport = True

#Let's run

theFiles = []
theTrees = []
theTree = ROOT.TChain(treeName)
for f in fileName:
  #theFiles.append(ROOT.TFile(f, "READ"))
  #theTrees.append(theFiles[-1].Get(treeName))
  theTree.Add(f)
#Now create the histograms

theObjs = []
for i in range(len(treeVars)):
    print treeVars[i], varTags[i]
    theTree.Draw("%s >> %s(20,-1.,1.0)"%(treeVars[i],varTags[i]), baseCut + extracuts[i])
    theTree.Draw("%s*%s >> %s_2(20,0,1.0)"%(treeVars[i],treeVars[i],varTags[i]), baseCut + extracuts[i])
    theTree.Draw("%s >> %s_fidu(20,-1.0,1.0)"%(treeVars[i],varTags[i]), fiducialCut + extracuts[i])

    theObjs.append(coeffs(ROOT.gDirectory.Get(varTags[i]), ROOT.gDirectory.Get(varTags[i] + "_2"), ROOT.gDirectory.Get(varTags[i] + "_fidu"), "Z" in varTags[i], varTags[i], lumi))

#Fitting plus rebasing
for o in theObjs:
    o.load()

for o in theObjs:
    if drawControlPlots: o.doControl()
    if doReport: o.doReport()
