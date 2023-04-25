# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 11:59:37 2023

@author: Simon & Izzi
"""

#%% setup

import pandas as pd

df = pd.read_csv("./data/data.csv")

#%% function

def my_plot(df, column):
    summary = df.groupby([column])["size"].sum()
    summary.plot(kind = "bar")
    

#%% execute

my_plot(df, "group")
my_plot(df, "region")
