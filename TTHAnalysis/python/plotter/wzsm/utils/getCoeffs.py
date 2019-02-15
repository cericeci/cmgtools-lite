#Minimodule to get polarization coefficients for W and Z from fTrees
import ROOT
from coeffsHelper import*

#Config options, likely not worth to add a proper parser
fileName = "/nfs/fanae/user/carlosec/WZ/CMSSW_8_0_19/src/CMGTools/TTHAnalysis/macros/test/test.root"
treeName = "sf/t"
treeVars = ["cos_genThetaWDn_HE", "cos_genThetaZDn_HE"]
varTags  = ["Pol_W", "Pol_Z"]
mode     = "quad"
drawControlPlots = True
doReport = True

#Let's run
theFile = ROOT.TFile(fileName, "READ") #Powheg is the one that works better
theTree = theFile.Get("sf/t")

#Now create the histograms

theObjs = []
for i in range(len(treeVars)):
    print treeVars[i], varTags[i]
    theTree.Draw("%s >> %s(20,-0.999,0.999)"%(treeVars[i],varTags[i]), "")
    theTree.Draw("%s*%s >> %s_2(20,0,0.999)"%(treeVars[i],treeVars[i],varTags[i]), "")
    theObjs.append(coeffs(ROOT.gDirectory.Get(varTags[i]), ROOT.gDirectory.Get(varTags[i] + "_2"), "Z" in varTags[i], varTags[i]))

#Fitting plus rebasing
for o in theObjs:
    o.load()

for o in theObjs:
    if drawControlPlots: o.doControl()
    if doReport: o.doReport()
