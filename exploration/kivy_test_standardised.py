# -*- coding: utf-8 -*-
"""
Created on Wed May 17 08:23:54 2023

@author: Simon & Izzi

Advancing kv language
- Self-defined widgets
- Parameterised settings
- Background colours

BoxLayout subclass ensures size management occurs.
Otherwise, custom widget appears in odd positions.

Custom widgets must either (1) be subclassed in kv_lang using
@Class, or (2) be given class inheritance in Python using
class Subclass(Class):
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
from kivy.uix.widget import Widget
from kivy.uix.label import Label


#%% Kivy string

kv_string2 = '''
# parameterised value for use later
#:set my_label "there"
#: set font_color 0.1, 0.8, 0.3, 1

# setting defaults for all items of this class
<Label>:
    text: "item2"
    color: font_color

# defining a new custom class
<Filler@BoxLayout>:
    BoxLayout:
        canvas.before:
            Color:
                rgba: 0.9, 0.9, 0.9, 1
            Rectangle:
                pos: self.pos
                size: self.size
        Label:
            text: "here"
            color: 0.1, 0.1, 0.1, 1
            # size: root.size
                
GridLayout:
    # fill gridlayout with coloured background
    canvas.before:
        Color:
            rgba: 0.7, 0.3, 0.3, 1
        Rectangle:
            pos: self.pos
            size: self.size
    cols: 3
    Label:
    Label:
        text: "item"
    Label:
        text: "item"
	Filler:
    ToggleButton:
        text: my_label
        font_size: 24
        background_color: 1, 0, 1, 1
    ToggleButton:
        text: "default"


'''

            

#%% class inheritance

# class Filler(Label):
    # pass

#%% app

class uiApp(App):
        
    # key method, must return widget instance
    def build(self):
        return Builder.load_string(kv_string2)
    
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
