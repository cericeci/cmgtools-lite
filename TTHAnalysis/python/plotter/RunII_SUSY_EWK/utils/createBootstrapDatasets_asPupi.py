import ROOT
import os
import copy
import array

#central  = "/nfs/fanae/user/carlosec/Combine_SLC7/CMSSW_8_1_0/src/LEE_EWKino_newID/LEE_16toys_[M]/cuts_3l.input.root"
#varsTemp = "/nfs/fanae/user/carlosec/Combine_SLC7/CMSSW_8_1_0/src/LEE_EWKino_newID/LEE_16toys[TAG]_[M]/cuts_3l.input.root"

central = "/nfs/fanae/user/carlosec/CMSSW_10_4_0/src/CMGTools/TTHAnalysis/python/plotter/LEEPFix_v2_toys_set1_dM[M]/cuts_3l.input.root"
varsTemp =  "/nfs/fanae/user/carlosec/CMSSW_10_4_0/src/CMGTools/TTHAnalysis/python/plotter/LEEPFix_v2_toys_[TAG]_dM[M]/cuts_3l.input.root"

tags = {"set1":[1,100]}#, "set1":[101,200], "set2":[201,300], "set3":[301,400], "set4":[401,500], "set5":[501,750], "set6":[751,999]}


signalInjections = []#"x_sig_TChiWZ_200_110","x_sig_TChiWZ_350_1","x_sig_TChiWZ_125_85"]

print signalInjections
outDatasets = "dataobs_newstrat.root"# "2016_dataobs_bootstrap_newscans.root"
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

template = "x_[P][W]"

def extract_histos(fil, m, ref=False, w=0, addHisto=False):
  print "File in:", fil.replace("[W]",str(w)).replace("[M]",m), " for weight ", w 
  toAdd = False
  tempInFile = ROOT.TFile(fil.replace("[W]",str(w)).replace("[M]",m), "OPEN")
  if addHisto:
    #print "Add histo ", addHisto[1].replace("[W]",str(w)).replace("[M]",m) ," in: ",addHisto[0].replace("[W]",str(w)).replace("[M]",m) 
    tempAddFile = ROOT.TFile(addHisto[0].replace("[W]",str(w)).replace("[M]",m), "OPEN") 
    toAdd = tempAddFile.Get(addHisto[1].replace("[W]",str(w)).replace("[M]",m))
    #toAdd.Print("all")
  for p in processes:
    hName = template.replace("[M]", m).replace("[P]", p)
    if w == 0: hName = hName.replace("[W]","")
    else: 
        if "toys_" in fil: hName = hName.replace("[W]","_weights_%iUp"%w)
        else: hName = hName.replace("[W]","_weight_%iUp"%w)
    #print hName
    #print ref, hName, tempInFile
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
    #print "Producing varied weight ", str(w)
  
    #print toAdd
    if toAdd:
      extra = "_" + "_".join(addHisto[1].split("_")[-2:])
    else:
      extra = ""
    data_obs = tempH["prompt_WZ"].Clone("data_obs"+extra+ str(w) + "_dM"+m + extra)
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
  for t in tags:
    for i in range(tags[t][0], tags[t][1]+1):
      extract_histos(varsTemp.replace("[TAG]",t), str(m), True,i)
      break 
    break
  break

print weiH
"""
print "Signal injections", signalInjections 
for s in signalInjections:
  for m in masses:
    print "Signal: %s, Mass: %i"%(s,m)
    extract_histos(central, str(m), False)
    for t in tags:
      for i in range(tags[t][0], tags[t][1]+1):
        extract_histos(varsTemp.replace("[TAG]",t), str(m), True,i,["/nfs/fanae/user/carlosec/Combine_SLC7/CMSSW_8_1_0/src/LEE_EWKino_newID/cards_LEE_[M]/cuts_3l.input.root".replace("[M]",str(m)),s])    
""" 
