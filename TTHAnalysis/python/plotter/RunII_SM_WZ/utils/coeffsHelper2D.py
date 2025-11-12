#Bunch of basis change functions
import ROOT
import CMS_lumi

"""sin2theff = 0.23152
cv = -0.5
ca = -0.5 + 2*sin2theff"""
alpha = 0.147

class coeffs(object):

    def __init__(self, histoc,histoc2,histofid, isZ, tag, lumi):
        self.histoc = histoc
        self.histoc2 = histoc2
        self.histofid = histofid
        self.isZ = isZ
        self.tag = tag
        self.lumi = lumi
        self.quadF = ROOT.TF2("quad" + tag, "[0]*(1+x)*(1+x)*(1+2*0.213*y+y*y) + [1]*(1+x)*(1+x)*(1-2*0.213*y+y*y)  + 2*[2]*(1+x)*(1+x)*(1-y*y) + [3]*(1-x)*(1-x)*(1+2*0.213*y+y*y)  + [4]*(1-x)*(1-x)*(1-2*0.213*y+y*y)  + 2*[5]*(1-x)*(1-x)*(1-y*y)+ 2*[6]*(1-x*x)*(1+2*0.213*y+y*y) + 2*[7]*(1-x*x)*(1-2*0.213*y+y*y)  + 4*[8]*(1-x*x)*(1-y*y)", -1.0,1.0,-1.0,1.0)
        self.quadF.SetParameters(100,100,100,100,100,100,100,100,100)
    def load(self):
        """self.ic = self.histoc.GetMean()
        self.icErr = self.histoc.GetMeanError()
        self.ic2 = self.histoc2.GetMean()     
        self.ic2Err = self.histoc2.GetMeanError()"""           
        self.histoc.Fit(self.quadF)
        self.ndof = self.quadF.GetNDF()
        self.chi2 = self.quadF.GetChisquare()    
        self.prob = self.quadF.GetProb()
        print "NDOF, chi2, prob", self.ndof, self.chi2, self.prob
        fLL,fLR,fLO,fRL,fRR,fRO,fOL,fOR,fOO = self.histoc.GetFunction("quad" + self.tag).GetParameter(0),self.histoc.GetFunction("quad" + self.tag).GetParameter(1),self.histoc.GetFunction("quad" + self.tag).GetParameter(2),self.histoc.GetFunction("quad" + self.tag).GetParameter(3),self.histoc.GetFunction("quad" + self.tag).GetParameter(4),self.histoc.GetFunction("quad" + self.tag).GetParameter(5),self.histoc.GetFunction("quad" + self.tag).GetParameter(6),self.histoc.GetFunction("quad" + self.tag).GetParameter(7),self.histoc.GetFunction("quad" + self.tag).GetParameter(8)
        print self.histoc.GetFunction("quad" + self.tag).GetParameter(0),self.histoc.GetFunction("quad" + self.tag).GetParameter(1),self.histoc.GetFunction("quad" + self.tag).GetParameter(2),self.histoc.GetFunction("quad" + self.tag).GetParameter(3),self.histoc.GetFunction("quad" + self.tag).GetParameter(4),self.histoc.GetFunction("quad" + self.tag).GetParameter(5),self.histoc.GetFunction("quad" + self.tag).GetParameter(6),self.histoc.GetFunction("quad" + self.tag).GetParameter(7),self.histoc.GetFunction("quad" + self.tag).GetParameter(8)
        self.fWL = fLL + fLR + fLO
        self.fWR = fRL + fRR + fRO
        self.fWO = fOL + fOR + fOO
        self.fZL = fLL + fRL + fOL
        self.fZR = fLR + fRR + fOR
        self.fZO = fLO + fRO + fOO
        norm = (fLL+fLR+fLO+fRL+fRR+fRO+fOL+fOR+fOO)
        print(fLL/norm,fLR/norm,fLO/norm,fRL/norm,fRR/norm,fRO/norm,fOL/norm,fOR/norm,fOO/norm)
        print "W pol: %1.3f, %1.3f, %1.3f"%(self.fWL/(self.fWL+self.fWR+self.fWO), self.fWR/(self.fWL+self.fWR+self.fWO),self.fWO/(self.fWL+self.fWR+self.fWO))
        print "Z pol: %1.3f, %1.3f, %1.3f"%(self.fZL/(self.fZL+self.fZR+self.fZO), self.fZR/(self.fZL+self.fZR+self.fZO),self.fZO/(self.fZL+self.fZR+self.fZO))
        print "fOO: %1.3f"%(fOO/(fLL+fLR+fLO+fRL+fRR+fRO+fOL+fOR+fOO))
        print "fOT: %1.3f"%((fOL+fOR)/(fLL+fLR+fLO+fRL+fRR+fRO+fOL+fOR+fOO))
        print "fTO: %1.3f"%((fLO+fRO)/(fLL+fLR+fLO+fRL+fRR+fRO+fOL+fOR+fOO))
        print "fTT: %1.3f"%((fLL+fLR+fRL+fRR)/(fLL+fLR+fLO+fRL+fRR+fRO+fOL+fOR+fOO))

    def doControl(self, what="Z"):
        c = ROOT.TCanvas("c", "test", 800,610)
        #self.histoc.Draw()
        self.histoc.SetTitle("")
        ROOT.gStyle.SetOptStat(0);
        ROOT.gStyle.SetPaintTextFormat("4.2f")
        ROOT.gStyle.SetOptTitle(0)
        ROOT.gPad.Update()
        c.SetTickx(1)
        c.SetTicky(1)
        c.SetRightMargin (0.04)
        c.SetTopMargin   (0.0984)
        c.SetLeftMargin  (0.14)
        c.SetBottomMargin(0.15666)        
        ROOT.gROOT.SetBatch(True)
        if what == "W":
            self.f0 = ROOT.TF1("f0" + what, "2*(1-x*x)*[0]", -1.0,1.)
            self.fL = ROOT.TF1("fL" + what, "(1-x)*(1-x)*[0]", -1.0,1.0)
            self.fR = ROOT.TF1("fR" + what, "(1+x)*(1+x)*[0]", -1.0,1.0)
            self.fR.SetParameter(0,self.fWR)
            self.fL.SetParameter(0,self.fWL)
            self.f0.SetParameter(0,self.fWO)

        elif what == "Z":
            self.f0 = ROOT.TF1("f0" + what, "2*(1-x*x)*[0]", -1.0,1.)
            self.fL = ROOT.TF1("fL" + what, "(1-2*0.213*x+x*x)*[0]", -1.0,1.0)
            self.fR = ROOT.TF1("fR" + what, "(1+2*0.213*x+x*x)*[0]", -1.0,1.0)
            self.fR.SetParameter(0,self.fZR)
            self.fL.SetParameter(0,self.fZL)
            self.f0.SetParameter(0,self.fZO)


        self.histoc.GetXaxis().SetTitle("cos(#theta_{Z})" if self.isZ else "q_{W} cos(#theta_{W})")
        self.histoc.GetYaxis().SetTitle("Events (generated)")
        self.histoc.SetLineColor(ROOT.kAzure)      
        self.histoc.GetXaxis().SetNdivisions(205)
        self.histoc.GetXaxis().SetLabelFont(42)
        self.histoc.GetXaxis().SetLabelSize(0.060)  
        self.histoc.GetXaxis().SetTitleFont(42)
        self.histoc.GetXaxis().SetTitleSize(0.08)
        self.histoc.GetXaxis().SetTitleOffset(0.75)

        self.histoc.GetYaxis().SetNdivisions(205)
        self.histoc.GetYaxis().SetLabelFont(42)
        self.histoc.GetYaxis().SetLabelSize(0.035)
        self.histoc.GetYaxis().SetTitleFont(42)
        self.histoc.GetYaxis().SetTitleSize(0.07)
        self.histoc.GetYaxis().SetTitleOffset(0.88)
        self.histoc.GetXaxis().SetRangeUser(-1.0,1.0)
        self.histoc.SetMaximum(self.histoc.GetMaximum()*2)
        self.histoc.SetMinimum(0)
        self.histoc.SetLineWidth(3)
        self.histoc.SetMarkerStyle(8)
        self.histoc.SetMarkerColor(ROOT.kBlue)
        self.histoc.SetMarkerSize(1.5)

        self.histoc.Draw("pE0")
        self.quadF.Draw("same")
        self.histofid.SetLineColor(ROOT.kBlack)
        self.histofid.SetLineWidth(3)
        self.histofid.Draw("same")

        CMS_lumi.writeExtraText = True
        CMS_lumi.lumi_13TeV = self.lumi
        CMS_lumi.extraText  = "Simulation"
        CMS_lumi.lumi_sqrtS = 13
        CMS_lumi.CMS_lumi(c, 4, 0, 0.15)
        theL = ROOT.TLegend(0.5, 0.53, 0.95, 0.88)
        theL.SetBorderSize(0)
        theL.AddEntry(self.histoc, "Generated", "LEP")
        theL.AddEntry(self.quadF, "Fit, #it{p}-value = %1.4f"%(self.prob if self.prob >= 1e-4 else 10*self.prob), "L")
        theL.AddEntry(self.histofid, "Fiducial","L")
        self.f0.SetLineStyle(4)
        self.f0.SetLineColor(ROOT.kBlue)
        self.f0.SetLineWidth(6)

        self.f0.Draw("same")
        self.fL.SetLineStyle(4)
        self.fL.SetLineColor(ROOT.kOrange+7)
        self.fL.SetLineWidth(6)

        self.fL.Draw("same")
        self.fR.SetLineStyle(4)
        self.fR.SetLineColor(ROOT.kBlack)
        self.fR.SetLineWidth(6)

        self.fR.Draw("same")

        if what == "W":
            theL.AddEntry(self.f0, "f_{0} = %1.3f"%(self.fWO), "L")
            theL.AddEntry(self.fL, "f_{L} = %1.3f"%(self.fWL), "L")
            theL.AddEntry(self.fR, "f_{R} = %1.3f"%(self.fWR), "L")
        if what == "Z":
            theL.AddEntry(self.f0, "f_{0} = %1.3f"%(self.fZO), "L")
            theL.AddEntry(self.fL, "f_{L} = %1.3f"%(self.fZL), "L")
            theL.AddEntry(self.fR, "f_{R} = %1.3f"%(self.fZR), "L")

        theL.Draw("same")
        theLState = ROOT.TLegend(0.15, 0.73, 0.495, 0.87)
        theLState.SetBorderSize(0)
        theLState.SetHeader("pp#rightarrowW^{#minus}Z" if (("WM" in self.tag) or ("ZM" in self.tag)) else "pp#rightarrowW^{+}Z" if (("WP" in self.tag) or ("ZP" in self.tag)) else "pp#rightarrowW^{#pm}Z","C")
        theLState.SetTextSize(0.090)
        theLState.Draw("same")
        c.SaveAs("/nfs/fanae/user/carlosec/www/public/wz/Legacy/polPlots_Oct2025_2D/"+what + "_" + self.tag + ".pdf")
        c.SaveAs("/nfs/fanae/user/carlosec/www/public/wz/Legacy/polPlots_Oct2025_2D/"+what + "_" + self.tag + ".png")
        c.SaveAs("/nfs/fanae/user/carlosec/www/public/wz/Legacy/polPlots_Oct2025_2D/"+what + "_" + self.tag + ".root")
  
