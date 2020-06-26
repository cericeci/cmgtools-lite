import ROOT
import copy
from numpy import ceil
from scipy.stats import chi2 as chi2

ROOT.gStyle.SetOptStat(0)
ROOT.gROOT.SetBatch(True)

inFNorm =ROOT.TFile("allBootstraps/2016_dataobs_bootstrap_normApprox.root","READ")
inFNaive =ROOT.TFile("allBootstraps/2016_dataobs_bootstrap_naive.root","READ")
inFQuantiles =ROOT.TFile("allBootstraps/2016_dataobs_bootstrap_quantiles.root","READ")
#masses = [6, 7, 8, 10, 14, 15, 16, 20, 30, 40,  50,  60, 70,  80,  90,  100,  110, 120,  125, 130,  140,  150, 175,  200, 225, 250, 275, 300, 325, 350, 375,  400,  425, 450,  475, 500, 525, 550, 575, 600, 625,  650,  675, 700, 725, 750, 775, 800, 825, 850, 875, 900, 925, 950, 975, 1000]

masses = [10,15,90,100,500,525]
bins = [1,2,10,11,19,20]

def produceVals(inF,dM1,dM2,ib1,ib2,typ):
  xvals = []
  yvals = []
  for w in range(1,1000):
    inC1 = inF.Get("data_obs_central_dM%i"%dM1)
    inC2 = inF.Get("data_obs_central_dM%i"%dM2)
    inH1 = inF.Get("data_obs_weight%i_dM%i"%(w,dM1))
    inH2 = inF.Get("data_obs_weight%i_dM%i"%(w,dM2))
    xvals.append((inH1.GetBinContent(ib1)-inC1.GetBinContent(ib1))/(inC1.GetBinContent(ib1))**0.5)
    yvals.append((inH2.GetBinContent(ib2)-inC2.GetBinContent(ib2))/(inC2.GetBinContent(ib2))**0.5)

  xmax = max(xvals)
  xmin = min(xvals)
  ymax = max(yvals)      
  ymin = min(yvals)
  outHist = ROOT.TH2D("hist%s_%i_%i_iB%i_iB%i"%(typ,dM1,dM2,ib1,ib2),"hist%s_%i_%i_iB%i_iB%i"%(typ,dM1,dM2,ib1,ib2),10,xmin,xmax,10,xmin,xmax) 
  for z in zip(xvals, yvals):
    outHist.Fill(z[0],z[1],1)
  c = ROOT.TCanvas("c","c",800,600)
  outHist.Draw("textcolz")
  c.SaveAs("test.pdf")
   
produceVals(inFNaive, 90,100,19,19,"Norm")
