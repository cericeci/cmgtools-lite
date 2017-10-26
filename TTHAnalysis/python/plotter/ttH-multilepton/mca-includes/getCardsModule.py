import os

base2 = "python makeShapeCards.py --2d-binning-function Twodbinningthing ttH-multilepton/mca-2lss-mc.txt ttH-multilepton/2lss_tight.txt Twodbinningvars ttH-multilepton/systsEnv.txt -P /afs/cern.ch/work/p/peruzzi/tthtrees/TREES_TTH_250117_Summer16_JECV3_noClean_qgV2_skimOnlyMC_v6 --Fs {P}/1_recleaner_230217_v6 --Fs {P}/2_eventVars_230217_v6 --Fs {P}/3_kinMVA_BDTv8_230217_v6 --Fs {P}/4_BDTv8_Hj_230217_v6 --Fs {P}/5_triggerDecision_230217_v6 --Fs {P}/6_bTagSF_v6 --Fs {P}/7_tauTightSel_v6 --tree treeProducerSusyMultilepton --s2v -j 8 -l 35.9 -f --od outputdir -L ttH-multilepton/functionsTTH.cc --mcc ttH-multilepton/lepchoice-ttH-FO.txt --mcc ttH-multilepton/ttH_2lss3l_triggerdefs.txt --neg -W 'puw2016_nTrueInt_36fb(nTrueInt)*leptonSF_ttH(LepGood_pdgId[iLepFO_Recl[0]],LepGood_pt[iLepFO_Recl[0]],LepGood_eta[iLepFO_Recl[0]],2)*leptonSF_ttH(LepGood_pdgId[iLepFO_Recl[1]],LepGood_pt[iLepFO_Recl[1]],LepGood_eta[iLepFO_Recl[1]],2)*triggerSF_ttH(LepGood_pdgId[iLepFO_Recl[0]],LepGood_pdgId[iLepFO_Recl[1]],2)*eventBTagSF' --asimov "

base3 = "python makeShapeCards.py --2d-binning-function Twodbinningthing ttH-multilepton/mca-3l-mc.txt ttH-multilepton/3l_tight.txt Twodbinningvars ttH-multilepton/systsEnv.txt -P /afs/cern.ch/work/p/peruzzi/tthtrees/TREES_TTH_250117_Summer16_JECV3_noClean_qgV2_skimOnlyMC_v6 --Fs {P}/1_recleaner_230217_v6 --Fs {P}/2_eventVars_230217_v6 --Fs {P}/3_kinMVA_BDTv8_230217_v6 --Fs {P}/4_BDTv8_Hj_230217_v6 --Fs {P}/5_triggerDecision_230217_v6 --Fs {P}/6_bTagSF_v6 --Fs {P}/7_tauTightSel_v6 --tree treeProducerSusyMultilepton --s2v -j 8 -l 35.9 -f --od cards/./cards/test -L ttH-multilepton/functionsTTH.cc --mcc ttH-multilepton/lepchoice-ttH-FO.txt --mcc ttH-multilepton/ttH_2lss3l_triggerdefs.txt --neg -W 'puw2016_nTrueInt_36fb(nTrueInt)*leptonSF_ttH(LepGood_pdgId[iLepFO_Recl[0]],LepGood_pt[iLepFO_Recl[0]],LepGood_eta[iLepFO_Recl[0]],3)*leptonSF_ttH(LepGood_pdgId[iLepFO_Recl[1]],LepGood_pt[iLepFO_Recl[1]],LepGood_eta[iLepFO_Recl[1]],3)*leptonSF_ttH(LepGood_pdgId[iLepFO_Recl[2]],LepGood_pt[iLepFO_Recl[2]],LepGood_eta[iLepFO_Recl[2]],3)*triggerSF_ttH(LepGood_pdgId[iLepFO_Recl[0]],LepGood_pdgId[iLepFO_Recl[1]],3)*eventBTagSF' --asimov "

base4 = "python makeShapeCards.py --2d-binning-function Twodbinningthing ttH-multilepton/mca-4l-mc.txt ttH-multilepton/4l_tight.txt Twodbinningvars ttH-multilepton/systsEnv.txt -P /afs/cern.ch/work/p/peruzzi/tthtrees/TREES_TTH_250117_Summer16_JECV3_noClean_qgV2_skimOnlyMC_v6 --Fs {P}/1_recleaner_230217_v6 --Fs {P}/2_eventVars_230217_v6 --Fs {P}/3_kinMVA_BDTv8_230217_v6 --Fs {P}/4_BDTv8_Hj_230217_v6 --Fs {P}/5_triggerDecision_230217_v6 --Fs {P}/6_bTagSF_v6 --Fs {P}/7_tauTightSel_v6 --tree treeProducerSusyMultilepton --s2v -j 8 -l 35.9 -f --od cards/./cards/test -L ttH-multilepton/functionsTTH.cc --mcc ttH-multilepton/lepchoice-ttH-FO.txt --mcc ttH-multilepton/ttH_2lss3l_triggerdefs.txt --neg -W 'puw2016_nTrueInt_36fb(nTrueInt)*leptonSF_ttH(LepGood_pdgId[iLepFO_Recl[0]],LepGood_pt[iLepFO_Recl[0]],LepGood_eta[iLepFO_Recl[0]],3)*leptonSF_ttH(LepGood_pdgId[iLepFO_Recl[1]],LepGood_pt[iLepFO_Recl[1]],LepGood_eta[iLepFO_Recl[1]],3)*leptonSF_ttH(LepGood_pdgId[iLepFO_Recl[2]],LepGood_pt[iLepFO_Recl[2]],LepGood_eta[iLepFO_Recl[2]],3)*leptonSF_ttH(LepGood_pdgId[iLepFO_Recl[3]],LepGood_pt[iLepFO_Recl[3]],LepGood_eta[iLepFO_Recl[3]],3)*triggerSF_ttH(LepGood_pdgId[iLepFO_Recl[0]],LepGood_pdgId[iLepFO_Recl[1]],3)*eventBTagSF' -o 4l"



#Uncat Channels
chem = "-o 2lss_em -E ^em"
chmm = "-o 2lss_mm -E ^mm"
chee = "-o 2lss_ee -E ^ee"
ch3l = "-o 3l "


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

ch3lnegbt = "-o 3l_bt_neg -A alwaystrue negative (LepGood1_charge+LepGood2_charge+LepGood3_charge)<0 -E ^BTight "
ch3lposbt = "-o 3l_bt_pos -A alwaystrue positive (LepGood1_charge+LepGood2_charge+LepGood3_charge)>0 -E ^BTight "
ch3lnegbl = "-o 3l_bl_neg -A alwaystrue negative (LepGood1_charge+LepGood2_charge+LepGood3_charge)<0 -E ^BLoose "
ch3lposbl = "-o 3l_bl_pos -A alwaystrue positive (LepGood1_charge+LepGood2_charge+LepGood3_charge)>0 -E ^BLoose "

def getCatCards(base,TwodbinFunc,TwodbinVars,outputdir,mode):
	if mode == "2lss":
		command = base2
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
	elif mode == "g2l":
		command = base3
	  	command = command.replace("Twodbinningthing", TwodbinFunc)
		command = command.replace("Twodbinningvars", TwodbinVars)
		command = command.replace("outputdir", outputdir)
		print "----------3l------------ \n"
		os.system(command+ch3lnegbt)
		os.system(command+ch3lposbt)
		os.system(command+ch3lnegbl)
		os.system(command+ch3lposbl)
		print "----------4l------------ \n"	
		command = base4
	  	command = command.replace("Twodbinningthing", TwodbinFunc)
		command = command.replace("Twodbinningvars", TwodbinVars)
		command = command.replace("outputdir", outputdir)
		os.system(command)	

def getUnCatCards(base,TwodbinFunc,TwodbinVars,outputdir,mode):
	if mode == "2lss":
		command = base
		command = command.replace("Twodbinningthing", TwodbinFunc)
		command = command.replace("Twodbinningvars", TwodbinVars)
		command = command.replace("outputdir", outputdir)
		print "cat"+ TwodbinVars
		os.system(command + chee)
		os.system(command + chem)
		os.system(command + chmm)
	elif mode == "g2l":
		print "----------3l------------ \n"
		command = base3
		command = command.replace("Twodbinningthing", TwodbinFunc)
		command = command.replace("Twodbinningvars", TwodbinVars)
		command = command.replace("outputdir", outputdir)
		os.system(command+ch3l)
		print "----------4l------------ \n"
		command = base4
	  	command = command.replace("Twodbinningthing", TwodbinFunc)
		command = command.replace("Twodbinningvars", TwodbinVars)
		command = command.replace("outputdir", outputdir)
		os.system(command)

