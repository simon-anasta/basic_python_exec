# -*- coding: utf-8 -*-
"""
Created on Sun Apr 30 11:48:43 2023

@author: Simon & Izzi
"""

import os
# os.environ['KIVY_TEXT'] = 'pil'
os.environ['KIVY_HOME'] = "C:/Users/Simon & Izzi/Documents/Simon/Projects/Current projects/basic_python_exec"
import kivy
kivy.require('2.1.0') # replace with your current kivy version !

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ListProperty

class RootWidget(BoxLayout):
    
    def __init__(self, **kwargs):
        super(RootWidget, self).__init__(**kwargs)
        self.add_widget(Button(text = "Button 1"))
        cb = CustomBtn(text = "Custom")
        cb.bind(pressed = self.btn_pressed)
        self.add_widget(cb)
        self.add_widget(Button(text = "Button 2"))
    
    def btn_pressed(self, instance, pos):
        print('pos: printed from root widget: {pos}'.format(pos = pos))


class CustomBtn(Button):
    
    pressed = ListProperty([0,0])
    
    def on_touch_up(self, touch):
        if self.collide_point(*touch.pos):
            self.pressed = touch.pos
            # return False
        return super(CustomBtn, self).on_touch_down(touch)
    
    def on_pressed(self, instance, pos):
        print('pressed at {pos}'.format(pos = pos))
        
class TestApp(App):
    
    def build(self):
        return RootWidget()
    
if __name__ == '__main__':
    TestApp().run()
