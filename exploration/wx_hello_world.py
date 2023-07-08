# -*- coding: utf-8 -*-
"""
Created on Sat May 20 12:53:30 2023

@author: Simon & Izzi
"""

# First things, first. Import the wxPython package.
import wx

# Next, create an application object.
app = wx.App()

# Then a frame.
frm = wx.Frame(None, title="Hello World")

# Show it.
frm.Show()

# Start the event loop.
app.MainLoop()
