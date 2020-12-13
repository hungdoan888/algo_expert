# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 10:36:00 2020

@author: hungd
"""

def minRewards(scores):

    rewards = [1 for _ in range(len(scores))]
    for i in range(1, len(scores)):
        if scores[i] > scores[i-1]:
            rewards[i] = rewards[i-1] + 1
            
    for i in reversed(range(len(scores) - 1)):
        if scores[i] > scores[i+1]:
            rewards[i] = max(rewards[i], rewards[i+1] + 1)
    return sum(rewards)

scores = [5, 10]
minRewards(scores)


    