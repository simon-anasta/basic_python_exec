# -*- coding: utf-8 -*-
"""
Created on Wed May 10 21:45:05 2023

@author: Simon & Izzi

Experimentation with Kivy language
- Expanded kv_string
"""

# command to run KivyCatalog app
# runfile('D:/Anaconda/share/kivy-examples/demo/kivycatalog/main.py', wdir='D:/Anaconda/share/kivy-examples/demo/kivycatalog')

import os
import kivy
kivy.require('2.1.0') # replace with your current kivy version !

from kivy.lang import Builder
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.button import Button


#%% Kivy string

kv_string = '''
BoxLayout:
    orientation: "vertical"
    spacing: 10
    
    # title bar
    BoxLayout:
        orientation: "horizontal"
        spacing: 10
        size_hint: 1, None
        height: sp(50)
        
        StackLayout:
            orientation: "tb-lr"
            size_hint: 0.5, None
            height: sp(50)
            Label:
                text: "Title goes here"
                font_size: "48sp"
            
        StackLayout:
            orientation: "tb-rl"
            size_hint: 0.5, None
            height: sp(50)
            Button:
                text: "?"
                size_hint: None, None
                width: sp(50)
                height: sp(50)
                
    # controls
    StackLayout:
        orientation: 'lr-tb'
        padding: 10
        spacing: 5
        size_hint: 1, None
        height: sp(70)
        Button:
            text: "add folder"
            size_hint: None, None
            width: sp(100)
            height: sp(50)
        Button:
            text: "add file"
            size_hint: None, None
            width: sp(100)
            height: sp(50)
        FloatLayout:
        	size_hint: None, None
            width: sp(100)
            height: sp(50)
                    
        Button:
            text: "clear all"
            size_hint: None, None
            width: sp(100)
            height: sp(50)
                            
    GridLayout:
        id: "main_display"
        cols: 3
#        Label:
#        	text: "item"
#		Label:
#        	text: "item"
#		Label:
#        	text: "item"
#		Label:
#        	text: "item"
#		Label:
#        	text: "item"
        
    BoxLayout:
        orientation: "horizontal"
        spacing: 10
        size_hint: 1, None
        height: sp(30)
        
        Label:
            text: "By Simon Anastasiadis"
            font_size: "14sp"

'''

#%% app

class uiApp(App):
        
    # key method, must return widget instance
    def build(self):
        return Builder.load_string(kv_string)
    
    # key method (optional)
    def on_start(self):
        pass
    
    # alternative as part of stopping app
    def on_stop(self):
        Window.close()
    
  
#%% running the application
if __name__ == '__main__':
    # more streamlined version using on_stop
    uiApp().run()
    # restart the Python kernal upon exit
    # (required to rerun app as kivy state is indeterminate upon close)
    os._exit(00)

kivy.uix.spinner