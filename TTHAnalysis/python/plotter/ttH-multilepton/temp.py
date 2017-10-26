import os

base = "python makeShapeCards.py --2d-binning-function Twodbinningthing ttH-multilepton/mca-2lss-mc.txt ttH-multilepton/2lss_tight.txt Twodbinningvars ttH-multilepton/systsEnv.txt -P /afs/cern.ch/work/p/peruzzi/tthtrees/TREES_TTH_250117_Summer16_JECV3_noClean_qgV2_skimOnlyMC_v6 --Fs {P}/1_recleaner_230217_v6 --Fs {P}/2_eventVars_230217_v6 --Fs {P}/3_kinMVA_BDTv8_230217_v6 --Fs {P}/4_BDTv8_Hj_230217_v6 --Fs {P}/5_triggerDecision_230217_v6 --Fs {P}/6_bTagSF_v6 --Fs {P}/7_tauTightSel_v6 --tree treeProducerSusyMultilepton --s2v -j 8 -l 35.9 -f --od outputdir -L ttH-multilepton/functionsTTH.cc --mcc ttH-multilepton/lepchoice-ttH-FO.txt --mcc ttH-multilepton/ttH_2lss3l_triggerdefs.txt --neg -W 'puw2016_nTrueInt_36fb(nTrueInt)*leptonSF_ttH(LepGood_pdgId[iLepFO_Recl[0]],LepGood_pt[iLepFO_Recl[0]],LepGood_eta[iLepFO_Recl[0]],2)*leptonSF_ttH(LepGood_pdgId[iLepFO_Recl[1]],LepGood_pt[iLepFO_Recl[1]],LepGood_eta[iLepFO_Recl[1]],2)*triggerSF_ttH(LepGood_pdgId[iLepFO_Recl[0]],LepGood_pdgId[iLepFO_Recl[1]],2)*eventBTagSF' --asimov "

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



def getCatCards(base,TwodbinFunc,TwodbinVars,outputdir):
	command = base
	command = command.replace("Twodbinningthing", TwodbinFunc)
	command = command.replace("Twodbinningvars", TwodbinVars)
	command = command.replace("outputdir", outputdir)
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

def getUnCatCards(base,TwodbinFunc,TwodbinVars,outputdir):
	command = base
	command = command.replace("Twodbinningthing", TwodbinFunc)
	command = command.replace("Twodbinningvars", TwodbinVars)
	command = command.replace("outputdir", outputdir)
	print "cat"+ TwodbinVars
	os.system(command + chee)
	os.system(command + chem)
	os.system(command + chmm)

dr1 = " 'abs(LepGood_eta[1]):abs(LepGood_eta[1])' 18,0.,2.5,18,0.,2.5 "
funcdr1  = " 18:MaxEta2Dto1D_18 "
outdr1_c = " /afs/cern.ch/user/c/cericeci/private/CMSSW_7_4_7/HiggsAnalysis/CombinedLimit/scripts/cards/Eta2_CAT_FINAL "
outdr1_nc = " /afs/cern.ch/user/c/cericeci/private/CMSSW_7_4_7/HiggsAnalysis/CombinedLimit/scripts/cards/Eta2_NOCAT_FINAL "
getCatCards(base,funcdr1,dr1,outdr1_c)
getUnCatCards(base,funcdr1,dr1,outdr1_nc)

dr1 = " 'abs(LepGood_eta[0]):abs(LepGood_eta[0])' 18,0.,2.5,18,0.,2.5 "
funcdr1  = " 18:MaxEta2Dto1D_18 "
outdr1_c = " /afs/cern.ch/user/c/cericeci/private/CMSSW_7_4_7/HiggsAnalysis/CombinedLimit/scripts/cards/Eta1_CAT_FINAL "
outdr1_nc = " /afs/cern.ch/user/c/cericeci/private/CMSSW_7_4_7/HiggsAnalysis/CombinedLimit/scripts/cards/Eta1_NOCAT_FINAL "
getCatCards(base,funcdr1,dr1,outdr1_c)
getUnCatCards(base,funcdr1,dr1,outdr1_nc)

dr1 = " LepGood_pt[1]:LepGood_pt[1] 18,0.,200.,18,0.,200. "
funcdr1  = " 18:PT22Dto1D_18 "
outdr1_c = " /afs/cern.ch/user/c/cericeci/private/CMSSW_7_4_7/HiggsAnalysis/CombinedLimit/scripts/cards/PT2_CAT_FINAL "
outdr1_nc = " /afs/cern.ch/user/c/cericeci/private/CMSSW_7_4_7/HiggsAnalysis/CombinedLimit/scripts/cards/PT2_NOCAT_FINAL "
getCatCards(base,funcdr1,dr1,outdr1_c)
getUnCatCards(base,funcdr1,dr1,outdr1_nc)

dr1 = " htJet25j:htJet25j 20,0.,1200.,20,0.,1200. "
funcdr1  = " 20:HT2Dto1D_20 "
outdr1_c = " /afs/cern.ch/user/c/cericeci/private/CMSSW_7_4_7/HiggsAnalysis/CombinedLimit/scripts/cards/HT_CAT_FINAL "
outdr1_nc = " /afs/cern.ch/user/c/cericeci/private/CMSSW_7_4_7/HiggsAnalysis/CombinedLimit/scripts/cards/HT_NOCAT_FINAL "
getCatCards(base,funcdr1,dr1,outdr1_c)
getUnCatCards(base,funcdr1,dr1,outdr1_nc)

dr1 = " 'max(abs(LepGood_eta[0]),abs(LepGood_eta[1]))':'max(abs(LepGood_eta[0]),abs(LepGood_eta[1]))' 18,0.,2.5,18,0.,2.5 "
funcdr1  = " 18:MaxEta2Dto1D_18 "
outdr1_c = " /afs/cern.ch/user/c/cericeci/private/CMSSW_7_4_7/HiggsAnalysis/CombinedLimit/scripts/cards/MaxEta_CAT_FINAL "
outdr1_nc = " /afs/cern.ch/user/c/cericeci/private/CMSSW_7_4_7/HiggsAnalysis/CombinedLimit/scripts/cards/MaxEta_NOCAT_FINAL "
getCatCards(base,funcdr1,dr1,outdr1_c)
getUnCatCards(base,funcdr1,dr1,outdr1_nc)

dr1 = " mindr_lep2_jet:mindr_lep2_jet 20,0.,3.,20,0.,3. "
funcdr1  = " 20:DR22Dto1D_20 "
outdr1_c = " /afs/cern.ch/user/c/cericeci/private/CMSSW_7_4_7/HiggsAnalysis/CombinedLimit/scripts/cards/DR2_CAT_FINAL "
outdr1_nc = " /afs/cern.ch/user/c/cericeci/private/CMSSW_7_4_7/HiggsAnalysis/CombinedLimit/scripts/cards/DR2_NOCAT_FINAL "
getCatCards(base,funcdr1,dr1,outdr1_c)
getUnCatCards(base,funcdr1,dr1,outdr1_nc)

dr1 = " mindr_lep1_jet:mindr_lep1_jet 20,0.,3.,20,0.,3. "
funcdr1  = " 20:DR12Dto1D_20 "
outdr1_c = " /afs/cern.ch/user/c/cericeci/private/CMSSW_7_4_7/HiggsAnalysis/CombinedLimit/scripts/cards/DR1_CAT_FINAL "
outdr1_nc = " /afs/cern.ch/user/c/cericeci/private/CMSSW_7_4_7/HiggsAnalysis/CombinedLimit/scripts/cards/DR1_NOCAT_FINAL "
getCatCards(base,funcdr1,dr1,outdr1_c)
getUnCatCards(base,funcdr1,dr1,outdr1_nc)

dr1 = " kinMVA_2lss_ttbar_withBDTv8:kinMVA_2lss_ttbar_withBDTv8 20,-1.,1.,20,-1.,1. "
funcdr1  = " 20:BDT2Dto1D_20 "
outdr1_c = " /afs/cern.ch/user/c/cericeci/private/CMSSW_7_4_7/HiggsAnalysis/CombinedLimit/scripts/cards/BDTTT_CAT_FINAL "
outdr1_nc = " /afs/cern.ch/user/c/cericeci/private/CMSSW_7_4_7/HiggsAnalysis/CombinedLimit/scripts/cards/BDTTT_NOCAT_FINAL "
getCatCards(base,funcdr1,dr1,outdr1_c)
getUnCatCards(base,funcdr1,dr1,outdr1_nc)

dr1 = " kinMVA_2lss_ttV_withHj:kinMVA_2lss_ttV_withHj 20,-1.,1.,20,-1.,1. "
funcdr1  = " 20:BDT2Dto1D_20 "
outdr1_c = " /afs/cern.ch/user/c/cericeci/private/CMSSW_7_4_7/HiggsAnalysis/CombinedLimit/scripts/cards/BDTTTV_CAT_FINAL "
outdr1_nc = " /afs/cern.ch/user/c/cericeci/private/CMSSW_7_4_7/HiggsAnalysis/CombinedLimit/scripts/cards/BDTTTV_NOCAT_FINAL "
getCatCards(base,funcdr1,dr1,outdr1_c)
getUnCatCards(base,funcdr1,dr1,outdr1_nc)

dr1 = " met_pt:met_pt 20,0.,400.,20,0.,400. "
funcdr1  = " 20:MET2Dto1D_20 "
outdr1_c = " /afs/cern.ch/user/c/cericeci/private/CMSSW_7_4_7/HiggsAnalysis/CombinedLimit/scripts/cards/MET_CAT_FINAL "
outdr1_nc = " /afs/cern.ch/user/c/cericeci/private/CMSSW_7_4_7/HiggsAnalysis/CombinedLimit/scripts/cards/MET_NOCAT_FINAL "
getCatCards(base,funcdr1,dr1,outdr1_c)
getUnCatCards(base,funcdr1,dr1,outdr1_nc)

dr1 = " LepGood_pt[0]:LepGood_pt[0] 16,0.,300.,16,0.,300. "
funcdr1  = " 16:PT12Dto1D_16 "
outdr1_c = " /afs/cern.ch/user/c/cericeci/private/CMSSW_7_4_7/HiggsAnalysis/CombinedLimit/scripts/cards/PT1_CAT_FINAL "
outdr1_nc = " /afs/cern.ch/user/c/cericeci/private/CMSSW_7_4_7/HiggsAnalysis/CombinedLimit/scripts/cards/PT1_NOCAT_FINAL "
getCatCards(base,funcdr1,dr1,outdr1_c)
getUnCatCards(base,funcdr1,dr1,outdr1_nc)

dr1 = " LepGood_pt[0]:LepGood_pt[0] 18,0.,300.,18,0.,300. "
funcdr1  = " 18:PT12Dto1D_18 "
outdr1_c = " /afs/cern.ch/user/c/cericeci/private/CMSSW_7_4_7/HiggsAnalysis/CombinedLimit/scripts/cards/PT1_CAT_FINAL "
outdr1_nc = " /afs/cern.ch/user/c/cericeci/private/CMSSW_7_4_7/HiggsAnalysis/CombinedLimit/scripts/cards/PT1_NOCAT_FINAL "
getCatCards(base,funcdr1,dr1,outdr1_c)
getUnCatCards(base,funcdr1,dr1,outdr1_nc)
