# -*- coding: utf-8 -*-
"""
Created on Sat May 20 12:57:23 2023

@author: Simon & Izzi
"""

import wx 
import wx.html2 

# sample html string to display in WebView widget
html_string = """
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
"http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html>
    <head>
       <title>Hello World!</title>
       <script type="text/javascript" src="jquery.js"></script>
       <style type="text/css" src="main.css"></style>
    </head>
    <body>
        <span id="foo">The quick brown fox jumped over the lazy dog</span>
        <script type="text/javascript">
        $(document.ready(function(){
           $("span#foo").click(function(){ alert('I was clicked!'); });
         });
        </script>
    </body>
</html>
"""



class MyBrowser(wx.Dialog): 
  def __init__(self, *args, **kwds): 
    wx.Dialog.__init__(self, *args, **kwds) 
    sizer = wx.BoxSizer(wx.VERTICAL) 
    self.browser = wx.html2.WebView.New(self) 
    sizer.Add(self.browser, 1, wx.EXPAND, 10) 
    self.SetSizer(sizer) 
    self.SetSize((700, 700)) 

if __name__ == '__main__': 
  app = wx.App() 
  dialog = MyBrowser(None, -1) 
  # dialog.browser.LoadURL("http://www.google.com") 
  
  
  # webviewer
  viewer = wx.html2.WebView.New()
  viewer.Create(dialog)
  dialog.browser.SetPage(html_string,"")
  
  dialog.Show() 
  app.MainLoop()
