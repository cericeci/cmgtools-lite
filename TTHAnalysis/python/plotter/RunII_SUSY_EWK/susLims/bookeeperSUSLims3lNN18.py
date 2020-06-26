import os
base183l = "python makeShapeCardsSusy.py  --Fs {P}/susyMVA_TChiWZ/  RunII_SUSY_EWK/2018/3l/mca_ewkino_v5.txt RunII_SUSY_EWK/2018/3l/cuts_3l.txt --FFasts {P}/puWeight/  '[VAR]' '[BINS]' RunII_SUSY_EWK/systs/systs_wz18_forplot3l.txt --tree treeProducerSusyMultilepton -P /pool/ciencias/HeppyTrees/RA7/nanoAODv5_2018_skimWZ/ -P /pool/ciencias/HeppyTrees/RA7/nanoAODv5_2018_signals/ --FFulls {P}/leptonPtCorrections/  --Fs {P}/leptonJetReCleanerWZSM/ --Fs {P}/leptonBuilderEWK/  --FMCs {P}/leptonMatcher/ --FMCs {P}/bTagEventWeights/ -L RunII_SM_WZ/functionsWZ.cc -L RunII_SM_WZ/functionsSF.cc -L RunII_SM_WZ/functionsMCMatch.cc -L RunII_SUSY_EWK/functionsEWKcorr.cc   --plotgroup data_fakes+=.*promptsub.* --neglist .*promptsub.* --neg --mcc RunII_SM_WZ/2018/mcc_triggerdefs.txt  -W 'puWeight*($MC{bTagWeightDeepCSVT_nom} $FASTSIM{bTagWeightDeepCSVT})*(getLeptonSF_v4(0,0,2018,LepSel_pt[0],LepSel_eta[0],LepSel_pdgId[0])*getLeptonSF_v4(0,0,2018,LepSel_pt[1],LepSel_eta[1],LepSel_pdgId[1])*getLeptonSF_v4(0,0,2018,LepSel_pt[2],LepSel_eta[2],LepSel_pdgId[2]))' --obj Events -j 16 -f  -l 59.8  -E [SRCUT] [EXCLUDERS] -o [OCARD] --od [OD]  --binname A"

allSignals = ['sig_TChiWZ.*', 'sig_TChiWH.*', 'sig_TChiZZ.*', 'sig_TChiHH.*', 'sig_TChiHZ.*', 'sig_TChiSlep.*', 'sig_TChiTESlep.*', 'sig_TChiStau.*']
vetoSignals =  ['sig_TChiWH.*', 'sig_TChiZZ.*', 'sig_TChiHH.*', 'sig_TChiHZ.*', 'sig_TChiSlep.*', 'sig_TChiTESlep.*', 'sig_TChiStau.*']
varsandbins = {}
oCARD = 'SR3lA_2018'
oDir  = {}

massSplits = [6, 7, 8, 10, 14, 15, 16, 20, 30, 40,  50,  60, 70,  80,  90, 91, 92, 93, 94, 95, 96, 97, 98, 99,  100,  110, 120,  125, 130,  140,  150, 175,  200, 225, 250, 275, 300, 165, 350, 375,  400,  425, 450,  475, 500, 525, 550, 575, 600, 625,  650,  675, 700, 725, 750, 775, 800, 825, 850, 875, 900, 925, 950, 975, 1000]
var = "TChiWZMVA_split"

for m in massSplits:
  varsandbins[var.replace("split",str(m))] = '40,0,1'
  oDir[var.replace("split",str(m))] = "/nfs/fanae/user/carlosec/Combine_SLC7/CMSSW_8_1_0/src/EWKINO_CARDS_LEGACY/cards_3lA18_"+str(m)

for sigs in allSignals:
  if sigs in vetoSignals: continue
  for vb in varsandbins:
     excluders = ""
     for v in allSignals:
       if v != sigs:
          excluders = excluders + " --xp " + v
     command = base183l.replace("[VAR]", vb).replace("[BINS]",varsandbins[vb]).replace("[SRCUT]","SR3lA").replace("[OCARD]",oCARD).replace("[OD]", oDir[vb]+ sigs.replace("sig_","").replace(".*","")).replace("[EXCLUDERS]", excluders)
     print command
     os.system("sbatch -c 16 -p batch -J" + sigs + " --wrap \"" + command.replace("$","\$") + "\"")

