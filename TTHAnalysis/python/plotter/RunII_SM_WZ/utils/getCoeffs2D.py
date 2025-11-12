#Minimodule to get polarization coefficients for W and Z from fTrees
import ROOT
from coeffsHelper2D import*

#Config options, likely not worth to add a proper parser
fileName = ["/lustrefs/hdd_pool_dir/HeppyTrees/RA7/nanoAODv5_2016_gendressed_estructure/allgen/evVarFriend_WZTo3LNu_powheg_part*root","/lustrefs/hdd_pool_dir/HeppyTrees/RA7/nanoAODv5_2017_gendressed_estructure/allgen/evVarFriend_WZTo3LNu_powheg_part*root","/lustrefs/hdd_pool_dir/HeppyTrees/RA7/nanoAODv5_2018_gendressed_estructure/allgen/evVarFriend_WZTo3LNu_powheg_part*root"]#["/lustrefs/hdd_pool_dir/HeppyTrees/RA7/nanoAODv5_20RunII_nondressed_gendressed_estructure/allgen_notdressed/evVarFriend_WZTo3LNu_powheg_part0.root","/lustrefs/hdd_pool_dir/HeppyTrees/RA7/nanoAODv5_20RunII_nondressed_gendressed_estructure/allgen_notdressed/evVarFriend_WZTo3LNu_powheg_part1.root"]#["/lustrefs/hdd_pool_dir/HeppyTrees/RA7/nanoAODv5_20RunII_nondressed_unSkimmed_estructure/allgen/evVarFriend_WZTo3LNu_pow_part*.root"] #["/lustrefs/hdd_pool_dir/HeppyTrees/RA7/nanoAODv5_20RunII_nondressed_gendressed_estructure/allgen/evVarFriend_WZTo3LNu_powheg_part0.root","/lustrefs/hdd_pool_dir/HeppyTrees/RA7/nanoAODv5_20RunII_nondressed_gendressed_estructure/allgen/evVarFriend_WZTo3LNu_powheg_part1.root"]#["/pool/ciencias/HeppyTrees/RA7/nanoAODv5_20RunII_nondressed_unSkimmed_estructure/bosonPolarizationGEN/*pow*root"]

#fileName = ["/lustrefs/hdd_pool_dir/HeppyTrees/RA7/nanoAODv5_2016_unSkimmed_estructure/bosonPolarizationGEN/evVarFriend_WZTo3LNu_pow_part*root","/lustrefs/hdd_pool_dir/HeppyTrees/RA7/nanoAODv5_2017_unSkimmed_estructure/bosonPolarizationGEN/evVarFriend_WZTo3LNu_pow_*root","/lustrefs/hdd_pool_dir/HeppyTrees/RA7/nanoAODv5_2018_unSkimmed_estructure/bosonPolarizationGEN/evVarFriend_WZTo3LNu_pow_part*root"]

#fileName = ["/lustrefs/hdd_pool_dir/HeppyTrees/RA7/nanoAODv5_2017_unSkimmed_estructure/bosonPolarizationGEN/evVarFriend_WZTo3LNu_pow_*root","/lustrefs/hdd_pool_dir/HeppyTrees/RA7/nanoAODv5_2018_unSkimmed_estructure/bosonPolarizationGEN/evVarFriend_WZTo3LNu_pow_part*root"]

varTags   = ["Pol_W_Pol_Z_RunII_nondressed", "Pol_WP_Pol_Z_RunII_nondressed", "Pol_Z_Pol_Z_RunII_nondressed"]#, "Pol_Z_RunII_nondressed" , "Pol_WP_RunII_nondressed", "Pol_WM_RunII_nondressed" , "Pol_ZP_RunII_nondressed", "Pol_ZM_RunII_nondressed"]
lumi = "137.2 fb^{-1}"

treeName = "sf/t"
treeVars  = ["cos_genThetaZDn_HE:cos_genThetaWDn_HE", "cos_genThetaZDn_HE:cos_genThetaWDn_HE", "cos_genThetaZDn_HE:cos_genThetaWDn_HE"]#,"cos_genThetaZDn_HE","cos_genThetaWDn_HE","cos_genThetaWDn_HE","cos_genThetaZDn_HE","cos_genThetaZDn_HE"] #["genThetaZ_CS","charge*genThetaW_CS", "genThetaZ_CS","genThetaZ_CS","charge*genThetaW_CS", "charge*genThetaW_CS"]#,"charge*cos(genThetaWDn_HE_CM)","cos(genThetaZDn_HE_CM)","cos(genThetaZDn_HE_CM)"]
#treeVars  = ["cos_genThetaWDn_CS", "cos_genThetaZDn_CS","cos_genThetaWDn_CS","cos_genThetaWDn_CS","cos_genThetaZDn_CS","cos_genThetaZDn_CS"]
baseCut   = "status == -1 && mll_3l_gen >= 60 &&  mll_3l_gen <= 120"
fiducialCut = "status == -1 && mll_3l_gen >= 75 &&  mll_3l_gen <= 105 && genLepZ1_eta <= 2.4  && genLepZ2_eta <= 2.4 && genLepW_eta <= 2.4 && genLepZ2_pt >= 10 && genLepZ1_pt >= 25 && genLepW_pt >= 25" 
extracuts = [""," && charge==1", " && charge==-1"]#, ""," && charge==1", " && charge==-1", " && charge==1", " && charge==-1"]
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
    theTree.Draw("%s >> %s(20,-1.,1.,20,-1.,1.)"%(treeVars[i],varTags[i]), baseCut + extracuts[i])
    theTree.Draw("%s*%s >> %s_2(20,0.,1.,20,-1.,1.)"%(treeVars[i],treeVars[i],varTags[i]), baseCut + extracuts[i])
    theTree.Draw("%s >> %s_fidu(20,-1.,1.,20,-1.,1.)"%(treeVars[i],varTags[i]), fiducialCut + extracuts[i])

    theObjs.append(coeffs(ROOT.gDirectory.Get(varTags[i]), ROOT.gDirectory.Get(varTags[i] + "_2"), ROOT.gDirectory.Get(varTags[i] + "_fidu"), False, varTags[i], lumi))

#Fitting plus rebasing
for o in theObjs:
    o.load()

for o in theObjs:
    if drawControlPlots: 
        o.doControl("W")
        o.doControl("Z")
    #if doReport: o.doReport()
