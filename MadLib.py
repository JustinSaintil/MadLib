#! /usr/bin/env python

import wx
from buttonmodule import *
from TextBox import *
from  CheckBoxes import *
# * imports everything in the module

vehicle = random.choice(vehicles)
names = random.choice(names)
objects = random.choice(objects)
animals = random.choice(animals)
place = random.choice(places)
verb = random.choice(verbs)
adj = random.choice(adj)
sent = random.choice(sent)

vehicle = "@"
name = "$"
objects = "\"
animals = "]"
place = ":"
verb = "_"
adj = " ' "

app = wx.App(False) 
frame = MadLibFrame(None)
frame.Show()
app.MainLoop()

"""
Sentence Structures:

$ hit the @ with a / on the way home from :.

$ will _ if $ won’t _.

When $ rode the ] to the :, the \ was forgotten at :.

A/an ' @ is a great way to _ to :.

The ' ] learned to _ by watching the ' \ _.

$ and $ will _ when they hear that the \ _.

It’d be rude for $ not to buy me a/an ' ].

My : is a/an ' place to _ while I do homework.

$ thinks that the ' \ is cool because it can _.
