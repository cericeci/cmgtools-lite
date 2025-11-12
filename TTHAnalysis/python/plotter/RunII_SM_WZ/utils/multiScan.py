import os
from multiprocessing import Pool
from contextlib import closing
import time

#base = "combine WZ_AC_m3LmetLegacy.root -M MultiDimFit -t -1 --expectSignal 1 -P cwww -P cb --floatOtherPOIs=0 --cl=0.95 --algo=grid --points=40000 --minimizerStrategy=2 -m [NUM] --firstPoint=[FIRST] --lastPoint=[LAST] -n cwww_cb --setPhysicsModelParameterRanges cb=-300.0,300.0:cwww=-6.0,6.0"
#base = "combine -M MultiDimFit WZ161718_pol.card.root  -P fLR -P fO --algo grid -t -1 --setParameters fLR=-0.112,fO=0.260,mu=1 --freezeParameter mu -m [NUM] -n 161718 -v 1 --firstPoint=[FIRST] --lastPoint=[LAST] --setParameterRanges fLR=-1.,1.:fO=-1.,1.  --points=640000"


base = "combine -M MultiDimFit polZ.root --algo grid --redefineSignalPOIs fLR,fO --freezeParameter mu --floatOtherPOIs 1 -m [NUM] -v 1 --firstPoint=[FIRST] --lastPoint=[LAST] --setParameterRanges fLR=-0.4,0.4:fO=0.15,0.35   --setParameters fLR=-0.116,fO=0.258,mu=1 --points=64000"

totaljobs = 640
nPoints = 64000
dN = nPoints/totaljobs + 1
commands = []

used = 0

for i in range(totaljobs):
  commands.append(base.replace("[NUM]",str(i)).replace("[FIRST]", str(used)).replace("[LAST]", str(used + dN-1)))
  used = used + dN

#print commands


def execute(com):
  os.system(com)

with closing(Pool(64)) as p:
	print "Now running " + str(len(commands)) + " commands using: " + str(80) + " processes. Please wait" 
	retlist1 = p.map_async(execute, commands, 1)
    	while not retlist1.ready():
       		print("Combine runs left: {}".format(retlist1._number_left ))
       		time.sleep(1)
    	retlist1 = retlist1.get()
   	p.close()
    	p.join()
	p.terminate()

