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

dr1 = " nJet25:nJet25 2,0.,3.,2,0.,3. "
funcdr1  = " 2:NJet2Dto1D_2 "
outdr1_c = " /afs/cern.ch/user/c/cericeci/private/CMSSW_7_4_7/HiggsAnalysis/CombinedLimit/scripts/cards/NJet_CAT_2BINS "
outdr1_nc = " /afs/cern.ch/user/c/cericeci/private/CMSSW_7_4_7/HiggsAnalysis/CombinedLimit/scripts/cards/NJet_NOCAT_2BINS "
getCatCards(base,funcdr1,dr1,outdr1_c)
getUnCatCards(base,funcdr1,dr1,outdr1_nc)

dr1 = " nJet25:nJet25 5,0.,3.,5,0.,3. "
funcdr1  = " 5:NJet2Dto1D_5 "
outdr1_c = " /afs/cern.ch/user/c/cericeci/private/CMSSW_7_4_7/HiggsAnalysis/CombinedLimit/scripts/cards/NJet_CAT_5BINS "
outdr1_nc = " /afs/cern.ch/user/c/cericeci/private/CMSSW_7_4_7/HiggsAnalysis/CombinedLimit/scripts/cards/NJet_NOCAT_5BINS "
getCatCards(base,funcdr1,dr1,outdr1_c)
getUnCatCards(base,funcdr1,dr1,outdr1_nc)

dr1 = " nJet25:nJet25 10,0.,3.,10,0.,3. "
funcdr1  = " 10:NJet2Dto1D_10 "
outdr1_c = " /afs/cern.ch/user/c/cericeci/private/CMSSW_7_4_7/HiggsAnalysis/CombinedLimit/scripts/cards/NJet_CAT_10BINS "
outdr1_nc = " /afs/cern.ch/user/c/cericeci/private/CMSSW_7_4_7/HiggsAnalysis/CombinedLimit/scripts/cards/NJet_NOCAT_10BINS "
getCatCards(base,funcdr1,dr1,outdr1_c)
getUnCatCards(base,funcdr1,dr1,outdr1_nc)


