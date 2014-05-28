import wx

class MadLibFrame(wx.Frame):
	def __init__(self, parent):
		wx.Frame.__init__(self, parent, wx.ID_ANY, "Mad Lib Game")
		self.panel = wx.Panel(self)
		
		self.btnClickMe = wx.Button(self.panel, label = "Random", pos = (20,30), size=(200,20))
		self.btnClickMe2 = wx.Button(self.panel, label = "I would Like to choose them", pos = (300,30), size=(200,20))
		self.btnClickMe3 = wx.Button(self.panel, label = "Random", pos = (20,80), size=(200,20))
		self.btnClickMe4 = wx.Button(self.panel, label = "I would Like to choose them", pos = (300,80), size=(200,20))
		heading = wx.StaticText(self.panel, label='How Would You like your nouns?', pos=(200, 15))
		heading2 = wx.StaticText(self.panel, label='How Would You like your Adjectives?', pos=(200, 60))
		
		self.btnClickMe.Bind(wx.EVT_BUTTON, self.OnClickMe)
		self.btnClickMe2.Bind(wx.EVT_BUTTON, self.OnClickMe2)
		self.btnClickMe3.Bind(wx.EVT_BUTTON, self.OnClickMe3)
		self.btnClickMe4.Bind(wx.EVT_BUTTON, self.OnClickMe4)
	
	
	def OnClickMe(self,e):
		wx.MessageBox(" " ,"Rules", wx.CANCEL)
	def OnClickMe2(self,e):
		wx.MessageBox("There will be NO REFUNDS" ,"Cancel", wx.CANCEL)
	def OnClickMe3(self,e):
		wx.MessageBox("You will be Choosing different words, for example: random, verbs, adjectives, and nouns.These words will then arranged creating sentences. " ,"Rules", wx.CANCEL)
	def OnClickMe4(self,e):
		wx.MessageBox("There will be NO REFUNDS" ,"Cancel", wx.CANCEL)

