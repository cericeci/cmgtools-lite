import ROOT
import copy
from numpy import ceil
from scipy.stats import chi2 as chi2

ROOT.gStyle.SetOptStat(0)
ROOT.gROOT.SetBatch(True)

inFNorm =ROOT.TFile("2016_dataobs_aspupi_bootstrap_noweights_noneg.root","READ")
#inFNaive =ROOT.TFile("allBootstraps/2016_dataobs_bootstrap_naive.root","READ")
#inFQuantiles =ROOT.TFile("allBootstraps/2016_dataobs_bootstrap_quantiles.root","READ")
masses = [6, 7, 8, 10, 14, 15, 16, 20, 30, 40,  50,  60, 70,  80,  90,  100,  110, 120,  125, 130,  140,  150, 175,  200, 225, 250, 275, 300, 325, 350, 375,  400,  425, 450,  475, 500, 525, 550, 575, 600, 625,  650,  675, 700, 725, 750, 775, 800, 825, 850, 875, 900, 925, 950, 975, 1000]

pullsNorm      = ROOT.TH1F("pulls_norm", "pulls_norm", 50,-1,1)
#pullsNaive     = ROOT.TH1F("pulls_naive", "pulls_naive", 50,-5,5)
pullsQuantiles = ROOT.TH1F("pulls_quant", "pulls_quant", 50,-1,1)

pvalsNorm      = ROOT.TH1F("pvals_norm", "pvals_norm", 25,0,1)
#pvalsNaive     = ROOT.TH1F("pvals_naive", "pvals_naive", 25,0,1)
pvalsQuantiles = ROOT.TH1F("pvals_quant", "pvals_quant", 25,0,1)


def produceVals(inF,dM):
  values = []
  central = []
  thePois = []
  num = []
  inC = inF.Get("data_obs_weight0_dM%i"%dM)
  for b in range(1,21):
    central.append(inC.GetBinContent(b))
    hLow = max(0,round(central[-1] - 4*(central[-1])**0.5))
    hHigh = round(central[-1] + 4*(central[-1])**0.5)
    nBins = min(40,ceil(hHigh-hLow))
    binWidth = ceil((hHigh-hLow)/nBins)
    #print dM, b, hLow, central[-1], hHigh, nBins, binWidth
    hLow = hLow - binWidth/2.
    hHigh = hLow + (nBins+1)*binWidth
    #print hLow, hHigh
    nBins += 1
    nBins = int(nBins)

    values.append(ROOT.TH1F("h"+str(b) + inF.GetName(),"h"+str(b)+ inF.GetName(), nBins, hLow, hHigh))
    thePois.append( ROOT.TF1("fit"+str(b)+ inF.GetName(),"%1.3f*TMath::Poisson(x,[0])"%((hHigh-hLow)/nBins),hLow, hHigh))
    thePois[-1].SetParameter(0, central[-1])
    #thePois[-1].SetParameter(0, (hHigh-hLow)/nBins)
    num.append(0)

  for w in range(1,500):
    inH = inF.Get("data_obs_weight%i_dM%i"%(w,dM))
    for b in range(1,21):
      values[b-1].Fill(inH.GetBinContent(b))#-central[b-1])
      num[b-1] += 1 
    values[b-1].Sumw2()
 
  for b in range(1,21):
    values[b-1].Scale(1./num[b-1])
    #print values[b-1].Integral()
  return values, thePois, central
  

def produceHistos(dM):
  valuesNorm, thePoisNorm, centralNorm = produceVals(inFNorm, dM)
  #valuesNaive, thePoisNaive, centralNaive = produceVals(inFNaive, dM)
  #valuesQuant, thePoisQuant, centralQuant = produceVals(inFQuantiles, dM)
 
  c = ROOT.TCanvas("c","c",800,600)
  for i in range(len(valuesNorm)):
    thePoisCentral = thePoisNorm[i].Clone("theCentralPoisson")
    #print centralNorm[i], centralNaive[i], centralQuant[i]
    valuesNorm[i].Fit(thePoisNorm[i],"L")
    #valuesNaive[i].Fit(thePoisNaive[i])
    #valuesQuant[i].Fit(thePoisQuant[i])
    #print thePoisQuant[i].GetNDF(), thePoisQuant[i].GetProb(),valuesNorm[i].GetNbinsX()-1 ,chi2.sf(thePoisQuant[i].GetChisquare(),(valuesNorm[i].GetNbinsX()-1))
    valuesNorm[i].SetLineColor(ROOT.kBlue)
    valuesNorm[i].GetXaxis().SetTitle("Yields in bin %i dM=%i GeV"%(i,dM))
    valuesNorm[i].GetYaxis().SetTitle("Toys/(Total)")
    valuesNorm[i].SetTitle("Toy distribution of yields in bin %i dM=%i GeV"%(i,dM))
    valuesNorm[i].Draw("hist")
    thePoisNorm[i].SetLineColor(ROOT.kBlue)
    thePoisNorm[i].Draw("same")

    #valuesNaive[i].SetLineColor(ROOT.kRed)
    #valuesNaive[i].Draw("histsame")
    #thePoisNaive[i].SetLineColor(ROOT.kRed)
    #thePoisNaive[i].Draw("same")

    #valuesQuant[i].SetLineColor(ROOT.kGreen)
    #valuesQuant[i].Draw("histsame")
    #thePoisQuant[i].SetLineColor(ROOT.kGreen)
    #thePoisQuant[i].Draw("same")

    thePoisCentral.SetLineColor(ROOT.kBlack)
    thePoisCentral.Draw("same")

    tl = ROOT.TLegend(0.6,0.7,0.9,0.9)
    tl.AddEntry(thePoisNorm[i] , "Norm (fit,pval): %1.3f, %1.5f"%(thePoisNorm[i].GetParameter(0), thePoisNorm[i].GetProb()),"l")
    #tl.AddEntry(thePoisNaive[i], "Naive (fit,pval): %1.3f, %1.5f"%(thePoisNaive[i].GetParameter(0), thePoisNaive[i].GetProb()),"l")
    #tl.AddEntry(thePoisQuant[i] , "Quant (fit,pval): %1.3f, %1.5f"%(thePoisQuant[i].GetParameter(0), thePoisQuant[i].GetProb()),"l")

    tl.AddEntry(thePoisCentral, "Expected pois (exp): %1.3f"%centralNorm[i], "l")
    tl.Draw("same")

    c.SaveAs("~/www/plots_bootstrap_newstrat/check_dM%i_bin%i.pdf"%(dM,i))
    c.SaveAs("~/www/plots_bootstrap_newstrat/check_dM%i_bin%i.png"%(dM,i))

    pullsNorm.Fill((thePoisNorm[i].GetParameter(0) - centralNorm[i])/(thePoisNorm[i].GetParError(0)))
    #pullsNaive.Fill((thePoisNaive[i].GetParameter(0) - centralNorm[i])/thePoisNaive[i].GetParError(0))
    #pullsQuantiles.Fill((thePoisQuant[i].GetParameter(0) - centralNorm[i])/thePoisQuant[i].GetParError(0))


    pvalsNorm.Fill(thePoisNorm[i].GetProb())
    #pvalsNaive.Fill(thePoisNaive[i].GetProb())
    #pvalsQuantiles.Fill(thePoisQuant[i].GetProb())


for m in masses:
  print "=================================================="
  print "=================================================="
  print "Processing dM=%i"%m
  produceHistos(m)
  print "=================================================="
  print "=================================================="

c = ROOT.TCanvas("c","c",800,600)

pullsNorm.SetTitle("Toys vs pulls of fitted #nu value")
pullsNorm.SetLineColor(ROOT.kBlue)
#pullsNaive.SetLineColor(ROOT.kRed)
#pullsQuantiles.SetLineColor(ROOT.kGreen)
tl = ROOT.TLegend(0.6,0.7,0.9,0.9)
tl.AddEntry(pullsNorm, "Norm, pulls","l")
#tl.AddEntry(pullsNaive, "Naive, pulls","l")
#tl.AddEntry(pullsQuantiles, "Quant, pulls","l")
pullsNorm.GetXaxis().SetTitle("(#nu_{fit}-#nu_{exp})/#epsilon(#nu_{fit})")
pullsNorm.GetYaxis().SetTitle("Toys/(Total)")
pullsNorm.Draw("hist")
#pullsNaive.Draw("same hist")
#pullsQuantiles.Draw("same hist")
tl.Draw("same")
c.SaveAs("~/www/plots_bootstrap_newstrat/pulls_all.pdf")
c.SaveAs("~/www/plots_bootstrap_newstrat/pulls_all.png")

pvalsNorm.SetTitle("Toys vs p-values of fit to a Poissonian")
pvalsNorm.SetLineColor(ROOT.kBlue)
#pvalsNaive.SetLineColor(ROOT.kRed)
#pvalsQuantiles.SetLineColor(ROOT.kGreen)
tl = ROOT.TLegend(0.6,0.7,0.9,0.9)
tl.AddEntry(pvalsNorm, "Norm, pvals","l")
#tl.AddEntry(pvalsNaive, "Naive, pvals","l")
#tl.AddEntry(pvalsQuantiles, "Quant, pvals","l")
pvalsNorm.GetXaxis().SetTitle("Toy fit to poissonian p-value")
pvalsNorm.GetYaxis().SetTitle("Toys/(Total)")

pvalsNorm.Draw("hist")
#pvalsNaive.Draw("same hist")
#pvalsQuantiles.Draw("same hist")
tl.Draw("same")
c.SaveAs("~/www/plots_bootstrap_newstrat/pvals_all.pdf")
c.SaveAs("~/www/plots_bootstrap_newstrat/pvals_all.png")


