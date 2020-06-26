accidenteCofCof = {
    2016: '',
    2017: '-P /pool/cienciasrw/HeppyTrees/RA7/nanoAODv4_2017_unSkimmed_estructure/',
    2018: '',
}
lumi = {
    2016: 35.9,
    2017: 41.2,
    2018: 58.9,
}
prefiringTrees = {
    2016: '--FMCs {P}/trigger_prefiring/',
    2017: '--FMCs {P}/trigger_prefiring/',
    2018: '',
}
prefiringWeights = {
    2016: '*weight_PrefiringJets*weight_PrefiringPhotons',
    2017: '*weight_PrefiringJets*weight_PrefiringPhotons',
    2018: '',
}
pileupTrees = {
    2016: '--FMCs {P}/pileUpWeight/',
    2017: '--FMCs {P}/pileUpWeights/',
    2018: '--FMCs {P}/pileUpWeight/',
}
pileupWeights = {
    2016: 'puWeight',
    2017: 'puWeight',
    2018: 'vtxWeight2018Nominal',
}
triggerTrees = {
    2016: '--Fs {P}/trigger_2016/',
    2017: '--mcc RunII_SM_WZ/2017/mcc_triggerdefs.txt',
    2018: '--mcc RunII_SM_WZ/2018/mcc_triggerdefs.txt',
}

