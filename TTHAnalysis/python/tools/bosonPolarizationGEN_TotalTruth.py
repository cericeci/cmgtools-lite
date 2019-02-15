from CMGTools.TTHAnalysis.treeReAnalyzer import *
import ROOT, copy, os
import array, math


## bosonPolarizationWZGEN
## ___________________________________________________________________
class bosonPolarizationGEN_TotalTruth:


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
        if getattr(event, "ngenLep") < 3 or getattr(event, "nOSSF_3l_gen") < 1 or getattr(event, "genLepZ1_pt") < 0.001 or getattr(event, "genLepZ2_pt") < 0.001 or getattr(event, "genLepW_pt") < 0.001: 
            self.ret["status"] = 0
            return self.ret
        self.defineLeptons(event)
        if not(len(self.iZleps) == 2 and len(self.iWleps) == 1):
            if len(self.iZleps) < 2: self.ret["status"] = 1
            elif len(self.iWleps) < 1: self.ret["status"] = 2
            elif len(self.iZleps) > 2: self.ret["status"] = 3 
            elif len(self.iWleps) > 1: self.ret["status"] = 4
            return self.ret
        self.ret["status"] = -1
        self.collectObjects(event)
        self.analyzeTopology()
        return self.ret


    ## analyzeTopology
    ## _______________________________________________________________
    def analyzeTopology(self):
        #Fill up the ret
        self.getNeuEta()
        #Lorentz's transformation from LAB, i.e. as in Helicity frame in https://arxiv.org/pdf/1810.11034.pdf
        self.LorToWUp = self.getPartRestFrameLor( self.pWUp)
        self.LorToWDn = self.getPartRestFrameLor( self.pWDn)
        self.LorToZ   = self.getPartRestFrameLor( self.pZ  )
        #Lorentz's transformation from LAB to WZ system, i.e. as in ATLAS-CONF-18-034
        self.LorToWZUp   = self.getPartRestFrameLor(self.pWZUp)
        self.LorToWUp_CM = self.getPartRestFrameLor(self.LorToWZUp*self.pWUp)*self.LorToWZUp
        self.LorToZUp_CM = self.getPartRestFrameLor(self.LorToWZUp*self.pZ)*self.LorToWZUp
        self.LorToWZDn   = self.getPartRestFrameLor(self.pWZDn)
        self.LorToWDn_CM = self.getPartRestFrameLor(self.LorToWZDn*self.pWDn)*self.LorToWZDn
        self.LorToZDn_CM = self.getPartRestFrameLor(self.LorToWZDn*self.pZ)*self.LorToWZDn
        #Now get the interesting angles
        self.ret["genThetaWUp_HE"] = (self.LorToWUp*self.pl3).Theta()
        self.ret["genThetaWDn_HE"] = (self.LorToWDn*self.pl3).Theta()
        self.ret["genThetaZUp_HE"] = (self.LorToZ*self.lepforZ).Theta()
        self.ret["genThetaZDn_HE"] = (self.LorToZ*self.lepforZ).Theta() #Not a bug, there is just one solution in this case
        self.ret["cos_genThetaWDn_HE"] = math.cos((self.LorToWDn*self.pl3).Theta())*self.charge
        self.ret["cos_genThetaZDn_HE"] = math.cos((self.LorToZ*self.lepforZ).Theta())
        #Now get the other interesting angles
        self.ret["genThetaWUp_HE_CM"] = (self.LorToWUp_CM*self.pl3).Theta()
        self.ret["genThetaWDn_HE_CM"] = (self.LorToWDn_CM*self.pl3).Theta()
        self.ret["genThetaZUp_HE_CM"] = (self.LorToZUp_CM*self.lepforZ).Theta()
        self.ret["genThetaZDn_HE_CM"] = (self.LorToZDn_CM*self.lepforZ).Theta() #In this case they are different

        #Now the CS frame angles
        self.LorToRotX = self.getRotatedFrame(self.pWUp, 1) #First rotate so the W pT is along the X axis
        tempP = (self.LorToRotX*self.pWUp).Clone()
        self.LorToRotWXRest = ROOT.TLorentzRotation()
        self.LorToRotWXRest.Boost(0, 0 , tempP.BoostVector().Z())
        self.LorToRotWXRest = self.LorToRotWXRest.Inverse()

        self.LorToRotWXZRest = ROOT.TLorentzRotation()
        tempP = (self.LorToRotWXRest*self.LorToRotX*self.pWUp).Clone()
        self.LorToRotWXZRest.Boost(tempP.BoostVector().X(),0,0)
        self.LorToRotWXZRest = self.LorToRotWXZRest.Inverse()

        #Collins-Soper Magic thingies
        self.pl3rot = self.LorToRotX*self.pl3
        self.metrot = self.LorToRotX*self.metUp

        #pexCS = 80.385*(self.pl3rot.X()- self.metrot.X())/(2*sqrt(80.385*80.385 + self.pWUp.Pt() * self.pWUp.Pt()))
        #pexAlt = ( self.pl3rot.X()*self.pWUp.E()*self.pWUp.E() - self.pWUp.X()*self.pWUp.E()*self.pl3rot.E() - self.pl3rot.X()*self.pWUp.Z()*self.pWUp.Z() + self.pl3rot.Z()*self.pWUp.Z()*self.pWUp.X() ) / (80.385*sqrt(self.pWUp.E()*self.pWUp.E() - self.pWUp.Z()*self.pWUp.Z()))
        #peyCS = self.pl3rot.Y()
        self.pl3CS = self.LorToRotWXZRest*self.LorToRotWXRest*self.LorToRotX*self.pl3
        self.metCS = self.LorToRotWXZRest*self.LorToRotWXRest*self.LorToRotX*self.metUp

        self.ret["mW_genrec"] = self.pWUp.M()
        self.ret["cos_genThetaWDn_CS"] = self.charge*sqrt(1- min(4*self.pl3CS.Pt()**2/( self.pWUp.M()**2),1))
        
        #print pexCS, pexAlt, self.pl3CS.X()
        #print sqrt(pexCS**2 + peyCS**2)*2/80.385, sqrt(pexAlt**2 + peyCS**2)*2/80.385 , sqrt(self.pl3CS.X()**2 + self.pl3CS.Y()**2)*2/80.385
        #if sqrt(self.pl3CS.X()**2 + self.pl3CS.Y()**2)*2/80.385 > 1: print sqrt(self.pl3CS.X()**2 + self.pl3CS.Y()**2)*2/80.385 #, sqrt(self.metCS.X()**2 + self.metCS.Y()**2)*2/80.385, sqrt(self.pl3CS.X()**2 + self.pl3CS.Y()**2)*2/80.385 + sqrt(self.metCS.X()**2 + self.metCS.Y()**2)*2/80.385
        #print self.pl3CS.E()/self.pWUp.M(), self.pWUp.M()
        #pezCS = (self.pl3rot.X()*self.pWUp.E() - self.pl3rot.E()* self.pWUp.Z() )/sqrt(self.pWUp.E()**2 - self.pWUp.Z()**2)
        #print sqrt(pexCS**2 + peyCS**2+ pezCS**2), self.pWUp.M()
        #self.ret["cos_genThetaWUp_CS"] = self.charge*sqrt(1- 4*(pexCS**2 + peyCS**2)/ 80.385**2) 
        #self.ret["cos_genThetaWDn_CS"] = -self.charge*sqrt(1- 4*(pexCS**2 + peyCS**2)/ 80.385**2)
        #print self.ret["cos_genThetaWUp_CS"], self.ret["cos_genThetaWDn_CS"]
        #print "________________________________________________________"
        #print " EVENT DONE "
        #print "________________________________________________________"

    def defineLeptons(self,event):
        self.genleps = [t             for t  in Collection(event, "genLep" , "ngenLep" )]
        self.iZleps = []
        self.iWleps = []
        #Only direct decays
        for i in range(len(self.genleps)):
            if getattr(self.genleps[i], "motherId") == 23:
                self.iZleps.append(i)
            elif abs(getattr(self.genleps[i], "motherId")) == 24:
                self.iWleps.append(i)

    ## collectObjects
    ## _______________________________________________________________
    def collectObjects(self, event):
        self.pl1.SetPtEtaPhiM(getattr(self.genleps[self.iZleps[0]], "pt"), getattr(self.genleps[self.iZleps[0]], "eta"),getattr(self.genleps[self.iZleps[0]], "phi"), getattr(self.genleps[self.iZleps[0]], "mass"))
        self.pl2.SetPtEtaPhiM(getattr(self.genleps[self.iZleps[1]], "pt"), getattr(self.genleps[self.iZleps[1]], "eta"),getattr(self.genleps[self.iZleps[1]], "phi"), getattr(self.genleps[self.iZleps[1]], "mass"))
        if getattr(self.genleps[self.iZleps[0]], "pdgId") > 0:
            self.lepforZ = self.pl1
        else:
            self.lepforZ = self.pl2
        self.charge = (getattr(self.genleps[self.iWleps[0]], "pdgId") < 0)*2 - 1
        self.pl3.SetPtEtaPhiM(getattr(self.genleps[self.iWleps[0]], "pt"), getattr(self.genleps[self.iWleps[0]], "eta"),getattr(self.genleps[self.iWleps[0]], "phi"), getattr(self.genleps[self.iWleps[0]], "mass"))
        self.pWUp = self.pl3.Clone()
        self.pWDn = self.pl3.Clone()
        self.pZ   = self.pl3.Clone()
        genColl = [t             for t  in Collection(event, "GenPart" , "nGenPart" )]
        """for p in genColl:
            if abs(p.pdgId) == 24:
                self.pWUp.SetPtEtaPhiM(p.pt, p.eta, p.phi, 80.385)
                self.pWDn.SetPtEtaPhiM(p.pt, p.eta, p.phi, 80.385)
            if abs(p.pdgId) == 23:
                self.pZ.SetPtEtaPhiM(p.pt, p.eta, p.phi, 91.16)
        """
        self.plneu = self.pl3.Clone()
        for p in genColl:
            if (abs(p.pdgId) - abs(getattr(self.genleps[self.iWleps[0]], "pdgId")) == 1) and abs(p.motherId) == 24: 
                #print "found!"
                self.plneu.SetPtEtaPhiM(getattr(p, "pt"), getattr(p, "eta"),getattr(p, "phi"), getattr(p, "mass")) 
        self.pWUp = self.pl3 + self.plneu
        #print self.pWUp.M()
        self.pWDn = self.pWUp
        self.pZ = self.pl1 + self.pl2
        self.pWZUp = self.pZ + self.pWUp
        self.pWZDn = self.pZ + self.pWDn
        for part in ["Z", "WUp", "WDn", "WZUp", "WZDn"]:
            self.ret[part+"_pt_Lab"] = getattr(self, "p" + part).Pt()
            self.ret[part+"_eta_Lab"] = getattr(self, "p" + part).Eta()
            self.ret[part+"_phi_Lab"] = getattr(self, "p" + part).Phi()
            self.ret[part+"_mass_Lab"] = getattr(self, "p" + part).M()

        self.ret["charge"] = self.charge
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


    
    def getPartRestFrameLor(self, p4): #Gets Lorentz Transformation from lab frame to W boson rest frame with the z axis aligned to the W boson p direction in the lab frame
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

    def getRotatedFrame(self, pW, axis = 1):
        #Take only the transverse
        theRot = ROOT.TRotation()
        if axis == 1: theRot.SetXAxis(ROOT.TVector3(pW.X(), pW.Y(), 0))
        if axis == 2: theRot.SetYAxis(ROOT.TVector3(pW.X(), pW.Y(), 0))
        theRotLor = ROOT.TLorentzRotation(theRot.Inverse())
        #print pW.X(), pW.Y(), pW.Z(), pW.T(), pW.Phi()
        #print (theRotLor*pW).X(), (theRotLor*pW).Y(), (theRotLor*pW).Z(), (theRotLor*pW).T(), (theRotLor*pW).Phi()
        return theRotLor       
      
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
            ("cos_genThetaZDn_HE"           , "F"),
            ("charge", "I"),
            ("status", "I"),
            ("cos_genThetaWDn_CS", "F"),
            ("mW_genrec", "F")]

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
            self.sf1 = bosonPolarizationGEN_TotalTruth()
        def analyze(self,ev):
            #print "\nrun %6d lumi %4d event %d: leps %d" % (ev.run, ev.lumi, ev.evt, ev.nLepGood)
            self.sf1(ev)
    el = EventLoop([ Tester("tester") ])
    el.loop([tree], maxEvents = 10000)

