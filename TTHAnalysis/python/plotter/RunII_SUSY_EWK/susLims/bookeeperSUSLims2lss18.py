import os

base643l = "python makeShapeCardsNew.py RunII_SUSY_EWK/2018/2lss/mca_ewkino_v5.txt RunII_SUSY_EWK/2018/2lss/cuts_2lss.txt '[VAR]' '[BINS]' --unc RunII_SUSY_EWK/systs/systs_wz18_forplot2l.txt --tree treeProducerSusyMultilepton -P /pool/ciencias/HeppyTrees/RA7/nanoAODv5_2018_estructure/ -P /pool/ciencias/HeppyTrees/RA7/nanoAODv5_2018_signals/ --FFulls {P}/leptonPtCorrections/ --FFasts {P}/puWeight/ --Fs {P}/leptonJetReCleanerEWK_NEWID/ --Fs {P}/leptonBuilderEWK_NEWID/ --FMCs {P}/leptonMatcher/ --FMCs {P}/bTagEventWeights_NEWID/  -L RunII_SUSY_EWK/functionsWZ.cc -L RunII_SUSY_EWK/functionsSF.cc -L RunII_SUSY_EWK/functionsMCMatch.cc  -L RunII_SUSY_EWK/functionsEWK.cc  --plotgroup data_fakes+=.*promptsub.* --neglist .*promptsub.* --neg   -W 'puWeight*bTagWeightDeepCSVT_nom*1*getLeptonSF_v5(1,0,2018,LepSel_conePt[0],LepSel_eta[0],LepSel_pdgId[0])*getLeptonSF_v5(1,0,2018,LepSel_conePt[1],LepSel_eta[1],LepSel_pdgId[1])' --obj Events -j 16 -f --FFasts {P}/ISR_nJets/   --mcc RunII_SUSY_EWK/2018/mcc_triggerdefs.txt  -l 59.8  -E [SRCUT] [EXCLUDERS]  --od [OD] --ms  --binname SS"

allSignals = ['sig_TChiWZ.*', 'sig_TChiWH.*', 'sig_TChiZZ.*', 'sig_TChiHH.*', 'sig_TChiHZ.*', 'sig_TChiSlep.*', 'sig_TChiTESlep.*', 'sig_TChiStau.*']
vetoSignals = [ 'sig_TChiTESlep.*', 'sig_TChiStau.*']
varsandbins = {'SR_ewk_ss2l_v6_plot(mt2davis(LepGood_pt[0], LepGood_eta[0],LepGood_phi[0], LepGood_pt[1], LepGood_eta[1],LepGood_phi[1], MET_pt_nom, MET_phi_nom), MET_pt, LepGood_pt[0]+LepGood_pt[1], pt_2(LepGood_conePt[0], LepGood_phi[0], LepGood_conePt[1], LepGood_phi[1]), min(mt_2(LepGood_conePt[0],LepGood_phi[0],MET_pt_nom,MET_phi_nom),mt_2(LepGood_conePt[1],LepGood_phi[1],MET_pt_nom,MET_phi_nom)),LepGood_charge[0])':'20,0.5,20.5'} 
oCARD = 'SR2lss_2018'
oDir  = {'SR_ewk_ss2l_v6_plot(mt2davis(LepGood_pt[0], LepGood_eta[0],LepGood_phi[0], LepGood_pt[1], LepGood_eta[1],LepGood_phi[1], MET_pt_nom, MET_phi_nom), MET_pt, LepGood_pt[0]+LepGood_pt[1], pt_2(LepGood_conePt[0], LepGood_phi[0], LepGood_conePt[1], LepGood_phi[1]), min(mt_2(LepGood_conePt[0],LepGood_phi[0],MET_pt_nom,MET_phi_nom),mt_2(LepGood_conePt[1],LepGood_phi[1],MET_pt_nom,MET_phi_nom)),LepGood_charge[0])':'cards_2lss18_SRnew'}
SRCUT = "SR2lss"

for sigs in allSignals:
  if sigs in vetoSignals: continue
  for vb in varsandbins:
     excluders = ""
     for v in allSignals:
       if v != sigs:
          excluders = excluders + " --xp " + v
     command = base643l.replace("[VAR]", vb).replace("[BINS]",varsandbins[vb]).replace("[SRCUT]",SRCUT).replace("[OCARD]",oCARD).replace("[OD]", oDir[vb]+ sigs.replace("sig_","").replace(".*","")).replace("[EXCLUDERS]", excluders)
     print command
     os.system("sbatch -c 16 -p batch -J" + sigs + " --wrap \"" + command.replace("$","\$") + "\"")

