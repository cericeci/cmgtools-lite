import os

base183l = "python makeShapeCardsNew.py RunII_SUSY_EWK/2018/3l/mca_ewkino_v5.txt RunII_SUSY_EWK/2018/3l/cuts_3l.txt '[VAR]' '[BINS]' --tree treeProducerSusyMultilepton -P /pool/ciencias/HeppyTrees/RA7/nanoAODv5_2018_estructure/ -P /pool/ciencias/HeppyTrees/RA7/nanoAODv5_2018_signals/ --FFulls {P}/leptonPtCorrections/ --FFasts {P}/puWeight/ --Fs {P}/leptonJetReCleanerEWK_NEWID/ --Fs {P}/leptonBuilderEWK_NEWID/ --FMCs {P}/leptonMatcher/ --FMCs {P}/bTagEventWeights_NEWID/  -L RunII_SM_WZ/functionsWZ.cc -L RunII_SUSY_EWK/functionsSF.cc -L RunII_SUSY_EWK/functionsMCMatch.cc -L RunII_SUSY_EWK/functionsWZ.cc --plotgroup data_fakes+=.*promptsub.* --neglist .*promptsub.* --neg -W 'puWeight*($MC{bTagWeightDeepCSVT_nom} $FASTSIM{bTagWeightDeepCSVT})*getLeptonSF_v5(2,0,2018,LepSel_conePt[0],LepSel_eta[0],LepSel_pdgId[0])*getLeptonSF_v5(2,0,2018,LepSel_conePt[1],LepSel_eta[1],LepSel_pdgId[1])*getLeptonSF_v5(2,0,2018,LepSel_conePt[2],LepSel_eta[2],LepSel_pdgId[2])' --obj Events -j 16 -f --FFasts {P}/ISR_nJets/  --od [OD] -l 59.8 -E [SRCUT] [EXCLUDERS] -L ./RunII_SUSY_EWK/functionsEWKcorr.cc --unc RunII_SUSY_EWK/systs/systs_wz18_forplot3l.txt  --ms --mcc RunII_SUSY_EWK/2018/mcc_triggerdefs.txt  --binname F"


allSignals = ['sig_TChiWZ.*', 'sig_TChiWH.*', 'sig_TChiZZ.*', 'sig_TChiHH.*', 'sig_TChiHZ.*', 'sig_TChiSlep.*', 'sig_TChiTESlep.*', 'sig_TChiStau.*']
vetoSignals = ['sig_TChiWZ.*', 'sig_TChiSlep.*']
varsandbins = {'SR3lF(mT2L_3l, mt2davis(LepGood_pt[iL_Mini[0]], LepGood_eta[iL_Mini[0]], LepGood_phi[iL_Mini[0]], TauSel_Mini_pt[0], TauSel_Mini_eta[0], TauSel_Mini_phi[0], MET_pt_nom,MET_phi_nom), mass_2(LepGood_pt[iL_Mini[0]], LepGood_eta[iL_Mini[0]], LepGood_phi[iL_Mini[0]], LepGood_mass[iL_Mini[0]], TauSel_Mini_pt[0], TauSel_Mini_eta[0], TauSel_Mini_phi[0], TauSel_Mini_mass[0]), -1, MET_pt_nom)' :'12,0.5,12.5'} 
oCARD = 'SR3lF_2018'
oDir  = {'SR3lF(mT2L_3l, mt2davis(LepGood_pt[iL_Mini[0]], LepGood_eta[iL_Mini[0]], LepGood_phi[iL_Mini[0]], TauSel_Mini_pt[0], TauSel_Mini_eta[0], TauSel_Mini_phi[0], MET_pt_nom,MET_phi_nom), mass_2(LepGood_pt[iL_Mini[0]], LepGood_eta[iL_Mini[0]], LepGood_phi[iL_Mini[0]], LepGood_mass[iL_Mini[0]], TauSel_Mini_pt[0], TauSel_Mini_eta[0], TauSel_Mini_phi[0], TauSel_Mini_mass[0]), -1, MET_pt_nom)':'cards_3lF18_SRnew'}

for sigs in allSignals:
  if sigs in vetoSignals: continue
  for vb in varsandbins:
     excluders = ""
     for v in allSignals:
       if v != sigs:
          excluders = excluders + " --xp " + v
     command = base183l.replace("[VAR]", vb).replace("[BINS]",varsandbins[vb]).replace("[SRCUT]","SR3lF").replace("[OCARD]",oCARD).replace("[OD]", oDir[vb]+ sigs.replace("sig_","").replace(".*","")).replace("[EXCLUDERS]", excluders)
     print command
     os.system("sbatch -c 16 -p batch -J" + sigs + " --wrap \"" + command.replace("$","\$") + "\"")

