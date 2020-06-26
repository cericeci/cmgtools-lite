import json
import ROOT

#with open("output.json") as fp:
#  indir = json.load(fp)

#print indir
#kss1617 = indir["kss1617"]
#kss1618 = indir["kss1618"]

ROOT.gROOT.SetBatch(True)
ROOT.gStyle.SetOptStat(0)

f = open("output.json")
cases = f.read().replace(" ","").split("]")

kss1617 = cases[0].replace("[","").split(",")
kss1618 = cases[1].replace("[","").split(",")

h17 = ROOT.TH1F("17","17", 20,0,1)
h18 = ROOT.TH1F("18","18", 20,0,1)

for kk in kss1617:
  h17.Fill(float(kk))

for kk in kss1618:
  h18.Fill(float(kk))

c = ROOT.TCanvas("c","c",800,600)
h17.SetLineColor(ROOT.kRed)
h17.GetXaxis().SetTitle("P-value")
h17.GetYaxis().SetTitle("Points")
h17.GetYaxis().SetRangeUser(0,2000)

h17.Draw()
h18.Draw("same")
tl = ROOT.TLegend(0.2,0.6,0.4,0.8)
tl.AddEntry(h17, "K-S 16/17", "l")
tl.AddEntry(h18, "K-S 16/18", "l")

tl.Draw("same")
c.SaveAs("pvalue.pdf")
