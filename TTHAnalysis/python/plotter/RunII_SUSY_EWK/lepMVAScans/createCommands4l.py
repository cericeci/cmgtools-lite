import os

base = "python makeShapeCardsSusy.py  RunII_SUSY_EWK/2016/4l/mca_ewkino_v5_lepgood.txt RunII_SUSY_EWK/2016/4l/cuts_4l_lepgood.txt  'MET_pt_nom' '[50,100,150,200,250,1000]' RunII_SUSY_EWK/systs/systs_wz16_lepgood.txt --tree treeProducerSusyMultilepton -P /pool/cienciasrw/HeppyTrees/RA7/nanoAODv5_2016_skimWZ/ -P /pool/cienciasrw/HeppyTrees/RA7/nanoAODv5_2016_signals/ --FFasts {P}/puWeight/ --FFulls {P}/leptonPtCorrections/ --FMCs {P}/trigger_prefiring/ --Fs {P}/leptonJetReCleanerWZSM/ --Fs {P}/leptonBuilderEWK/ --Fs {P}/trigger_2016/ --FMCs {P}/leptonMatcher/ --FMCs {P}/bTagEventWeights/ -L RunII_SM_WZ/functionsWZ.cc -L RunII_SM_WZ/functionsSF.cc -L RunII_SM_WZ/functionsMCMatch.cc -L RunII_SUSY_EWK/functionsEWKcorr.cc --plotgroup data_fakes+=.*promptsub.* --neglist .*promptsub.* --neg -W 'puWeight*($MC{bTagWeightDeepCSVT_nom} $FASTSIM{bTagWeightDeepCSVT})*weight_PrefiringJets*weight_PrefiringPhotons' -X SRevent -A  alwaystrue lepMVA 'allTight(LepGood_mvaTTH[0],LepGood_mvaTTH[1],LepGood_mvaTTH[2],LepGood_pdgId[0],LepGood_pdgId[1],LepGood_pdgId[2], [CUT1],[CUT2])' -p prompt.*  -p fakes.* -p sig_TChiZZ_400_1.* -p sig_TChiHZ_175_1.*  --obj Events -j 8 -f  -l 35.9  -E SR4lG  -o mvael[TAG1]mvamu[TAG2] --od testleptonMVA16_4l --asimov"

for i in range(20):
  for j in range(20):
    x = -1. + 0.1*i
    y = -1. + 0.1*j
    #print base.replace("[CUT1]", str(x)).replace("[CUT2]", str(y)).replace("[TAG1]", str(x).replace("-","m")).replace("[TAG2]", str(x).replace("-","m"))
    #os.system("sbatch -c 8 -p batch -J" + " --wrap \"" + base.replace("[CUT1]", str(x)).replace("[CUT2]", str(y)).replace("[TAG1]", str(x).replace("-","m")).replace("[TAG2]", str(x).replace("-","m")) + "\"")
    print "sbatch -c 8 -p short " + " --wrap \"" + base.replace("[CUT1]", str(x)).replace("[CUT2]", str(y)).replace("[TAG1]", str(x).replace("-","m")).replace("[TAG2]", str(y).replace("-","m")).replace("$","\$") + "\""
