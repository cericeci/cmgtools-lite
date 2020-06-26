import os

base163l = "python makeShapeCardsNew.py RunII_SUSY_EWK/2016/3l/mca_ewkino_v5.txt RunII_SUSY_EWK/2016/3l/cuts_3l.txt '[VAR]' '[BINS]' --tree treeProducerSusyMultilepton -P /pool/ciencias/HeppyTrees/RA7/nanoAODv5_2016_skimWZ/ -P /pool/ciencias/HeppyTrees/RA7/nanoAODv5_2016_signals/ -P /pool/ciencias/HeppyTrees/RA7/nanoAODv5_2016_estructure/ --FFulls {P}/leptonPtCorrections/ --FFasts {P}/puWeight/ --Fs {P}/leptonJetReCleanerEWK_NEWID/ --Fs {P}/leptonBuilderEWK_NEWID/ --FMCs {P}/leptonMatcher/ --FMCs {P}/bTagEventWeights_NEWID/ --FFulls {P}/trigger_2016/ --FMCs {P}/trigger_prefiring/ -L RunII_SM_WZ/functionsWZ.cc -L RunII_SUSY_EWK/functionsSF.cc -L RunII_SUSY_EWK/functionsMCMatch.cc -L RunII_SUSY_EWK/functionsWZ.cc --plotgroup data_fakes+=.*promptsub.* --neglist .*promptsub.* --neg -W 'puWeight*($MC{bTagWeightDeepCSVT_nom} $FASTSIM{bTagWeightDeepCSVT})*weight_PrefiringJets*weight_PrefiringPhotons*getLeptonSF_v5(2,0,2016,LepSel_conePt[0],LepSel_eta[0],LepSel_pdgId[0])*getLeptonSF_v5(2,0,2016,LepSel_conePt[1],LepSel_eta[1],LepSel_pdgId[1])*getLeptonSF_v5(2,0,2016,LepSel_conePt[2],LepSel_eta[2],LepSel_pdgId[2])' --obj Events -j 16 -f --od [OD] -l 35.9 -E [SRCUT] [EXCLUDERS] -L ./RunII_SUSY_EWK/functionsEWKcorr.cc --unc RunII_SUSY_EWK/systs/systs_wz16_forplot3l.txt  --ms  --binname A"

allSignals = ['sig_TChiWZ.*', 'sig_TChiWH.*', 'sig_TChiZZ.*', 'sig_TChiHH.*', 'sig_TChiHZ.*', 'sig_TChiSlep.*', 'sig_TChiTESlep.*', 'sig_TChiStau.*']
vetoSignals = ['sig_TChiStau.*',  'sig_TChiSlep.*',  'sig_TChiWZ.*']
varsandbins = {'SRcorr(mll_3l, mT_3l , MET_pt_nom, htJet30j_Mini)' : '58, 0.5,58.5',  'SR3lA(-1, -1, mll_3l, mT_3l, MET_pt_nom)':'44,0.5,44.5'} 
oCARD = 'SR3lA_2016'
oDir  = {'SRcorr(mll_3l, mT_3l , MET_pt_nom, htJet30j_Mini)':'cards_3lA16_SRcorr', 'SR3lA(-1, -1, mll_3l, mT_3l, MET_pt_nom)':'cards_3lA16_SR16'}

for sigs in allSignals:
  if sigs in vetoSignals: continue
  for vb in varsandbins:
     excluders = ""
     for v in allSignals:
       if v != sigs:
          excluders = excluders + " --xp " + v
     command = base163l.replace("[VAR]", vb).replace("[BINS]",varsandbins[vb]).replace("[SRCUT]","SR3lA").replace("[OCARD]",oCARD).replace("[OD]", oDir[vb]+ sigs.replace("sig_","").replace(".*","")).replace("[EXCLUDERS]", excluders)
     print command
     #os.system("sbatch -c 16 -p batch -J" + sigs + " --wrap \"" + command.replace("$","\$") + "\"")

