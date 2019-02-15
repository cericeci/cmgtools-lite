from CMGTools.TTHAnalysis.treeReAnalyzer import *
import ROOT 

class JetPhotonPrefiring: 
    def __init__(self):
        self.branches = ["is_Prefiring_central","is_Prefiring", "weight_Prefiring"]
        fJets = ROOT.TFile("/nfs/fanae/user/carlosec/EWKino/CMSSW_9_4_4/src/CMGTools/TTHAnalysis/data/jetPref/L1prefiring_jet_2017BtoF.root")
        self.mapJets = fJets.Get("L1prefiring_jet_2017BtoF")

    def listBranches(self):
        return self.branches[:]

    def __call__(self,event):
        self.allret = {}
        self.allret["is_Prefiring_central"] = 0
        self.allret["is_Prefiring"] = 0
        self.allret["weight_Prefiring"] = 1.
        self.jets      = [j             for j  in Collection(event, "Jet", "nJet")  ]
        self.photons   = []#p             for p  in Collection(event, "PhoGood", "nPhoGood")] For future use
        self.catchFire()
        self.weightFire()
        return self.allret

    def catchFire(self):
        self.problematicJets = []
        self.problematicPhotons = []
        for j in self.jets:
            if j.pt > 40 and abs(j.eta) < 3.25 and abs(j.eta) > 2.0:
                self.problematicJets.append(j)
            if j.pt > 100 and abs(j.eta) < 3.0 and abs(j.eta) > 2.5:
                self.allret["is_Prefiring_central"] = 1
        #for p in self.photons:
        #    if p.pt > 20 and abs(p.eta) < 3.25 and abs(p.eta) > 2.0:
        #        self.problematicPhotons.append(p)
        #    if p.pt > 50 and abs(p.eta) < 3.0 and abs(p.eta) > 2.5:
        #        self.allret["is_Prefiring_central"] = 1
        if len(self.problematicJets + self.problematicPhotons) > 0: 
                self.allret["is_Prefiring"] = 1
                  

    def weightFire(self):
        for j in (self.problematicJets + self.problematicPhotons):
                self.allret["weight_Prefiring"] *= (1- self.mapJets.GetBinContent(self.mapJets.FindBin(j.eta, j.pt)))


