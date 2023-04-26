# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 09:49:54 2023

@author: Simon & Izzi
"""

#%% setup

import unittest as unittest
import pandas as pandas
from app.my_plot import my_plot

#%% test class

class test_my_plot(unittest.TestCase):
    
    @classmethod
    def setUpClass(self):
        df = pandas.DataFrame(
            data = {
                "size": [1,2,3,4,5,6],
                "label": ['a','b','c','a','b','c']
                }
            )
        self.plot = my_plot(df, "label")
    
    def test_x_labels(self):
        labels = list(self.plot.index)
        self.assertEqual(labels, ['a','b','c'])
        
    def test_y_values(self):
        values = list(self.plot)
        self.assertEqual(values, [5,7,9])
       
#%% execute

if __name__ == "__main__":
    unittest.main()