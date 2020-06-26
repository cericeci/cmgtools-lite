import os
from optparse import OptionParser

pr = OptionParser(usage="%prog doWhat [options]")


"""python doAnal.py friend_all --year 2018 --datatype nano --pdir ~/www/wz/ --extra '-N 50000 --onlyMC -n -q all.q --env oviedo'"""

#Model options
pr.add_option("--year", dest = "year", type=int, default = 2018, help = "What year to use")
pr.add_option("--datatype", dest = "datatype", type="string", default = "nano", help = "What kind of data format: nanoAOD, heppyTree, etc.")
pr.add_option("--extra", dest = "extra", type="string", default = "", help = "Whatever fancy things you want to add to the command")
pr.add_option("--pdir", dest = "outname", type="string", default = "~/www/wzsm/", help = "Output (folder) name")
pr.add_option("--idir", dest = "inname", type="string", default = "NONE", help = "Input (folder) name")
pr.add_option("--skim", dest = "skim", action="store_true", default = False, help = "Input (folder) name")
pr.add_option("--cut", dest = "cut", type="string", default = "RunII_SM_WZ/2018/cuts_wzsm.txt", help = "Input cutfile")
pr.add_option("--mca", dest = "mca", type="string", default = "RunII_SM_WZ/2018/mca_wz.txt", help = "Input mcafile")
pr.add_option("--plots", dest = "plots", type="string", default = "RunII_SM_WZ/2018/plots_wz.txt", help = "Input plotfile")
pr.add_option("-j", dest = "jobs", type="int", default = None, help = "Number of simultaneous jobs for multithreaded procedures")

#Output formats
(options, args) = pr.parse_args()

doWhat = args[0]

# This is to avoid lots of "if"
from yearlyStuff import *

### Always copy the php script for easiness of work and also create the output dir 
if False: #not(os.path.isdir(options.outname)):
    os.mkdir(options.outname)
    showIt = any([j in doWhat for j in toShow])
    if showIt:
        os.system("cp ~/www/index.php %s"%options.outname)

### This are general use cases
if options.datatype == "nano":
    treeName     = "Events"
    moduleFolder = "multilepWZTreeProducers"
    if options.inname == "NONE":
        options.inname = "/pool/ciencias/HeppyTrees/RA7/nanoAODv5_%s_estructure/"%(str(options.year)) if not(options.skim) else "/pool/ciencias/HeppyTrees/RA7/nanoAODv5_%s_skimWZ/"%(str(options.year))

elif options.datatype == "heppy":
    treeName = "tree"
    moduleFolder = "multilepFriendTreeProducersToCleanup"



###FriendTree producer
if "friend_" in doWhat:
    baseCommand = "python prepareEventVariablesFriendTree.py %s [OUTTREES] --tree treeProducerSusyMultilepton --ttree %s --tra2 -n -I CMGTools.TTHAnalysis.tools.%s [MODULES] [EXTRAARGS]"%(options.inname, treeName, moduleFolder)
    
    if "PU" in doWhat or "PileUp" in doWhat or "all" in doWhat:
        ### Pile-up reweighting. Nominal (62.9) +-5% files already in ../data/pileup/ folder
        print "----------------------------------------------------"
        print "The script runs all trees in %s by default unless a specific dataset is given by -d"%options.inname
        print baseCommand.replace("[INTREES]", options.inname).replace("[OUTTREES]", options.inname + "/pileUpWeight/").replace("[MODULES]", "-m vtxWeight%s -m vtxWeight%sUp -m vtxWeight%sDown"%(str(options.year),str(options.year),str(options.year))).replace("[EXTRAARGS]", options.extra + " --onlyMC ")
        print "----------------------------------------------------"
    if "Corrections" in doWhat or "Co" in doWhat or "all" in doWhat:
        ### Standard 3l recleaner
        print "----------------------------------------------------"
        print "The script runs all trees in %s by default unless a specific dataset is given by -d"%options.inname
        print baseCommand.replace("[INTREES]", options.inname).replace("[OUTTREES]", options.inname + "/leptonPtCorrections/").replace("[MODULES]", " -m leptonEnergyCorrections_%s "%str(options.year)).replace("[EXTRAARGS]", options.extra)
        print "----------------------------------------------------"
    if "ReCleaner" in doWhat or "Cl" in doWhat or "all" in doWhat:
        ### Standard 3l recleaner
        print "----------------------------------------------------"
        print "The script runs all trees in %s by default unless a specific dataset is given by -d"%options.inname
        print baseCommand.replace("[INTREES]", options.inname).replace("[OUTTREES]", options.inname + "/leptonJetReCleanerWZSM/").replace("[MODULES]", " -m leptonJetReCleanerWZSM_%s "%str(options.year)).replace("[EXTRAARGS]", options.extra + "-F sf/t %s/leptonPtCorrections/evVarFriend_{cname}.root"%options.inname )
        print "----------------------------------------------------"    
    if "Builder" in doWhat or "Bu" in doWhat or "all" in doWhat:
        ### Standard 3l builder
        print "----------------------------------------------------"
        print "The script runs all trees in %s by default unless a specific dataset is given by -d"%options.inname
        print baseCommand.replace("[INTREES]", options.inname).replace("[OUTTREES]", options.inname+ "/leptonBuilderWZSM/").replace("[MODULES]", " -m leptonBuilderWZSM_%s "%str(options.year)).replace("[EXTRAARGS]", options.extra+ "-F sf/t %s/leptonPtCorrections/evVarFriend_{cname}.root -F sf/t %s/leptonJetReCleanerWZSM/evVarFriend_{cname}.root"%(options.inname, options.inname))
        print "----------------------------------------------------"

    if "bTag" in doWhat or "Bt" in doWhat or "all" in doWhat:
        ### Standard 3l btag Weights
        print "----------------------------------------------------"
        print "The script runs all trees in %s by default unless a specific dataset is given by -d"%options.inname
        print baseCommand.replace("[INTREES]", options.inname).replace("[OUTTREES]", options.inname+ "/bTagEventWeights/").replace("[MODULES]", " -m eventBTagWeightDeepCSVT_%s"%str(options.year)).replace("[EXTRAARGS]", options.extra + " --onlyMC " + "-F sf/t %s/leptonPtCorrections/evVarFriend_{cname}.root --onlyMC -F sf/t %s/leptonJetReCleanerWZSM/evVarFriend_{cname}.root"%(options.inname, options.inname))
        print "----------------------------------------------------"

    if "Matcher" in doWhat or "Ma" in doWhat or "all" in doWhat:
        ### UCSX matching
        print "----------------------------------------------------"
        print "The script runs all trees in %s by default unless a specific dataset is given by -d"%options.inname
        print baseCommand.replace("[INTREES]", options.inname).replace("[OUTTREES]", options.inname+ "/leptonMatcher/").replace("[MODULES]", " -m leptonMatcher ").replace("[EXTRAARGS]", options.extra + " --onlyMC " + "-F sf/t %s/leptonPtCorrections/evVarFriend_{cname}.root --onlyMC -F sf/t %s/leptonJetReCleanerWZSM/evVarFriend_{cname}.root"%(options.inname, options.inname))
        print "----------------------------------------------------"

    if "Trigger" in doWhat or "Tr" in doWhat or "all" in doWhat:
        ### Trigger Flags
        print "----------------------------------------------------"
        print "The script runs all trees in %s by default unless a specific dataset is given by -d"%options.inname
        print baseCommand.replace("[INTREES]", options.inname).replace("[OUTTREES]", options.inname+ "/trigger_%s/"%str(options.year)).replace("[MODULES]", " -m Trigger_%s "%str(options.year)).replace("[EXTRAARGS]", options.extra + " --onlyMC " + "-F sf/t %s/leptonPtCorrections/evVarFriend_{cname}.root -F sf/t %s/leptonJetReCleanerWZSM/evVarFriend_{cname}.root"%(options.inname, options.inname))
        print "----------------------------------------------------"

    if "Gen" in doWhat or "Ge" in doWhat or "all" in doWhat:
        ### Gen Level variables
        print "----------------------------------------------------"
        print "The script runs all trees in %s by default unless a specific dataset is given by -d"%options.inname
        print baseCommand.replace("[INTREES]", options.inname).replace("[OUTTREES]", options.inname+ "/lepgenVarsWZSM/").replace("[MODULES]", " -m lepgenVarsWZSM_%s "%str(options.year)).replace("[EXTRAARGS]", options.extra + " --onlyMC " + "-F sf/t %s/leptonPtCorrections/evVarFriend_{cname}.root --onlyMC -F sf/t %s/leptonJetReCleanerWZSM/evVarFriend_{cname}.root"%(options.inname, options.inname))
        print "----------------------------------------------------"

    if "Polarization" in doWhat or "Po" in doWhat or "all" in doWhat:
        ### Boson polarization variables
        print "----------------------------------------------------"
        print "The script runs all trees in %s by default unless a specific dataset is given by -d"%options.inname
        print baseCommand.replace("[INTREES]", options.inname).replace("[OUTTREES]", options.inname+ "/bosonPolarizationWZ/").replace("[MODULES]", " -m bosonPolarizationWZ_%s "%str(options.year)).replace("[EXTRAARGS]", options.extra + " --onlyMC " + "-F sf/t %s/leptonPtCorrections/evVarFriend_{cname}.root -F sf/t %s/leptonJetReCleanerWZSM/evVarFriend_{cname}.root"%(options.inname, options.inname))
        print "----------------------------------------------------"

    if "PolarizationGEN" in doWhat or "Pg" in doWhat or "all" in doWhat:
        ### Boson polarization gen level variables
        print "----------------------------------------------------"
        print "The script runs all trees in %s by default unless a specific dataset is given by -d"%options.inname
        print baseCommand.replace("[INTREES]", options.inname).replace("[OUTTREES]", options.inname+ "/bosonPolarizationGEN/").replace("[MODULES]", " -m bosonPolarizationGEN ").replace("[EXTRAARGS]", options.extra + " --onlyMC " + "-F sf/t %s/leptonPtCorrections/evVarFriend_{cname}.root --onlyMC -F sf/t %s/leptonJetReCleanerWZSM/evVarFriend_{cname}.root"%(options.inname, options.inname))
        print "----------------------------------------------------"


if "plot" in doWhat:

    print "python mcPlots.py RunII_SM_WZ/{year}/mca_wz_v5.txt RunII_SM_WZ/{year}/cuts_wzsm.txt RunII_SM_WZ/2016/plots_wz.txt --tree treeProducerSusyMultilepton -P /pool/ciencias/HeppyTrees/RA7/nanoAODv5_{year}_skimWZ/  --Fs {{P}}/leptonPtCorrections/ {prefiringTrees} --Fs {{P}}/leptonJetReCleanerWZSM/ --Fs {{P}}/leptonBuilderWZSM/ {triggerTrees} --FMCs {{P}}/leptonMatcher/ --FMCs {{P}}/bTagEventWeights/ --FMCs {{P}}/bosonPolarization/ --FMCs {{P}}/bosonPolarizationGEN/  -L RunII_SM_WZ/functionsSF.cc -L RunII_SM_WZ/functionsMCMatch.cc  --mcc RunII_SM_WZ/{year}/mcc_triggerdefs.txt --maxRatioRange 0.5 2.0 --fixRatioRange --print C,pdf,png,txt --legendWidth 0.23 --legendFontSize 0.036 --showMCError --showRatio --perBin -W 'getLeptonSF_v4(0,0,{year},LepSel_pt[0],LepSel_eta[0],LepSel_pdgId[0])*getLeptonSF_v4(0,0,{year},LepSel_pt[1],LepSel_eta[1],LepSel_pdgId[1])*getLeptonSF_v4(0,0,{year},LepSel_pt[2],LepSel_eta[2],LepSel_pdgId[2])*puWeight*bTagWeightDeepCSVT_nom{prefiringWeights}' --obj Events -j 32 -l {lumi} -f --pdir ./plots/ --showRatio -E SRWZ ".format(year=options.year,prefiringTrees=prefiringTrees[options.year],prefiringWeights=prefiringWeights[options.year],triggerTrees=triggerTrees[options.year],lumi=lumi[options.year])

if "cards" in doWhat:

    var = "\"4*(LepW_pdgId < 0) + (abs(LepZ1_pdgId)+abs(LepZ2_pdgId)+abs(LepW_pdgId)-33)/2\""
    binning = "\"8,-0.5,7.5\""

    print "python makeShapeCardsSusy.py RunII_SM_WZ/{year}/mca_wz_v5.txt RunII_SM_WZ/{year}/cuts_wzsm.txt {var} {binning} RunII_SM_WZ/{year}/systs_wz.txt  --tree treeProducerSusyMultilepton -P /pool/ciencias/HeppyTrees/RA7/nanoAODv5_{year}_skimWZ/ --Fs {{P}}/leptonPtCorrections/ {prefiringTrees} {pileupTrees} --Fs {{P}}/leptonJetReCleanerWZSM/ --Fs {{P}}/leptonBuilderWZSM/ {triggerTrees} --FMCs {{P}}/leptonMatcher/ --FMCs {{P}}/bTagEventWeights/ --FMCs {{P}}/bosonPolarization/ --FMCs {{P}}/bosonPolarizationGEN/  -L RunII_SM_WZ/functionsSF.cc -L RunII_SM_WZ/functionsMCMatch.cc -L RunII_SM_WZ/functionsWZ.cc -W 'getLeptonSF_v4(0,0,{year},LepSel_pt[0],LepSel_eta[0],LepSel_pdgId[0])*getLeptonSF_v4(0,0,{year},LepSel_pt[1],LepSel_eta[1],LepSel_pdgId[1])*getLeptonSF_v4(0,0,{year},LepSel_pt[2],LepSel_eta[2],LepSel_pdgId[2])*puWeight*bTagWeightDeepCSVT_nom{prefiringWeights}' --obj Events -j 32 -l {lumi} -f  -E SRWZ -o {year} --od ./cards/ --ms".format(var=var,binning=binning,year=options.year,prefiringTrees=prefiringTrees[options.year],prefiringWeights=prefiringWeights[options.year],triggerTrees=triggerTrees[options.year],lumi=lumi[options.year])
    


