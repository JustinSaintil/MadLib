#!/usr/bin/env python
import wx

# In this lesson you will learn about the wx.TextCtrl, and simple message boxes.
# You are familiar with both of these widgets, and you will likely find them very useful.

class HelloFrame(wx.Frame):

	def __init__(self, parent):
	
		# Do you remember why include the next line?
		wx.Frame.__init__(self, parent, wx.ID_ANY, "Mad Lib")
		
		# We will create a panel here because it is good practice not to put widgets directly in a frame.
		self.panel = wx.Panel(self)
		
		# A simple wx.StaticText label just like we've used before
		self.prompt = wx.StaticText(self.panel, label="Enter some Verbs:", pos=(40, 10))
		
		# Another wx.StaticText. This one does not have a label yet. We will set it later.
		self.response = wx.StaticText(self.panel, pos=(40, 100))
		
		
		# Now, this lesson's main feature. A wx.TextCtrl
		# TextCtrl can also take a size=(width, height) argument.
		self.nameBox = wx.TextCtrl(self.panel, pos=(200, 10))

		# A wx.Button just like before
		self.btnSubmit = wx.Button(self.panel, label="Submit", pos=(150, 50))
		self.btnSubmit.Bind(wx.EVT_BUTTON, self.OnSubmitSimple)
		
		
		
		
	def OnSubmitSimple(self, e):
		# This event handler is called when the submit button is clicked.
		# The purpose is to greet the user by name. It is the fancy version of: print "Hello", name
		
		# First we get whatever text the user entered in the text box
		name = self.nameBox.GetValue()
		
		# Now we finally greet the user by displaying a message in our response wx.StaticText
		self.response.SetLabel("Nice to meet you, " + name)
		
	def OnSubmitComplex(self, e):
		# This event handler is used instead after you change the binding on line 30.
		# This one makes sure the user entered a name.
		
		# Again, we get whatever text the user entered in the text box
		name = self.nameBox.GetValue()
		
		# This time we make sure the user entered something before greeting them.
		if len(name) > 0:
			self.response.SetLabel("Nice to meet you, " + name)
		else:
			# If they didn't enter a name, we display a message telling them so.
			# The dialog box that we create here is called a Modal Dialog. With modal dialogs
			# you can't interact with the main window until you close the modal dialog.
			# There are lots of modal dialogs like open and save windows, or error messages.
			wx.MessageBox("Hey, you didn't enter a name!", "Info", wx.OK)


