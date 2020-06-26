import ROOT

ROOT.gROOT.SetBatch(True)
ROOT.gStyle.SetOptStat(False)
inputs = ["/pool/ciencias/HeppyTrees/RA7/nanoAODv5_2018_skimWZ/bosonPolarizationGEN/evVarFriend_WZTo3LNu_pow.root", "/pool/ciencias/HeppyTrees/RA7/nanoAODv5_2018_skimWZ/bosonPolarization/evVarFriend_WZTo3LNu_pow.root", "/pool/ciencias/HeppyTrees/RA7/nanoAODv5_2018_skimWZ/leptonBuilderWZSM/evVarFriend_WZTo3LNu_pow.root"]
variables= {"#eta^{Dn}(W)":"WDn_eta_Lab","#eta^{Up}(W)":"WUp_eta_Lab","#eta^{Real}(W)":"(WDn_eta_Lab+WUp_eta_Lab)/2.","#eta^{ZRec}(W)":"((abs(cosh(WDn_eta_Lab)*WDn_pt_Lab - cosh(Z_eta_Lab)*Z_pt_Lab) < abs(cosh(WUp_eta_Lab)*WUp_pt_Lab - cosh(Z_eta_Lab)*Z_pt_Lab))*WUp_eta_Lab  + (abs(cosh(WDn_eta_Lab)*WDn_pt_Lab - cosh(Z_eta_Lab)*Z_pt_Lab) >= abs(cosh(WUp_eta_Lab)*WUp_pt_Lab - cosh(Z_eta_Lab)*Z_pt_Lab))*WDn_eta_Lab)", "#eta(Z)":"Z_eta_Lab", "#phi(W)":"WDn_phi_Lab","#phi(Z)":"Z_phi_Lab", "p_{T}(W)":"WDn_pt_Lab", "p_{T}(Z)":"Z_pt_Lab","#eta^{MaxPt}(W)":"((abs(cosh(WDn_eta_Lab)*WDn_pt_Lab) < abs(cosh(WUp_eta_Lab)*WUp_pt_Lab))*WUp_eta_Lab  + (abs(cosh(WDn_eta_Lab)*WDn_pt_Lab) >= abs(cosh(WUp_eta_Lab)*WUp_pt_Lab))*WDn_eta_Lab)","#eta^{MinPt}(W)":"((abs(cosh(WDn_eta_Lab)*WDn_pt_Lab) > abs(cosh(WUp_eta_Lab)*WUp_pt_Lab))*WUp_eta_Lab  + (abs(cosh(WDn_eta_Lab)*WDn_pt_Lab) <= abs(cosh(WUp_eta_Lab)*WUp_pt_Lab))*WDn_eta_Lab)"  , "#theta^{W}_{Up}":"ThetaWUp_HE", "#theta^{W}_{Dn}":"ThetaWDn_HE", "#theta^{Z}":"ThetaZDn_HE"}

inF = ROOT.TFile(inputs[0],"READ")
inT = inF.Get("sf/t")
innF = []
innT = []
for f in inputs[1:]:
  innF.append(ROOT.TFile(f,"READ"))
  innT.append(innF[-1].Get("sf/t"))
  inT.AddFriend(innT[-1])
i = 0
for k in variables.keys():
    if "eta" in k:
       gen = "_eta_Lab"
       target = "20,-4.,4."
    if "phi" in k:
       gen = "_phi_Lab"
       target = "20,-3.15,3.15"
    if "p_{T}" in k:
       gen = "_pt_Lab"
       target = "20,0.,200."
    if "W" in k:
       gen = "genWDn"+ gen
    if "Z" in k and not("Rec" in k):
       gen = "genZ"+ gen
    if "theta" in k and "W" in k: 
       gen = "genThetaWDn_HE"
       target = "20,0.,3.15"
    if "theta" in k and "Z" in k:
       gen = "genThetaZDn_HE"
       target = "20,0.,3.15"

    print k, variables[k]
    short = k.replace("#","_").replace("{","_").replace("}","_").replace("(","_").replace(")","_").replace("^","_")
    inT.Draw("%s : %s >> %s(%s, %s)"%(variables[k], gen, short, target,target), "cos_genThetaWDn_HE > -1 && cos_ThetaZDn_HE > -1 && LepZ1_pt >= 25 && LepZ2_pt >= 10 && LepW_pt >= 25","textcolz")
    c = ROOT.TCanvas("c", "test", 800,600)
    c.SetTickx(1)
    c.SetTicky(1)
    c.SetRightMargin (0.14)
    c.SetTopMargin   (0.08)
    c.SetLeftMargin  (0.14)
    c.SetBottomMargin(0.14)   
    theH2 = ROOT.gDirectory.Get(short)
    theH2.GetYaxis().SetTitle(k)
    theH2.SetTitle("")
    theH2.GetXaxis().SetTitle("Gen " + k)
    theH2.Draw("textcolz")
    theL = ROOT.TLegend(0.75, 0.9,1.0,1.0)
    theL.SetTextSize(0.05)
    theL.AddEntry(0, "r-val: %1.3f"%theH2.GetCorrelationFactor(), "")
    theL.Draw("same")
    c.SaveAs(short + ".pdf")
    c.SaveAs(short + ".png")
