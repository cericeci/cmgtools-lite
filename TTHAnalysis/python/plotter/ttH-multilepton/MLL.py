import os
from getCardsModule import*

dr1 = "  'if3(nLepFO>1,mass_2(LepGood1_conePt,LepGood1_eta,LepGood1_phi,LepGood1_mass,LepGood2_conePt,LepGood2_eta,LepGood2_phi,LepGood2_mass),-99)':'if3(nLepFO>1,mass_2(LepGood1_conePt,LepGood1_eta,LepGood1_phi,LepGood1_mass,LepGood2_conePt,LepGood2_eta,LepGood2_phi,LepGood2_mass),-99)' 4,0.,400.,4,0.,400. "
funcdr1  = " 4:MLL2Dto1D_4 "
outdr1_c = " /afs/cern.ch/user/c/cericeci/private/CMSSW_7_4_7/HiggsAnalysis/CombinedLimit/scripts/cards/ttH_all/MLL_CAT_4BINS "
outdr1_nc = " /afs/cern.ch/user/c/cericeci/private/CMSSW_7_4_7/HiggsAnalysis/CombinedLimit/scripts/cards/ttH_all/MLL_NOCAT_4BINS "
getCatCards(base,funcdr1,dr1,outdr1_c,"2lss")
getUnCatCards(base,funcdr1,dr1,outdr1_nc,"2lss")

dr1 = "  'if3(nLepFO>1,mass_2(LepGood1_conePt,LepGood1_eta,LepGood1_phi,LepGood1_mass,LepGood2_conePt,LepGood2_eta,LepGood2_phi,LepGood2_mass),-99)':'if3(nLepFO>1,mass_2(LepGood1_conePt,LepGood1_eta,LepGood1_phi,LepGood1_mass,LepGood2_conePt,LepGood2_eta,LepGood2_phi,LepGood2_mass),-99)' 6,0.,400.,6,0.,400. "
funcdr1  = " 6:MLL2Dto1D_6 "
outdr1_c = " /afs/cern.ch/user/c/cericeci/private/CMSSW_7_4_7/HiggsAnalysis/CombinedLimit/scripts/cards/ttH_all/MLL_CAT_6BINS "
outdr1_nc = " /afs/cern.ch/user/c/cericeci/private/CMSSW_7_4_7/HiggsAnalysis/CombinedLimit/scripts/cards/ttH_all/MLL_NOCAT_6BINS "
getCatCards(base,funcdr1,dr1,outdr1_c,"2lss")
getUnCatCards(base,funcdr1,dr1,outdr1_nc,"2lss")

dr1 = "  'if3(nLepFO>1,mass_2(LepGood1_conePt,LepGood1_eta,LepGood1_phi,LepGood1_mass,LepGood2_conePt,LepGood2_eta,LepGood2_phi,LepGood2_mass),-99)':'if3(nLepFO>1,mass_2(LepGood1_conePt,LepGood1_eta,LepGood1_phi,LepGood1_mass,LepGood2_conePt,LepGood2_eta,LepGood2_phi,LepGood2_mass),-99)' 8,0.,400.,8,0.,400. "
funcdr1  = " 8:MLL2Dto1D_8 "
outdr1_c = " /afs/cern.ch/user/c/cericeci/private/CMSSW_7_4_7/HiggsAnalysis/CombinedLimit/scripts/cards/ttH_all/MLL_CAT_8BINS "
outdr1_nc = " /afs/cern.ch/user/c/cericeci/private/CMSSW_7_4_7/HiggsAnalysis/CombinedLimit/scripts/cards/ttH_all/MLL_NOCAT_8BINS "
getCatCards(base,funcdr1,dr1,outdr1_c,"2lss")
getUnCatCards(base,funcdr1,dr1,outdr1_nc,"2lss")

dr1 = "  'if3(nLepFO>1,mass_2(LepGood1_conePt,LepGood1_eta,LepGood1_phi,LepGood1_mass,LepGood2_conePt,LepGood2_eta,LepGood2_phi,LepGood2_mass),-99)':'if3(nLepFO>1,mass_2(LepGood1_conePt,LepGood1_eta,LepGood1_phi,LepGood1_mass,LepGood2_conePt,LepGood2_eta,LepGood2_phi,LepGood2_mass),-99)' 10,0.,400.,10,0.,400. "
funcdr1  = " 10:MLL2Dto1D_10 "
outdr1_c = " /afs/cern.ch/user/c/cericeci/private/CMSSW_7_4_7/HiggsAnalysis/CombinedLimit/scripts/cards/ttH_all/MLL_CAT_10BINS "
outdr1_nc = " /afs/cern.ch/user/c/cericeci/private/CMSSW_7_4_7/HiggsAnalysis/CombinedLimit/scripts/cards/ttH_all/MLL_NOCAT_10BINS "
getCatCards(base,funcdr1,dr1,outdr1_c,"2lss")
getUnCatCards(base,funcdr1,dr1,outdr1_nc,"2lss")

dr1 = "  'if3(nLepFO>1,mass_2(LepGood1_conePt,LepGood1_eta,LepGood1_phi,LepGood1_mass,LepGood2_conePt,LepGood2_eta,LepGood2_phi,LepGood2_mass),-99)':'if3(nLepFO>1,mass_2(LepGood1_conePt,LepGood1_eta,LepGood1_phi,LepGood1_mass,LepGood2_conePt,LepGood2_eta,LepGood2_phi,LepGood2_mass),-99)' 12,0.,400.,12,0.,400. "
funcdr1  = " 12:MLL2Dto1D_12 "
outdr1_c = " /afs/cern.ch/user/c/cericeci/private/CMSSW_7_4_7/HiggsAnalysis/CombinedLimit/scripts/cards/ttH_all/MLL_CAT_12BINS "
outdr1_nc = " /afs/cern.ch/user/c/cericeci/private/CMSSW_7_4_7/HiggsAnalysis/CombinedLimit/scripts/cards/ttH_all/MLL_NOCAT_12BINS "
getCatCards(base,funcdr1,dr1,outdr1_c,"2lss")
getUnCatCards(base,funcdr1,dr1,outdr1_nc,"2lss")

dr1 = "  'if3(nLepFO>1,mass_2(LepGood1_conePt,LepGood1_eta,LepGood1_phi,LepGood1_mass,LepGood2_conePt,LepGood2_eta,LepGood2_phi,LepGood2_mass),-99)':'if3(nLepFO>1,mass_2(LepGood1_conePt,LepGood1_eta,LepGood1_phi,LepGood1_mass,LepGood2_conePt,LepGood2_eta,LepGood2_phi,LepGood2_mass),-99)' 14,0.,400.,14,0.,400. "
funcdr1  = " 14:MLL2Dto1D_14 "
outdr1_c = " /afs/cern.ch/user/c/cericeci/private/CMSSW_7_4_7/HiggsAnalysis/CombinedLimit/scripts/cards/ttH_all/MLL_CAT_14BINS "
outdr1_nc = " /afs/cern.ch/user/c/cericeci/private/CMSSW_7_4_7/HiggsAnalysis/CombinedLimit/scripts/cards/ttH_all/MLL_NOCAT_14BINS "
getCatCards(base,funcdr1,dr1,outdr1_c,"2lss")
getUnCatCards(base,funcdr1,dr1,outdr1_nc,"2lss")

dr1 = "  'if3(nLepFO>1,mass_2(LepGood1_conePt,LepGood1_eta,LepGood1_phi,LepGood1_mass,LepGood2_conePt,LepGood2_eta,LepGood2_phi,LepGood2_mass),-99)':'if3(nLepFO>1,mass_2(LepGood1_conePt,LepGood1_eta,LepGood1_phi,LepGood1_mass,LepGood2_conePt,LepGood2_eta,LepGood2_phi,LepGood2_mass),-99)' 16,0.,400.,16,0.,400. "
funcdr1  = " 16:MLL2Dto1D_16 "
outdr1_c = " /afs/cern.ch/user/c/cericeci/private/CMSSW_7_4_7/HiggsAnalysis/CombinedLimit/scripts/cards/ttH_all/MLL_CAT_16BINS "
outdr1_nc = " /afs/cern.ch/user/c/cericeci/private/CMSSW_7_4_7/HiggsAnalysis/CombinedLimit/scripts/cards/ttH_all/MLL_NOCAT_16BINS "
getCatCards(base,funcdr1,dr1,outdr1_c,"2lss")
getUnCatCards(base,funcdr1,dr1,outdr1_nc,"2lss")

dr1 = "  'if3(nLepFO>1,mass_2(LepGood1_conePt,LepGood1_eta,LepGood1_phi,LepGood1_mass,LepGood2_conePt,LepGood2_eta,LepGood2_phi,LepGood2_mass),-99)':'if3(nLepFO>1,mass_2(LepGood1_conePt,LepGood1_eta,LepGood1_phi,LepGood1_mass,LepGood2_conePt,LepGood2_eta,LepGood2_phi,LepGood2_mass),-99)' 18,0.,400.,18,0.,400. "
funcdr1  = " 18:MLL2Dto1D_18 "
outdr1_c = " /afs/cern.ch/user/c/cericeci/private/CMSSW_7_4_7/HiggsAnalysis/CombinedLimit/scripts/cards/ttH_all/MLL_CAT_18BINS "
outdr1_nc = " /afs/cern.ch/user/c/cericeci/private/CMSSW_7_4_7/HiggsAnalysis/CombinedLimit/scripts/cards/ttH_all/MLL_NOCAT_18BINS "
getCatCards(base,funcdr1,dr1,outdr1_c,"2lss")
getUnCatCards(base,funcdr1,dr1,outdr1_nc,"2lss")

dr1 = "  'if3(nLepFO>1,mass_2(LepGood1_conePt,LepGood1_eta,LepGood1_phi,LepGood1_mass,LepGood2_conePt,LepGood2_eta,LepGood2_phi,LepGood2_mass),-99)':'if3(nLepFO>1,mass_2(LepGood1_conePt,LepGood1_eta,LepGood1_phi,LepGood1_mass,LepGood2_conePt,LepGood2_eta,LepGood2_phi,LepGood2_mass),-99)' 20,0.,400.,20,0.,400. "
funcdr1  = " 20:MLL2Dto1D_20 "
outdr1_c = " /afs/cern.ch/user/c/cericeci/private/CMSSW_7_4_7/HiggsAnalysis/CombinedLimit/scripts/cards/ttH_all/MLL_CAT_20BINS "
outdr1_nc = " /afs/cern.ch/user/c/cericeci/private/CMSSW_7_4_7/HiggsAnalysis/CombinedLimit/scripts/cards/ttH_all/MLL_NOCAT_20BINS "
getCatCards(base,funcdr1,dr1,outdr1_c,"2lss")
getUnCatCards(base,funcdr1,dr1,outdr1_nc,"2lss")
