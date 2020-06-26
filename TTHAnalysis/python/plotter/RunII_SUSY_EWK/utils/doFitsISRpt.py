import ROOT
import os
import json

ROOT.gStyle.SetOptStat(0)
ROOT.gROOT.SetBatch()
folds = {16: "/pool/ciencias/HeppyTrees/RA7/nanoAODv5_2016_signals/", 17: "/pool/ciencias/HeppyTrees/RA7/nanoAODv5_2017_signals/", 18: "/pool/ciencias/HeppyTrees/RA7/nanoAODv5_2018_signals/"}

inTrees = {}
i = 0
done = True
#First get a list of '16 samples
if not done:
 for f in os.listdir(folds[16]):
  if not("TChi" in f) or ("MVA" in f): continue
  tf16 = folds[16] + "/" + f + "/treeProducerSusyMultilepton/tree.root"
  tf17 = tf16.replace("16","17").replace("TChiSlepSnu_x0p05","TChiSelpSnu_x0p05")
  tf18 = tf16.replace("16","18")
  if not(os.path.isfile(tf16)): print "NOT16"; continue
  if not(os.path.isfile(tf17)): print "NOT17"; continue
  if not(os.path.isfile(tf18)): print "NOT18"; continue
  inTrees[f] = {16: tf16, 17: tf17, 18: tf18}
  print i 
  i += 1 

 print inTrees
 with open('samples.json', 'w') as fp:
    json.dump(inTrees, fp)

failures = []
kss1617 = []
kss1618 = []

if done:
 with open("samples.json") as fp:
  inTrees = json.load(fp)
  total = len(inTrees.keys())
  i = 0
  for k in inTrees.keys():
    print i, total, k
    i += 1
    #Get ISR pt
    tf16 = ROOT.TFile(inTrees[k]["16"],"READ")
    tt16 = tf16.Get("Events")
    tt16.Draw("ISR_pt >> h16(40,0,400)")
    h16 = ROOT.gDirectory.Get("h16")
    #tf16.Close()
    #print "16"
    tf17 = ROOT.TFile(inTrees[k]["17"],"READ")
    tt17 = tf17.Get("Events")
    tt17.Draw("ISR_pt >> h17(40,0,400)")
    h17 = ROOT.gDirectory.Get("h17")
    #tf17.Close()
    #print "17"
    tf18 = ROOT.TFile(inTrees[k]["18"],"READ")
    tt18 = tf18.Get("Events")
    tt18.Draw("ISR_pt >> h18(40,0,400)")
    h18 = ROOT.gDirectory.Get("h18")
    #tf18.Close()
    #print "18"
    h16.Sumw2()
    h17.Sumw2()
    h18.Sumw2()
    h16.Scale(1./h16.Integral())
    h17.Scale(1./h17.Integral())
    h18.Scale(1./h18.Integral())

    h16.SetLineColor(ROOT.kBlack)
    h17.SetLineColor(ROOT.kRed)
    canvas = ROOT.TCanvas("c", "c", 800, 600)
    canvas.cd()
    canvas.SetLogy()
    tl = ROOT.TLegend(0.6,0.6,0.95,0.8) 
    ROOT.gStyle.SetOptStat(0);
    ROOT.gStyle.SetPaintTextFormat("4.2f")
    h16.GetXaxis().SetTitle("ISR p_{T} [GeV]")
    h16.GetYaxis().SetTitle("Events")
    h16.Draw()
    h17.Draw("same")
    h18.Draw("same")
    ks1716 = h16.KolmogorovTest(h17)
    ks1816 = h16.KolmogorovTest(h18)
    #print ks1716, ks1816
    tl.AddEntry(h16,"2016","l")
    tl.AddEntry(h17,"2017,ks=%1.4f"%ks1716,"l")
    tl.AddEntry(h18,"2018,ks=%1.4f"%ks1816,"l")
    tl.Draw("same")
    if ks1716 >= 0.05 and ks1816 >= 0.05:
      canvas.SaveAs("/nfs/fanae/user/carlosec//www/EWKino/Legacy/ISRgood/"+ k + ".png")
    else:
      canvas.SaveAs("/nfs/fanae/user/carlosec//www/EWKino/Legacy/ISRbad/"+ k + ".png")
    tf16.Close()
    tf17.Close()
    tf18.Close()
    kss1617.append(ks1716)
    kss1618.append(ks1816)

print kss1617
print kss1618
with open('output.json', 'w') as fp:
    json.dump(kss1617, fp)
    json.dump(kss1618, fp)

