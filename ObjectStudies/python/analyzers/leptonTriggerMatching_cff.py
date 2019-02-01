import PhysicsTools.HeppyCore.framework.config as cfg
from PhysicsTools.Heppy.analyzers.core.TriggerMatchAnalyzer import TriggerMatchAnalyzer
from PhysicsTools.Heppy.analyzers.core.AutoFillTreeProducer  import * 

_MuPathTemplate = cfg.Analyzer(TriggerMatchAnalyzer, 
    processName = 'PAT',
    fallbackProcessName = 'RECO',
    unpackPathNames = True,
    collToMatch = 'selectedLeptons',
    collMatchSelectors = [ lambda l,t : abs(l.pdgId()) == 13 ],
    collMatchDRCut = 0.2,
    univoqueMatching = True,
    verbose = False,
)
_MuFilterTemplate = _MuPathTemplate.clone(unpackPathNames = False)
_ElPathTemplate   = _MuPathTemplate.clone(collMatchSelectors = [ lambda l,t : abs(l.pdgId()) == 11 ])
_ElFilterTemplate = _ElPathTemplate.clone(unpackPathNames = False)

allTriggerMatchers = {}
def defineMatcher(template, label, selector):
    if label in allTriggerMatchers: raise RuntimeError, "Duplicate definition of "+label
    module = template.clone(
        name = "trigMatcher"+label, label = label,
        trgObjSelectors = [ selector ]
    )
    allTriggerMatchers[label] = module

# Singles Muons (unprescaled)
defineMatcher(_MuPathTemplate, "IsoMu24orIsoTkMu24",  lambda t : t.path("HLT_IsoMu24_v*",1,0) or t.path("HLT_IsoTkMu24_v*",1,0))
defineMatcher(_MuPathTemplate, "IsoMu27orIsoTkMu27",  lambda t : t.path("HLT_IsoMu27_v*",1,0) or t.path("HLT_IsoTkMu27_v*",1,0))

## Singles Muons (prescaled)
defineMatcher(_MuPathTemplate, "Mu17TrkIso",  lambda t : t.path("HLT_Mu17_TrkIsoVVL_*",1,0))
defineMatcher(_MuPathTemplate, "Mu8TrkIso",  lambda t : t.path("HLT_Mu8_TrkIsoVVL_*",1,0))
defineMatcher(_MuPathTemplate, "Mu17",  lambda t : t.path("HLT_Mu17_v*",1,0))
defineMatcher(_MuPathTemplate, "Mu8",  lambda t : t.path("HLT_Mu8_v*",1,0))

# SingleElectron
#defineMatcher(_ElPathTemplate, "Ele27Loose",  lambda t : t.path("HLT_Ele27_WPLoose_Gsf_v*",1,0))
defineMatcher(_ElPathTemplate, "Ele35Tight",  lambda t : t.path("HLT_Ele35_WPTight_Gsf_v*",1,0))
defineMatcher(_ElPathTemplate, "Ele32Tight",  lambda t : t.path("HLT_Ele32_WPTight_Gsf_v*",1,0))


# Define a Sequence and a Mixin Type
LeptonTriggerMatchersSequence = allTriggerMatchers.values()
WithLeptonTriggerMatchType = NTupleObjectType("withLeptonTriggerMatchType", baseObjectTypes = [], variables = [
    NTupleVariable(k, eval("lambda x : getattr(x, 'matchedTrgObj%s', None) != None" % k), int, help = 'TriggerMatching: '+k) for k in allTriggerMatchers.keys()
])

