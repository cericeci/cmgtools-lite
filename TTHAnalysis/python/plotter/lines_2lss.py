import ROOT
items = [
  {"name":"mt2",
   "mode":"range",
   "before":7,
   "after":10,
   "y1":0.1,
   "y2":65000,
   "style":1,
   "color":ROOT.kBlue+3,
   "widht":4,
   "doOnRatio":True,
  },
  {"name":"ptll1",
   "mode":"range",
   "before":2,
   "after":6,
   "y1":0.1,
   "y2":20000,
   "style":9,
   "color":ROOT.kBlue+3,
   "widht":3,
   "doOnRatio":True,
  },
  {"name":"ptll2",
   "mode":"range",
   "before":7,
   "after":9,
   "y1":0.1,
   "y2":20000,
   "style":9,
   "color":ROOT.kBlue+3,
   "widht":3,
   "doOnRatio":True,
  },

  {"name":"ptll2",
   "mode":"range",
   "before":11,
   "after":15,
   "y1":0.1,
   "y2":20000,
   "style":9,
   "color":ROOT.kBlue+3,
   "widht":3,
   "doOnRatio":True,
  },


  {"name":"lowmt2",
   "mode":"text",
   "x":2.5,
   "y":30000,
   "size":0.036,
   "text":"M_{T2} (ll) = 0 GeV",
   "doOnRatio":True,
  },
  {"name":"lowmt2",
   "mode":"text",
   "x":6.57,
   "y":30000,
   "size":0.036,
   "text":"0 GeV < M_{T2} (ll) #leq 80 GeV",
   "doOnRatio":True,
  },
  {"name":"lowmt2",
   "mode":"text",
   "x":14.3,
   "y":30000,
   "size":0.036,
   "text":"M_{T2} (ll) > 80 GeV",
   "doOnRatio":True,
  },

  {"name":"lowmt2",
   "mode":"text",
   "x":1.29,
   "y":1200,
   "size":0.027,
   "text":"p_{T} (ll)< 70 GeV",
   "doOnRatio":True,
   "angle": 90
  },

  {"name":"lowmt2",
   "mode":"text",
   "x":3.1,
   "y":12000,
   "size":0.025,
   "text":"p_{T} (ll) #geq 70 GeV",
   "doOnRatio":True,
  },


  {"name":"lowmt2",
   "mode":"text",
   "x":7.15,
   "y":12000,
   "size":0.025,
   "text":"p_{T} (ll) < 30 GeV",
   "doOnRatio":True,
  },

  {"name":"lowmt2",
   "mode":"text",
   "x":9.57,
   "y":9500,
   "size":0.022,
   "text":"#splitline{p_{T} (ll)}{#geq 30 GeV}",
   "doOnRatio":True,
  },

  {"name":"lowmt2",
   "mode":"text",
   "x":12.1,
   "y":12000,
   "size":0.025,
   "text":"p_{T} (ll) < 200 GeV",
   "doOnRatio":True,
  },

  {"name":"lowmt2",
   "mode":"text",
   "x":17.2,
   "y":12000,
   "size":0.025,
   "text":"p_{T} (ll) #geq 200 GeV",
   "doOnRatio":True,
  },

  {"name":"lowmt2",
   "mode":"text",
   "x":9.5,
   "y":-1.9,
   "size":0.115,
   "text":"p_{T}^{miss} (GeV)/Charge",
   "doOnRatio":True,
   "forceRatio":True,
  },

]