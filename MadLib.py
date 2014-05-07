#! /usr/bin/env python

import wx 
class MadLibFrame(wx.Frame):
	def __init__(self, parent):
		wx.Frame.__init__(self, parent, wx.ID_ANY, "Mad Lib Game")
		self.panel = wx.Panel(self)
		
		self.btnClickMe = wx.Button(self.panel, label = "YES", pos = (20,80), size=(200,20))
		self.btnClickMe2 = wx.Button(self.panel, label = "NO", pos = (20,120), size=(200,20))
		heading = wx.StaticText(self.panel, label='Would You like to Start a Mad Lib Game?', pos=(20, 15))
	
		self.btnClickMe.Bind(wx.EVT_BUTTON, self.OnClickMe)
		self.btnClickMe2.Bind(wx.EVT_BUTTON, self.OnClickMe2)

	
	def OnClickMe(self,e):
		wx.MessageBox("LET THE GAMES BEGIN" ,"May the ODDS be forever in your favor", wx.CANCEL)
	def OnClickMe2(self,e):
		wx.MessageBox("Now That's a let down" ,"Go Die in a hole", wx.CANCEL)
	

app = wx.App(False) 
frame = MadLibFrame(None)
frame.Show()
app.MainLoop()