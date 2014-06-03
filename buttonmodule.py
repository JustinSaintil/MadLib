import wx

class MadLibFrame(wx.Frame):
	def __init__(self, parent):
		wx.Frame.__init__(self, parent, wx.ID_ANY, "Mad Lib Game")
		
		adjectives = []
		file = open('adjectives.txt', 'r')
		for line in file:
			self.adjectives.append(line.strip())
		file.close()
		
		animals = []
		file = open('animals.txt', 'r')
		for line in file:
			self.animals.append(line.strip())
		file.close()
		
		names = []
		file = open('names.txt', 'r')
		for line in file:
			self.names.append(line.strip())
		file.close()
		
		objects = [] 
		file = open('objects.txt', 'r')
		for line in file:
			self.names.append(line.strip())
		file.close()
		
		places = []
		file = open('places.txt', 'r')
		for line in file:
			self.places.append(line.strip())
		file.close() 
		
		vehicles = []
		file = open('vehicles.txt', 'r')
		for line in file:
			self.places.append(line.strip())
		file.close()
		
		verbs = []
		file = open('verbs.txt', 'r')
		for line in file:
			self.verbs.append(line.strip())
		file.close()
		
		self.panel = wx.Panel(self)
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
		heading3 = wx.StaticText(self.panel, label='How Would You like Your Verbs?', pos=(200, 300), style=wx.TE_RICH)
		
		self.btnClickMe.Bind(wx.EVT_BUTTON, self.OnClickMe)
		self.btnClickMe2.Bind(wx.EVT_BUTTON, self.OnClickMe2)
		self.btnClickMe3.Bind(wx.EVT_BUTTON, self.OnClickMe3)
		self.btnClickMe4.Bind(wx.EVT_BUTTON, self.OnClickMe4)
		self.btnClickMe5.Bind(wx.EVT_BUTTON, self.OnClickMe5)
		self.btnClickMe6.Bind(wx.EVT_BUTTON, self.OnClickMe6)
	
	
	
	def OnClickMe(self,e):
		animals = random.choice(self.animals)
		names = random.choice(self.names)
		objects = random.choice(self.objects)
		places = random.choice(self.places)
		vehicles = random.choice(self.vehicles)
		print 'Animals:', animals
		print 'Names', names
		print 'Objects', objects
		print 'Places:', places
		print 'Vehicles:', vehicles
		
		
	def OnClickMe2(self,e):
		#---------------------------------
		
	def OnClickMe3(self,e):
		adjectives = random.choice(self.adjectives)
		print 'Adjectives:', adjectives 
		
	def OnClickMe4(self,e):
		#---------------------------------
		
	def OnClickMe5(self, e)
		verbs = random.choice(self.verbs)
		print 'Verbs:", verbs 
		
	def OnClickMe6(self, e)
		#-------------------------------
		
