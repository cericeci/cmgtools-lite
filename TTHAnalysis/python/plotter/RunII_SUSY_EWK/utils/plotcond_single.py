import ROOT
import copy
from numpy import ceil, mean
from scipy.stats import chi2 as chi2

ROOT.gStyle.SetOptStat(0)
ROOT.gROOT.SetBatch(True)

inFNorm =ROOT.TFile("2016_dataobs_aspupi_bootstrap_noweights_noneg.root","READ")
#inFNormNoCut = ROOT.TFile("2016_dataobs_bootstrap_normnocut.root","READ")#allBootstraps/2016_dataobs_bootstrap_normnocut.root","READ")
inFNaive =ROOT.TFile("allBootstraps/2016_dataobs_bootstrap_naive.root","READ")
#inFQuantiles =ROOT.TFile("allBootstraps/2016_dataobs_bootstrap_quantiles.root","READ")
masses = [6, 7, 8, 10, 14, 15, 16, 20, 30, 40,  50,  60, 70,  80,  90,  100,  110, 120,  125, 130,  140,  150, 175,  200, 225, 250, 275, 300, 325, 350, 375,  400,  425, 450,  475, 500, 525, 550, 575, 600, 625,  650,  675, 700, 725, 750, 775, 800, 825, 850, 875, 900, 925, 950, 975, 1000]

pullsNorm      = ROOT.TH1F("pulls_norm", "pulls_norm", 51,-0.0005,0.0505)
#pullsNormnocut = ROOT.TH1F("pulls_normnocut", "pulls_normnocut", 50,-0.0005,0.0505)
pullsNaive     = ROOT.TH1F("pulls_naive", "pulls_naive", 51,-0.0005,0.0505)
#pullsQuantiles = ROOT.TH1F("pulls_quant", "pulls_quant", 51,-0.0005,0.0505)


def produceVals(inF,toy, histType):
  inC = {}
  inH = {}
  yields = []

  for dM in masses:
    #inC[dM] = inF.Get("data_obs_central_dM%i"%dM)
    inH[dM] = inF.Get("data_obs_weight%i_dM%i"%(toy,dM))
    yields.append(inH[dM].Integral())
  central = mean(yields)
  minY = -0.0525
  maxY = 0.0525
  nbins = 21
  condHisto = ROOT.TH1F("cond_%s_%i"%(histType, toy),"cond_%s_%i"%(histType, toy),nbins, minY, maxY)
  maxdev = 0
  for y in yields:
    val = (y-central)/central
    if abs(val) > maxdev: maxdev = abs(val)
    condHisto.Fill(val)
  if histType == "Norm":
    pullsNorm.Fill(maxdev)
  elif histType == "NormNoCut":
    pullsNormnocut.Fill(maxdev)
  elif histType == "Naive":
    pullsNaive.Fill(maxdev)
  elif histType == "Quantiles":
    pullsQuantiles.Fill(maxdev)

  return condHisto

for toy in range(1,500):
  print toy
  c = ROOT.TCanvas("c","c",800,600)
  condNorm = produceVals(inFNorm, toy, "Norm")
  #condNormNoCut = produceVals(inFNormNoCut, toy, "NormNoCut")
  condNaive = produceVals(inFNaive, toy, "Naive")
  #condQuantiles = produceVals(inFQuantiles, toy, "Quantiles")
  
  condNorm.SetLineColor(ROOT.kBlue)
  #condNormNoCut.SetLineColor(ROOT.kBlack)
  condNaive.SetLineColor(ROOT.kRed)
  #condQuantiles.SetLineColor(ROOT.kGreen)
  tl = ROOT.TLegend(0.6,0.7,0.9,0.9)
  tl.AddEntry(condNorm, "Standard, yield pull","l")
  #tl.AddEntry(condNormNoCut, "Norm no cut, yield pull","l")

  tl.AddEntry(condNaive, "Naive, yield pull","l")
  #tl.AddEntry(condQuantiles, "Quant, yield pull","l")

  condNorm.SetTitle("")
  condNorm.GetXaxis().SetTitle("Yields pull")
  condNorm.GetYaxis().SetTitle("# Mass hypothesis")

  condNorm.Draw("hist")
  #condNormNoCut.Draw("hist")
  condNaive.Draw("same hist")
  #condQuantiles.Draw("same hist")
  tl.Draw("same")
  c.SaveAs("~/www/plots_bootstrap_newstrat/condscomp_all_%i.pdf"%toy)
  c.SaveAs("~/www/plots_bootstrap_newstrat/condscomp_all_%i.png"%toy)

c = ROOT.TCanvas("c","c",800,600)
pullsNorm.SetLineColor(ROOT.kBlue)
#pullsNormnocut.SetLineColor(ROOT.kBlack)
pullsNaive.SetLineColor(ROOT.kRed)
#pullsQuantiles.SetLineColor(ROOT.kGreen)
tl = ROOT.TLegend(0.6,0.7,0.9,0.9)
tl.AddEntry(pullsNorm, "Standard, max deviations","l")
#tl.AddEntry(pullsNormnocut, "Norm no cut, max deviations","l")
tl.AddEntry(pullsNaive, "Naive, max deviations","l")
#tl.AddEntry(pullsQuantiles, "Quant, max deviations","l")
#pullsNormnocut.Draw("hist")
pullsNorm.SetTitle("")
pullsNorm.GetXaxis().SetTitle("Max yields pull deviation")
pullsNorm.GetYaxis().SetTitle("Toys")
pullsNorm.Draw("hist")
pullsNaive.Draw("same hist")
#pullsQuantiles.Draw("same hist")
tl.Draw("same")
c.SaveAs("~/www/plots_bootstrap_newstrat/maxdevcomp_all.pdf")
c.SaveAs("~/www/plots_bootstrap_newstrat/maxdevcomp_all.png")
