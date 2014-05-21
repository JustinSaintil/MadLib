#! /usr/bin/env python

import wx
from buttonmodule import *
# * imports everything in the module

vehicle = random.choice(vehicles)
names = random.choice(names)
objects = random.choice(objects)
places = random.choice(places)
verbs = random.choice(verbs)
adj = random.choice(adj)


app = wx.App(False) 
frame = MadLibFrame(None)
frame.Show()
app.MainLoop()
