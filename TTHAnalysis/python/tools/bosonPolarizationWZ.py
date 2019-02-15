from CMGTools.TTHAnalysis.treeReAnalyzer import *
import ROOT, copy, os
import array, math


## bosonPolarizationWZ
## ___________________________________________________________________
class bosonPolarizationWZ:


    ## __init__
    ## _______________________________________________________________
    def __init__(self):
        self.pl1 = ROOT.TLorentzVector()
        self.pl2 = ROOT.TLorentzVector()
        self.pl3 = ROOT.TLorentzVector()
        self.met = ROOT.TLorentzVector()
        self.metUp = ROOT.TLorentzVector()
        self.metDn = ROOT.TLorentzVector()

    ## __call__
    ## _______________________________________________________________
    def __call__(self, event):
        self.resetMemory()
        if getattr(event, "nLepSel") < 3 or getattr(event, "nOSSF_3l") < 1: return self.ret
        self.collectObjects(event)
        self.analyzeTopology()
        return self.ret


    ## analyzeTopology
    ## _______________________________________________________________
    def analyzeTopology(self):
        #Fill up the ret
        self.getNeuEta()
        self.buildBosonP_Lab()
        #Lorentz's transformation from LAB, i.e. as in Helicity frame in https://arxiv.org/pdf/1810.11034.pdf
        self.LorToWUp = self.getPartRestFrameLor( self.pWUp)
        self.LorToWDn = self.getPartRestFrameLor( self.pWDn)
        self.LorToZ   = self.getPartRestFrameLor( self.pZ  )
        #Lorentz's transformation from LAB to WZ system, i.e. as in ATLAS-CONF-18-034
        self.LorToWZUp   = self.getPartRestFrameLor(self.pWZUp)
        self.LorToWUp_CM = self.LorToWZUp*self.getPartRestFrameLor(self.LorToWZUp*self.pWUp)
        self.LorToZUp_CM = self.LorToWZUp*self.getPartRestFrameLor(self.LorToWZUp*self.pZ)
        self.LorToWZDn   = self.getPartRestFrameLor(self.pWZDn)
        self.LorToWDn_CM = self.LorToWZUp*self.getPartRestFrameLor(self.LorToWZDn*self.pWDn)
        self.LorToZDn_CM = self.LorToWZUp*self.getPartRestFrameLor(self.LorToWZDn*self.pZ)
        #Now get the interesting angles
        self.ret["ThetaWUp_HE"] = (self.LorToWUp*self.pl3).Theta()
        self.ret["ThetaWDn_HE"] = (self.LorToWDn*self.pl3).Theta()
        self.ret["ThetaZUp_HE"] = (self.LorToZ*self.lepforZ).Theta()
        self.ret["ThetaZDn_HE"] = (self.LorToZ*self.lepforZ).Theta() #Not a bug, there is just one solution in this case
        self.ret["cos_ThetaWDn_HE"] = math.cos((self.LorToWUp*self.pl3).Theta())*self.charge
        self.ret["cos_ThetaZDn_HE"] = math.cos((self.LorToWUp*self.pl3).Theta())
        #Now get the other interesting angles
        self.ret["ThetaWUp_HE_CM"] = (self.LorToWUp_CM*self.pl3).Theta()
        self.ret["ThetaWDn_HE_CM"] = (self.LorToWDn_CM*self.pl3).Theta()
        self.ret["ThetaZUp_HE_CM"] = (self.LorToZUp_CM*self.lepforZ).Theta()
        self.ret["ThetaZDn_HE_CM"] = (self.LorToZDn_CM*self.lepforZ).Theta() #In this case they are different


        #print "________________________________________________________"
        #print " EVENT DONE "
        #print "________________________________________________________"
    ## collectObjects
    ## _______________________________________________________________
    def collectObjects(self, event):
        self.pl1.SetPtEtaPhiM(getattr(event, "LepZ1_pt"), getattr(event, "LepZ1_eta"),getattr(event, "LepZ1_phi"), getattr(event, "LepZ1_mass"))
        self.pl2.SetPtEtaPhiM(getattr(event, "LepZ2_pt"), getattr(event, "LepZ2_eta"),getattr(event, "LepZ2_phi"), getattr(event, "LepZ2_mass"))
        if getattr(event, "LepZ1_pdgId") > 0:
            self.lepforZ = self.pl1
        else:
            self.lepforZ = self.pl2
        self.charge = (getattr(event, "LepW_pdgId") < 0)*2 - 1
        self.pl3.SetPtEtaPhiM(getattr(event, "LepW_pt") , getattr(event, "LepW_eta") ,getattr(event, "LepW_phi") , getattr(event, "LepW_mass") )
        self.metUp.SetPtEtaPhiM(getattr(event, "met_pt")  , 0  ,getattr(event, "met_phi")                          , 0                           )
        self.metUp.SetPtEtaPhiM(getattr(event, "met_pt")  , 0  ,getattr(event, "met_phi")                          , 0                           )
        self.metDn.SetPtEtaPhiM(getattr(event, "met_pt")  , 0  ,getattr(event, "met_phi")                          , 0                           )
       
        
    def getNeuEta(self):
        #Solve for W mass
        phil = self.pl3.Phi()
        etal = self.pl3.Eta()
        ptl = self.pl3.Pt()
        phinu = self.met.Phi()
        etanuUp = 0
        etanuDn = 0
        ptnu  = self.met.Pt()
        muVal = (80.385)**2/2. + ptl*ptnu*cos(phil-phinu)
        disc  = (muVal**2*ptl**2*sinh(etal)**2/ptl**4 - ((ptl**2*cosh(etal)**2)*ptnu**2 - muVal**2)/ptl**2)        
        #print disc
        if disc < 0:
             print "IMAGINARY!!!"
             self.metUp.SetXYZM(ptnu*cos(phinu), ptnu*sin(phinu),muVal*ptl*sinh(etal)/ptl**2,0)
             self.metDn.SetXYZM(ptnu*cos(phinu), ptnu*sin(phinu),muVal*ptl*sinh(etal)/ptl**2,0)
        else:
             self.metUp.SetXYZM(ptnu*cos(phinu), ptnu*sin(phinu),muVal*ptl*sinh(etal)/ptl**2 + sqrt(disc),0)
             self.metDn.SetXYZM(ptnu*cos(phinu), ptnu*sin(phinu),muVal*ptl*sinh(etal)/ptl**2 - sqrt(disc),0)

    def buildBosonP_Lab(self):
        self.pZ = self.pl1 + self.pl2
        self.pWUp = self.pl3 + self.metUp
        self.pWDn = self.pl3 + self.metDn
        self.pWZUp = self.pZ + self.pWUp
        self.pWZDn = self.pZ + self.pWDn
        for part in ["Z", "WUp", "WDn", "WZUp", "WZDn"]:
            self.ret[part+"_pt_Lab"] = getattr(self, "p" + part).Pt()
            self.ret[part+"_eta_Lab"] = getattr(self, "p" + part).Eta()
            self.ret[part+"_phi_Lab"] = getattr(self, "p" + part).Phi()
            self.ret[part+"_mass_Lab"] = getattr(self, "p" + part).M()
    
    def getPartRestFrameLor(self, p4): #Gets Lorentz Transformation from lab frame to W boson rest frame with the Z axis aligned to the W boson pT direction in the lab frame
        #First the rotation
        rot    = ROOT.TRotation()
        rot.SetZAxis(p4.Vect())        
        rotLor = ROOT.TLorentzRotation(rot)
        p4p    = rotLor.Inverse()*p4
        #print "P4P", p4p.X(), p4p.Y(), p4p.Z(), p4p.T()
        #Then the boost
        boost  = p4p.BoostVector()
        rotboost = ROOT.TLorentzRotation(boost)  
        p4pp   = rotboost.Inverse() * p4p
        #print "P4PP", p4pp.X(), p4pp.Y(), p4pp.Z(), p4pp.T()
        #print "NEXT=================\n\n"
        return rotboost.Inverse()*rotLor.Inverse()

      
    ## listBranches
    ## _______________________________________________________________
    def listBranches(self):

        biglist = [
            ("ThetaWUp_HE"               , "F"),
            ("ThetaWDn_HE"               , "F"),
            ("ThetaZUp_HE"               , "F"),
            ("ThetaZDn_HE"               , "F"),
            ("ThetaWUp_HE_CM"            , "F"),
            ("ThetaWDn_HE_CM"            , "F"),
            ("ThetaZUp_HE_CM"            , "F"),
            ("ThetaZDn_HE_CM"            , "F"),
            ("cos_ThetaWDn_HE"           , "F"),
            ("cos_ThetaZDn_HE"           , "F")]
        for part in ["Z", "WUp", "WDn", "WZUp", "WZDn"]:
            for var in ["pt", "eta", "phi", "mass"]:
                biglist.append((part+"_" + var +"_Lab", "F"))
        return biglist



    ## resetMemory
    ## _______________________________________________________________
    def resetMemory(self):
        self.pl1.SetPtEtaPhiM(0,0,0,0)
        self.pl2.SetPtEtaPhiM(0,0,0,0)
        self.pl3.SetPtEtaPhiM(0,0,0,0)
        self.met.SetPtEtaPhiM(0,0,0,0)

        self.ret = {};
        #Set everything to 0
        for l in self.listBranches():
            self.ret[l[0]] = -99

if __name__ == '__main__':
    from sys import argv
    file = ROOT.TFile(argv[1])
    tree = file.Get("tree")
    tree.AddFriend("sf/t",argv[2]) # recleaner
    tree.vectorTree = True
    class Tester(Module):
        def __init__(self, name):
            Module.__init__(self,name,None)
            self.sf1 = bosonPolarizationWZ()
        def analyze(self,ev):
            #print "\nrun %6d lumi %4d event %d: leps %d" % (ev.run, ev.lumi, ev.evt, ev.nLepGood)
            self.sf1(ev)
    el = EventLoop([ Tester("tester") ])
    el.loop([tree], maxEvents = 20)

