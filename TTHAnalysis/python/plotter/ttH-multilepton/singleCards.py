import os

base = "python makeShapeCards.py  ttH-multilepton/mca-2lss-mc.txt ttH-multilepton/2lss_tight.txt variableandbinning ttH-multilepton/systsEnv.txt -P /afs/cern.ch/work/p/peruzzi/tthtrees/TREES_TTH_250117_Summer16_JECV3_noClean_qgV2_skimOnlyMC_v6 --Fs {P}/1_recleaner_230217_v6 --Fs {P}/2_eventVars_230217_v6 --Fs {P}/3_kinMVA_BDTv8_230217_v6 --Fs {P}/4_BDTv8_Hj_230217_v6 --Fs {P}/5_triggerDecision_230217_v6 --Fs {P}/6_bTagSF_v6 --Fs {P}/7_tauTightSel_v6 --tree treeProducerSusyMultilepton --s2v -j 8 -l 35.9 -f --od outputdir -L ttH-multilepton/functionsTTH.cc --mcc ttH-multilepton/lepchoice-ttH-FO.txt --mcc ttH-multilepton/ttH_2lss3l_triggerdefs.txt --neg -W 'puw2016_nTrueInt_36fb(nTrueInt)*leptonSF_ttH(LepGood_pdgId[iLepFO_Recl[0]],LepGood_pt[iLepFO_Recl[0]],LepGood_eta[iLepFO_Recl[0]],2)*leptonSF_ttH(LepGood_pdgId[iLepFO_Recl[1]],LepGood_pt[iLepFO_Recl[1]],LepGood_eta[iLepFO_Recl[1]],2)*triggerSF_ttH(LepGood_pdgId[iLepFO_Recl[0]],LepGood_pdgId[iLepFO_Recl[1]],2)*eventBTagSF' --asimov "

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



def getCatCards(base,var,outputdir):
	command = base
	command = command.replace("variableandbinning", var)
	command = command.replace("outputdir", outputdir)
	os.system(command + cheepos)
	os.system(command + cheemin)
	os.system(command + chemposbl)
	os.system(command + chemminbl)
	os.system(command + chemposbt)
	os.system(command + chemminbt)
	os.system(command + chmmposbl)
	os.system(command + chmmminbl)
	os.system(command + chmmposbt)
	os.system(command + chmmminbt)

def getUnCatCards(base,var,outputdir):
	command = base
	command = command.replace("variableandbinning", var)
	command = command.replace("outputdir", outputdir)
	os.system(command + chee)
	os.system(command + chem)
	os.system(command + chmm)

print "=========================ETA1============================"
eta1 = " LepGood_eta[0] 10,-2.5,2.5"
outeta1_c = "/afs/cern.ch/user/c/cericeci/private/CMSSW_7_4_7/HiggsAnalysis/CombinedLimit/scripts/cards/ETA1_CAT"
outeta1_nc = "/afs/cern.ch/user/c/cericeci/private/CMSSW_7_4_7/HiggsAnalysis/CombinedLimit/scripts/cards/ETA1_NOCAT"
getCatCards(base,eta1,outeta1_c)
getUnCatCards(base,eta1,outeta1_nc)


print "=========================ETA2============================"
eta2 = " LepGood_eta[1] 10,-2.5,2.5"
outeta2_c = "/afs/cern.ch/user/c/cericeci/private/CMSSW_7_4_7/HiggsAnalysis/CombinedLimit/scripts/cards/ETA2_CAT"
outeta2_nc = "/afs/cern.ch/user/c/cericeci/private/CMSSW_7_4_7/HiggsAnalysis/CombinedLimit/scripts/cards/ETA2_NOCAT"
getCatCards(base,eta2,outeta2_c)
getUnCatCards(base,eta2,outeta2_nc)

print "=========================HT============================"
ht = " htJet25j 12,0.,1200."
outht_c = "/afs/cern.ch/user/c/cericeci/private/CMSSW_7_4_7/HiggsAnalysis/CombinedLimit/scripts/cards/HT_CAT"
outht_nc = "/afs/cern.ch/user/c/cericeci/private/CMSSW_7_4_7/HiggsAnalysis/CombinedLimit/scripts/cards/HT_NOCAT"
getCatCards(base,ht,outht_c)
getUnCatCards(base,ht,outht_nc)


print "=========================MET============================"
met = " met_pt 8,0.,400."
outmet_c = "/afs/cern.ch/user/c/cericeci/private/CMSSW_7_4_7/HiggsAnalysis/CombinedLimit/scripts/cards/MET_CAT"
outmet_nc = "/afs/cern.ch/user/c/cericeci/private/CMSSW_7_4_7/HiggsAnalysis/CombinedLimit/scripts/cards/MET_NOCAT"
getCatCards(base,met,outmet_c)
getUnCatCards(base,met,outmet_nc)

print "=========================TTV============================"
bdtTTV = " kinMVA_2lss_ttV_withHj 20,-1.,1."
outTTV_c = "/afs/cern.ch/user/c/cericeci/private/CMSSW_7_4_7/HiggsAnalysis/CombinedLimit/scripts/cards/BDTTTV_CAT"
outTTV_nc = "/afs/cern.ch/user/c/cericeci/private/CMSSW_7_4_7/HiggsAnalysis/CombinedLimit/scripts/cards/BDTTTV_NOCAT"
getCatCards(base,bdtTTV,outTTV_c)
getUnCatCards(base,bdtTTV,outTTV_nc)

print "=========================TT============================"
bdtTT = " kinMVA_2lss_ttbar_withBDTv8 20,-1.,1."
outTT_c = "/afs/cern.ch/user/c/cericeci/private/CMSSW_7_4_7/HiggsAnalysis/CombinedLimit/scripts/cards/BDTTT_CAT"
outTT_nc = "/afs/cern.ch/user/c/cericeci/private/CMSSW_7_4_7/HiggsAnalysis/CombinedLimit/scripts/cards/BDTTT_NOCAT"
getCatCards(base,bdtTT,outTT_c)
getUnCatCards(base,bdtTT,outTT_nc)

print "=========================DR1============================"
dr1 = " mindr_lep1_jet 10,0.,3."
outdr1_c = "/afs/cern.ch/user/c/cericeci/private/CMSSW_7_4_7/HiggsAnalysis/CombinedLimit/scripts/cards/DR1_CAT"
outdr1_nc = "/afs/cern.ch/user/c/cericeci/private/CMSSW_7_4_7/HiggsAnalysis/CombinedLimit/scripts/cards/DR1_NOCAT"
getCatCards(base,dr1,outdr1_c)
getUnCatCards(base,dr1,outdr1_nc)

print "=========================DR2============================"
dr2 = " mindr_lep2_jet 10,0.,3."
outdr2_c = "/afs/cern.ch/user/c/cericeci/private/CMSSW_7_4_7/HiggsAnalysis/CombinedLimit/scripts/cards/DR2_CAT"
outdr2_nc = "/afs/cern.ch/user/c/cericeci/private/CMSSW_7_4_7/HiggsAnalysis/CombinedLimit/scripts/cards/DR2_NOCAT"
getCatCards(base,dr2,outdr2_c)
getUnCatCards(base,dr2,outdr2_nc)

print "=========================PT1============================"
pt1 = " LepGood_pt[0] 10,-2.5,2.5"
outpt1_c = "/afs/cern.ch/user/c/cericeci/private/CMSSW_7_4_7/HiggsAnalysis/CombinedLimit/scripts/cards/PT1_CAT"
outpt1_nc = "/afs/cern.ch/user/c/cericeci/private/CMSSW_7_4_7/HiggsAnalysis/CombinedLimit/scripts/cards/PT1_NOCAT"
getCatCards(base,pt1,outpt1_c)
getUnCatCards(base,pt1,outpt1_nc)

print "=========================PT2============================"
pt2 = " LepGood_pt[1] 10,-2.5,2.5"
outpt2_c = "/afs/cern.ch/user/c/cericeci/private/CMSSW_7_4_7/HiggsAnalysis/CombinedLimit/scripts/cards/PT2_CAT"
outpt2_nc = "/afs/cern.ch/user/c/cericeci/private/CMSSW_7_4_7/HiggsAnalysis/CombinedLimit/scripts/cards/PT2_NOCAT"
getCatCards(base,pt2,outpt2_c)
getUnCatCards(base,pt2,outpt2_nc)


print "=========================NJET============================"
njet = " nJet25 10,0.5,10.5"
outnjet_c = "/afs/cern.ch/user/c/cericeci/private/CMSSW_7_4_7/HiggsAnalysis/CombinedLimit/scripts/cards/NJET_CAT"
outnjet_nc = "/afs/cern.ch/user/c/cericeci/private/CMSSW_7_4_7/HiggsAnalysis/CombinedLimit/scripts/cards/NJET_NOCAT"
getCatCards(base,njet,outnjet_c)
getUnCatCards(base,njet,outnjet_nc)

print "=========================MLL============================"
mll = " 'if3(nLepFO>1,mass_2(LepGood1_conePt,LepGood1_eta,LepGood1_phi,LepGood1_mass,LepGood2_conePt,LepGood2_eta,LepGood2_phi,LepGood2_mass),-99)' 10,0.,400."
outmll_c = "/afs/cern.ch/user/c/cericeci/private/CMSSW_7_4_7/HiggsAnalysis/CombinedLimit/scripts/cards/MLL_CAT"
outmll_nc = "/afs/cern.ch/user/c/cericeci/private/CMSSW_7_4_7/HiggsAnalysis/CombinedLimit/scripts/cards/MLL_NOCAT"
getCatCards(base,mll,outmll_c)
getUnCatCards(base,mll,outmll_nc)

