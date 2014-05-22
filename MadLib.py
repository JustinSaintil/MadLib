#! /usr/bin/env python

import wx
from buttonmodule import *
from TextBox import *
from  CheckBoxes import *
# * imports everything in the module


app = wx.App(False) 
frame = MadLibFrame(None)
frame.Show()
app.MainLoop()