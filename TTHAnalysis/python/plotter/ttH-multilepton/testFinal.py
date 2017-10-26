import os
from getCardsModule import*

lumVals = ["100.","120."]

for l in lumVals:
	dr1 = " mindr_lep1_jet:mindr_lep1_jet 30,0.4,3.,30,0.4,3. "
	funcdr1  = " 5:_2lss_sel "
	outdr1_c = " /afs/cern.ch/work/c/cericeci/private/ttHTest/%s "%l
	outdr1_nc = " /afs/cern.ch/work/c/cericeci/private/ttHTest/ "
	getCatCards(base,funcdr1,dr1,outdr1_c,"2lss",l)
#getUnCatCards(base,funcdr1,dr1,outdr1_nc,"2lss")

	dr1 = " mindr_lep1_jet:mindr_lep1_jet 30,0.4,3.,30,0.4,3. "
	funcdr1  = " 3:_3l_sel "
	outdr1_c = " /afs/cern.ch/work/c/cericeci/private/ttHTest/%s "%l
	outdr1_nc = " /afs/cern.ch/work/c/cericeci/private/ttHTest/ "
	getCatCards(base,funcdr1,dr1,outdr1_c,"3l",l)
#getUnCatCards(base,funcdr1,dr1,outdr1_nc,"3l")

	dr1 = " mindr_lep1_jet:mindr_lep1_jet 2,0.4,3.,2,0.4,3. "
	funcdr1  = " 1:_4l_sel "
	outdr1_c = " /afs/cern.ch/work/c/cericeci/private/ttHTest/%s "%l
	outdr1_nc = " /afs/cern.ch/work/c/cericeci/private/ttHTest/ "
	getCatCards(base,funcdr1,dr1,outdr1_c,"4l",l)
#getUnCatCards(base,funcdr1,dr1,outdr1_nc,"4l")
