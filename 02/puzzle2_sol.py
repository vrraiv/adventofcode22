# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 10:48:37 2022

@author: Vikram
"""

import os
import pandas as pd
import numpy as np
os.chdir(os.path.abspath(os.path.dirname(__file__)))

##

data = pd.read_csv('input.txt',header=None, sep=' ', index_col=None)

data.rename(columns = {0: "move", 1: "reply"}, inplace=True) 

data['pts_result'] = 0
data['pts_pick'] = 0

# 0 for losing, 3 for draw, 6 for winning

# A for rock, # B for paper, # C for scissors
# X for rock, Y for paper, Z for scissors

data['move'] = data['move'].replace({'A': 'rock', 'B': 'paper', 'C' : 'scissors'})
data['reply'] = data['reply'].replace({'X': 'rock', 'Y': 'paper', 'Z' : 'scissors'})


# pts for picking:
picks = [data['reply'].eq('rock'),
    data['reply'].eq('paper'),
    data['reply'].eq('scissors')]

pts_for_pick = [1,2,3]
data['pts_pick'] = np.select(picks, pts_for_pick, default=0)


## pts for tying
results = [ 
    # ties
        data['move'].eq('rock') & data['reply'].eq('rock'),
        data['move'].eq('paper') & data['reply'].eq('paper'),
        data['move'].eq('scissors') & data['reply'].eq('scissors'),
    #wins
        data['move'].eq('rock') & data['reply'].eq('paper'),
        data['move'].eq('paper') & data['reply'].eq('scissors'),
        data['move'].eq('scissors') & data['reply'].eq('rock')]
pts_for_result = [3,3,3,6,6,6]
data['pts_result'] = np.select(results, pts_for_result, default=0)



# total pts
data['pts'] = data['pts_pick'] + data['pts_result']
print(sum(data['pts']))

# part two
data['result_guide'] = data['reply'].replace({'rock': 'lose', 'paper': 'draw', 'scissors' : 'win'})
data['new_pts_result'] = data['result_guide'].replace({'lose': 0, 'draw': 3, 'win' : 6})
data['new_reply'] = 'A'

data.loc[data['result_guide'].eq('lose') & data['move'].eq('paper'), 'new_reply'] = 'rock'
data.loc[data['result_guide'].eq('lose') & data['move'].eq('rock'), 'new_reply'] = 'scissors'
data.loc[data['result_guide'].eq('lose') & data['move'].eq('scissors'), 'new_reply'] = 'paper'

data.loc[data['result_guide'].eq('draw') & data['move'].eq('paper'), 'new_reply'] = 'paper'
data.loc[data['result_guide'].eq('draw') & data['move'].eq('rock'), 'new_reply'] = 'rock'
data.loc[data['result_guide'].eq('draw') & data['move'].eq('scissors'), 'new_reply'] = 'scissors'

data.loc[data['result_guide'].eq('win') & data['move'].eq('paper'), 'new_reply'] = 'scissors'
data.loc[data['result_guide'].eq('win') & data['move'].eq('rock'), 'new_reply'] = 'paper'
data.loc[data['result_guide'].eq('win') & data['move'].eq('scissors'), 'new_reply'] = 'rock'

new_picks = [
        data['new_reply'].eq('rock'), 
        data['new_reply'].eq('paper'), 
        data['new_reply'].eq('scissors')]
new_pts_for_pick = [1,2,3]
data['new_pts_pick'] = np.select(new_picks, new_pts_for_pick, default=0)

data['new_pts'] = data['new_pts_result'] + data['new_pts_pick']
print(sum(data['new_pts']))


# step 1: figure out move to calculate pts for pick


       
# o_rock = data['move'].ne('A') # rock 
# o_paper = data['move'].ne('B') # paper
# o_scis = data['move'].ne('C') # scizzors
# me_rock = data['reply'].ne('X') # rock 
# me_paper = data['reply'].ne('Y') # paper
# me_scis = data['reply'].ne('Z') # scissors


# # fill in pts for picks
# data.loc[(me_rock), 'pts_pick'] = 1
# data.loc[(me_paper), 'pts_pick'] = 2
# data.loc[(me_scis), 'pts_pick'] = 3

# # results
# ties = [
        


# # ties
# data.loc[(me_rock & o_rock), 'pts_result'] = 3
# data.loc[(me_paper & o_paper), 'pts_result'] = 3
# data.loc[(me_scis & o_scis), 'pts_result'] = 3

# # # wins
# data.loc[(me_rock & o_scis), 'pts_result'] = 6
# data.loc[(me_paper & o_rock), 'pts_result'] = 6
# data.loc[(me_scis & o_paper), 'pts_result'] = 6

# # data['pts'] = data['pts_result'] + data['pts_pick']
# # print(sum(data['pts']))
