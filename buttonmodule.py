import wx
import random

class MadLibFrame(wx.Frame):
	def __init__(self, parent):
		wx.Frame.__init__(self, parent, wx.ID_ANY, "Mad Lib Game")
		self.panel = wx.Panel(self)
		
		self.adjectives = []
		file = open('adjectives.txt', 'r')
		for line in file:
			self.adjectives.append(line.strip())
		file.close()

		self.animals = []
		file = open('animals.txt', 'r')
		for line in file:
			self.animals.append(line.strip())
		file.close()

		self.names = []
		file = open('names.txt', 'r')
		for line in file:
			self.names.append(line.strip())
		file.close()

		self.objects = []
		file = open('objects.txt', 'r')
		for line in file:
			self.objects.append(line.strip())
		file.close()

		self.places = []
		file = open('places.txt', 'r')
		for line in file:
			self.places.append(line.strip())
		file.close()

		self.vehicles = []
		file = open('vehicles.txt', 'r')
		for line in file:
			self.vehicles.append(line.strip())
		file.close()

		self.verbs = []
		file = open('verbs.txt', 'r')
		for line in file:
			self.verbs.append(line.strip())
		file.close()
		
		self.sent = []
		file = open('sent.txt', 'r')
		for line in file:
			self.sent.append(line.strip())
		file.close()

		self.heading = wx.StaticText(self.panel, label='Welcome To the Mad Lib Game', pos=(200, 15))
		wx.StaticLine(self.panel, pos=(200, 45), size=(200,2))
		self.btnClickMe = wx.Button(self.panel, label = "Random", pos = (20,100), size=(200,20))
		self.btnClickMe2 = wx.Button(self.panel, label = "Choose", pos = (300,100), size=(200,20))
		self.btnClickMe3 = wx.Button(self.panel, label = "Random", pos = (20,200), size=(200,20))
		self.btnClickMe4 = wx.Button(self.panel, label = "Choose", pos = (300,200), size=(200,20))
		self.btnClickMe5 = wx.Button(self.panel, label = "Random", pos = (20,300), size=(200,20))
		self.btnClickMe6 = wx.Button(self.panel, label = "Choose", pos = (300,300), size=(200,20))	
		heading = wx.StaticText(self.panel, label='How Would You like Your nouns?', pos=(200, 60), style=wx.TE_RICH)
		heading2 = wx.StaticText(self.panel, label='How Would You like Your Adjectives?', pos=(200, 150), style=wx.TE_RICH)
		heading3 = wx.StaticText(self.panel, label='How Would You like Your Verbs?', pos=(200, 260), style=wx.TE_RICH)

		self.btnClickMe.Bind(wx.EVT_BUTTON, self.OnNounRandom)
#	self.btnClickMe2.Bind(wx.EVT_BUTTON, self.OnNounChoose)
		self.btnClickMe3.Bind(wx.EVT_BUTTON, self.OnAdjectiveRandom)
#		self.btnClickMe4.Bind(wx.EVT_BUTTON, self.OnAdjectiveChoose)
		self.btnClickMe5.Bind(wx.EVT_BUTTON, self.OnVerbsRandom)
			#		self.btnClickMe6.Bind(wx.EVT_BUTTON, self.OnVerbsChoose)


	
	def OnNounRandom(self,e):
		self.animal = random.choice(self.animals)
		self.name = random.choice(self.names)
		self.object = random.choice(self.objects)
		self.place = random.choice(self.places)
		self.vehicle = random.choice(self.vehicles)
		print 'Animal:', self.animal
		print 'Name:', self.name
		print 'Object:', self.object
		print 'Place:', self.place
		print 'Vehicle:', self.vehicle
		print 'Sentences:', self.sent


	#def OnClickMe2(self,e):
#---------------------------------

	def OnAdjectiveRandom(self,e):
		self.adjective = random.choice(self.adjectives)
		print 'Adjective:', self.adjective

	#def OnClickMe4(self,e):
#---------------------------------

	def OnVerbsRandom(self, e):
		self.verb = random.choice(self.verbs)
		print 'Verb:', self.verb

	#def OnClickMe6(self, e)
#-------------------------------
myApp = wx.App(False)
frame = MadLibFrame(None)

frame.Show(True)

myApp.MainLoop()



