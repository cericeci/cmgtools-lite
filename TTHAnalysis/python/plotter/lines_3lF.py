import ROOT
items = [
  {"name":"lowmtw",
   "mode":"range",
   "before":1,
   "after":10,
   "y1":0.5,
   "y2":8000,
   "style":1,
   "color":ROOT.kBlue+3,
   "widht":4,
   "doOnRatio":True,
  },
  {"name":"lowmll",
   "mode":"range",
   "before":1,
   "after":6,
   "y1":0.5,
   "y2":2000,
   "style":9,
   "color":ROOT.kBlue+3,
   "widht":3,
   "doOnRatio":True,
  },
  {"name":"highmt2",
   "mode":"text",
   "x":10.6,
   "y":2000,
   "size":0.050,
   "text":"#splitline{M_{T2}(l#tau_{h})}{#geq 100 GeV}",
   "doOnRatio":True,
  },
  {"name":"lowmt2",
   "mode":"text",
   "x":7.5,
   "y":3600,
   "size":0.050,
   "text":"M_{T2}(l#tau_{h}) < 100 GeV",
   "doOnRatio":True,
  },
  {"name":"low mll",
   "mode":"text",
   "x":3.1,
   "y":800,
   "size":0.042,
   "text":"M_{l#tau_{h}} < 100 GeV",
   "doOnRatio":True,
  },
  {"name":"high mll",
   "mode":"text",
   "x":7.8,
   "y":800,
   "size":0.042,
   "text":"M_{l#tau_{h}} #geq 100 GeV",
   "doOnRatio":True,
  },
]
