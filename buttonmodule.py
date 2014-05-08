import wx

class MadLibFrame(wx.Frame):
	def __init__(self, parent):
		wx.Frame.__init__(self, parent, wx.ID_ANY, "Mad Lib Game")
		self.panel = wx.Panel(self)
		
		self.btnClickMe = wx.Button(self.panel, label = "Start", pos = (20,80), size=(200,20))
		self.btnClickMe2 = wx.Button(self.panel, label = "Cancel", pos = (20,120), size=(200,20))
		heading = wx.StaticText(self.panel, label='Press Start to Begin.', pos=(20, 15))
		heading2 = wx.StaticText(self.panel, label='Press Cancel to End.', pos=(20, 30))
		
		self.btnClickMe.Bind(wx.EVT_BUTTON, self.OnClickMe)
		self.btnClickMe2.Bind(wx.EVT_BUTTON, self.OnClickMe2)
	
	
	def OnClickMe(self,e):
		wx.MessageBox("You will be Choosing different words, for example: random, verbs, adjectives, and nouns.These words will then arranged creating sentences. " ,"Rules", wx.CANCEL)
	def OnClickMe2(self,e):
		wx.MessageBox("There will be NO REFUNDS" ,"Cancel", wx.CANCEL)

