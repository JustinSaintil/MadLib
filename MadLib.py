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

"""
Sentence Structures:

NAME hit the NOUN with a NOUN on the way home from PLACE.

NAME will VERB if NAME won’t VERB.

When NAME rode the ANIMAL NOUN / VEHICLE NOUN  to the PLACE, the OBJECT NOUN was forgotten at PLACE.

A/an ADJECTIVE   VEHICLE NOUN / ANIMAL NOUN  is a great way to ACTION VERB to PLACE.

The ADJECTIVE    ANIMAL NOUN learned to ACTION VERB by watching the ADJECTIVE    OBJECT NOUN   ACTION VERB.

NAME and NAME  will ACTION VERB when they hear that the OBJECT NOUN   ACTION VERB.

 It’d be rude for NAME not to buy me a/an ADJECTIVE    OBJECT / VEHICLE / ANIMAL NOUN.

My PLACE is a/an ADJECTIVE place to ACTION VERB while I do homework.

NAME thinks that the ADJECTIVE    OBJECT NOUN is cool because it can ACTION VERB.
