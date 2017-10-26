import os

base = "python makeShapeCards.py --2d-binning-function Twodbinningthing ttH-multilepton/mca-2lss-mc.txt ttH-multilepton/2lss_tight.txt Twodbinningvars ttH-multilepton/systsATLASlike.txt -P /afs/cern.ch/work/p/peruzzi/tthtrees/TREES_TTH_250117_Summer16_JECV3_noClean_qgV2_skimOnlyMC_v6 --Fs {P}/1_recleaner_230217_v6 --Fs {P}/2_eventVars_230217_v6 --Fs {P}/3_kinMVA_BDTv8_230217_v6 --Fs {P}/4_BDTv8_Hj_230217_v6 --Fs {P}/5_triggerDecision_230217_v6 --Fs {P}/6_bTagSF_v6 --Fs {P}/7_tauTightSel_v6 --tree treeProducerSusyMultilepton --s2v -j 8 -l 35.9 -f --od outputdir -L ttH-multilepton/functionsTTH.cc --mcc ttH-multilepton/lepchoice-ttH-FO.txt --mcc ttH-multilepton/ttH_2lss3l_triggerdefs.txt --neg -W 'puw2016_nTrueInt_36fb(nTrueInt)*leptonSF_ttH(LepGood_pdgId[iLepFO_Recl[0]],LepGood_pt[iLepFO_Recl[0]],LepGood_eta[iLepFO_Recl[0]],2)*leptonSF_ttH(LepGood_pdgId[iLepFO_Recl[1]],LepGood_pt[iLepFO_Recl[1]],LepGood_eta[iLepFO_Recl[1]],2)*triggerSF_ttH(LepGood_pdgId[iLepFO_Recl[0]],LepGood_pdgId[iLepFO_Recl[1]],2)*eventBTagSF' --asimov "

#Uncat Channels
chem = "-o 2lss_em -E ^em"
chmm = "-o 2lss_mm -E ^mm"
chee = "-o 2lss_ee -E ^ee"

#Cat channels
cheepos = "-o 2lss_ee_pos -E ^ee -A alwaystrue positive 'LepGood_charge[0]>0' "
cheemin = "-o 2lss_ee_neg -E ^ee -A alwaystrue negative 'LepGood_charge[0]<0' "

chemposbl = "-o 2lss_em_bl_pos -E ^em -A alwaystrue positive 'LepGood_charge[0]>0' -E ^BLoose "
chemminbl = "-o 2lss_em_bl_neg -E ^em -A alwaystrue negative 'LepGood_charge[0]<0' -E ^BLoose "
chemposbt = "-o 2lss_em_bt_pos -E ^em -A alwaystrue positive 'LepGood_charge[0]>0' -E ^BTight "
chemminbt = "-o 2lss_em_bt_neg -E ^em -A alwaystrue negative 'LepGood_charge[0]<0' -E ^BTight "

chmmposbl = "-o 2lss_mm_bl_pos -E ^mm -A alwaystrue positive 'LepGood_charge[0]>0' -E ^BLoose "
chmmminbl = "-o 2lss_mm_bl_neg -E ^mm -A alwaystrue negative 'LepGood_charge[0]<0' -E ^BLoose "
chmmposbt = "-o 2lss_mm_bt_pos -E ^mm -A alwaystrue positive 'LepGood_charge[0]>0' -E ^BTight "
chmmminbt = "-o 2lss_mm_bt_neg -E ^mm -A alwaystrue negative 'LepGood_charge[0]<0' -E ^BTight "



def getCatCards(base,TwodbinFunc,TwodbinVars,systFile,outputdir):
	command = base
	command = command.replace("Twodbinningthing", TwodbinFunc)
	command = command.replace("Twodbinningvars", TwodbinVars)
	command = command.replace("outputdir", outputdir)
	command = command.replace("ttH-multilepton/systsATLASlike.txt",systFile)
	print "ee"+ TwodbinVars
	os.system(command + cheepos)
	os.system(command + cheemin)
	print "em"+ TwodbinVars
	os.system(command + chemposbl)
	os.system(command + chemminbl)
	os.system(command + chemposbt)
	os.system(command + chemminbt)
	print "mm"+ TwodbinVars
	os.system(command + chmmposbl)
	os.system(command + chmmminbl)
	os.system(command + chmmposbt)
	os.system(command + chmmminbt)

def getUnCatCards(base,TwodbinFunc,TwodbinVars,systFile,outputdir):
	command = base
	command = command.replace("Twodbinningthing", TwodbinFunc)
	command = command.replace("Twodbinningvars", TwodbinVars)
	command = command.replace("outputdir", outputdir)
	command = command.replace("ttH-multilepton/systsATLASlike.txt",systFile)
	print "cat"+ TwodbinVars
	os.system(command + chee)
	os.system(command + chem)
	os.system(command + chmm)

dr1 = " kinMVA_2lss_ttV_withHj:kinMVA_2lss_ttbar_withBDTv8 40,-1,1,40,-1,1 "
funcdr1  = " 8:OurBin2l "
outdr1_c = " /afs/cern.ch/user/c/cericeci/private/CMSSW_7_4_7/HiggsAnalysis/CombinedLimit/scripts/cards/SYSTS_ALL "
outdr1_nc = " /afs/cern.ch/user/c/cericeci/private/CMSSW_7_4_7/HiggsAnalysis/CombinedLimit/scripts/cards/SYSTS_ALL "
getCatCards(base,funcdr1,dr1,"ttH-multilepton/AllSy.txt",outdr1_c)
getUnCatCards(base,funcdr1,dr1,"ttH-multilepton/AllSy.txt",outdr1_nc)

dr1 = " kinMVA_2lss_ttV_withHj:kinMVA_2lss_ttbar_withBDTv8 40,-1,1,40,-1,1 "
funcdr1  = " 8:OurBin2l "
outdr1_c = " /afs/cern.ch/user/c/cericeci/private/CMSSW_7_4_7/HiggsAnalysis/CombinedLimit/scripts/cards/SYSTS_LUM "
outdr1_nc = " /afs/cern.ch/user/c/cericeci/private/CMSSW_7_4_7/HiggsAnalysis/CombinedLimit/scripts/cards/SYSTS_LUM "
getCatCards(base,funcdr1,dr1,"ttH-multilepton/nolumSy.txt",outdr1_c)
getUnCatCards(base,funcdr1,dr1,"ttH-multilepton/nolumSy.txt",outdr1_nc)

dr1 = " kinMVA_2lss_ttV_withHj:kinMVA_2lss_ttbar_withBDTv8 40,-1,1,40,-1,1 "
funcdr1  = " 8:OurBin2l "
outdr1_c = " /afs/cern.ch/user/c/cericeci/private/CMSSW_7_4_7/HiggsAnalysis/CombinedLimit/scripts/cards/SYSTS_LEPE "
outdr1_nc = " /afs/cern.ch/user/c/cericeci/private/CMSSW_7_4_7/HiggsAnalysis/CombinedLimit/scripts/cards/SYSTS_LEPE "
getCatCards(base,funcdr1,dr1,"ttH-multilepton/nolepeSy.txt",outdr1_c)
getUnCatCards(base,funcdr1,dr1,"ttH-multilepton/nolepeSy.txt",outdr1_nc)

dr1 = " kinMVA_2lss_ttV_withHj:kinMVA_2lss_ttbar_withBDTv8 40,-1,1,40,-1,1 "
funcdr1  = " 8:OurBin2l "
outdr1_c = " /afs/cern.ch/user/c/cericeci/private/CMSSW_7_4_7/HiggsAnalysis/CombinedLimit/scripts/cards/SYSTS_LEPMU "
outdr1_nc = " /afs/cern.ch/user/c/cericeci/private/CMSSW_7_4_7/HiggsAnalysis/CombinedLimit/scripts/cards/SYSTS_LEPMU "
getCatCards(base,funcdr1,dr1,"ttH-multilepton/nolepmuSy.txt",outdr1_c)
getUnCatCards(base,funcdr1,dr1,"ttH-multilepton/nolepmuSy.txt",outdr1_nc)

dr1 = " kinMVA_2lss_ttV_withHj:kinMVA_2lss_ttbar_withBDTv8 40,-1,1,40,-1,1 "
funcdr1  = " 8:OurBin2l "
outdr1_c = " /afs/cern.ch/user/c/cericeci/private/CMSSW_7_4_7/HiggsAnalysis/CombinedLimit/scripts/cards/SYSTS_TRIG "
outdr1_nc = " /afs/cern.ch/user/c/cericeci/private/CMSSW_7_4_7/HiggsAnalysis/CombinedLimit/scripts/cards/SYSTS_TRIG "
getCatCards(base,funcdr1,dr1,"ttH-multilepton/notrigSy.txt",outdr1_c)
getUnCatCards(base,funcdr1,dr1,"ttH-multilepton/notrigSy.txt",outdr1_nc)

dr1 = " kinMVA_2lss_ttV_withHj:kinMVA_2lss_ttbar_withBDTv8 40,-1,1,40,-1,1 "
funcdr1  = " 8:OurBin2l "
outdr1_c = " /afs/cern.ch/user/c/cericeci/private/CMSSW_7_4_7/HiggsAnalysis/CombinedLimit/scripts/cards/SYSTS_JES "
outdr1_nc = " /afs/cern.ch/user/c/cericeci/private/CMSSW_7_4_7/HiggsAnalysis/CombinedLimit/scripts/cards/SYSTS_JES "
getCatCards(base,funcdr1,dr1,"ttH-multilepton/noJESSy.txt",outdr1_c)
getUnCatCards(base,funcdr1,dr1,"ttH-multilepton/noJESSy.txt",outdr1_nc)

dr1 = " kinMVA_2lss_ttV_withHj:kinMVA_2lss_ttbar_withBDTv8 40,-1,1,40,-1,1 "
funcdr1  = " 8:OurBin2l "
outdr1_c = " /afs/cern.ch/user/c/cericeci/private/CMSSW_7_4_7/HiggsAnalysis/CombinedLimit/scripts/cards/SYSTS_BTAG "
outdr1_nc = " /afs/cern.ch/user/c/cericeci/private/CMSSW_7_4_7/HiggsAnalysis/CombinedLimit/scripts/cards/SYSTS_BTAG "
getCatCards(base,funcdr1,dr1,"ttH-multilepton/nobtagSy.txt",outdr1_c)
getUnCatCards(base,funcdr1,dr1,"ttH-multilepton/nobtagSy.txt",outdr1_nc)

dr1 = " kinMVA_2lss_ttV_withHj:kinMVA_2lss_ttbar_withBDTv8 40,-1,1,40,-1,1 "
funcdr1  = " 8:OurBin2l "
outdr1_c = " /afs/cern.ch/user/c/cericeci/private/CMSSW_7_4_7/HiggsAnalysis/CombinedLimit/scripts/cards/SYSTS_STAT "
outdr1_nc = " /afs/cern.ch/user/c/cericeci/private/CMSSW_7_4_7/HiggsAnalysis/CombinedLimit/scripts/cards/SYSTS_STAT "
getCatCards(base,funcdr1,dr1,"ttH-multilepton/nostatSy.txt",outdr1_c)
getUnCatCards(base,funcdr1,dr1,"ttH-multilepton/nostatSy.txt",outdr1_nc)

dr1 = " kinMVA_2lss_ttV_withHj:kinMVA_2lss_ttbar_withBDTv8 40,-1,1,40,-1,1 "
funcdr1  = " 8:OurBin2l "
outdr1_c = " /afs/cern.ch/user/c/cericeci/private/CMSSW_7_4_7/HiggsAnalysis/CombinedLimit/scripts/cards/SYSTS_WZ "
outdr1_nc = " /afs/cern.ch/user/c/cericeci/private/CMSSW_7_4_7/HiggsAnalysis/CombinedLimit/scripts/cards/SYSTS_WZ "
getCatCards(base,funcdr1,dr1,"ttH-multilepton/noWZSy.txt",outdr1_c)
getUnCatCards(base,funcdr1,dr1,"ttH-multilepton/noWZSy.txt",outdr1_nc)

dr1 = " kinMVA_2lss_ttV_withHj:kinMVA_2lss_ttbar_withBDTv8 40,-1,1,40,-1,1 "
funcdr1  = " 8:OurBin2l "
outdr1_c = " /afs/cern.ch/user/c/cericeci/private/CMSSW_7_4_7/HiggsAnalysis/CombinedLimit/scripts/cards/SYSTS_RARES "
outdr1_nc = " /afs/cern.ch/user/c/cericeci/private/CMSSW_7_4_7/HiggsAnalysis/CombinedLimit/scripts/cards/SYSTS_RARES "
getCatCards(base,funcdr1,dr1,"ttH-multilepton/noRaresSy.txt",outdr1_c)
getUnCatCards(base,funcdr1,dr1,"ttH-multilepton/noRaresSy.txt",outdr1_nc)

dr1 = " kinMVA_2lss_ttV_withHj:kinMVA_2lss_ttbar_withBDTv8 40,-1,1,40,-1,1 "
funcdr1  = " 8:OurBin2l "
outdr1_c = " /afs/cern.ch/user/c/cericeci/private/CMSSW_7_4_7/HiggsAnalysis/CombinedLimit/scripts/cards/SYSTS_CONVS "
outdr1_nc = " /afs/cern.ch/user/c/cericeci/private/CMSSW_7_4_7/HiggsAnalysis/CombinedLimit/scripts/cards/SYSTS_CONVS "
getCatCards(base,funcdr1,dr1,"ttH-multilepton/noConvsSy.txt",outdr1_c)
getUnCatCards(base,funcdr1,dr1,"ttH-multilepton/noConvsSy.txt",outdr1_nc)

dr1 = " kinMVA_2lss_ttV_withHj:kinMVA_2lss_ttbar_withBDTv8 40,-1,1,40,-1,1 "
funcdr1  = " 8:OurBin2l "
outdr1_c = " /afs/cern.ch/user/c/cericeci/private/CMSSW_7_4_7/HiggsAnalysis/CombinedLimit/scripts/cards/SYSTS_QCD "
outdr1_nc = " /afs/cern.ch/user/c/cericeci/private/CMSSW_7_4_7/HiggsAnalysis/CombinedLimit/scripts/cards/SYSTS_QCD "
getCatCards(base,funcdr1,dr1,"ttH-multilepton/noQCDSy.txt",outdr1_c)
getUnCatCards(base,funcdr1,dr1,"ttH-multilepton/noQCDSy.txt",outdr1_nc)

dr1 = " kinMVA_2lss_ttV_withHj:kinMVA_2lss_ttbar_withBDTv8 40,-1,1,40,-1,1 "
funcdr1  = " 8:OurBin2l "
outdr1_c = " /afs/cern.ch/user/c/cericeci/private/CMSSW_7_4_7/HiggsAnalysis/CombinedLimit/scripts/cards/SYSTS_PDF "
outdr1_nc = " /afs/cern.ch/user/c/cericeci/private/CMSSW_7_4_7/HiggsAnalysis/CombinedLimit/scripts/cards/SYSTS_PDF "
getCatCards(base,funcdr1,dr1,"ttH-multilepton/nopdfSy.txt",outdr1_c)
getUnCatCards(base,funcdr1,dr1,"ttH-multilepton/nopdfSy.txt",outdr1_nc)




