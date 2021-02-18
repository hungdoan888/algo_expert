# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 22:10:39 2021

@author: hungd
"""

def nonConstructibleChange(coins):
    # Write your code here.
    coins.sort()
    totalChange = 0
    for i in range(len(coins)):
        if coins[i] > totalChange + 1:
            return totalChange + 1
        totalChange += coins[i]
    return totalChange + 1

coins = [5, 7, 1, 1, 2, 3, 22]
nonConstructibleChange(coins)