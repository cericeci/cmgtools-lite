import argparse
import os

parser = argparse.ArgumentParser(description='EWKino command generator')
parser.add_argument('-j', '--jobs', dest="jobs"  , default = "8"  , help = 'Number of parallel jobs to use in execution')
parser.add_argument('-y', '--year', dest="year"  , default = "2016"  , help = 'Running year')
parser.add_argument('--mcfakes', dest="mcfakes"  , default = False, action="store_true"  , help = 'Activate to run with MC fakes')
parser.add_argument('-f', '--finalState', dest="finalState", action="append", help = "Which final state you want to produce plots from")
parser.add_argument('-p', '--pdir', dest="pdir", default=False, help = "Where to put output plots, by default it will print to Carlos' Legacy web page")
parser.add_argument('-q', '--queue', dest="queue", default=None, help = "Submit plots to this queue")
parser.add_argument('-s','--add-signals', dest="addsignals"  , default = False, action="store_true"  , help = 'If not activated, signals wont be plotted')
parser.add_argument('--sP', dest="selectPlots"  , default = ""  , help = 'Select this plots')

parser.add_argument('-u','--add-uncertainties', dest="uncertainties"  , default = False, action="store_true"  , help = 'If not activated, wont plot with uncertainties')

args = parser.parse_args()

SFWPs        = {"2lss":"1", "3l":"2", "FO":"3"}
skimDict     = {"3l":"skimWZ", "None": "estructure"}
baseFTrees   = "--FFulls {P}/leptonPtCorrections/ --FFasts {P}/puWeight/ --Fs {P}/leptonJetReCleanerEWK_NEWID/ --Fs {P}/leptonBuilderEWK_NEWID/ --FMCs {P}/leptonMatcher/ --FMCs {P}/bTagEventWeights_NEWID/"
yearlyTrees  = {"2016": "--FFulls {P}/trigger_2016/  --FMCs {P}/trigger_prefiring/ ", "2017": "--FMCs {P}/trigger_prefiring/ ", "2018":""}
baseLoaders  = "-L RunII_SUSY_EWK/functionsWZ.cc -L RunII_SUSY_EWK/functionsSF.cc -L RunII_SUSY_EWK/functionsMCMatch.cc  -L RunII_SUSY_EWK/functionsEWK.cc"
basePlotting = "--maxRatioRange 0. 2. --fixRatioRange --print C,pdf,png,txt --legendWidth 0.23 --legendFontSize 0.036 --showMCError --showRatio --perBin"
fakesDict    = {"datafakes" : "--plotgroup data_fakes+=.*promptsub.* --neglist .*promptsub.* --neg ", "mcfakes" : " "}
weightbase   = "puWeight*bTagWeightDeepCSVT_nom"
yearlyWeight = {"2016": "weight_PrefiringJets*weight_PrefiringPhotons", "2017": "weight_PrefiringJets*weight_PrefiringPhotons", "2018":"1"}
weight1l     = "getLeptonSF_v5({WP},0,{year},LepSel_conePt[{idx}],LepSel_eta[{idx}],LepSel_pdgId[{idx}])"
thelumi = {"2016": "35.9", "2017":"41.5","2018":"59.8"}
extramccs = {"2016":"", "2017":" --mcc RunII_SUSY_EWK/2017/mcc_triggerdefs.txt ", "2018":" --mcc RunII_SUSY_EWK/2018/mcc_triggerdefs.txt "} 
nLight = {"2lss":2, "3lA":3, "3lB":3, "3lC":2, "3lD": 2, "3lE":2, "3lF":1, "4lG":4, "4lH":4, "4lI":3, "4lJ":2, "4lK":2}
nTau   = {"2lss":0, "3lA":0, "3lB":0, "3lC":1, "3lD": 1, "3lE":1, "3lF":2, "4lG":0, "4lH":0, "4lI":1, "4lJ":2, "4lK":2}
folder = {"2lss":"2lss", "3lA":"3l", "3lB":"3l", "3lC":"3l", "3lD": "3l", "3lE":"3l", "3lF":"3l", "4lG":"4l", "4lH":"4l", "4lI":"4l", "4lJ":"4l", "4lK":"4l"}
sigs = ' --xp sig.* ' if not(args.addsignals) else ''
base = "python mcPlots.py RunII_SUSY_EWK/{year}/{folder}/mca_ewkino_v5.txt RunII_SUSY_EWK/{year}/{folder}/cuts_{nlep}l.txt RunII_SUSY_EWK/{year}/{folder}/plots_wz.txt --tree treeProducerSusyMultilepton -P /pool/ciencias/HeppyTrees/RA7/nanoAODv5_{year}_{skim}/ -P /pool/ciencias/HeppyTrees/RA7/nanoAODv5_{year}_{skim}/ {ftrees} {loaders} {plotting} {fakes}  -W \'{weight}\' --obj Events -j {jobs} -f --pdir {plotdir} {extramcc} -l {lumi} {extracuts} {sigs} {unc} {sP} --split-factor -1 "

for state in args.finalState:
  wp = 1 if state == "2lss" else 2
  extraCut = " -E SR%s "%state
  pdir   = args.pdir if args.pdir != False else "/nfs/fanae/user/carlosec/www/EWKino/Legacy/SR%s_%s"%(state,args.year) 
  if state == "CRWZ":
    extraCut = " -E CRWZ "
    pdir   = args.pdir if args.pdir != False else "/nfs/fanae/user/carlosec/www/EWKino/Legacy/CRWZ_%s"%(args.year) 
    state = "3lA"
  if state == "CRconv":
    extraCut = " -E CRconv -X met -X convVeto "
    pdir   = args.pdir if args.pdir != False else "/nfs/fanae/user/carlosec/www/EWKino/Legacy/CRconv_%s"%(args.year)
    state = "3lA"

  ftrees = baseFTrees +" "+ yearlyTrees[args.year]
  fakes  = fakesDict["datafakes" if not(args.mcfakes)  else "mcfakes"]
  weight = weightbase +"*"+yearlyWeight[args.year]
  skim   = skimDict["3l"] if nLight[state] >= 3 else skimDict["None"]
  pdir   = args.pdir if args.pdir != False else "/nfs/fanae/user/carlosec/www/EWKino/Legacy/SR%s_%s"%(state,args.year) 
  unc    = " --unc RunII_SUSY_EWK/systs/systs_wz%s_forplot%s.txt"%(args.year.replace("20",""), str(nLight[state]+nTau[state])+"l") if args.uncertainties else ""
  selectPlots = "--sP " +  args.selectPlots if len(args.selectPlots) >= 1 else ""
  for l in range(nLight[state] + nTau[state]):
    weight += "*" + weight1l.replace("{WP}", str(wp)).replace("{idx}", str(l)).replace("{year}", args.year)
  result =  base.replace("{year}", args.year).replace("{folder}", folder[state]).replace("{nlep}",str(int(nLight[state]) + int(nTau[state]))).replace("{skim}", skim).replace("{ftrees}",ftrees).replace("{loaders}", baseLoaders).replace("{plotting}", basePlotting).replace("{fakes}",fakes).replace("{weight}",weight).replace("{jobs}", args.jobs).replace("{plotdir}", pdir).replace("{extramcc}",extramccs[args.year]).replace("{lumi}",thelumi[args.year]).replace("{extracuts}", extraCut).replace("{sigs}", sigs).replace("cuts_2l","cuts_2lss").replace("{unc}", unc).replace("{sP}",selectPlots)
  if not args.queue: print result
  else:
    os.system("sbatch -c %s -p %s --wrap \"%s\""%(args.jobs, args.queue, result))
