#!/usr/bin/env python
from CMGTools.TTHAnalysis.plotter.mcAnalysis import *
from CMGTools.TTHAnalysis.plotter.histoWithNuisances import _cloneNoDir
import re, sys, os, os.path
import copy
systs = {}

from optparse import OptionParser
parser = OptionParser(usage="%prog [options] mc.txt cuts.txt var bins")
addMCAnalysisOptions(parser)
parser.add_option("--od", "--outdir", dest="outdir", type="string", default=None, help="output directory name") 
parser.add_option("--asimov", dest="asimov", type="string", default=None, help="Use an Asimov dataset of the specified kind: including signal ('signal','s','sig','s+b') or background-only ('background','bkg','b','b-only')")
parser.add_option("--bbb", dest="bbb", type="string", default=None, help="Options for bin-by-bin statistical uncertainties with the specified nuisance name")
parser.add_option("--amc", "--autoMCStats", dest="autoMCStats", action="store_true", default=False, help="use autoMCStats")
parser.add_option("--autoMCStatsThreshold", dest="autoMCStatsValue", type="int", default=10, help="threshold to put on autoMCStats")
parser.add_option("--infile", dest="infile", action="store_true", default=False, help="Read histograms to file")
parser.add_option("--savefile", dest="savefile", action="store_true", default=False, help="Save histos to file")
parser.add_option("--categorize", dest="categ", type="string", nargs=3, default=None, help="Split in categories. Requires 3 arguments: expression, binning, bin labels")
parser.add_option("--regularize", dest="regularize", action="store_true", default=False, help="Regularize templates")
parser.add_option("--ms", dest="multiSignals", action="store_true", default=False, help="Create a card for each process tagged as signal")
parser.add_option("--addgmN", dest="addgmN", action="store_true", default=False, help="Create extra process + nuisance for MC with low stats in each bin ")

(options, args) = parser.parse_args()
options.weight = True
options.final  = True

if "/functions_cc.so" not in ROOT.gSystem.GetLibraries(): 
    ROOT.gROOT.ProcessLine(".L %s/src/CMGTools/TTHAnalysis/python/plotter/functions.cc+" % os.environ['CMSSW_BASE']);

mca  = MCAnalysis(args[0],options)
cuts = CutsFile(args[1],options)

binname = os.path.basename(args[1]).replace(".txt","") if options.binname == 'default' else options.binname
if binname[0] in "1234567890": raise RuntimeError("Bins should start with a letter.")
outdir  = options.outdir+"/" if options.outdir else ""
if not os.path.exists(outdir): os.mkdir(outdir)

report={}
if options.infile:
    infile = ROOT.TFile(outdir+binname+".bare.root","read")
    for p in mca.listSignals(True)+mca.listBackgrounds(True)+['data']:
        variations = mca.getProcessNuisances(p) if p != "data" else []
        h = readHistoWithNuisances(infile, "x_"+p, variations, mayBeMissing=True)
        if h: report[p] = h
else:
    if options.categ:
       cexpr, cbins, _ = options.categ
       report = mca.getPlotsRaw("x", cexpr+":"+args[2], makeBinningProductString(args[3],cbins), cuts.allCuts(), nodata=options.asimov) 
    else:
       report = mca.getPlotsRaw("x", args[2], args[3], cuts.allCuts(), nodata=options.asimov) 
    for p,h in report.iteritems(): h.cropNegativeBins()

if options.savefile:
    savefile = ROOT.TFile(outdir+binname+".bare.root","recreate")
    for k,h in report.iteritems(): 
        h.writeToFile(savefile, takeOwnership=False)
    savefile.Close()

if options.asimov:
    if options.asimov in ("s","sig","signal","s+b"):
        asimovprocesses = mca.listSignals() + mca.listBackgrounds()
    elif options.asimov in ("b","bkg","background", "b-only"):
        asimovprocesses = mca.listBackgrounds()
    else: raise RuntimeError("the --asimov option requires to specify signal/sig/s/s+b or background/bkg/b/b-only")
    tomerge = None
    for p in asimovprocesses:
        if p in report: 
            if tomerge is None: 
                tomerge = report[p].raw().Clone("x_data_obs"); tomerge.SetDirectory(None)
            else: tomerge.Add(report[p].raw())
    report['data_obs'] = HistoWithNuisances(tomerge)
else:
    report['data_obs'] = report['data'].Clone("x_data_obs") 

if options.categ:
    allreports = dict()
    catlabels = options.categ[2].split(",")
    if len(catlabels) != report["data_obs"].GetNbinsY(): raise RuntimeError("Mismatch between category labels and bins")
    for ic,lab in enumerate(catlabels):
        allreports["%s_%s"%(binname,lab)] = dict( (k, h.projectionX("x_"+k,ic+1,ic+1)) for (k,h) in report.iteritems() )
else:
    allreports = {binname:report}


for binname, report in allreports.iteritems():
  if options.bbb:
    if options.autoMCStats: raise RuntimeError("Can't use --bbb together with --amc/--autoMCStats")
    for p,h in report.iteritems(): 
      if p not in ("data", "data_obs"):
        h.addBinByBin(namePattern="%s_%s_%s_bin{bin}" % (options.bbb, binname, p), conservativePruning = True)
  addToProcs = []
  extrareport = {}
  if options.addgmN:
    for p,h in report.iteritems():
      if p not in ("data", "data_obs"):
        theW, theBins = h.GetEmptyBins()
        if theW < 0.25 or "data" in p: continue
        for b in theBins:
          extrareport[p + "_statbin"+str(b) + "_w%1.3f"%theW] = h.Clone("x_" + p + "_statbin"+str(b) + "_w%1.3f"%theW)
          extrareport[p + "_statbin"+str(b) + "_w%1.3f"%theW].gmNWeight = theW
          extrareport[p + "_statbin"+str(b) + "_w%1.3f"%theW].variations[extrareport[p + "_statbin"+str(b) + "_w%1.3f"%theW].central.GetName()+ "_statbin" + str(b) + "_w%1.3f"%theW] = [extrareport[p + "_statbin"+str(b) + "_w%1.3f"%theW].central, extrareport[p + "_statbin"+str(b) + "_w%1.3f"%theW].central]
          addToProcs.append(p + "_statbin"+str(b) + "_w%1.3f"%theW)
          for bb in xrange(1,extrareport[p + "_statbin"+str(b) + "_w%1.3f"%theW].GetNbinsX()+1):
            if bb != b:
              extrareport[p + "_statbin"+str(b) + "_w%1.3f"%theW].SetBinContent(bb, 0)
              extrareport[p + "_statbin"+str(b) + "_w%1.3f"%theW].SetBinError(bb, 0)
              for vv in extrareport[p + "_statbin"+str(b) + "_w%1.3f"%theW].variations:
                extrareport[p + "_statbin"+str(b) + "_w%1.3f"%theW].variations[vv][0].SetBinContent(bb,0)
                extrareport[p + "_statbin"+str(b) + "_w%1.3f"%theW].variations[vv][0].SetBinError(bb,0)
                extrareport[p + "_statbin"+str(b) + "_w%1.3f"%theW].variations[vv][1].SetBinContent(bb,0)
                extrareport[p + "_statbin"+str(b) + "_w%1.3f"%theW].variations[vv][1].SetBinError(bb,0)

            else:
              extrareport[p + "_statbin"+str(b) + "_w%1.3f"%theW].SetBinContent(bb, 1e-3)
              extrareport[p + "_statbin"+str(b) + "_w%1.3f"%theW].SetBinError(bb, 0)
              for vv in extrareport[p + "_statbin"+str(b) + "_w%1.3f"%theW].variations:
                extrareport[p + "_statbin"+str(b) + "_w%1.3f"%theW].variations[vv][0].SetBinContent(bb,1e-3)
                extrareport[p + "_statbin"+str(b) + "_w%1.3f"%theW].variations[vv][0].SetBinError(bb,0)
                extrareport[p + "_statbin"+str(b) + "_w%1.3f"%theW].variations[vv][1].SetBinContent(bb,1e-3)
                extrareport[p + "_statbin"+str(b) + "_w%1.3f"%theW].variations[vv][1].SetBinError(bb,0)


    for p,h in extrareport.iteritems():
      report[p] = h

  for p,h in report.iteritems():
    for b in xrange(1,h.GetNbinsX()+1):
      h.SetBinError(b,min(h.GetBinContent(b),h.GetBinError(b))) # crop all uncertainties to 100% to avoid negative variations
  nuisances = sorted(listAllNuisances(report))

  allyields = dict([(p,h.Integral()) for p,h in report.iteritems()])
  procs = []; iproc = {}
  for i,s in enumerate(mca.listSignals()):
    if s not in allyields: continue
    if allyields[s] == 0: continue
    procs.append(s); iproc[s] = i-len(mca.listSignals())+1
  for i,b in enumerate(mca.listBackgrounds()):
    if b not in allyields: continue
    if allyields[b] == 0: continue
    procs.append(b); iproc[b] = i+1
 
  for p in addToProcs:
    i += 1
    if not(p in procs):
      procs.append(p)
      iproc[p] = i + 1
    
  for p in procs: print "%-10s %10.4f" % (p, allyields[p])

  systs = {}
  for name in nuisances:
    effshape = {}
    isShape = False
    for p in procs:
        h = report[p]
        n0 = h.Integral()
        print p, h, name, h.hasVariation(name)
        if h.hasVariation(name):
            if isShape or h.isShapeVariation(name):
                if name.endswith("_lnU"): 
                    raise RuntimeError("Nuisance %s should be lnU but has shape effect on %s" % (name,p))
                #print "Nuisance %s has a shape effect on process %s" % (name, p)
                #if "templstat" not in name and not isShape:
                #    h.isShapeVariation(name,debug=True)
                isShape = True
            variants = list(h.getVariation(name))
            for hv,d in zip(variants, ('up','down')):
                k = hv.Integral()/n0
                if k == 0: 
                    print "Warning: underflow template for %s %s %s %s. Will take the nominal scaled down by a factor 2" % (binname, p, name, d)
                    hv.Add(h.raw()); hv.Scale(0.5)
                elif k < 0.2 or k > 5:
                    print "Warning: big shift in template for %s %s %s %s: kappa = %g " % (binname, p, name, d, k)
            effshape[p] = variants 
    if isShape:
        if options.regularize: 
            for p in procs:
                report[p].regularizeVariation(name,binname=binname)
        systs[name] = ("shape", dict((p,"1" if p in effshape else "-") for p in procs), effshape)
    else:
        effyield = dict((p,"-") for p in procs)
        isNorm = False
        for p,(hup,hdn) in effshape.iteritems():
            i0 = allyields[p]
            kup, kdn = hup.Integral()/i0, hdn.Integral()/i0
            if abs(kup*kdn-1)<1e-5:
                if abs(kup-1)>2e-4:
                    effyield[p] = "%.3f" % kup
                    isNorm = True
            else:
                effyield[p] = "%.3f/%.3f" % (kdn,kup)
                isNorm = True
        if isNorm:
            if name.endswith("_lnU"):
                systs[name] = ("lnU", effyield, {})
            else:
                systs[name] = ("lnN", effyield, {})
  # make a new list with only the ones that have an effect
  nuisances = sorted(systs.keys())
  if not(options.multiSignals):
    datacard = open(outdir+binname+".card.txt", "w"); 
    datacard.write("## Datacard for cut file %s\n"%args[1])
    datacard.write("shapes *        * %s.input.root x_$PROCESS x_$PROCESS_$SYSTEMATIC\n" % binname)
    datacard.write('##----------------------------------\n')
    datacard.write('bin         %s\n' % binname)
    datacard.write('observation %s\n' % allyields['data_obs'])
    datacard.write('##----------------------------------\n')
    klen = max([7, len(binname)]+[len(p) for p in procs])
    kpatt = " %%%ds "  % klen
    fpatt = " %%%d.%df " % (klen,3)
    npatt = "%%-%ds " % max([len('process')]+map(len,nuisances))
    datacard.write('##----------------------------------\n')
    datacard.write((npatt % 'bin    ')+(" "*6)+(" ".join([kpatt % binname  for p in procs]))+"\n")
    datacard.write((npatt % 'process')+(" "*6)+(" ".join([kpatt % p        for p in procs]))+"\n")
    datacard.write((npatt % 'process')+(" "*6)+(" ".join([kpatt % iproc[p] for p in procs]))+"\n")
    datacard.write((npatt % 'rate   ')+(" "*6)+(" ".join([fpatt % allyields[p] for p in procs]))+"\n")
    datacard.write('##----------------------------------\n')
    towrite = [ report[p].raw() for p in procs ] + [ report["data_obs"].raw() ]
    for name in nuisances:
      (kind,effmap,effshape) = systs[name]
      datacard.write(('%s %5s' % (npatt % name,kind)) + " ".join([kpatt % effmap[p]  for p in procs]) +"\n")
      for p,(hup,hdn) in effshape.iteritems():
        towrite.append(hup.Clone("x_%s_%sUp"   % (p,name)))
        towrite.append(hdn.Clone("x_%s_%sDown" % (p,name)))
    if options.autoMCStats: 
      datacard.write('* autoMCStats %d\n' % options.autoMCStatsValue)

    workspace = ROOT.TFile.Open(outdir+binname+".input.root", "RECREATE")
    for h in towrite:
        workspace.WriteTObject(h,h.GetName())
    workspace.Close()
    print "Wrote to {0}.card.txt and {0}.input.root ".format(outdir+binname)
  else:
   towrite = [ report[p].raw() for p in procs ] + [ report["data_obs"].raw() ]
   for name in nuisances:
     (kind,effmap,effshape) = systs[name]
     for p,(hup,hdn) in effshape.iteritems():
       towrite.append(hup.Clone("x_%s_%sUp"   % (p,name)))
       towrite.append(hdn.Clone("x_%s_%sDown" % (p,name)))

   for s in mca.listSignals():
    newprocs = []
    for key in procs:
      if (key in mca.listBackgrounds() or key==s): 
        newprocs.append(key)
        for p in addToProcs:
          if not "sig" in p and not(p in newprocs):
            newprocs.append(p)

    datacard = open(outdir+binname+s+".card.txt", "w");
    datacard.write("## Datacard for cut file %s\n"%args[1])
    datacard.write("shapes *        * %s.input.root x_$PROCESS x_$PROCESS_$SYSTEMATIC\n" % binname)
    datacard.write('##----------------------------------\n')
    datacard.write('bin         %s\n' % binname)
    datacard.write('observation %s\n' % allyields['data_obs'])
    datacard.write('##----------------------------------\n')
    klen = max([7, len(binname)]+[len(p) for p in newprocs])
    kpatt = " %%%ds "  % klen
    fpatt = " %%%d.%df " % (klen,3)
    npatt = "%%-%ds " % max([len('process')]+map(len,nuisances))
    datacard.write('##----------------------------------\n')
    datacard.write((npatt % 'bin    ')+(" "*6)+(" ".join([kpatt % binname  for p in newprocs]))+"\n")
    datacard.write((npatt % 'process')+(" "*6)+(" ".join([kpatt % p        for p in newprocs]))+"\n")
    datacard.write((npatt % 'process')+(" "*6)+(" ".join([kpatt % iproc[p] for p in newprocs]))+"\n")
    datacard.write((npatt % 'rate   ')+(" "*6)+(" ".join([fpatt % allyields[p] for p in newprocs]))+"\n")
    datacard.write('##----------------------------------\n')
    for name in nuisances:
      (kind,effmap,effshape) = systs[name]
      datacard.write(('%s %5s' % (npatt % name,kind)) + " ".join([kpatt % effmap[p]  for p in newprocs]) +"\n")
    if options.autoMCStats:
      datacard.write('* autoMCStats %d\n' % options.autoMCStatsValue)
    if options.addgmN:
      for p in newprocs:
        if "statbin" in p:
          words = p.split("_")
          theweight = float(words[-1].replace("w",""))/1e-3
          
          datacard.write(('%s lnN ' % (p)) + " ".join([kpatt % "-" if pp!=p else kpatt%("1/%1.4f"%theweight) for pp in newprocs]) +"\n")
    print "Wrote to %s "%(outdir+s+".card.txt")
   workspace = ROOT.TFile.Open(outdir+binname+".input.root", "RECREATE")
   for h in towrite:
      workspace.WriteTObject(h,h.GetName())
   workspace.Close()
   print "Wrote to {0}.card.txt and {0}.input.root ".format(outdir+binname)
