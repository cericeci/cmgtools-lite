import PhysicsTools.HeppyCore.framework.config as cfg
from PhysicsTools.Heppy.analyzers.core.AutoFillTreeProducer  import * 
from CMGTools.ObjectStudies.analyzers.leptonTriggerMatching_cff import WithLeptonTriggerMatchType
from CMGTools.TTHAnalysis.analyzers.ntupleTypes import *

leptonTypeTnP = NTupleObjectType("leptonTnP", baseObjectTypes = [ leptonTypeSusyExtraLight, WithLeptonTriggerMatchType ], variables = [
])

tnpType = NTupleObjectType("tnpType", baseObjectTypes=[fourVectorType], variables = [
    NTupleSubObject("tag",   lambda x : x.tag,   leptonTypeTnP),
    NTupleSubObject("probe", lambda x : x.probe, leptonTypeTnP),
])

treeProducerTnP = cfg.Analyzer(
     AutoFillTreeProducer, name='treeProducerTnP',
     vectorTree = True,
     saveTLorentzVectors = False,  # can set to True to get also the TLorentzVectors, but trees will be bigger
     globalVariables = [
        NTupleVariable("nVert",  lambda ev: len(ev.goodVertices), int, help="Number of good vertices"),
        NTupleVariable("nJet20", lambda ev: sum([j.pt() > 20 for j in ev.cleanJets]), int, help="Number of jets with pt > 20"),
        NTupleVariable("nJet25", lambda ev: sum([j.pt() > 25 for j in ev.cleanJets]), int, help="Number of jets with pt > 25"),
        NTupleVariable("nJet30", lambda ev: sum([j.pt() > 30 for j in ev.cleanJets]), int, help="Number of jets with pt > 30"),
        NTupleVariable("nJet40", lambda ev: sum([j.pt() > 40 for j in ev.cleanJets]), int, help="Number of jets with pt > 40"),
     ], 
     globalObjects = {
        "met" : NTupleObject("met", metType, help="PF E_{T}^{miss}, after type 1 corrections"),
     },
     collections = {
        "TnP" : NTupleCollection("TnP", tnpType, 20, help="Dilepton Candidates"),    
     },
     defaultFloatType = 'F',
)

