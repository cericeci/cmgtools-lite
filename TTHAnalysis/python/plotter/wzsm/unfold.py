'''
Script for doing the full unfolding analysis.

Created by Pietro Vischia -- pietro.vischia@cern.ch
'''
import os
import copy

import argparse
import utils
import ROOT
from array import array

#from abc import ABCMeta, abstractmethod
# 
#class AbstractTSpline(object):
#    __metaclass__ = ABCMeta
#     
#    @abstractmethod
#    def run(self):
#        pass

class ResponseComputation:

    def __init__(self, inputFiles):
        print('Initialization')
        print('Input for matrix creation: %s' % inputFiles)
        self.inputFiles=inputFiles
        
        
        
        
class AcceptanceComputer:

    def __init__(self, inputFiles):
        print('Initialization')
        print('Input files are: %s' % inputFiles)

### End class AcceptanceCounter

class Unfolder(object):

    def __init__(self, args, var):
        print('Initialization')
        self.var=var
        self.unfold=None
        self.response_nom=None
        self.response_alt=None
        self.response_inc=None
        self.data=None
        self.mc=None
        self.proofOfConcept=False
        self.verbose=args.verbose
        self.combineInput=args.combineInput
        self.nScan=30
        # Automatic L-curve scan: start with taumin=taumax=0.0
        self.tauMin=0.0
        self.tauMax=0.0
        self.iBest=None # Best value
        self.logTauX=ROOT.TSpline3() # TSpline*
        self.logTauY=ROOT.TSpline3() # TSpline*
        self.lCurve=ROOT.TGraph(0) # TGraph*
        self.gHistInvEMatrix=ROOT.TH2D() # store the inverse of error matrix
        self.gHistInvJEMatrix=None
        self.inputDir=args.inputDir
        self.responseAsPdf=args.responseAsPdf
        
        self.load_data(args.data, args.mc, args.gen)


    def load_data(self, dataFName, mcFName, genFName, treeName=['tree']):
        folder=self.inputDir
        # To be extended with the damn friend trees
        # Alternatively, take some minitrees as input (with only the few variables we are interested in. This is a better option, actually.
        # TH1D MgenMC;1
        # TH1D MdetMC;1
        # TH2D MdetgenMC;1
        # TH2D MdetgenSysMC;1
        # TH1D MgenData;1
        # TH1D MdetData;1
        # TH1D DensityGenData;1
        # TH1D DensityGenMC;1
        if self.proofOfConcept:
            file_handle = ROOT.TFile.Open('wzsm/testUnfold.root')
            self.data     = copy.deepcopy(TH1D(file_handle.Get('MdetData') ))
            self.mc       = copy.deepcopy(TH1D(file_handle.Get('MdetMC')   ))
            self.response_nom = copy.deepcopy(ROOT.TH2D(file_handle.Get('MdetgenMC')))
        else:
            dataFile=None
            mcFile=None
            #genFile=None
            if self.combineInput:
                file_handle = ROOT.TFile.Open(utils.get_file_from_glob(os.path.join(folder, self.combineInput) if folder else self.combineInput))
                gdata=file_handle.Get('shapes_fit_s/ch1/data')
                gdata.Draw('AP')
                hdata=self.get_graph_as_hist(gdata, ('recodata','recodata',4,0,4))
                data   = copy.deepcopy(ROOT.TH1F(hdata))
                signal = copy.deepcopy(ROOT.TH1F(file_handle.Get('shapes_fit_s/ch1/total_signal')))
                bkg    = copy.deepcopy(ROOT.TH1F(file_handle.Get('shapes_fit_s/ch1/total_background')))
                
                # Scheme 1: subtraction
                data.Add(bkg, -1)
                self.data=data
                self.mc=signal
                # Scheme 2: no subtraction
                # ...

            else:
                dataFile = utils.get_file_from_glob(os.path.join(folder, dataFName) if folder else dataFName)
                mcFile   = utils.get_file_from_glob(os.path.join(folder, mcFName)   if folder else mcFName)
                #data_handle = ROOT.TFile.Open(dataFile)
                #mc_handle   = ROOT.TFile.Open(mcFile)
                # Pass histograms, not trees?
                self.data = TChain("data")
                self.data.Add(dataFile+'/'+treeName)
                self.mc = TChain("mc")
                self.mc.Add(mcFile+'/'+treeName)

            #genFile  = utils.get_file_from_glob(os.path.join(folder, genFName)  if folder else genFName)

            # Add reading gen file to build response matrix
            self.get_responses()

        # Pass through numpy arrays?
        print('Data correctly loaded.')
        #return data, mc, response
        
    def get_responses(self):
        print('Acquiring response matrices.')
        folder=os.path.join(self.inputDir, 'response/%s_response_WZ_' % self.var)
        file_handle_nom = ROOT.TFile.Open('%s%s.root' % (folder, 'Pow'))
        file_handle_alt = ROOT.TFile.Open('%s%s.root' % (folder, 'aMC'))
        file_handle_inc = ROOT.TFile.Open('%s%s.root' % (folder, 'Inc'))

        self.response_nom = copy.deepcopy(ROOT.TH2D(file_handle_nom.Get('%s_response_canvas' % self.var).GetPrimitive('%s_response_WZ_%s' %(self.var, 'Pow'))))
        self.response_alt = copy.deepcopy(ROOT.TH2D(file_handle_alt.Get('%s_response_canvas' % self.var).GetPrimitive('%s_response_WZ_%s' %(self.var, 'aMC'))))
        self.response_inc = copy.deepcopy(ROOT.TH2D(file_handle_inc.Get('%s_response_canvas' % self.var).GetPrimitive('%s_response_WZ_%s' %(self.var, 'Inc'))))

    def print_responses(self):
        c = ROOT.TCanvas('matrix', 'Response Matrix', 2000, 2000)
        c.cd()
        # Margin not being applied somehow. Must do it via gStyle?
        c.SetTopMargin(0.1)
        c.SetBottomMargin(0.1)
        c.SetLeftMargin(0.1)
        c.SetRightMargin(0.1)
        ROOT.gStyle.SetOptStat(0)
        if self.responseAsPdf:
            self.response_nom.Scale(1./self.response_nom.Integral())
            self.response_alt.Scale(1./self.response_alt.Integral())
            self.response_inc.Scale(1./self.response_inc.Integral())

        self.response_nom.Draw('COLZ')
        utils.saveCanva(c, os.path.join(args.outputDir, 'responseMatrix_%s_Nom' % self.var))
        c.Clear()
        self.response_alt.Draw('COLZ')
        utils.saveCanva(c, os.path.join(args.outputDir, 'responseMatrix_%s_Alt' % self.var))
        c.Clear()
        self.response_inc.Draw('COLZ')
        utils.saveCanva(c, os.path.join(args.outputDir, 'responseMatrix_%s_Inc' % self.var))
        
    
    def get_graph_as_hist(self, g, args):
        h = ROOT.TH1F(args[0], args[1], args[2], args[3], args[4])

        for ibin in range(0,args[2]):
            x=0
            y=0
            g.GetPoint(ibin, ROOT.Double(x), ROOT.Double(y))
            h.Fill(x,y)
        print('h bins: %d; g bin: %d' %(h.GetNbinsX(), g.GetN()))
        #g.Draw('PAE')
        #print('h bins: %d; g bin: %d' %(h.GetNbinsX(), g.GetN()))
        #h=copy.deepcopy(ROOT.TH1F(g.GetHistogram()))
        print('h bins: %d; g bin: %d' %(h.GetNbinsX(), g.GetN()))
        return h

    def print_histo(self,h,opt=''):
        c = TCanvas(h.GetName(), h.GetTitle(), 2000, 2000)
        c.cd()
        h.Draw(opt)
        utils.saveCanva(c, os.path.join(args.outputDir, h.GetName()))

    def do_unfolding(self, key):
        self.set_unfolding(key)
        self.do_scan()
        self.print_unfolding_results()

    def set_unfolding(self, key):

        if   key == 'nom':
            self.unfold = ROOT.TUnfoldDensity(self.response_nom,ROOT.TUnfold.kHistMapOutputVert)
        elif key == 'alt':
            self.unfold = ROOT.TUnfoldDensity(self.response_alt,ROOT.TUnfold.kHistMapOutputVert)
        elif key == 'inc':
            self.unfold = ROOT.TUnfoldDensity(self.response_inc,ROOT.TUnfold.kHistMapOutputVert)
        else:
            print('ERROR: the response matrix you asked for (%s) does not exist' % key)
        # Check if the input data points are enough to constrain the unfolding process
        check = self.unfold.SetInput(self.data)
        if check>=10000:
            print('TUnfoldDensity error %d! Unfolding result may be wrong (not enough data to constrain the unfolding process)' % check)

    def do_scan(self):
        # Scan the L-curve and find the best point
        
        # Set verbosity
        oldinfo=ROOT.gErrorIgnoreLevel
        if self.verbose:
            ROOT.gErrorIgnoreLevel=kInfo

        # Scan the parameter tau, finding the kink in the L-curve. Finally, do the unfolding for the best choice of tau
        self.iBest=self.unfold.ScanLcurve(self.nScan, self.tauMin, self.tauMax, self.lCurve, self.logTauX, self.logTauY)

        # Reset verbosity
        if self.verbose:
            ROOT.gErrorIgnoreLevel=oldInfo

        # Here do something for the error
        ### 

    def print_unfolding_results(self):
        # Print results
        print('Tau: %d' % self.unfold.GetTau())
        print('chi^2: %d+%d/%d' %(self.unfold.GetChi2A(), self.unfold.GetChi2L(), self.unfold.GetNdf() ) )
        print('chi^2(syst): %d' % self.unfold.GetChi2Sys())
        
        print('ibest: %d, type %s' % ( self.iBest, type(self.iBest)))
        # Visualize best choice of tau
        t=0.0
        x=0.0
        y=0.0
        self.logTauX.GetKnot(self.iBest, ROOT.Double(t), ROOT.Double(x))
        self.logTauY.GetKnot(self.iBest, ROOT.Double(t), ROOT.Double(y))
        vt =array('d')
        vx =array('d')
        vy =array('d')
        vt.append(t)
        vx.append(x)
        vy.append(y)
        bestLcurve = TGraph(1, vx, vy)
        bestLogTauLogChi2 = TGraph(1, vt, vx);
        
        # Retrieve results as histograms

        histMunfold=self.unfold.GetOutput('Unfolded') # Unfolded result
        histMdetFold=self.unfold.GetFoldedOutput('FoldedBack') # Unfolding result, folded back
        # histEmatData=TH1(self.unfold.GetEmatrix('EmatData0')) # Error matrix (stat errors only)
        histEmatTotal=self.unfold.GetEmatrixTotal('EmatTotal') # Total error matrix. Migration matrix uncorrelated and correlated syst errors added in quadrature to the data statistical errors

        nDet=250
        nGen=100
        xminDet=0.0
        xmaxDet=10.0
        xminGen=0.0
        xmaxGen=10.0
        histTotalError = TH1D('TotalError',';mass(gen)', nGen, xminGen, xmaxGen)# Data histogram with total errors
        for bin in range(1,nGen):
            histTotalError.SetBinContent(bin, histMunfold.GetBinContent(bin))
            histTotalError.SetBinError(bin, TMath.Sqrt(histEmatTotal.GetBinContent(bin,bin)))


        print('Now get global correlation coefficients')
        # get global correlation coefficients
        # for this calculation one has to specify whether the
        # underflow/overflow bins are included or not
        # default: include all bins
        # here: exclude underflow and overflow bins

        #self.gHistInvEMatrix=copy.deepcopy(self.response_nom)
        #self.gHistInvEMatrix.SetName('gHistInvEMatrix')
        #self.gHistInvEMatrix.Print()
        #histRhoi=self.unfold.GetRhoItotal('rho_I',
        #                                  '', # use default title
        #                                  '', # all distributions
        #                                  "*[UO]", # discard underflow and overflow bins on all axes
        #                                  ROOT.kTRUE, # use original binning
        #                                  self.gHistInvEMatrix # store inverse of error matrix
        #                                  )

        # other try self.gHistInvJEMatrix=self.unfold.GetRhoIJtotal('rho_I',
        # other try                                     '', # use default title
        # other try                                     '', # all distributions
        # other try                                     "*[UO]", # discard underflow and overflow bins on all axes
        # other try                                     ROOT.kTRUE, # use original binning
        # other try                                     )
        #  
        #  #======================================================================
        #  # fit Breit-Wigner shape to unfolded data, using the full error matrix
        #  # here we use a "user" chi**2 function to take into account
        #  # the full covariance matrix
        #  
        #  #gFitter=TVirtualFitter::Fitter(histMunfold)
        #  #gFitter.SetFCN(chisquare_corr)
        #  
        #  bw=TF1("bw",bw_func,xminGen,xmaxGen,3)
        #  bw.SetParameter(0,1000.)
        #  bw.SetParameter(1,3.8)
        #  bw.SetParameter(2,0.2)
        #  
        #  # for (wrong!) fitting without correlations, drop the option "U"
        #  # here.
        #  histMunfold.Fit(bw,"UE")

        # =====================================================================
        #  plot some histograms
        output=TCanvas('out', 'out', 2000, 2000)
        output.Divide(3,2)

        # Show the matrix which connects input and output
        # There are overflow bins at the bottom, not shown in the plot
        # These contain the background shape.
        # The overflow bins to the left and right contain
        # events which are not reconstructed. These are necessary for proper MC
        # normalisation
        output.cd(1)
        ##histMdetGenMC.Draw("BOX")

        # draw generator-level distribution:
        #   data (red) [for real data this is not available]
        #   MC input (black) [with completely wrong peak position and shape]
        #   unfolded data (blue)
        output.cd(2)
        histTotalError.SetLineColor(kBlue)
        histTotalError.Draw("E")
        histMunfold.SetLineColor(kGreen)
        histMunfold.Draw("SAME E1")
        ###histDensityGenData.SetLineColor(kRed)
        ##histDensityGenData.Draw("SAME")
        ##histDensityGenMC.Draw("SAME HIST")

        # show detector level distributions
        #    data (red)
        #    MC (black) [with completely wrong peak position and shape]
        #    unfolded data (blue)
        output.cd(3)
        histMdetFold.SetLineColor(kBlue)
        histMdetFold.Draw()
        #histMdetMC.Draw("SAME HIST")

        histInput=self.unfold.GetInput("Minput",";mass(det)")

        histInput.SetLineColor(kRed)
        histInput.Draw("SAME")

        # show correlation coefficients
        output.cd(4)
        ##histRhoi.Draw()

        # show tau as a function of chi**2
        output.cd(5)
        self.logTauX.Draw()
        bestLogTauLogChi2.SetMarkerColor(kRed)
        bestLogTauLogChi2.Draw("*")

        # show the L curve
        output.cd(6)
        self.lCurve.Draw("AL")
        bestLcurve.SetMarkerColor(kRed)
        bestLcurve.Draw("*")

        output.SaveAs("testUnfold1.png")

        self.print_histo(histMunfold)
        self.print_histo(histMdetFold)
        self.print_histo(histEmatTotal,'colz')
        self.print_histo(histTotalError)


### End class Unfolder
def main(args): 
    print('start')
    for var in ['Zpt', 'ZconePt', 'nJet30']:
        u = Unfolder(args,var)
        u.print_responses()
        u.do_unfolding('nom')
        u.do_unfolding('alt')
        u.do_unfolding('inc')

### End main

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--inputDir',     help='Input directory', default=None)
    parser.add_argument('-o', '--outputDir',    help='Output directory', default='./')
    parser.add_argument('-c', '--combineInput', help='Data and postfit from combine output', default=None)
    parser.add_argument('-d', '--data',         help='File containing data histogram', default=None)
    parser.add_argument('-m', '--mc',           help='File containing mc reco histogram', default=None)
    parser.add_argument('-g', '--gen',          help='File containing gen info for matrix', default=None)
    parser.add_argument('-l', '--lepCat',       help='Lepton multiplicity (1 or 2)', default=1, type=int)
    parser.add_argument('-e', '--epochs',       help='Number of epochs', default=100, type=int)
    parser.add_argument('-s', '--splitMode',    help='Split mode (input or random)', default='input')
    parser.add_argument('-v', '--verbose',      help='Verbose printing of the L-curve scan', action='store_true')
    parser.add_argument('-r', '--responseAsPdf', help='Print response matrix as pdf', action='store_true') 
    args = parser.parse_args()
    # execute only if run as a script
    print('here')
    ROOT.gROOT.SetBatch()
    print('here')
    main(args)
