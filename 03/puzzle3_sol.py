# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 22:30:25 2022

@author: Vikram
"""
import os
import pandas as pd
import numpy as np
import string 

os.chdir(os.path.abspath(os.path.dirname(__file__)))


data = pd.read_csv('input.txt',header=None, sep='\n', index_col=None)

df = data
df.rename(columns = {0: "contents"}, inplace=True) 

# new column for each part of rucksacks
df['bin1'] = ' '
df['bin2'] = ' '

# each compartment has half the contents
df['size'] = df['contents'].apply(len)
df['bin1'] = df['contents'].apply(lambda contents: contents[:len(contents) // 2])
df['bin2'] = df['contents'].apply(lambda contents: contents[len(contents)//2:len(contents)])

df['check_bin1'] = df['bin1'].apply(len)
df['check_bin2'] = df['bin2'].apply(len)

common = list()

#
for s,t in zip(df['bin1'],df['bin2']):
    # print(s,t)    
    common.append(list(set(s)&set(t)))

# print(common)

df['common'] = pd.Series(common).apply(lambda x: ','.join(map(str, x)))

# make the map
priorities = list(range(1,53))
numbers_l = list(string.ascii_lowercase)
numbers_u  = list(string.ascii_uppercase)
numbers_l.extend(numbers_u)


# assign values
priority_values = {numbers_l[i]: priorities[i] for i in range(len(numbers_l))}                                                                                               

# get value
df['value'] = df['common'].replace(priority_values)

print(sum(df['value']))

# part two
new_contents = list(data['contents'])
nc_grouped = list(zip(new_contents, new_contents[1:], new_contents[2:]))

# only want every 3rd group
idx = np.array(range(0,len(new_contents),3))
nc_proper = [nc_grouped[i] for i in idx]
nc = nc_proper

nc_unique = [set(nc[i][0]) & set(nc[i][1]) & set(nc[i][2]) for i in range(0,100)]
# in the long run I don't want to hardcode 100....

nc_unique_str = pd.Series(nc_unique).apply(lambda x: ','.join(map(str, x)))
nc_value = pd.Series(nc_unique_str, dtype='string').replace(priority_values)

print(sum(nc_value))


# oops I didn't need any of this
# create two groups of strings
# even = [x for x in list(range(0,100,1)) if x%2==0]
# odd = [x for x in list(range(0,100,1)) if x%2==1]

# nc1 = [nc[i] for i in even]
# nc2 = [nc[i] for i in odd]

# nc1_unique = [set(nc1[i][0]) & set(nc1[i][1]) & set(nc1[i][2]) for i in range(0,50)]
# nc2_unique = [set(nc2[i][0]) & set(nc2[i][1]) & set(nc2[i][2]) for i in range(0,50)]


# nc1_value = pd.Series(nc1).apply(lambda x: ','.join(map(str, x)))
# nc2_value = pd.Series(nc2).apply(lambda x: ','.join(map(str, x)))

