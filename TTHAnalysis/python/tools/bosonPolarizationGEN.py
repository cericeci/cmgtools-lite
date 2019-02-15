from CMGTools.TTHAnalysis.treeReAnalyzer import *
import ROOT, copy, os
import array, math


## bosonPolarizationWZGEN
## ___________________________________________________________________
class bosonPolarizationGEN:


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
        if getattr(event, "ngenLep") < 3 or getattr(event, "nOSSF_3l_gen") < 1 or getattr(event, "genLepZ1_pt") < 0.01 or getattr(event, "genLepZ2_pt") < 0.01 or getattr(event, "genLepW_pt") < 0.01: return self.ret
        #print getattr(event, "ngenLep"), getattr(event, "nOSSF_3l_gen")
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
        self.ret["genThetaWUp_HE"] = (self.LorToWUp*self.pl3).Theta()
        self.ret["genThetaWDn_HE"] = (self.LorToWDn*self.pl3).Theta()
        self.ret["genThetaZUp_HE"] = (self.LorToZ*self.lepforZ).Theta()
        self.ret["genThetaZDn_HE"] = (self.LorToZ*self.lepforZ).Theta() #Not a bug, there is just one solution in this case
        self.ret["cos_genThetaWDn_HE"] = math.cos((self.LorToWUp*self.pl3).Theta())*self.charge
        self.ret["cos_genThetaZDn_HE"] = math.cos((self.LorToWUp*self.pl3).Theta())
        #Now get the other interesting angles
        self.ret["genThetaWUp_HE_CM"] = (self.LorToWUp_CM*self.pl3).Theta()
        self.ret["genThetaWDn_HE_CM"] = (self.LorToWDn_CM*self.pl3).Theta()
        self.ret["genThetaZUp_HE_CM"] = (self.LorToZUp_CM*self.lepforZ).Theta()
        self.ret["genThetaZDn_HE_CM"] = (self.LorToZDn_CM*self.lepforZ).Theta() #In this case they are different
        #print "________________________________________________________"
        #print " EVENT DONE "
        #print "________________________________________________________"
    ## collectObjects
    ## _______________________________________________________________
    def collectObjects(self, event):
        self.pl1.SetPtEtaPhiM(getattr(event, "genLepZ1_pt"), getattr(event, "genLepZ1_eta"),getattr(event, "genLepZ1_phi"), getattr(event, "genLepZ1_mass"))
        self.pl2.SetPtEtaPhiM(getattr(event, "genLepZ2_pt"), getattr(event, "genLepZ2_eta"),getattr(event, "genLepZ2_phi"), getattr(event, "genLepZ2_mass"))
        if getattr(event, "genLepZ1_pdgId") > 0:
            self.lepforZ = self.pl1
        else:
            self.lepforZ = self.pl2
        self.charge = (getattr(event, "genLepW_pdgId") < 0)*2 - 1
        self.pl3.SetPtEtaPhiM(getattr(event, "genLepW_pt") , getattr(event, "genLepW_eta") ,getattr(event, "genLepW_phi") , getattr(event, "genLepW_mass") )
        self.met.SetPtEtaPhiM(getattr(event, "met_genPt")  , 0                             ,getattr(event, "met_genPhi")                           , 0     )
        self.metUp.SetPtEtaPhiM(getattr(event, "met_genPt")  , 0                             ,getattr(event, "met_genPhi")                           , 0     )
        self.metDn.SetPtEtaPhiM(getattr(event, "met_genPt")  , 0                             ,getattr(event, "met_genPhi")                           , 0     )
       
        
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
        #print "MUVAL!", ptl
        disc  = (muVal**2*ptl**2*sinh(etal)**2/ptl**4 - ((ptl**2*cosh(etal)**2)*ptnu**2 - muVal**2)/ptl**2)        
        #print disc
        if disc < 0:
             #print "IMAGINARY!!!"
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
            ("genThetaWUp_HE"               , "F"),
            ("genThetaWDn_HE"               , "F"),
            ("genThetaZUp_HE"               , "F"),
            ("genThetaZDn_HE"               , "F"),
            ("genThetaWUp_HE_CM"            , "F"),
            ("genThetaWDn_HE_CM"            , "F"),
            ("genThetaZUp_HE_CM"            , "F"),
            ("genThetaZDn_HE_CM"            , "F"),
            ("cos_genThetaWDn_HE"           , "F"),
            ("cos_genThetaZDn_HE"           , "F")]

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
            self.sf1 = bosonPolarizationGEN()
        def analyze(self,ev):
            #print "\nrun %6d lumi %4d event %d: leps %d" % (ev.run, ev.lumi, ev.evt, ev.nLepGood)
            self.sf1(ev)
    el = EventLoop([ Tester("tester") ])
    el.loop([tree], maxEvents = 20)

