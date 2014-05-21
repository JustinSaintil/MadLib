#! /usr/bin/env python

import wx
from buttonmodule import *
# * imports everything in the module

vehicle = random.choice(vehicles)
names = random.choice(names)
objects = random.choice(objects)
place = random.choice(places)
verb = random.choice(verbs)
adj = random.choice(adj)
sent = random.choice(sent)

vehicle = @
name = $
objects = \
place = :
verb = _
adj = '

app = wx.App(False) 
frame = MadLibFrame(None)
frame.Show()
app.MainLoop()
