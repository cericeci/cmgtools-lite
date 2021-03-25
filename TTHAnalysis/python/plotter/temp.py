import ROOT

tf = ROOT.TFile("RunIIAC_datafakes.root", "READ")

tNom = tf.Get("pol_Wpt_diboson")
tVars = ["pol_Wpt_prompt_WZ_aTGC_cw","pol_Wpt_prompt_WZ_aTGC_cwww","pol_Wpt_prompt_WZ_aTGC_cb","pol_Wpt_prompt_WZ_aTGC_cpw","pol_Wpt_prompt_WZ_aTGC_cpwww"]

for t in tVars:
  val = []
  tVar = tf.Get(t)
  tVar.Divide(tNom)
  for iB in range(1, tNom.GetNbinsX()+2):
    val.append("%1.5f"%tVar.GetBinContent(iB))

  print t.split("_")[-1],",".join(val)
