import ROOT
import os
import copy
import array

central  = "/nfs/fanae/user/carlosec/www/EWKino/LEE/3lA16_central/plots_wz.root"
varsTemp = "/nfs/fanae/user/carlosec/www/EWKino/LEE/3lA16_weight[W]/plots_wz.root" 
outDatasets = "2016_dataobs.root"
outFile = ROOT.TFile(outDatasets,"RECREATE")
eVar = array.array('d',[0])
centH = {}
weiH  = {}
tempH = {}
processes = ["prompt_ZZ",
"prompt_WZ",	
"prompt_ggZZ",	
"prompt_hZZ",	
"data_fakes",	
"prompt_TZQ",	
"convs",
"prompt_VH",
"prompt_TTX",
"prompt_VVV"
]
masses = [6, 7, 8, 10, 14, 15, 16, 20, 30, 40,  50,  60, 70,  80,  90,  100,  110, 120,  125, 130,  140,  150, 175,  200, 225, 250, 275, 300, 325, 350, 375,  400,  425, 450,  475, 500, 525, 550, 575, 600, 625,  650,  675, 700, 725, 750, 775, 800, 825, 850, 875, 900, 925, 950, 975, 1000]

template = "susyMVA_dM[M]_[P]"

def extract_histos(fil, m, ref=False, w=0, addHisto=False):
  toAdd = False
  tempInFile = ROOT.TFile(fil.replace("[W]",str(w)), "OPEN")
  if addHisto:
    tempAddFile = ROOT.TFile(central.replace("[W]",str(w)), "OPEN") 
    toAdd = tempAddFile.Get(addHisto.replace("[W]",str(w)).replace("[M]",m))
    #toAdd.Print("all")
  for p in processes:
    hName = template.replace("[M]", m).replace("[P]", p)
    if ref==False:
      centH[p] = copy.copy(tempInFile.Get(hName))
      integ = centH[p].IntegralAndError(0,centH[p].GetNbinsX()+1,eVar)
      weiH[p] = eVar[0]**2/integ
    else:
      tempH[p] = copy.copy(tempInFile.Get(hName))
      for i in range(1, tempH[p].GetNbinsX()+1):
        tempH[p].SetBinContent(i, 1./(weiH[p])**0.5*(tempH[p].GetBinContent(i)-centH[p].GetBinContent(i)) +centH[p].GetBinContent(i))
  if ref==False:
    data_obs = centH["prompt_WZ"].Clone("data_obs")
    data_obs.SetName("data_obs_central_dM"+m)
    for p in centH.keys():
      if p == "prompt_WZ": continue
      data_obs = data_obs + centH[p]
    for i in range(1,data_obs.GetNbinsX()+1):
      data_obs.SetBinContent(i, max(0.,data_obs.GetBinContent(i)))
      data_obs.SetBinError(i, data_obs.GetBinContent(i)**0.5)
      #print data_obs.GetBinContent(i)
    outFile.cd()
    data_obs.Write()
  else:
    if toAdd:
      extra = "_" + "_".join(s.split("_")[-2:])
    else:
      extra = ""
    data_obs = tempH["prompt_WZ"].Clone("data_obs"+extra)
    data_obs.SetName("data_obs_weight" + str(w) + "_dM"+m + extra)
    for p in centH.keys():
      if p == "prompt_WZ": continue
      data_obs = data_obs + tempH[p]
    if toAdd:
      #print "BEFORE"
      #data_obs.Print("all")
      data_obs = data_obs + toAdd
      #print "AFTER"
      #data_obs.Print("all")

    for i in range(1,data_obs.GetNbinsX()+1):
      data_obs.SetBinContent(i, max(0.,data_obs.GetBinContent(i)))
      data_obs.SetBinError(i, data_obs.GetBinContent(i)**0.5)
      #print data_obs.GetBinContent(i)
    outFile.cd()
    data_obs.Write()
  #print data_obs.GetBinContent(data_obs.GetNbinsX())

for m in masses:
  print "Mass: %i"%m
  extract_histos(central, str(m), False)
  for i in range(100):
    extract_histos(varsTemp, str(m), True,i)

signalInjections = ["susyMVA_dM[M]_sig_TChiWZ_225_135","susyMVA_dM[M]_sig_TChiWZ_400_300", "susyMVA_dM1000_sig_TChiWZ_500_1"]
for s in signalInjections:
  for m in masses:
    print "Signal: %s, Mass: %i"%("_".join(s.split("_")[-2:]),m)
    extract_histos(central, str(m), False)
    for i in range(100):
      extract_histos(varsTemp, str(m), True,i,s)
