import ROOT

mca = open("/nfs/fanae/user/carlosec/CMSSW_10_4_0/src/CMGTools/TTHAnalysis/python/plotter/RunII_SUSY_EWK/2016/3l/mca_ewkino_v5_bootstrap.txt","r")
baseTree = "/pool/ciencias/HeppyTrees/RA7/nanoAODv5_2016_signals/[sample]/treeProducerSusyMultilepton/tree.root"
theLumi = 35900

baseOut = "from CMGTools.TTHAnalysis.tools.eventWeighterWeighted import eventWeighterWeighted\nMODULES.append( ('eventWeighterWeighted_[SAMPLE]', lambda : eventWeighterWeighted(100000,3461924,[WEIGHT])))\n"
basePrep = "python prepareEventVariablesFriendTree.py /pool/ciencias/HeppyTrees/RA7/nanoAODv5_2016_signals/ /pool/ciencias/HeppyTrees/RA7/nanoAODv5_2016_signals/bootstrap_weights_asPupi/ --tree treeProducerSusyMultilepton --ttree Events --tra2  -I CMGTools.TTHAnalysis.tools.multilepSUSTreeProducers -m  eventWeighter_[SAMPLE] -q batch --env oviedo -N 10000000 -d [SAMPLE] "
out = open("out.py","w")

countsDict = {"TChiWZ_400_175": 46561.0,"TChiWZ_225_135": 48218, "TChiWZ_450_1": 44304}
xsecDict   = {"TChiWZ_400_175": 121.013*0.10099/1000.,"TChiWZ_225_135": 1165.09*0.10099/1000., "TChiWZ_450_1": 73.4361*0.10099/1000.}
allImports = []
allPreps = []
for line in mca.readlines():
  if len(line) == 0 or line[0] == "#":
    #print line
    continue
  else:
    linesp = line.split(";")[0]
    words = linesp.split(":")
    if len(words) < 2: print line; continue
    tag = words[0]
    samples = words[1].replace(" ","").split("+")
    norm = words[2].replace(" ","")
    print samples, baseTree.replace("[sample]",samples[0]) 
    xsec = 0.
    counts = 0.
    for s in samples:
      tf = ROOT.TFile(baseTree.replace("[sample]",s),"READ")
      tc = tf.Get("Count")
      tev = tf.Get("Events")
      counts += tc.GetBinContent(1) if not s in countsDict else countsDict[s]
      for ev in tev:
        xsec = ev.xsec if s not in xsecDict else xsecDict[s]
        break
    #xsec = eval(norm)
    #print "Weight for sample %s is %1.8f"%(samples[0],xsec*theLumi*1./counts)
    for s in samples:
      print xsec, theLumi, counts, xsec*theLumi*1./counts
      allImports.append(baseOut.replace("[SAMPLE]",s).replace("[WEIGHT]","%1.8f"%(xsec*theLumi*1./counts)))
      out.write(baseOut.replace("[SAMPLE]",s).replace("[WEIGHT]","%1.8f"%(xsec*theLumi*1./counts)))
      allPreps.append(basePrep.replace("[SAMPLE]",s))
    line = line.replace(norm, "%i/35900."%counts)
    print line
"""print allImports

print "=============="
"""
print allPreps
