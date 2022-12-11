# -*- coding: utf-8 -*-
"""
Created on Fri Dec  9 22:34:38 2022

@author: Vikram
"""

import os
import pandas as pd
import numpy as np
import string 
import re


os.chdir(os.path.abspath(os.path.dirname(__file__)))


raw = open('input.txt').read()
data = raw.replace("-", " ").replace(","," ").replace('\n',' ')
num_data = list(zip(*[iter(map(int, data.split()))]*2))

num_data_1 = [num_data[x] for x in list(range(0,int(len(num_data)),1)) if x%2==0]
num_data_2 = [num_data[x] for x in list(range(0,int(len(num_data)),1)) if x%2==1]

# make list of ranges to check
task_list_1 = [range(num_data_1[x][0],num_data_1[x][1]+1) for x in list(range(0,int(len(num_data_1))))]
task_list_2 = [range(num_data_2[x][0],num_data_2[x][1]+1) for x in list(range(0,int(len(num_data_2))))]

# check if ranges fully overlap
def range_overlap(range1, range2):
    r1_start, r1_stop = range1.start, range1.stop
    r2_start, r2_stop = range2.start, range2.stop
    if r1_start <= r2_start and r1_stop >= r2_stop:
        return True
    else:
        if r2_start <= r1_start and r2_stop >= r1_stop:
            return True
        else:
            return False

# test
r1 = task_list_1[0]
r2 = task_list_2[0]

range_overlap(r1,r2)

# go through all items of task lists
result1 = [range_overlap(task_list_1[n],task_list_2[n]) for n in range(0,int(len(task_list_1)))]
print(sum(result1))

# check if the ranges overlap at all
def range_overlap_2(range1, range2): 
    if len(set.intersection(set(range1)&set(range2))) > 0:
        return True
    else: 
        return False

result2 = [range_overlap_2(task_list_1[n],task_list_2[n]) for n in range(0,int(len(task_list_1)))]
print(sum(result2))