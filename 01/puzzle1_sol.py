# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 12:23:07 2022

@author: Vikram
"""

import os
import pandas as pd
import numpy as np

os.chdir(os.path.abspath(os.path.dirname(__file__)))


data  = pd.read_csv("input.csv", skip_blank_lines=False, header=None)
# data = data[0:20]
data = data[0].apply(pd.to_numeric)


cumsum = data[:].cumsum().fillna(method='pad')
reset = -cumsum[data.isnull()].diff().fillna(cumsum)
result = data.where(data.notnull(), reset).cumsum()

print(result.max())

inds = np.where(data.isnull())[0] -1

result2 = result[inds]
sorted_result2  = np.sort(result2,axis=0)[::-1]

result2_final = sum(sorted_result2[0:3])

print(result2_final)