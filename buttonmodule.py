import wx

class MadLibFrame(wx.Frame):
	def __init__(self, parent):
		wx.Frame.__init__(self, parent, wx.ID_ANY, "Mad Lib Game")
		self.panel = wx.Panel(self)
		self.heading = wx.StaticText(self.panel, label='Welcome To the Mad Lib Game', pos=(200, 15))
		wx.StaticLine(self.panel, pos=(200, 45), size=(200,2))
		self.btnClickMe = wx.Button(self.panel, label = "Random", pos = (20,100), size=(200,20))
		self.btnClickMe2 = wx.Button(self.panel, label = "Choose", pos = (300,100), size=(200,20))
		self.btnClickMe3 = wx.Button(self.panel, label = "Random", pos = (20,200), size=(200,20))
		self.btnClickMe4 = wx.Button(self.panel, label = "Choose", pos = (300,200), size=(200,20))
		heading = wx.StaticText(self.panel, label='How Would You like Your nouns?', pos=(200, 60), style=wx.TE_RICH)
		heading2 = wx.StaticText(self.panel, label='How Would You like Your Adjectives?', pos=(200, 150), style=wx.TE_RICH)
		
		self.btnClickMe.Bind(wx.EVT_BUTTON, self.OnClickMe)
		self.btnClickMe2.Bind(wx.EVT_BUTTON, self.OnClickMe2)
		self.btnClickMe3.Bind(wx.EVT_BUTTON, self.OnClickMe3)
		self.btnClickMe4.Bind(wx.EVT_BUTTON, self.OnClickMe4)
	
	
	def OnClickMe(self,e):
		wx.MessageBox("You will be Choosing different words, for example: random, verbs, adjectives, and nouns.These words will then arranged creating sentences. " ,"Rules", wx.CANCEL)
	def OnClickMe2(self,e):
		wx.MessageBox("There will be NO REFUNDS" ,"Cancel", wx.CANCEL)
	def OnClickMe3(self,e):
		wx.MessageBox("You will be Choosing different words, for example: random, verbs, adjectives, and nouns.These words will then arranged creating sentences. " ,"Rules", wx.CANCEL)
	def OnClickMe4(self,e):
		wx.MessageBox("There will be NO REFUNDS" ,"Cancel", wx.CANCEL)

