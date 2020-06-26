import os
import ROOT


inFile = ROOT.TFile("/nfs/fanae/user/carlosec/WZ/CMSSW_9_4_4/src/CMGTools/TTHAnalysis/python/plotter/bTag_2017/plots_beff.root", "READ")

flavors = {"B":"b", "C":"c", "L":"udsg"}
WPs = ["L", "M", "T"]
Algos = ["CSV", "DeepCSV", "DeepFlavor"]

baseHisto = "jet_eta_pt_{flavor}_total"
histoName = "jet_eta_pt_{flavor}_{algo}{WP}_total"

doControlPlots = True

hEffVector = []
for alg in Algos: #For each algorithm create an efficiency file
    theAlgFile = ROOT.TFile("./btagEff" + alg + ".root", "RECREATE")
    for wp in WPs:
        print alg, wp
        for f in flavors.keys():
            hPass  = inFile.Get(histoName.replace("{flavor}", f).replace("{algo}", alg).replace("{WP}", wp))
            hTotal = inFile.Get(baseHisto.replace("{flavor}", f))
            #We need to put the non-central terms to 0 or TEfficiency crashes
            for i in range(0,hPass.GetNbinsX()+2):
                hPass.SetBinContent(i, 0, 0)
            for i in range(0,hPass.GetNbinsY()+2):
                hPass.SetBinContent(0, i, 0)
            hPass.Sumw2()
            hTotal.Sumw2()
            eTemp = ROOT.TEfficiency(hPass, hTotal)
            eTemp.SetName("eff_TT_%s_%s"%(wp,flavors[f]))
            theAlgFile.cd()
            eTemp.Write()
            if doControlPlots:
                c = ROOT.TCanvas("c","", 800,600)
                c.SetLogy(True)
                eTemp.Draw()
                c.Update() #If we don't do this, we don't get to take the PaintedHistogram
                hTemp = eTemp.GetPaintedHistogram()
                hTemp.Sumw2(False)
                for i in range(1,hTemp.GetNbinsX()+1):
                    for j in range(1,hTemp.GetNbinsY()+1):
                        hTemp.SetBinError(i,j, max(eTemp.GetEfficiencyErrorLow(eTemp.GetGlobalBin(i,j)), eTemp.GetEfficiencyErrorUp(eTemp.GetGlobalBin(i,j))))
                        print hTemp.GetBinContent(i,j), hTemp.GetBinError(i,j)
                hTemp.SetTitle("eff_TT_%s_%s"%(wp,flavors[f]))
                hTemp.GetXaxis().SetTitle("Jet #eta")
                hTemp.GetYaxis().SetTitle("Jet p_{T} [GeV]")
                ROOT.gStyle.SetPaintTextFormat("4.3f")
                #hTemp.Sumw2(False)
                hTemp.Draw("colz text E")
                c.SaveAs("./plots/eff_TT_%s_%s_%s_2017.pdf"%(wp,flavors[f], alg))
                c.SaveAs("./plots/eff_TT_%s_%s_%s_2017.png"%(wp,flavors[f], alg))
                c.SaveAs("./plots/eff_TT_%s_%s_%s_2017.root"%(wp,flavors[f], alg))
    theAlgFile.Close()
