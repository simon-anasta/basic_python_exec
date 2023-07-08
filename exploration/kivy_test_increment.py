# -*- coding: utf-8 -*-
"""
Created on Sun May 28 12:30:16 2023

@author: Simon & Izzi

Advancing kv language
- referencing widgets by id
- reactive changes

Need to store the loaded string in order to access ids
during runtime.

When creating a sub-class, need to call `super(...)`
to ensure correct creation of the super-class.

Update to the UI happens automaticly when widget
properties are changed. Manual 'redraw' command not
required (different from PyGame).
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
#:set font_color 0.1, 0.8, 0.3, 1

GridLayout:
    cols: 1
    Label:
        id: output
        text: "0"
    Button:
        id: b1
        text: "increment"
        on_press: app.increment()

'''

#%% app

class uiApp(App):
    
    # load string on initialisation
    def __init__(self):
        super(uiApp, self).__init__()
        self.app = Builder.load_string(kv_string2)
        
    # key method, must return widget instance
    def build(self):
        return self.app
    
    # key method (optional)
    def on_start(self):
        pass
    
    # alternative as part of stopping app
    def on_stop(self):
        Window.close()
        
    # increment
    def increment(self):
        current_value = int(self.app.ids.output.text)
        self.app.ids.output.text = str(current_value + 1)
        
    
  
#%% running the application
if __name__ == '__main__':
    # more streamlined version using on_stop
    uiApp().run()
    # restart the Python kernal upon exit
    # (required to rerun app as kivy state is indeterminate upon close)
    os._exit(00)
    
