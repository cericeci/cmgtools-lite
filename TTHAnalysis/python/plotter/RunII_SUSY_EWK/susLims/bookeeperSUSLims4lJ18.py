import os

base183l = "python makeShapeCardsNew.py RunII_SUSY_EWK/2018/4l/mca_ewkino_v5.txt RunII_SUSY_EWK/2018/4l/cuts_4l.txt '[VAR]' '[BINS]' --unc RunII_SUSY_EWK/systs/systs_wz18_forplot4l.txt --tree treeProducerSusyMultilepton -P /pool/ciencias/HeppyTrees/RA7/nanoAODv5_2018_estructure/ -P /pool/ciencias/HeppyTrees/RA7/nanoAODv5_2018_signals/ --FFulls {P}/leptonPtCorrections/ --FFasts {P}/puWeight/ --Fs {P}/leptonJetReCleanerEWK_NEWID/ --Fs {P}/leptonBuilderEWK_NEWID/ --FMCs {P}/leptonMatcher/ --FMCs {P}/bTagEventWeights_NEWID/ -L RunII_SUSY_EWK/functionsWZ.cc -L RunII_SUSY_EWK/functionsSF.cc -L RunII_SUSY_EWK/functionsMCMatch.cc -L RunII_SUSY_EWK/functionsEWK.cc  --plotgroup data_fakes+=.*promptsub.* --neglist .*promptsub.* --neg -W 'puWeight*bTagWeightDeepCSVT_nom*1*getLeptonSF_v5(2,0,2018,LepSel_conePt[0],LepSel_eta[0],LepSel_pdgId[0])*getLeptonSF_v5(2,0,2018,LepSel_conePt[1],LepSel_eta[1],LepSel_pdgId[1])*getLeptonSF_v5(2,0,2018,LepSel_conePt[2],LepSel_eta[2],LepSel_pdgId[2])*getLeptonSF_v5(2,0,2018,LepSel_conePt[3],LepSel_eta[3],LepSel_pdgId[3])' --obj Events -j 16 -f --FFasts {P}/ISR_nJets/   --mcc RunII_SUSY_EWK/2018/mcc_triggerdefs.txt -l 59.8 -E [SRCUT] [EXCLUDERS]  --ms --od [OD]  --binname J"

allSignals = ['sig_TChiWZ.*', 'sig_TChiWH.*', 'sig_TChiZZ.*', 'sig_TChiHH.*', 'sig_TChiHZ.*', 'sig_TChiSlep.*', 'sig_TChiTESlep.*', 'sig_TChiStau.*']
vetoSignals = ['sig_TChiWZ.*', 'sig_TChiSlep.*',  'sig_TChiTESlep.*', 'sig_TChiWH.*', 'sig_TChiStau.*']
varsandbins = {'SR4lHplot(deltaR(LepSel_eta[unused4(mll_i1[0], mll_i2[0], 1)], LepSel_phi[unused4(mll_i1[0], mll_i2[0], 1)], LepSel_eta[unused4(mll_i1[0], mll_i2[0], 2)], LepSel_phi[unused4(mll_i1[0], mll_i2[0], 2)]),mllL_4l)' :  '3,0.5,3.5'}
oCARD = 'SR4lJ_2018'
oDir = {'SR4lHplot(deltaR(LepSel_eta[unused4(mll_i1[0], mll_i2[0], 1)], LepSel_phi[unused4(mll_i1[0], mll_i2[0], 1)], LepSel_eta[unused4(mll_i1[0], mll_i2[0], 2)], LepSel_phi[unused4(mll_i1[0], mll_i2[0], 2)]),mllL_4l)': 'cards_4lJ18_SRnew'}
SRCUT = "SR4lJ"

for sigs in allSignals:
  if sigs in vetoSignals: continue
  for vb in varsandbins:
     excluders = ""
     for v in allSignals:
       if v != sigs:
          excluders = excluders + " --xp " + v
     command = base183l.replace("[VAR]", vb).replace("[BINS]",varsandbins[vb]).replace("[SRCUT]",SRCUT).replace("[OCARD]",oCARD).replace("[OD]", oDir[vb]+ sigs.replace("sig_","").replace(".*","")).replace("[EXCLUDERS]", excluders)
     print command
     os.system("sbatch -c 16 -p batch -J" + sigs + " --wrap \"" + command.replace("$","\$") + "\"")

