############### W
#Create the workspace
text2workspace.py WZ16_pol.card.txt -P HiggsAnalysis.CombinedLimit.PhysicsModel:BosonPolarizationWZ --PO fO=0.246 --PO fR=0.271 --PO fL=0.482
#Single best fit to pol fractions + normalization
combine -M MultiDimFit WZ16_pol.card.root  -P fLR -P fO --algo singles -t -1 --setParameters fLR=0.211,fO=0.246,mu=1 --freezeParameter mu   -v 1 --cl 0.68
#Longitudinal polarization significance
combine -M Significance WZ16_pol.card.root --redefineSignalPOIs fO  -t -1 --setParameters fLR=0.211,fO=0.246,mu=1 --freezeParameter mu,fLR   -v 1 

############## Z
text2workspace.py WZ16_pol.card.txt -P HiggsAnalysis.CombinedLimit.PhysicsModel:BosonPolarizationWZ --PO fO=0.260 --PO fR=0.426 --PO fL=0.314
combine -M MultiDimFit WZ16_pol.card.root  -P fLR -P fO --algo singles -t -1 --setParameters fLR=-0.112,fO=0.260,mu=1 --freezeParameter mu   -v 1 --cl 0.68
combine -M Significance WZ16_pol.card.root --redefineSignalPOIs fO  -t -1 --setParameters fLR=-0.112,fO=0.260,mu=1 --freezeParameter mu,fLR   -v 1

############## WP
text2workspace.py WZ16_pol.card.txt -P HiggsAnalysis.CombinedLimit.PhysicsModel:BosonPolarizationWZ --PO fO=0.229 --PO fR=0.233 --PO fL=0.538
combine -M MultiDimFit WZ16_pol.card.root  -P fLR -P fO --algo singles -t -1 --setParameters fLR=0.229,fO=0.305,mu=1 --freezeParameter mu   -v 1 --cl 0.68
combine -M Significance WZ16_pol.card.root --redefineSignalPOIs fO  -t -1 --setParameters fLR=0.229,fO=0.305,mu=1 --freezeParameter mu,fLR   -v 1

############## WM
text2workspace.py WZ16_pol.card.txt -P HiggsAnalysis.CombinedLimit.PhysicsModel:BosonPolarizationWZ --PO fO=0.277 --PO fR=0.331 --PO fL=0.392
combine -M MultiDimFit WZ16_pol.card.root  -P fLR -P fO --algo singles -t -1 --setParameters fLR=0.061,fO=0.277,mu=1 --freezeParameter mu   -v 1 --cl 0.68
combine -M Significance WZ16_pol.card.root --redefineSignalPOIs fO  -t -1 --setParameters fLR=0.061,fO=0.277,mu=1 --freezeParameter mu,fLR   -v 1


############## ZP
text2workspace.py WZ16_pol.card.txt -P HiggsAnalysis.CombinedLimit.PhysicsModel:BosonPolarizationWZ --PO fO=0.269 --PO fR=0.401 --PO fL=0.331
combine -M MultiDimFit WZ16_pol.card.root  -P fLR -P fO --algo singles -t -1 --setParameters fLR=-0.070,fO=0.269,mu=1 --freezeParameter mu   -v 1 --cl 0.68
combine -M Significance WZ16_pol.card.root --redefineSignalPOIs fO  -t -1 --setParameters fLR=-0.070,fO=0.269,mu=1 --freezeParameter mu,fLR   -v 1

############## ZM
text2workspace.py WZ16_pol.card.txt -P HiggsAnalysis.CombinedLimit.PhysicsModel:BosonPolarizationWZ --PO fO=0.246 --PO fR=0.466 --PO fL=0.288
combine -M MultiDimFit WZ16_pol.card.root  -P fLR -P fO --algo singles -t -1 --setParameters fLR=-0.158,fO=0.246,mu=1 --freezeParameter mu   -v 1 --cl 0.68
combine -M Significance WZ16_pol.card.root --redefineSignalPOIs fO  -t -1 --setParameters fLR=-0.158,fO=0.246,mu=1 --freezeParameter mu,fLR   -v 1
