#!/usr/bin/env python
import wx

# Here is a simple demonstration of how a checkbox can be used.
# This lesson is based on a zetcode tutorial. (http://zetcode.com/wxpython/widgets/#checkbox)

class CheckBoxFrame(wx.Frame):

	def __init__(self, parent):

		
		
		wx.Frame.__init__(self, parent, wx.ID_ANY, "Let's learn about checkboxes.")
		
		self.panel = wx.Panel(self)

		# Create our checkbox. I always prefix my checkbox variable names them with cb.
		# It is up to you whether you do this or not.
		self.cbNounList = wx.CheckBox(self.panel, label='Nouns', pos=(20, 20))
		self.cbAdjectiveList = wx.CheckBox(self.panel, label = 'Adjectives', pos=(20, 40))
        
		# By default our box will be checked. I bet you can guess how to change that.
		self.cbNounList.SetValue(True)
		self.cbAdjectiveList.SetValue(True)

		# We will bind out checkbox to an event handler.
		# Before we have only bound buttons and EVT_BUTTON.
		# Now we see that most widgets have some events.
		# The EVT_CHECKBOX event occurs whenever a checkbox changes state
		self.cbNounList.Bind(wx.EVT_CHECKBOX, self.OnToggleNounList)
		self.cbAdjectiveList.Bind(wx.EVT_CHECKBOX, self.OnToggleAdjectiveList)

		# Here is a useful line to know. (It has nothing to do with checkboxes.)
		# Calling the Centre() method (note the British spelling) on a frame
		# automatically places it in the centre of your window.
		self.Centre()
   
	# Here is the event handler for whenever the checkbox is checked or unchecked.
	# What is that 'e' again? What does it do?
	def OnToggleNounList(self, e):
        
		# Earlier we learned about setValue() now we'll use getValue()
		# these methods are called getters and setters. They often come in pairs.
		isChecked = self.cbNounList.GetValue()
		
		if isChecked:
			self.SetTitle("Let's learn about checkboxes.")            
		else: 
			self.SetTitle('') 
			 
	def OnToggleAdjectiveList(self, e):
        
		# Earlier we learned about setValue() now we'll use getValue()
		# these methods are called getters and setters. They often come in pairs.
		isChecked = self.cbAdjectiveList.GetValue()
		
		if isChecked:
			self.SetTitle("Let's learn about checkboxes.")            
		else: 
			self.SetTitle('')  




