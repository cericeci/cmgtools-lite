import ROOT
import copy

ROOT.gROOT.SetBatch(True)
ROOT.gStyle.SetOptStat(0)


inFileFriend = ROOT.TFile("/pool/ciencias/HeppyTrees/RA7/nanoAODv5_2016_skimWZ/leptonBuilderWZSM/evVarFriend_WZTo3LNu_pow.root","READ")
ftree = inFileFriend.Get("sf/t")
inFileFriend2 = ROOT.TFile("/pool/ciencias/HeppyTrees/RA7/nanoAODv5_2016_skimWZ/bosonPolarization/evVarFriend_WZTo3LNu_pow.root","READ")
ftree2 = inFileFriend2.Get("sf/t")

inFile = ROOT.TFile("/pool/ciencias/HeppyTrees/RA7/nanoAODv5_2016_skimWZ/WZTo3LNu_pow/treeProducerSusyMultilepton/tree.root","READ")
tree = inFile.Get("Events")

baseCut = "nOSSF_3l >= 1 && WZDn_pt_Lab > [MINCUT] && WZDn_pt_Lab < [MAXCUT]"
theCuts = [[0,50],[50,100],[100,200],[200,100000]]

tevtList = []
theTrees = []
colors = [ROOT.kRed, ROOT.kBlue, ROOT.kBlack, ROOT.kGreen]
labels = ["0 < p_{T,WZ} < 50 GeV","50 < p_{T,WZ} < 100 GeV","100 < p_{T,WZ} < 200 GeV","200 GeV< p_{T,WZ}"]
i = 0

print "Computing event lists..."
for cuts in theCuts:
  print i, len(theCuts)
  #tree.Draw('>>elist'+ str(i), baseCut.replace("[MINCUT]",str(cuts[0])).replace("[MAXCUT]",str(cuts[1])), 'entrylist', tree.GetEntries(), 0)
  #tevtList.append(ROOT.gDirectory.Get('elist'+str(i)))
  theTrees.append(tree.Clone("tree"+str(i)))
  theTrees[-1].AddFriend(ftree)
  theTrees[-1].AddFriend(ftree2)
  theTrees[-1].Draw('>>elist'+ str(i), baseCut.replace("[MINCUT]",str(cuts[0])).replace("[MAXCUT]",str(cuts[1])), 'entrylist', tree.GetEntries(), 0)
  tevtList.append(ROOT.gDirectory.Get('elist'+str(i)))
  theTrees[-1].SetEntryList(tevtList[-1])
  i += 1

print tevtList, theTrees
print "Getting branch names..."
branches = [i.GetName() for i in tree.GetListOfBranches()] + [i.GetName() for i in ftree.GetListOfBranches()] + [i.GetName() for i in ftree2.GetListOfBranches()]

print "Now start the plotting..."

for branch in branches:
  h = []
  print branch
  c1 = ROOT.TCanvas("c1","c1",800,600)
  c1.Divide(1,2)
  c1.cd(1)
  c1.GetPad(1).SetPad(.005, .2525, .995, .995)
  for i, tt in enumerate(theTrees):
    if i==0:
      tt.Draw(branch + ">>h_%s_%s"%(branch,i),"","")
      h.append(ROOT.gDirectory.Get("h_%s_%s"%(branch,i)))
      #h[-1].GetYaxis().SetRangeUser(0.,1.)
      h[-1].GetXaxis().SetTitle(branch)
      h[-1].SetLineColor(colors[i])
      tl = ROOT.TLegend(0.6,0.5,0.8,0.8)
      tl.AddEntry(h[-1],labels[i], 'l')

    else:
      tt.Draw(branch + ">>h_%s_%s"%(branch,i),"","same")
      h.append(ROOT.gDirectory.Get("h_%s_%s"%(branch,i)))
      h[-1].SetLineColor(colors[i])
      tl.AddEntry(h[-1],labels[i], 'l')
  theMax = max([hh.GetMaximum() for hh in h])
  for hh in h:
    hh.GetYaxis().SetRangeUser(0., theMax*1.1)
  tl.Draw("same")
  c1.cd(2)
  c1.GetPad(2).SetPad(.005, .0005, .995, .2525) 
  hTotal = h[0].Clone()
  for i in h[1:]:
    hTotal.Add(i)
  qH = []
  for i in h:
    qH.append(i.Clone())
    qH[-1].Divide(hTotal)
    qH[-1].GetYaxis().SetTitle("X/Total")
    qH[-1].GetYaxis().SetRangeUser(0.,1.)
    qH[-1].Draw("same")
  c1.SaveAs("/nfs/fanae/user/carlosec/www/plotsWZpt/%s.pdf"%branch)
  c1.SaveAs("/nfs/fanae/user/carlosec/www/plotsWZpt/%s.eps"%branch)
  c1.SaveAs("/nfs/fanae/user/carlosec/www/plotsWZpt/%s.png"%branch)
 
inFile.Close()
inFileFriend.Close()
