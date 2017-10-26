import os
from getCardsModule import*

lumVals = ["20.","40.","60."]

for l in lumVals:
	dr1 = " kinMVA_2lss_ttV_withHj:kinMVA_2lss_ttbar_withBDTv8 40,-1,1,40,-1,1 "
	funcdr1  = " 8:OurBin2l "
	outdr1_c = " /afs/cern.ch/work/c/cericeci/private/ttHTest/BDT%s "%l
	outdr1_nc = " /afs/cern.ch/work/c/cericeci/private/ttHTest/ "
	getCatCards(base,funcdr1,dr1,outdr1_c,"2lss",l)
#getUnCatCards(base,funcdr1,dr1,outdr1_nc,"2lss")

	dr1 = " kinMVA_3l_ttV_withMEM:kinMVA_3l_ttbar 40,-1,1,40,-1,1 "
	funcdr1  = " 5:OurBin3lMEM "
	outdr1_c = " /afs/cern.ch/work/c/cericeci/private/ttHTest/BDT%s "%l
	outdr1_nc = " /afs/cern.ch/work/c/cericeci/private/ttHTest/ "
	getCatCards(base,funcdr1,dr1,outdr1_c,"3l",l)
#getUnCatCards(base,funcdr1,dr1,outdr1_nc,"3l")

	dr1 = " mindr_lep1_jet:mindr_lep1_jet 2,0.4,3.,2,0.4,3. "
	funcdr1  = " 1:_4l_sel "
	outdr1_c = " /afs/cern.ch/work/c/cericeci/private/ttHTest/BDT%s "%l
	outdr1_nc = " /afs/cern.ch/work/c/cericeci/private/ttHTest/ "
	getCatCards(base,funcdr1,dr1,outdr1_c,"4l",l)
#getUnCatCards(base,funcdr1,dr1,outdr1_nc,"4l")
