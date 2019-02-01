##########################################################
##          T&P COMMON MODULES ARE DEFINED HERE         ##
##########################################################
import PhysicsTools.HeppyCore.framework.config as cfg

from PhysicsTools.Heppy.analyzers.core.all import *
from PhysicsTools.Heppy.analyzers.objects.all import *
from PhysicsTools.Heppy.analyzers.gen.all import *

##------------------------------------------
##  Core modules
##------------------------------------------

from CMGTools.ObjectStudies.analyzers.treeProducerLepTnP import treeProducerTnP
from CMGTools.ObjectStudies.analyzers.ZTagAndProbeAnalyzer import ZTagAndProbeAnalyzer
from CMGTools.TTHAnalysis.analyzers.ttHFastLepSkimmer import ttHFastLepSkimmer
from CMGTools.ObjectStudies.analyzers.leptonTriggerMatching_cff import LeptonTriggerMatchersSequence

skimAnalyzer = cfg.Analyzer(
    SkimAnalyzerCount, name='skimAnalyzerCount',
    useLumiBlocks = False,
    )

# Apply json file (if the dataset has one)
jsonAna = cfg.Analyzer(
    JSONAnalyzer, name="JSONAnalyzer",
    )

# Filter using the 'triggers' and 'vetoTriggers' specified in the dataset
triggerAna = cfg.Analyzer(
    TriggerBitFilter, name="TriggerBitFilter",
    )

# Fast skimming
fastSkim1LTag = cfg.Analyzer( ttHFastLepSkimmer, name="fastSkim1LTag",
        muons = 'slimmedMuons',         muCut  = lambda mu  : mu.pt()  > 25 and mu.isMediumMuon() and mu.pfIsolationR03().sumChargedHadronPt < 0.2*mu.pt(),
        electrons = 'slimmedElectrons', eleCut = lambda ele : ele.pt() > 25                       and ele.pfIsolationVariables().sumChargedHadronPt < 0.2*ele.pt(),
        minLeptons = 1,
)
fastSkim2L = cfg.Analyzer( ttHFastLepSkimmer, name="fastSkim2L",
        muons = 'slimmedMuons', muCut = lambda mu : mu.pt() > 3.5,
        electrons = 'slimmedElectrons', eleCut = lambda ele : ele.pt() > 5,
        minLeptons = 2,
)



# Create flags for trigger bits
triggerFlagsAna = cfg.Analyzer(
    TriggerBitAnalyzer, name="TriggerFlags",
    processName = 'HLT',
    triggerBits = {
        # "<name>" : [ 'HLT_<Something>_v*', 'HLT_<SomethingElse>_v*' ] 
    }
    )

# Select a list of good primary vertices (generic)
vertexAna = cfg.Analyzer(
    VertexAnalyzer, name="VertexAnalyzer",
    vertexWeight = None,
    fixedWeight = 1,
    verbose = False
    )



##------------------------------------------
##  gen
##------------------------------------------

## Gen Info Analyzer (generic, but should be revised)
genAna = cfg.Analyzer(
    GeneratorAnalyzer, name="GeneratorAnalyzer",
    # BSM particles that can appear with status <= 2 and should be kept
    stableBSMParticleIds = [ 1000022 ],
    # Particles of which we want to save the pre-FSR momentum (a la status 3).
    # Note that for quarks and gluons the post-FSR doesn't make sense,
    # so those should always be in the list
    savePreFSRParticleIds = [ 1,2,3,4,5, 11,12,13,14,15,16, 21 ],
    # Make also the list of all genParticles, for other analyzers to handle
    makeAllGenParticles = True,
    # Make also the splitted lists
    makeSplittedGenLists = True,
    allGenTaus = False,
    # Print out debug information
    verbose = False,
    )

##------------------------------------------
##  leptons 
##------------------------------------------

# Lepton Analyzer (generic)
lepAna = cfg.Analyzer(
    LeptonAnalyzer, name="leptonAnalyzer",
    # input collections
    muons='slimmedMuons',
    electrons='slimmedElectrons',
    rhoMuon= 'fixedGridRhoFastjetAll',
    rhoElectron = 'fixedGridRhoFastjetAll',
    # energy scale corrections and ghost muon suppression (off by default)
    doMuonScaleCorrections=False,
    doElectronScaleCorrections=False, # "embedded" in 5.18 for regression
    doSegmentBasedMuonCleaning=False,
    # inclusive very loose muon selection
    inclusive_muon_id  = "POG_ID_Loose",
    inclusive_muon_pt  = 3,
    inclusive_muon_eta = 2.4,
    inclusive_muon_dxy = 0.5,
    inclusive_muon_dz  = 1.0,
    muon_dxydz_track = "innerTrack",
    # loose muon selection
    loose_muon_id     = "POG_ID_Loose",
    loose_muon_pt     = 5,
    loose_muon_eta    = 2.4,
    loose_muon_dxy    = 0.05,
    loose_muon_dz     = 0.1,
    loose_muon_relIso = 0.5,
    # inclusive very loose electron selection
    inclusive_electron_id  = "",
    inclusive_electron_pt  = 5,
    inclusive_electron_eta = 2.5,
    inclusive_electron_dxy = 0.5,
    inclusive_electron_dz  = 1.0,
    inclusive_electron_lostHits = 1.0,
    # loose electron selection
    loose_electron_id     = "MVA_ID_nonIso_Fall17_Loose",
    loose_electron_pt     = 7,
    loose_electron_eta    = 2.5,
    loose_electron_dxy    = 0.05,
    loose_electron_dz     = 0.1,
    loose_electron_relIso = 0.5,
    loose_electron_lostHits = 1.0,
    # muon isolation correction method (can be "rhoArea" or "deltaBeta")
    mu_isoCorr = "rhoArea" ,
    mu_effectiveAreas = "Fall17", #(can be 'Data2012' or 'Phys14_25ns_v1' or 'Spring15_25ns_v1')
    # electron isolation correction method (can be "rhoArea" or "deltaBeta")
    ele_isoCorr = "rhoArea" ,
    ele_effectiveAreas = "Fall17" , #(can be 'Data2012' or 'Phys14_25ns_v1' or 'Spring15_25ns_v1')
    ele_tightId = "Cuts_2012" ,
    # Mini-isolation, with pT dependent cone: will fill in the miniRelIso, miniRelIsoCharged, miniRelIsoNeutral variables of the leptons (see https://indico.cern.ch/event/368826/ )
    doMiniIsolation = True, # off by default since it requires access to all PFCandidates 
    packedCandidates = 'packedPFCandidates',
    miniIsolationPUCorr = 'rhoArea', # Allowed options: 'rhoArea' (EAs for 03 cone scaled by R^2), 'deltaBeta', 'raw' (uncorrected), 'weights' (delta beta weights; not validated)
    miniIsolationVetoLeptons = None, # use 'inclusive' to veto inclusive leptons and their footprint in all isolation cones
    doDirectionalIsolation = [], # calculate directional isolation with leptons (works only with doMiniIsolation, pass list of cone sizes)
    doFixedConeIsoWithMiniIsoVeto = False, # calculate fixed cone isolations with the same vetoes used for miniIso,
    # minimum deltaR between a loose electron and a loose muon (on overlaps, discard the electron)
    min_dr_electron_muon = 0.05,
    # do MC matching 
    do_mc_match = True, # note: it will in any case try it only on MC, not on data
    do_mc_match_photons = "all",
    match_inclusiveLeptons = False, # match to all inclusive leptons
)

trigMatcher1Mu = cfg.Analyzer(
    TriggerMatchAnalyzer, name="trigMatcher1Mu",
    label='1Mu',
    processName = 'PAT',
    fallbackProcessName = 'RECO',
    unpackPathNames = True,
    trgObjSelectors = [ lambda t : t.path("HLT_IsoMu27_v*",1,0) or t.path("HLT_IsoMu24_v*",1,0) or t.path("HLT_IsoTkMu27_v*",1,0) or t.path("HLT_IsoTkMu24_v*",1,0)],
    collToMatch = 'selectedLeptons',
    collMatchSelectors = [ lambda l,t : abs(l.pdgId()) == 13 ],
    collMatchDRCut = 0.2,
    univoqueMatching = True,
    verbose = False,
)
trigMatcher1El = trigMatcher1Mu.clone(
    name="trigMatcher1El",
    label='1El',
    trgObjSelectors = [ lambda t : t.path("HLT_Ele35_WPTight_Gsf_v*",1,0) or t.path("HLT_Ele32_WPTight_Gsf_v*",1,0) ],
    collMatchSelectors = [ lambda l,t : abs(l.pdgId()) == 11 ],
)

jetAna = cfg.Analyzer(
    JetAnalyzer, name='jetAnalyzer',
    jetCol = 'slimmedJets',
    copyJetsByValue = False,      #Whether or not to copy the input jets or to work with references (should be 'True' if JetAnalyzer is run more than once)
    genJetCol = 'slimmedGenJets',
    rho = ('fixedGridRhoFastjetAll','',''),
    jetPt = 25.,
    jetEta = 4.7,
    jetEtaCentral = 2.4,
    cleanJetsFromLeptons = True,
    jetLepDR = 0.4,
    jetLepArbitration = (lambda jet,lepton : lepton), # you can decide which to keep in case of overlaps; e.g. if the jet is b-tagged you might want to keep the jet
    cleanSelectedLeptons = True, #Whether to clean 'selectedLeptons' after disambiguation. Treat with care (= 'False') if running Jetanalyzer more than once
    minLepPt = 10,
    lepSelCut = lambda lep : True,
    relaxJetId = False,  
    doPuId = False, # Not commissioned in 7.0.X
    recalibrateJets = True, #'MC', # True, False, 'MC', 'Data'
    applyL2L3Residual = True, # Switch to 'Data' when they will become available for Data
    recalibrationType = "AK4PFchs",
    mcGT     = "Fall17_17Nov2017_V6_MC",
    dataGT   = [(1,"Fall17_17Nov2017B_V6_DATA"),(299337,"Fall17_17Nov2017C_V6_DATA"),(302030,"Fall17_17Nov2017D_V6_DATA"),(303435,"Fall17_17Nov2017E_V6_DATA"),(304911,"Fall17_17Nov2017F_V6_DATA")],
    jecPath = "${CMSSW_BASE}/src/CMGTools/RootTools/data/jec/",
    shiftJEC = 0, # set to +1 or -1 to apply +/-1 sigma shift to the nominal jet energies
    addJECShifts = False, # if true, add  "corr", "corrJECUp", and "corrJECDown" for each jet (requires uncertainties to be available!)
    jetPtOrUpOrDnSelection = False, # if true, apply pt cut on the maximum among central, JECUp and JECDown values of corrected pt
    smearJets = False,
    shiftJER = 0, # set to +1 or -1 to get +/-1 sigma shifts  
    alwaysCleanPhotons = False,
    cleanGenJetsFromPhoton = False,
    cleanJetsFromFirstPhoton = False,
    cleanJetsFromTaus = False,
    cleanJetsFromIsoTracks = False,
    doQG = False,
    do_mc_match = True,
    collectionPostFix = "",
    calculateSeparateCorrections = True, # should be True if recalibrateJets is True, otherwise L1s will be inconsistent
    calculateType1METCorrection  = False,
    type1METParams = { 'jetPtThreshold':15., 'skipEMfractionThreshold':0.9, 'skipMuons':True },
    storeLowPtJets = False,
)


metAna = cfg.Analyzer(
    METAnalyzer, name="metAnalyzer",
    metCollection     = "slimmedMETs",
    noPUMetCollection = "slimmedMETs",    
    copyMETsByValue = False,
    makeShiftedMETs=False,
    doTkMet = False,
    doPuppiMet = False,
    doMetNoPU = False,
    doMetNoMu = False,
    doMetNoEle = False,
    doMetNoPhoton = False,
    storePuppiExtra = False, # False for MC, True for re-MiniAOD
    recalibrate = False, # or "type1", or True
    applyJetSmearing = False, # does nothing unless the jet smearing is turned on in the jet analyzer
    old74XMiniAODs = False, # set to True to get the correct Raw MET when running on old 74X MiniAODs
    jetAnalyzerPostFix = "",
    candidates='packedPFCandidates',
    candidatesTypes='std::vector<pat::PackedCandidate>',
    dzMax = 0.1,
    collectionPostFix = "",
)

analyzerTnP = cfg.Analyzer(
    ZTagAndProbeAnalyzer, name="analyzerTnP",
    probeCollection = "selectedLeptons", 
    probeSelection  = lambda lep : True,
    tagSelectionMC  = lambda lep : lep.pt() > 25 and lep.tightId()  and (lep.matchedTrgObj1El if abs(lep.pdgId())==11 else lep.matchedTrgObj1Mu) ,


    tagSelectionData = lambda lep : lep.pt() > 25 and lep.tightId()  and (lep.matchedTrgObj1El if abs(lep.pdgId())==11 else lep.matchedTrgObj1Mu),
    massRange = (50,130),
    filter = True,
)

from CMGTools.TTHAnalysis.analyzers.ttHCoreEventAnalyzer import *
#For LeptonMVA
ttHCoreEventAna = cfg.Analyzer(
    ttHCoreEventAnalyzer, name='ttHCoreEventAnalyzer',
    maxLeps = 4, ## leptons to consider
    mhtForBiasedDPhi = "mhtJet40jvec",
    jetForBiasedDPhi = "cleanJets",
    jetPt = 40.,
    doLeptonMVASoft = False,
)

pileUpAna = cfg.Analyzer(
    PileUpAnalyzer, name="PileUpAnalyzer",
    true = True,  # use number of true interactions for reweighting
    makeHists=True
)

tnpSequence = [
    pileUpAna,
    skimAnalyzer,
    jsonAna,
    triggerAna,
    fastSkim2L,
    fastSkim1LTag,
    triggerFlagsAna,
    genAna,
    vertexAna,
    lepAna,
] + LeptonTriggerMatchersSequence + [
    trigMatcher1Mu,
    trigMatcher1El,
    analyzerTnP,
    jetAna,
    metAna,
    ttHCoreEventAna,
    treeProducerTnP
]
