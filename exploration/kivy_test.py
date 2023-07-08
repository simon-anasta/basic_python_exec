# -*- coding: utf-8 -*-
"""
Created on Sat May  6 18:56:48 2023

@author: Simon & Izzi

Initial basic kivy app
- close window when app closes
- enable rerunning of app for ease of development
- set skeleton for future development
"""

import os
import kivy
kivy.require('2.1.0') # replace with your current kivy version !

from kivy.lang import Builder
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.button import Button


#%% Kivy string

kv_string = '''
#:import C kivy.utils.get_color_from_hex
Button:
  
   # text which will appear on first button
   text:"Close App"
   on_release: app.close_application()

'''

#%% app


class uiApp(App):
    
    # called by on_request_close
    def handle_X_close(self, event):
        self.close_application()
    
    # called by button release
    def close_application(self):
        # closing application
        App.get_running_app().stop()
        # removing window
        Window.close()
        
    # key method, must return widget instance
    def build(self):
        Window.bind(on_request_close = self.handle_X_close)
        return Builder.load_string(kv_string)
    
    # key method (optional)
    def on_start(self):
        pass
  
#%% app v2

class uiApp2(App):
    
    # called by button release
    def close_application(self):
        # closing application
        App.get_running_app().stop()
        
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
    
    # original working version
    uiApp().run()
    
    # more streamlined version using on_stop
    uiApp2().run()
    # restart the Python kernal upon exit
    # 
    # As kivy state is indeterminate upon close, it is
    # necessary to restart the kernal in order to rerun app.
    os._exit(00)




