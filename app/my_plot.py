# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 11:59:37 2023

@author: Simon & Izzi
"""

#%% setup

import pandas as pd
import pathlib

#%% locations

file_path = pathlib.PurePath(pathlib.Path(__file__))
package_path = file_path.parents[1]
data_path = package_path.joinpath("data")

#%% function

def my_plot(df, column):
    # checks
    assert isinstance(df, pd.DataFrame), "[df] must be a dataframe"
    assert isinstance(column, str), "[column] must be a string"
    assert column in df.columns, "[column] must be column of [df]"
    assert "size" in df.columns, "size must be a column of [df]"
    
    summary = df.groupby([column])["size"].sum()
    summary.plot(kind = "bar")
    return(summary)
    

#%% execute

if __name__ == "__main__":
    df = pd.read_csv(data_path.joinpath("data.csv"))
    my_plot(df, "group")
    my_plot(df, "region")
