import os
import ROOT
import array

inFiles = ["/pool/cienciasrw/HeppyTrees/RA7/nanoAODv5_2016_estructure/bTagEffsDeepCSV/"+ f for f in os.listdir("/pool/ciencias/HeppyTrees/RA7/nanoAODv5_2016_estructure/bTagEffsDeepCSV/")] 
tChain = ROOT.TChain()
for f in inFiles:
  tChain.Add(f + "/sf/t")

flavors = {"B":"B", "C":"C", "L":"L"}
WPs = ["L", "M", "T"]
Algos = ["DeepCSV"]

passVar = "JetPassWP{wp}FL{fl}_{var}"
failVar = "JetFailWP{wp}FL{fl}_{var}"

doControlPlots = True

hEffVector = []
for alg in Algos: #For each algorithm create an efficiency file
    theAlgFile = ROOT.TFile("./btagEff" + alg + "2016.root", "RECREATE")
    for wp in WPs:
        for f in flavors.keys():
            print alg, wp, f            
            tChain.Draw(passVar.replace("{wp}", wp).replace("{fl}", f).replace("{var}", "pt") + " : abs(" + passVar.replace("{wp}", wp).replace("{fl}", f).replace("{var}", "eta") + ") >> hPasst(25,0,2.5,200,0,1000)")
            tChain.Draw(failVar.replace("{wp}", wp).replace("{fl}", f).replace("{var}", "pt") + " : abs(" + failVar.replace("{wp}", wp).replace("{fl}", f).replace("{var}", "eta") + ") >> hFailt(25,0,2.5,200,0,1000)")
            hPasst  = ROOT.gDirectory.Get("hPasst")
            hFailt = ROOT.gDirectory.Get("hFailt")
            hPass  = ROOT.TH2F("hp","hp",3,array.array('d',[0,0.8,1.6,2.5]), 8, array.array('d',[0,20,30,50,70,100,140,200,1000]))
            hFail = ROOT.TH2F("hf","hf",3,array.array('d',[0,0.8,1.6,2.5]), 8, array.array('d',[0,20,30,50,70,100,140,200,1000]))
            for i in range(1,hPasst.GetNbinsX()+1):
                for j in range(1,hPasst.GetNbinsY()+1):
                    bidx = hPass.FindBin( hPasst.GetXaxis().GetBinCenter(i), hPasst.GetYaxis().GetBinCenter(j))
                    hPass.SetBinContent( bidx,  hPass.GetBinContent(bidx) + hPasst.GetBinContent(i,j) )
                    hFail.SetBinContent( bidx,  hFail.GetBinContent(bidx) + hFailt.GetBinContent(i,j) )
            hTotal = hFail
            hTotal.Add(hPass)

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
                        #print hTemp.GetBinContent(i,j), hTemp.GetBinError(i,j)
                hTemp.SetTitle("eff_TT_%s_%s"%(wp,flavors[f]))
                hTemp.GetXaxis().SetTitle("Jet #eta")
                hTemp.GetYaxis().SetTitle("Jet p_{T} [GeV]")
                ROOT.gStyle.SetPaintTextFormat("4.3f")
                #hTemp.Sumw2(False)
                hTemp.Draw("colz text E")
                c.SaveAs("./plots/eff_TT_%s_%s_%s_2016.pdf"%(wp,flavors[f], alg))
                c.SaveAs("./plots/eff_TT_%s_%s_%s_2016.png"%(wp,flavors[f], alg))
                c.SaveAs("./plots/eff_TT_%s_%s_%s_2016.root"%(wp,flavors[f], alg))
    theAlgFile.Close()
