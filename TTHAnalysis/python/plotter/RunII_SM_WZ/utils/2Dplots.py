import ROOT
import array
import CMS_lumi

#Build Histo 
par1 = "fO" #X AXIS
par3 = "fLR" #Y AXIS
par1Pret = "f_{O}^{Z}"
par3Pret = "f_{L} - f_{R}"
par2 = "fLR"
par2Pret = "f_{L}^{Z} - f_{R}^{Z}"

DONE = False 
TOFLIP = True
REBIN = 2
if not DONE:
  inFile = ROOT.TFile("Zfitted.root", "READ")
  d3 = 0.8/200
  d1 = 0.2/200
  d2 = 0.0025
  min1 = 0.15
  max1 = 0.35
  min3 = -0.4
  max3 = 0.4
  min2 = -1.
  max2 = +1.
  n1 = int((max1-min1)/d1)
  n3 = int((max2-min2)/d2)
  n2 = int((max3-min3)/d3)
  theH2 = ROOT.TH2F("test","test", n1,min1,max1,n2,min2,max2)
  theHCounts = theH2.Clone()
  theHCounts.SetName("counts")
  limTree = inFile.Get("limit")

  #Fill it

  for i in range(1,n1+1):
    if( i%1000 == 0): print i, n1+1
    for j in range(1,n2+1):
      theH2.SetBinContent(i,j,0)
      theHCounts.SetBinContent(i,j,0)

  i = 0
  for ev in limTree:
    if( i%5000 == 0): print i, limTree.GetEntries()
    p1 = getattr(ev,par1)
    p2 = getattr(ev,par2)
    XBin = max(1, min(n1, theH2.GetXaxis().FindBin(p1)))
    YBin = max(1, min(n2, theH2.GetYaxis().FindBin(p2)))
    theH2.SetBinContent(XBin,YBin,theH2.GetBinContent(XBin,YBin)+2*ev.deltaNLL)
    theHCounts.SetBinContent(XBin,YBin,theHCounts.GetBinContent(XBin,YBin)+1)
    i += 1
 
  fileOut = ROOT.TFile("%s%sHists_Exp_Legacy.root"%(par1,par2), "RECREATE")
  fileOut.cd()
  theH2.Write()
  theHCounts.Write()
  fileOut.Close()


#Read from file 

if DONE:
  fileIn = ROOT.TFile("%s%sHists_Exp_Legacy.root"%(par1,par2), "READ")
  theH2 = fileIn.Get("test")
  theHCounts = fileIn.Get("counts")


#theH2.Smooth(1,"k5b")
if REBIN:
  theH2.Rebin2D(REBIN,REBIN)
  theHCounts.Rebin2D(REBIN,REBIN)
  #theH2.Scale(theH2.Integral())
theH2.Divide(theH2,theHCounts)
for i in range(2):
  print "SMOOTHING", i, 1
  theH2.Smooth(2,"k5b")

if TOFLIP:
  theH2Flipped = ROOT.TH2D("Flipperino", "Flipperino", theH2.GetNbinsY(), theH2.GetYaxis().GetBinLowEdge(1),theH2.GetYaxis().GetBinLowEdge(theH2.GetNbinsY())+theH2.GetYaxis().GetBinWidth(theH2.GetNbinsY()), theH2.GetNbinsX(), theH2.GetXaxis().GetBinLowEdge(1),theH2.GetXaxis().GetBinLowEdge(theH2.GetNbinsX())+theH2.GetXaxis().GetBinWidth(theH2.GetNbinsX()))
  for i in range(1,theH2Flipped.GetNbinsX()+1):
    if( i%100 == 0): print "FLIPPING", i, theH2Flipped.GetNbinsX()+1
    for j in range(1,theH2Flipped.GetNbinsY()+1):
      theH2Flipped.SetBinContent(i,j, theH2.GetBinContent(j,i))
  theH2 = theH2Flipped


q = theH2

q68 = q.Clone()
q95 = q.Clone()
q99 = q.Clone()

theContour68 = array.array('d',[-999.,2.2789])
theContour95 = array.array('d',[-999.,5.9915])
theContour99 = array.array('d',[-999.,9.2103])

q68.SetContour(2, theContour68)
q95.SetContour(2, theContour95)
q99.SetContour(2, theContour99)

q68.SetLineColor(ROOT.kBlue)
q95.SetLineColor(ROOT.kMagenta)
q99.SetLineColor(ROOT.kRed)

q68.SetLineStyle(7)
q95.SetLineStyle(7)
q99.SetLineStyle(7)

ROOT.gROOT.SetBatch(True)
canvas = ROOT.TCanvas("c", "c", 1600, 1080)
canvas.cd()
leg = ROOT.TLegend(0.6, 0.74, 0.75, 0.9);
leg.SetTextSize(0.032)
ROOT.gStyle.SetOptStat(0);
ROOT.gStyle.SetPaintTextFormat("4.2f")
ROOT.gStyle.SetOptTitle(0)
ROOT.gPad.Update()
canvas.SetTickx(1)
canvas.SetTicky(1)

canvas.SetRightMargin (0.19)
canvas.SetTopMargin   (0.06)
canvas.SetLeftMargin  (0.14)
canvas.SetBottomMargin(0.14)
q68.GetYaxis().SetRangeUser(0.15,0.35)
q68.GetXaxis().SetRangeUser(-0.35,0.35)

q68.GetYaxis().SetTitle(par1Pret)
q68.GetXaxis().SetTitle(par2Pret)
q68.GetXaxis().SetNdivisions(50210)
q68.GetXaxis().SetLabelFont(42)
q68.GetXaxis().SetLabelSize(0.035)  
q68.GetXaxis().SetTitleFont(42)
q68.GetXaxis().SetTitleSize(0.05)
q68.GetXaxis().SetLabelOffset(0.0045)
q68.GetXaxis().SetTitleOffset(1.05)
q68.GetYaxis().SetNdivisions(50210)
q68.GetYaxis().SetLabelFont(42)
q68.GetYaxis().SetLabelSize(0.035)
q68.GetYaxis().SetTitleFont(42)
q68.GetYaxis().SetTitleSize(0.05)
q68.GetYaxis().SetLabelOffset(0.007)
q68.GetYaxis().SetTitleOffset(1.2)
q68.GetZaxis().SetLabelFont(42)
q68.GetZaxis().SetTitleFont(42)
q68.GetZaxis().SetLabelSize(0.03)
q68.GetZaxis().SetTitleSize(0.040)
q68.GetZaxis().SetTitleOffset(0.8)

q68.Draw("cont3")
q95.Draw("cont3 same")
q99.Draw("cont3 same")

leg.AddEntry(q68, "Observed, 68% CL","l")
leg.AddEntry(q95, "Observed, 95% CL","l")
leg.AddEntry(q99, "Observed, 99% CL","l")


if True:
    p2b = array.array('d',[-0.038])
    p1b = array.array('d',[0.245])
    pCen = ROOT.TGraph(1,p2b,p1b)
    pCen.SetMarkerColor(ROOT.kBlack)
    pCen.SetMarkerStyle(34)
    pCen.SetMarkerSize(3)
    leg.AddEntry(pCen, "Best Fit", "p")
    pCen.Draw("p same")

    p2be = array.array('d',[-0.116])
    p1be = array.array('d',[0.258])
    pCene = ROOT.TGraph(1,p2be,p1be)
    pCene.SetMarkerColor(ROOT.kBlack)
    pCene.SetMarkerStyle(27)
    pCene.SetMarkerSize(3)
    leg.AddEntry(pCene, "Powheg+Pythia", "p")
    pCene.Draw("p same")


leg.SetFillColor(ROOT.kWhite)
leg.SetBorderSize(0);
leg.Draw("same")


CMS_lumi.writeExtraText = True
CMS_lumi.lumi_13TeV = "%.1f fb^{-1}" % (137.2)
CMS_lumi.extraText  = "Preliminary"
CMS_lumi.lumi_sqrtS = "13"
CMS_lumi.CMS_lumi(canvas, 4, 0, 0.035)

canvas.SaveAs("2D_%s_%s_Legacy.pdf"%(par1,par2))
canvas.SaveAs("2D_%s_%s_Legacy.png"%(par1,par2))
