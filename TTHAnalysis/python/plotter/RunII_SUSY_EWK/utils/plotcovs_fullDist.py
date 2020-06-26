import ROOT
import copy
from numpy import ceil
import numpy as np
from scipy.stats import chi2 as chi2
from multiprocessing import Pool
from contextlib import closing
import time

ROOT.gStyle.SetOptStat(0)
ROOT.gStyle.SetPaintTextFormat("1.3f")
ROOT.gROOT.SetBatch(True)

inFNorm =ROOT.TFile("allBootstraps/2016_dataobs_bootstrap_normApprox.root","READ")
inFNaive =ROOT.TFile("allBootstraps/2016_dataobs_bootstrap_naive.root","READ")
inFQuantiles =ROOT.TFile("allBootstraps/2016_dataobs_bootstrap_quantiles.root","READ")
inFNoW =ROOT.TFile("allBootstraps/2016_dataobs_bootstrap_noweights.root","READ")

masses = [6, 7, 8, 10, 14, 15, 16, 20, 30, 40,  50,  60, 70,  80,  90,  100,  110, 120,  125, 130,  140,  150, 175,  200, 225, 250, 275, 300, 325, 350, 375,  400,  425, 450,  475, 500, 525, 550, 575, 600, 625,  650,  675, 700, 725, 750, 775, 800, 825, 850, 875, 900, 925, 950, 975, 1000]

#masses = [10,15,90,100,500,525]

def produceVals(coms):
  inF = coms[0]
  dM1 = coms[1]
  dM2 = coms[2]
  typ = coms[3]
  vals1 = {}
  vals2 = {}
  covars = ROOT.TH2D("hist%s_%i_%i"%(typ,dM1,dM2),"hist%s_%i_%i"%(typ,dM1,dM2),20,0.5,20.5,20,0.5,20.5)
  print "Getting yields..."
  for w in range(1,1000):
    inC1 = inF.Get("data_obs_central_dM%i"%dM1)
    inC2 = inF.Get("data_obs_central_dM%i"%dM2)
    inH1 = inF.Get("data_obs_weight%i_dM%i"%(w,dM1))
    inH2 = inF.Get("data_obs_weight%i_dM%i"%(w,dM2))
    for b1 in range(1,21):
      for b2 in range(1,21):
        pull1 = (inH1.GetBinContent(b1)-inC1.GetBinContent(b1))/(inC1.GetBinContent(b1))**0.5
        pull2 = (inH2.GetBinContent(b2)-inC2.GetBinContent(b2))/(inC2.GetBinContent(b2))**0.5
        if not (b1,b2) in vals1.keys():
          vals1[(b1,b2)] = [pull1]
          vals2[(b1,b2)] = [pull2]
        else:
          vals1[(b1,b2)].append(pull1)
          vals2[(b1,b2)].append(pull2)
  print "Filling covariance...."
  for b1 in range(1,21):
    print "....step %i of 20"%(b1-1)
    for b2 in range(1,21):
      vec1 = np.array(vals1[(b1,b2)])
      vec2 = np.array(vals2[(b1,b2)])
      covars.SetBinContent(b1,b2, np.cov(vec1,vec2)[0,1]/(np.var(vec1)*np.var(vec2))**0.5)

  
  c = ROOT.TCanvas("c","c",800,600)
  covars.SetTitle("Correlation between bins in the dM=%i and dM=%i discriminants"%(dM1,dM2))
  covars.GetZaxis().SetRangeUser(-1,1)
  covars.GetXaxis().SetTitle("Bins in dM=%i"%dM1)
  covars.GetYaxis().SetTitle("Bins in dM=%i"%dM2)
  covars.Draw("textcolz")
  c.SaveAs("~/www/plots_bootstrap/covs2D/covs%s_%i_%i.pdf"%(typ,dM1,dM2))
  c.SaveAs("~/www/plots_bootstrap/covs2D/covs%s_%i_%i.png"%(typ,dM1,dM2))

def execute(commands):
  produceVals(commands[0],commands[1],commands[2],commands[3])


commands = []
for m1 in [90]:
  for m2 in [100]:
    commands.append([inFNorm,m1,m2,"Norm"])
    commands.append([inFNaive,m1,m2,"Naive"])
    commands.append([inFQuantiles,m1,m2,"Quantile"])
    #commands.append([inFNoW,m1,m2,"No Weights"])

for c in commands:
  produceVals(c)
"""for m1 in masses:
  for m2 in masses:
    produceVals(inFNorm, m1, m2, "Norm")
    produceVals(inFNaive, m1,m2,"Naive")
    produceVals(inFQuantiles, m1,m2,"Quantile")
    produceVals(inFNoW, m1,m2,"No Weights")
"""

"""with closing(Pool(4)) as p:
        print "Now running " + str(len(commands)) + " commands using: " + str(10) + " processes. Please wait"
        retlist1 = p.map_async(produceVals, commands, 1)
        while not retlist1.ready():
                print("Combine runs left: {}".format(retlist1._number_left ))
                time.sleep(1)
        retlist1 = retlist1.get()
        p.close()
        p.join()
        p.terminate()"""
