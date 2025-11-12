from HiggsAnalysis.CombinedLimit.PhysicsModel import *

class ChargeAsymmetryWZ(PhysicsModelBase):
    "Measure the ratio of W+/W- and total signal strength in WZ"
    def __init__(self):
        PhysicsModelBase.__init__(self)
    def setPhysicsOptions(self,physOptions):
        for po in physOptions:
          print "Setting parameter: ", po
          setattr(self, po.split("=")[0], float(po.split("=")[1]))

    def doParametersOfInterest(self):
        """Create POI out of signal strength and MH"""
        self.modelBuilder.doVar("ratio[1,0,20]")
        self.modelBuilder.doVar("mu[1,0,20]")
        ##  AWZ needs to be set as a Physics Parameter when generating the workspace
        self.modelBuilder.factory_("expr::rplus(\"(1+%1.3f)*@0*@1/(1+%1.3f*@1)\",mu,ratio)"%(self.AWZ,self.AWZ))
        self.modelBuilder.factory_("expr::rminus(\"(1+%1.3f)*@0/(1+%1.3f*@1)\",mu,ratio)"%(self.AWZ,self.AWZ))
        self.modelBuilder.factory_("expr::rtot(\"@0\",mu)")

        poi = "ratio,mu"
        self.modelBuilder.doSet("POI",poi)

    def getYieldScale(self,bin,process):
        "Return the name of a RooAbsReal to scale this yield by or the two special values 1 and 0 (don't scale, and set to zero)"
        if process == "prompt_WZ_plus": return "rplus"
        if process == "prompt_WZ_minus": return "rminus"
        if process == "prompt_WZ": return "rtot"
        else: return 1


class bosonPolarizationWZ(PhysicsModelBase):
    "Measure the pol. parameters fL-fR, fO and total signal strength in WZ"
    def __init__(self):
        PhysicsModelBase.__init__(self)
    def setPhysicsOptions(self,physOptions):
        for po in physOptions:
            print "Setting parameter: ", po
            setattr(self, po.split("=")[0], float(po.split("=")[1]))
            print self,  po.split("=")[0], float(po.split("=")[1])

    def doParametersOfInterest(self):
        """Create POI corresponding to polarization fractions"""
        ##  f0,fL,fR (SM values) need to be set as a Physics Parameter when generating the workspace
        print self.fL, self.fR, self.fO
        self.modelBuilder.doVar("mu[1.,0.,5.]")
        self.modelBuilder.doVar("fLR[%1.3f,-1.,1.]"%(self.fL - self.fR))
        self.modelBuilder.doVar("fO[%1.3f,-1.,1.]"%(self.fO))
        self.modelBuilder.factory_("expr::rfL(\"@0*(1.-@1+@2)/(2.*%1.3f)\",mu,fO,fLR)"%self.fL)
        self.modelBuilder.factory_("expr::rfR(\"@0*(1.-@1-@2)/(2.*%1.3f)\",mu,fO,fLR)"%self.fR)
        self.modelBuilder.factory_("expr::rfO(\"@0*@1/(%1.3f)\",mu,fO)"%self.fO)
        self.modelBuilder.factory_("expr::rOther(\"@0\",mu)")
        poi = "mu,fO,fLR"
        self.modelBuilder.doSet("POI",poi)

    def getYieldScale(self,bin,process):
        "Return the name of a RooAbsReal to scale this yield by or the two special values 1 and 0 (don't scale, and set to zero)"
        if process == "prompt_WZ_WfOther" or process == "prompt_WZ": return "rOther" # Tau contributions/WZ in the CR just scale according to x-sec
        if process == "prompt_WZ_WfL": return "rfL"
        if process == "prompt_WZ_WfR": return "rfR"
        if process == "prompt_WZ_WfO": return "rfO"
        else: return 1

class bosonPolarization2DWZ(PhysicsModelBase):
    "Measure the pol. parameters fOO, fOT, fTO, fTT, and total signal strength in WZ"
    def __init__(self):
        PhysicsModelBase.__init__(self)
    def setPhysicsOptions(self,physOptions):
        for po in physOptions:
            print "Setting parameter: ", po
            setattr(self, po.split("=")[0], float(po.split("=")[1]))
            print self,  po.split("=")[0], float(po.split("=")[1])

    def doParametersOfInterest(self):
        """Create POI corresponding to polarization fractions"""
        ##  f0,fL,fR (SM values) need to be set as a Physics Parameter when generating the workspace
        print self.fOO, self.fOT, self.fTO, self.fTT
        self.modelBuilder.doVar("mu[1.,0.,5.]")
        self.modelBuilder.doVar("fOO[%1.3f,0.,1.]"%(self.fOO))
        self.modelBuilder.doVar("fOTTO[%1.3f,-1.,1.]"%(self.fOT))
        self.modelBuilder.doVar("fTT[%1.3f,0.,1.]"%(self.fTO))
        self.modelBuilder.factory_("expr::rfTT(\"@0*@1/(%1.3f)\",mu,fTT)"%self.fTT)
        self.modelBuilder.factory_("expr::rfOT(\"@0*(1-@1-@2+@3)/(2*%1.3f)\",mu,fOO,fTT,fOTTO)"%self.fOT)
        self.modelBuilder.factory_("expr::rfTO(\"@0*(1-@1-@2-@3)/(2*%1.3f)\",mu,fOO,fTT,fOTTO)"%self.fTO)
        self.modelBuilder.factory_("expr::rfOO(\"@0*@1/(%1.3f)\",mu,fOO)"%self.fOO)
        self.modelBuilder.factory_("expr::rOther(\"@0\",mu)")
        poi = "mu,fOO,fOT,fTO"
        self.modelBuilder.doSet("POI",poi)

    def getYieldScale(self,bin,process):
        "Return the name of a RooAbsReal to scale this yield by or the two special values 1 and 0 (don't scale, and set to zero)"
        if process == "prompt_WZ_other" or process == "prompt_WZ": return "rOther" # Tau contributions/WZ in the CR just scale according to x-sec
        if process == "prompt_WZ_WfOO": return "rfOO"
        if process == "prompt_WZ_WfOT": return "rfOT"
        if process == "prompt_WZ_WfTO": return "rfTO"
        if process == "prompt_WZ_WfTT": return "rfTT"
        else: return 1

chargeAsymmetryWZ = ChargeAsymmetryWZ()
BosonPolarizationWZ = bosonPolarizationWZ()
BosonPolarization2DWZ = bosonPolarization2DWZ()
