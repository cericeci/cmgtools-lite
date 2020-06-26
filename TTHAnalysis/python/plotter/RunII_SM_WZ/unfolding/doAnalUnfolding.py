# Do Analysis of Unfolding
# Restructured everything in a single steering script
# Code by pietro.vischia@cern.ch

# First restructure the doUnfoldInput.py script 

# Created by pietro.vischia@cern.ch
# Build inputs to the unfolding procedure (together with systematics)
# and run the unfolding (either using TUnfold or combine)

import os
import sys
from multiprocessing import Pool


sys.path.append('{cmsswpath}/src/CMGTools/TTHAnalysis/python/plotter/RunII_SM_WZ/utils/'.format(cmsswpath=os.environ['CMSSW_BASE']))
from yearlyStuff import *


# This is needed for multiprocessing.Pool, and cannot be into the class (<type 'instancemethod'> is not pickable)
def runner(cmd):
    print(cmd)
    os.system(cmd)
    


class Steer:

    def __init__(self, args):
        self.year=args.year
        self.outputDir=args.outputDir+str(self.year)
        self.channels=['incl', 'eee', 'eem', 'mme', 'mmm']
        self.mca='./mca_unfoldingInputs.txt' # File to be updated
        self.nthreads=args.nthreads
        self.base=args.base
        self.dryrun=args.dryrun

        if not os.path.isdir(self.outputDir):
            #os.mkdir(self.outputDir)
            print('mkdir -p {outputDir}'.format(outputDir=self.outputDir))

        for ch in self.channels:
            if not os.path.isdir('%s_%s'.format(self.outputDir,ch)):
                #os.mkdir('%s_%s'.format(self.outputDir,ch))
                print('mkdir -p {outputDir}_{ch}'.format(outputDir=self.outputDir,ch=ch))
            
        print('Folders with base %s have been created'.format(self.outputDir))

        self.chanCuts ={ 'incl':'',
                         'eee':'-E eee',
                         'eem':'-E eem',
                         'mme':'-E mme',
                         'mmm':'-E mmm'
                     }

        self.inputPairs={
            #'sump4(0, LepZ1_pt,LepZ1_eta,LepZ1_phi,LepZ1_mass,LepZ2_pt,LepZ2_eta,LepZ2_phi,LepZ2_mass)' : ['[0,5,10,15,20,25,30,40,50,60,70,80,90,100,110,120,130,140,160,180,200,250,300]','Reco p\_\{T\}(Z) [GeV]','Zpt'],
            ##'LeadJet_pt' : ['[25,30,35,40,50,60,70,80,90,100,110,120,130,140,160,180,200,250,300]','Reco p\_\{T\}(leading jet) [GeV]','LeadJetPt'],
            #'m3Lmet' :  ['[100,140,160,180,200,250,300,400,600,1000,3000]','Reco M\_\{WZ\} [GeV]','MWZ'],
            #'LepW_pt' : ['[25,30,35,40,50,60,70,80,90,100,110,120,130,140,160,180,200,250,300]','Reco p\_\{T\}(W) [GeV]','Wpt'],
            'nJet25_Mini'   : ['[0,1,2,3,4,5]', 'Reco N\_\{jets\}', 'Njets'], 
            #'cos_ThetaWDn_HE'   : ['[-1,-0.9,-0.8,-0.7,-0.6,-0.5,-0.4,-0.3,-0.2,-0.1,0.0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0]', 'cos(#theta_{W}^{Dn})', 'Wpol'],
            #'cos_ThetaZDn_HE'   : ['[-1,-0.9,-0.8,-0.7,-0.6,-0.5,-0.4,-0.3,-0.2,-0.1,0.0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0]', 'cos(#theta_{Z}^{Dn})', 'Zpol'],
        }
        self.responsePairs={
            #'sump4(0, genLepZ1_pt,genLepZ1_eta,genLepZ1_phi,genLepZ1_mass,genLepZ2_pt,genLepZ2_eta,genLepZ2_phi,genLepZ2_mass):sump4(0,LepZ1_pt,LepZ1_eta,LepZ1_phi,LepZ1_mass,LepZ2_pt,LepZ2_eta,LepZ2_phi,LepZ2_mass)' : ['[0,5,10,15,20,25,30,40,50,60,70,80,90,100,110,120,130,140,160,180,200,250,300]*[0,10,20,30,50,70,90,110,130,160,200,300]','Reco p\_\{T\}(Z) [GeV]','Gen p\_\{T\}(Z) [GeV]','Zpt'],
            ##'LeadJet_mcPt:LeadJet_pt' : ['[25,30,35,40,50,60,70,80,90,100,110,120,130,140,160,180,200,250,300]*[25,35,50,70,90,110,130,160,200,300]','Reco p\_\{T\}(leading jet) [GeV]','Gen p\_\{T\}(leading jet) [GeV]','LeadJetPt'],
            #'m3Lmet_gen:m3Lmet' : ['[100,140,160,180,200,250,300,400,600,1000,3000]*[100,160,200,300,600,3000]','Reco M\_\{WZ\} [GeV]','Gen M\_\{WZ\} [GeV]','MWZ'],
            #'genLepW_pt:LepW_pt' : ['[25,30,35,40,50,60,70,80,90,100,110,120,130,140,160,180,200,250,300]*[25,35,50,70,90,110,130,160,200,300]','Reco p\_\{T\}(W) [GeV]','Gen p\_\{T\}(W) [GeV]','Wpt'],
            'Sum$(GenJet_pt>25&&abs(GenJet_eta)<2.5&&deltaR(GenJet_eta,GenJet_phi,genLepZ1_eta,genLepZ1_phi)>0.5&&deltaR(GenJet_eta,GenJet_phi,genLepZ2_eta,genLepZ2_phi)>0.5&&deltaR(GenJet_eta,GenJet_phi,genLepW_eta,genLepW_phi)>0.5):nJet25_Mini'   : ['[0,1,2,3,4,5]*[0,1,2,3,4,5]', 'Reco N\_\{jets\}', 'Gen N\_\{jets\}', 'Njets'], # Not sure that genLepW is what we want
            #'cos_genThetaWDn_HE:cos_ThetaWDn_HE' : ['[-1,-0.9,-0.8,-0.7,-0.6,-0.5,-0.4,-0.3,-0.2,-0.1,0.0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0]*[-1,-0.8,-0.6,-0.4,-0.2,0.0,0.2,0.4,0.6,0.8,1.0]','Reco cos(#theta_{W}^{Dn})','Gen cos(#theta_{W}^{Dn})', 'Wpol' ],
            #'cos_genThetaZDn_HE:cos_ThetaZDn_HE' : ['[-1,-0.9,-0.8,-0.7,-0.6,-0.5,-0.4,-0.3,-0.2,-0.1,0.0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0]*[-1,-0.8,-0.6,-0.4,-0.2,0.0,0.2,0.4,0.6,0.8,1.0]','Reco cos(#theta_{Z}^{Dn})','Gen cos(#theta_{Z}^{Dn})', 'Zpol' ],
        }

    def prepareInputs(self):
        
        for ch in self.channels:
            if not os.path.isdir('%s_%s/inputs'.format(self.outputDir,ch)):
                #os.mkdir('%s_%s/inputs'.format(self.outputDir,ch))
                print('mkdir -p {outputDir}_{ch}/inputs'.format(outputDir=self.outputDir,ch=ch))
            
        
        inputdir = "/pool/cienciasrw/HeppyTrees/RA7/nanoAODv4_%s_estructure/"%(str(self.year))

        # Preliminary cleanup
        for ch in self.channels:
            print('rm -r {outputDir}_{ch}/inputs/*'.format(outputDir=self.outputDir, ch=ch))
            
        doSignSplit=False

        if not doSignSplit: 
            for iShape, iPack in self.inputPairs.items():
                iRange=iPack[0]
                iXTitle=iPack[1]
                iOut=iPack[2]
                iYTitle='Events'
                
                for iChan, iChanCut in self.chanCuts.items():
                    print('mkdir -p {outdir}/{year}_{chan}_fitWZonly_{thevar}/'.format(outdir=self.outputDir, year=self.year,chan=iChan, cut=iChanCut, thevar=iOut))
                    perchan = ' --od {outdir}/{year}_{chan}_fitWZonly_{thevar}/ --bin {chan} -E SRWZ {cut} '.format(outdir=self.outputDir, year=self.year,chan=iChan, cut=iChanCut, thevar=iOut)
                    
                    print('python makeShapeCardsSusy.py RunII_SM_WZ/{year}/mca_wz.txt RunII_SM_WZ/{year}/cuts_wzsm.txt \'{iShape}\' \'{iRange}\' RunII_SM_WZ/{year}/systs_wz.txt  --tree treeProducerSusyMultilepton -P /pool/cienciasrw/HeppyTrees/RA7/nanoAODv4_{year}_skimWZ/ {accidenteCofCof}  --Fs {{P}}/leptonPtCorrections/ {prefiringTrees} {pileupTrees} --Fs {{P}}/leptonJetReCleanerWZSM/ --Fs {{P}}/leptonBuilderWZSM_v2/ {triggerTrees} --FMCs {{P}}/leptonMatcher/ --FMCs {{P}}/bTagWeights/ --FMCs {{P}}/lepgenVarsWZSM/ --Fs {{P}}/bosonPolarization/ -L RunII_SM_WZ/functionsSF.cc -L RunII_SM_WZ/functionsMCMatch.cc -L RunII_SM_WZ/functionsWZ.cc -W \'getLeptonSF_v4(0,0,{year},LepSel_pt[0],LepSel_eta[0],LepSel_pdgId[0])*getLeptonSF_v4(0,0,{year},LepSel_pt[1],LepSel_eta[1],LepSel_pdgId[1])*getLeptonSF_v4(0,0,{year},LepSel_pt[2],LepSel_eta[2],LepSel_pdgId[2])*{pileupWeights}*bTagWeightDeepCSVT{prefiringWeights}\' --obj Events -j {nthreads} -l {lumi} -f  -E SRWZ {perchan} --neglist promptsub --autoMCStats  --XTitle "{iXTitle}" --YTitle "{iYTitle}" -o WZSR_{year} '.format(year=self.year,accidenteCofCof=accidenteCofCof[self.year],prefiringTrees=prefiringTrees[self.year],prefiringWeights=prefiringWeights[self.year],triggerTrees=triggerTrees[self.year],lumi=lumi[self.year],pileupTrees=pileupTrees[self.year],pileupWeights=pileupWeights[self.year], perchan=perchan, nthreads=self.nthreads, iShape=iShape, iRange=iRange, iXTitle=iXTitle, iYTitle=iYTitle) )

                 
                    # Must configure for cleanup or stuff like that
                    #print('rm -r /nfs/fanae/user/vischia/workarea/cmssw/combine/CMSSW_8_1_0/src/wz_unfolding/incl_fitWZonly_%s/' % iOut)
                    #print('mv /nfs/fanae/user/vischia/workarea/cmssw/combine/CMSSW_8_1_0/src/wz_unfolding/incl_fitWZonly/ /nfs/fanae/user/vischia/workarea/cmssw/combine/CMSSW_8_1_0/src/wz_unfolding/incl_fitWZonly_%s/' % iOut)
    
            else:

                enabler={
                    'plus' : ' -E pmp ',
                    'minus' : ' -E pmm',
                }

                for iWhat, iCut in enabler.items():
        
                    # Preliminary cleanup
                    print('rm -r /nfs/fanae/user/vischia/workarea/cmssw/combine/CMSSW_8_1_0/src/wz_unfolding/incl_fitWZonly/')
                    print('rm -r /nfs/fanae/user/vischia/workarea/cmssw/combine/CMSSW_8_1_0/src/wz_unfolding/eee_fitWZonly/ ')
                    print('rm -r /nfs/fanae/user/vischia/workarea/cmssw/combine/CMSSW_8_1_0/src/wz_unfolding/eem_fitWZonly/ ')
                    print('rm -r /nfs/fanae/user/vischia/workarea/cmssw/combine/CMSSW_8_1_0/src/wz_unfolding/mme_fitWZonly/ ')
                    print('rm -r /nfs/fanae/user/vischia/workarea/cmssw/combine/CMSSW_8_1_0/src/wz_unfolding/mmm_fitWZonly/ ')
                    
                    # WZ exclusive
                    for iShape, iPack in self.inputPairs.items():
                        iRange=iPack[0]
                        iXTitle=iPack[1]
                        iOut=iPack[2]
                        iYTitle='Events'
                        
                        for iChan, iChanCut in self.chanCuts.items():
                            print('mkdir -p {outdir}/{year}_{chan}_fitWZonly_{thevar}_{iWhat}/'.format(outdir=self.outputDir, year=self.year,chan=iChan, cut=iChanCut,thevar=iOut, iWhat=iWhat) )
                            perchan = ' --od {outdir}/{year}_{chan}_fitWZonly_{thevar}_{iWhat}/ --bin {chan} -E SRWZ {cut} '.format(outdir=self.outputDir, year=self.year,chan=iChan, cut=iChanCut, thevar=iOut, iWhat=iWhat)
                    
                            print('python makeShapeCardsSusy.py RunII_SM_WZ/{year}/mca_wz.txt RunII_SM_WZ/{year}/cuts_wzsm.txt \'{iShape}\' \'{iRange}\' RunII_SM_WZ/{year}/systs_wz.txt  --tree treeProducerSusyMultilepton -P /pool/cienciasrw/HeppyTrees/RA7/nanoAODv4_{year}_skimWZ/ {accidenteCofCof}  --Fs {{P}}/leptonPtCorrections/ {prefiringTrees} {pileupTrees} --Fs {{P}}/leptonJetReCleanerWZSM/ --Fs {{P}}/leptonBuilderWZSM_v2/ {triggerTrees} --FMCs {{P}}/leptonMatcher/ --FMCs {{P}}/bTagWeights/ --FMCs {{P}}/lepgenVarsWZSM/ --Fs {{P}}/bosonPolarization/ -L RunII_SM_WZ/functionsSF.cc -L RunII_SM_WZ/functionsMCMatch.cc -L RunII_SM_WZ/functionsWZ.cc -W \'getLeptonSF_v4(0,0,{year},LepSel_pt[0],LepSel_eta[0],LepSel_pdgId[0])*getLeptonSF_v4(0,0,{year},LepSel_pt[1],LepSel_eta[1],LepSel_pdgId[1])*getLeptonSF_v4(0,0,{year},LepSel_pt[2],LepSel_eta[2],LepSel_pdgId[2])*{pileupWeights}*bTagWeightDeepCSVT{prefiringWeights}\' --obj Events -j {nthreads} -l {lumi} -f  -E SRWZ {perchan} {chargecut} --neglist promptsub --autoMCStats  --XTitle "{iXTitle}" --YTitle "{iYTitle}" -o WZSR_{year} '.format(year=self.year,accidenteCofCof=accidenteCofCof[self.year],prefiringTrees=prefiringTrees[self.year],prefiringWeights=prefiringWeights[self.year],triggerTrees=triggerTrees[self.year],lumi=lumi[self.year],pileupTrees=pileupTrees[self.year],pileupWeights=pileupWeights[self.year], perchan=perchan, nthreads=self.nthreads, iShape=iShape, iRange=iRange, iXTitle=iXTitle, iYTitle=iYTitle, chargecut=iCut) )

                            # Must configure for cleanup or stuff like that
                            #print('rm -r /nfs/fanae/user/vischia/workarea/cmssw/combine/CMSSW_8_1_0/src/wz_unfolding/incl_fitWZonly_%s_%s/' % (iOut, iWhat))
                            #print('mv /nfs/fanae/user/vischia/workarea/cmssw/combine/CMSSW_8_1_0/src/wz_unfolding/incl_fitWZonly/ /nfs/fanae/user/vischia/workarea/cmssw/combine/CMSSW_8_1_0/src/wz_unfolding/incl_fitWZonly_%s_%s/' % (iOut, iWhat))
                        print('echo Done inputs preparation!')

    # End of prepareInputs()


    def prepareResponses(self):

        print('Blah')

        # Then restructure the doVariedResponses.py script


        mca='./wzsm/mca_unfolding.txt'
        #inputdir='/pool/ciencias/HeppyTrees/RA7/estructura/wzSkimmed/'
        inputdir='/pool/cienciasrw/HeppyTrees/RA7/wz/wzUnskimmed/'
        baseoutputdir='/nfs/fanae/user/vischia/workarea/cmssw/combine/CMSSW_8_1_0/src/wz_unfolding/responses/'
        #baseoutputdir="tempo/"
        fts='--Fs {P}/lepgenVarsWZSM --Fs {P}/leptonJetReCleanerWZSM --Fs {P}/leptonBuilderWZSM --FMCs {P}/bTagEventWeightFullSimWZ30 '
        #processes="-p data -p prompt_.* -p convs.* -p rares.* -p fakes_appldata.* --plotgroup fakes_appldata+=promptsub "
        processes=' -p prompt_altWZ.* '
        
        # Preliminary cleanup
        #echo "rm -r ${baseoutputdir}incl_fitWZonly/"
        #echo "rm -r ${baseoutputdir}eee_fitWZonly/ "
        #echo "rm -r ${baseoutputdir}eem_fitWZonly/ "
        #echo "rm -r ${baseoutputdir}mme_fitWZonly/ "
        #echo "rm -r ${baseoutputdir}mmm_fitWZonly/ "
        
        doSignSplit=False

        if not doSignSplit:
            for iShape, iPack in self.responsePairs.items():
                iRange=iPack[0]
                iXTitle=iPack[1]
                iYTitle=iPack[2]
                iOut=iPack[3]
                print('echo \"{iShape}, range {iRange}\"'.format(iShape=iShape,iRange=iRange))

                for iChan, iChanCut in self.chanCuts.items():
                    print('mkdir -p {outdir}/responses/{year}_{chan}_fitWZonly_{iOut}/'.format(outdir=self.outputDir, year=self.year,chan=iChan, cut=iChanCut, iOut=iOut))
                    perchan = ' --od {outdir}/responses/{year}_{chan}_fitWZonly_{iOut}/ --bin {chan} -E SRWZ {cut} '.format(outdir=self.outputDir, year=self.year,chan=iChan, cut=iChanCut, iOut=iOut)
                    print('python makeShapeCardsSusy.py RunII_SM_WZ/unfolding/mca_unfolding_{year}.txt RunII_SM_WZ/{year}/cuts_fiducial.txt \'{iShape}\' \'{iRange}\' RunII_SM_WZ/{year}/systs_wz.txt  --tree treeProducerSusyMultilepton -P /pool/cienciasrw/HeppyTrees/RA7/nanoAODv4_{year}_unSkimmed_estructure/ {accidenteCofCof}  --Fs {{P}}/leptonPtCorrections/ {prefiringTrees} {pileupTrees} --Fs {{P}}/leptonJetReCleanerWZSM/ --Fs {{P}}/leptonBuilderWZSM_v2/ {triggerTrees} --FMCs {{P}}/leptonMatcher/ --FMCs {{P}}/bTagWeights/ --FMCs {{P}}/lepgenVarsWZSM/ --Fs {{P}}/bosonPolarization/ -L RunII_SM_WZ/functionsSF.cc -L RunII_SM_WZ/functionsMCMatch.cc -L RunII_SM_WZ/functionsWZ.cc -W \'getLeptonSF_v4(0,0,{year},LepSel_pt[0],LepSel_eta[0],LepSel_pdgId[0])*getLeptonSF_v4(0,0,{year},LepSel_pt[1],LepSel_eta[1],LepSel_pdgId[1])*getLeptonSF_v4(0,0,{year},LepSel_pt[2],LepSel_eta[2],LepSel_pdgId[2])*{pileupWeights}*bTagWeightDeepCSVT{prefiringWeights}\' --obj Events -j {nthreads} -l {lumi} -f  -E SRWZ {perchan} {chargecut} --neglist promptsub --asimov --autoMCStats  --XTitle "{iXTitle}" --YTitle "{iYTitle}" -o WZSR_{year} '.format(year=self.year,accidenteCofCof=accidenteCofCof[self.year],prefiringTrees=prefiringTrees[self.year],prefiringWeights=prefiringWeights[self.year],triggerTrees=triggerTrees[self.year],lumi=lumi[self.year],pileupTrees=pileupTrees[self.year],pileupWeights=pileupWeights[self.year], perchan=perchan, nthreads=self.nthreads,iShape=iShape, iRange=iRange, iXTitle=iXTitle, iYTitle=iYTitle, chargecut=iChanCut) )

                    #print('rm -r {baseoutputdir}incl_fitWZonly_{iout}/'.format(baseoutputdir=baseoutputdir,iout=iOut))
                    #print('mv {baseoutputdir}incl_fitWZonly/ {baseoutputdir}incl_fitWZonly_{iout}/'.format(baseoutputdir=baseoutputdir,iout=iOut))
        else:         

            enabler={
                'plus' : ' -E pmp ',
                'minus' : ' -E pmm',
            }

            for iWhat, iCut in enabler.items():

                for iShape, iPack in self.responsePairs.items():
                    iRange=iPack[0]
                    iXTitle=iPack[1]
                    iYTitle=iPack[2]
                    iOut=iPack[3]

                    print('echo \"{iShape}, range {iRange}\"'.format(iShape=iShape,iRange=iRange))

                    for iChan, iChanCut in self.chanCuts.items():
                        print('mkdir -p {outdir}/responses/{year}_{chan}_fitWZonly_{iout}_{chargeinfo}/'.format(outdir=self.outputDir, year=self.year,chan=iChan, cut=iChanCut, iout=iOut,chargeinfo=iWhat))
                        perchan = ' --od {outdir}/responses/{year}_{chan}_fitWZonly_{iout}_{chargeinfo}/ --bin {chan} -E SRWZ {cut} '.format(outdir=self.outputDir, year=self.year,chan=iChan, cut=iChanCut, iout=iOut,chargeinfo=iWhat)
                    
                        print('python makeShapeCardsSusy.py RunII_SM_WZ/unfolding/mca_unfolding_{year}.txt RunII_SM_WZ/{year}/cuts_fiducial.txt \'{iShape}\' \'{iRange}\' RunII_SM_WZ/{year}/systs_wz.txt  --tree treeProducerSusyMultilepton -P /pool/cienciasrw/HeppyTrees/RA7/nanoAODv4_{year}_unSkimmed_estructure/ {accidenteCofCof}  --Fs {{P}}/leptonPtCorrections/ {prefiringTrees} {pileupTrees} --Fs {{P}}/leptonJetReCleanerWZSM/ --Fs {{P}}/leptonBuilderWZSM_v2/ {triggerTrees} --FMCs {{P}}/leptonMatcher/ --FMCs {{P}}/bTagWeights/ --FMCs {{P}}/lepgenVarsWZSM/ --Fs {{P}}/bosonPolarization/ -L RunII_SM_WZ/functionsSF.cc -L RunII_SM_WZ/functionsMCMatch.cc -L RunII_SM_WZ/functionsWZ.cc -W \'getLeptonSF_v4(0,0,{year},LepSel_pt[0],LepSel_eta[0],LepSel_pdgId[0])*getLeptonSF_v4(0,0,{year},LepSel_pt[1],LepSel_eta[1],LepSel_pdgId[1])*getLeptonSF_v4(0,0,{year},LepSel_pt[2],LepSel_eta[2],LepSel_pdgId[2])*{pileupWeights}*bTagWeightDeepCSVT{prefiringWeights}\' --obj Events -j {nthreads} -l {lumi} -f  -E SRWZ {perchan} {chargecut} --neglist promptsub --autoMCStats --asimov  --XTitle "{iXTitle}" --YTitle "{iYTitle}" -o WZSR_{year} '.format(year=self.year,accidenteCofCof=accidenteCofCof[self.year],prefiringTrees=prefiringTrees[self.year],prefiringWeights=prefiringWeights[self.year],triggerTrees=triggerTrees[self.year],lumi=lumi[self.year],pileupTrees=pileupTrees[self.year],pileupWeights=pileupWeights[self.year], perchan=perchan, nthreads=self.nthreads, iShape=iShape, iRange=iRange, iXTitle=iXTitle, iYTitle=iYTitle, chargecut=iCut) )

                        #print('rm -r {baseoutputdir}incl_fitWZonly_{iout}_{chargeinfo}/'.format(baseoutputdir=baseoutputdir,iout=iOut,chargeinfo=iWhat))
                        #print('mv {baseoutputdir}incl_fitWZonly/ {baseoutputdir}incl_fitWZonly_{iout}_{chargeinfo}/'.format(baseoutputdir=baseoutputdir,iout=iOut,chargeinfo=iWhat))
            


    def get_list_of_jobs(self, base):
    
        ret=[]
        executable='RunII_SM_WZ/unfolding/unfold.py'

        #for charge in [ '', '_plus', '_minus' ]:
        #for charge in [ '_plus', '_minus' ]:
        for charge in [ '_none', '_plus', '_minus' ]:
            for fs in [ 'incl', 'eee', 'eem', 'mme', 'mmm']:
                if not base:
                    # No bias, area constraint     
                    ret.append('python {executable} -i {outputdir} -y {year} -f {fs} --charge {charge}  -b 0 -a -o unfold_nobias/{fs}{charge}/data -c common/WZSR_{year}.input.root -r >& logs/nobias_data_{fs}.log'.format(outputdir=self.outputDir,year=self.year,executable=executable,fs=fs,charge=charge))
                    ret.append('python {executable} -i {outputdir} -y {year} -f {fs} --charge {charge}  -b 0 -a -o unfold_nobias/{fs}{charge}/mcclosure -c common/WZSR_{year}.input.root -r --closure >& logs/nobias_mcclosure_{fs}.log'.format(outputdir=self.outputDir,year=self.year,executable=executable,fs=fs,charge=charge))

                    # No bias, no area constraint
                    ret.append('python {executable} -i {outputdir} -y {year} -f {fs} --charge {charge}  -b 0 -o unfold_nobias_noconstraintarea/{fs}{charge}/data -c common/WZSR_{year}.input.root -r >& logs/nobias_noconstraintarea_data_{fs}.log'.format(outputdir=self.outputDir,year=self.year,executable=executable,fs=fs,charge=charge))
                    ret.append('python {executable} -i {outputdir} -y {year} -f {fs} --charge {charge}  -b 0 -o unfold_nobias_noconstraintarea/{fs}{charge}/mcclosure -c common/WZSR_{year}.input.root -r --closure >& logs/nobias_noconstraintarea_mcclosure_{fs}.log'.format(outputdir=self.outputDir,year=self.year,executable=executable,fs=fs,charge=charge))
            
                    # Bias 1, area constraint
                    ret.append('python {executable} -i {outputdir} -y {year} -f {fs} --charge {charge}  -b 1.0 -a -o unfold_1p0bias/{fs}{charge}/data -c common/WZSR_{year}.input.root -r >& logs/1p0bias_data_{fs}.log'.format(outputdir=self.outputDir,year=self.year,executable=executable,fs=fs,charge=charge))
                    ret.append('python {executable} -i {outputdir} -y {year} -f {fs} --charge {charge}  -b 1.0 -a -o unfold_1p0bias/{fs}{charge}/mcclosure -c common/WZSR_{year}.input.root -r --closure >& logs/1p0bias_mcclosure_{fs}.log'.format(outputdir=self.outputDir,year=self.year,executable=executable,fs=fs,charge=charge))
                
                    # Bias 1, no area constraint
                    ret.append('python {executable} -i {outputdir} -y {year} -f {fs} --charge {charge}  -b 1.0 -o unfold_1p0bias_noconstraintarea/{fs}{charge}/data -c common/WZSR_{year}.input.root -r >& logs/1p0bias_noconstraintarea_data_{fs}.log'.format(outputdir=self.outputDir,year=self.year,executable=executable,fs=fs,charge=charge))
                    ret.append('python {executable} -i {outputdir} -y {year} -f {fs} --charge {charge}  -b 1.0 -o unfold_1p0bias_noconstraintarea/{fs}{charge}/mcclosure -c common/WZSR_{year}.input.root -r --closure >& logs/1p0bias_noconstraintarea_mcclosure_{fs}.log'.format(outputdir=self.outputDir,year=self.year,executable=executable,fs=fs,charge=charge))
        
                    # Bias 1.13, no area constraint
                    ret.append('python {executable} -i {outputdir} -y {year} -f {fs} --charge {charge}  -b 1.13 -o unfold_nnlobias_noconstraintarea/{fs}{charge}/data -c common/WZSR_{year}.input.root -r >& logs/nnlobias_noconstraintarea_data_{fs}.log'.format(outputdir=self.outputDir,year=self.year,executable=executable,fs=fs,charge=charge))
                    ret.append('python {executable} -i {outputdir} -y {year} -f {fs} --charge {charge}  -b 1.13 -o unfold_nnlobias_noconstraintarea/{fs}{charge}/mcclosure -c common/WZSR_{year}.input.root -r --closure >& logs/nnlobias_noconstraintarea_mcclosure_{fs}.log'.format(outputdir=self.outputDir,year=self.year,executable=executable,fs=fs,charge=charge))

                else:
                    # Bias 1.13, area constraint
                    ret.append('python {executable} -i {outputdir} -y {year} -f {fs} --charge {charge}  -b 1.13 -a -o unfold_nnlobias/{fs}{charge}/data -c common/WZSR_{year}.input.root -r >& logs/nnlobias_data_{fs}.log'.format(outputdir=self.outputDir,year=self.year,executable=executable,fs=fs,charge=charge))
                    ret.append('python {executable} -i {outputdir} -y {year} -f {fs} --charge {charge}  -b 1.13 -a -o unfold_nnlobias/{fs}{charge}/mcclosure -c common/WZSR_{year}.input.root -r --closure >& logs/nnlobias_mcclosure_{fs}.log'.format(outputdir=self.outputDir,year=self.year,executable=executable,fs=fs,charge=charge))
            
                    
        return ret

    def doTheUnfolding(self):
        # Finally call runUnfold and unfold.py 
        print("python runUnfold.py -n 1")
        
        jobs = self.get_list_of_jobs(args.base)
        
        if self.dryrun:
            print jobs
            quit()
        pool=Pool(self.nthreads)
        pool.map(runner, jobs)
        pool.close()
        pool.join()
        

def bad(what):
    ret=True
    if 'all' in what:
        ret=False
    if 'inputs' in what:
        ret=False
    if 'responses' in what:
        ret=False
    if 'unfolding' in what:
        ret=False
    return ret

def main(args):

    if bad(args.what):
        print("I don't recognize this action. Why don't you do it yourself with pen and paper?")
        return 1
        
    anal=Steer(args) # Perhaps (depending on combination strategy) I will put the scan on the year inside the unfolding script

    if 'all' in args.what:
        args.what='inputs responses unfolding'
        
    if 'inputs' in args.what:
        anal.prepareInputs()
    if 'responses' in args.what:
        anal.prepareResponses()
    if 'unfolding' in args.what:
        anal.doTheUnfolding()


import argparse
import ROOT

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-w', '--what',           help='Action to be taken [inputs, responses, unfolding, all]', default='all')
    parser.add_argument('-o', '--outputDir',      help='Output directory', default='./temp')
    parser.add_argument('-y', '--year',           help='Year', default=2016, type=int)
    parser.add_argument('-n', '--nthreads',       help='Number of multiprocessing threads (only for -w unfolding)', default=35, type=int)
    parser.add_argument('-b', '--base',           help='Run only on base (the one to put in the paper) parameter set (only for -w unfolding)', action='store_true')
    parser.add_argument('-d', '--dryrun',         help='Only print commands and exit (only for -w unfolding, because of legacy structure)', action='store_true')
    args = parser.parse_args()
    # execute only if run as a script
    ROOT.gROOT.SetBatch()
    main(args)

