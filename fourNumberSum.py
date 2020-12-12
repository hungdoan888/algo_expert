# -*- coding: utf-8 -*-
"""
Created on Sat Nov 28 13:12:54 2020

@author: hungd
"""

def fourNumberSum(array, targetSum):
    fourNumberSumArray = []
    pairsDict = {}
    for i in range(len(array)-1):
        for j in range(i+1, len(array)):
            P = array[i] + array[j]
            Q = targetSum - P
            if Q in pairsDict:
                for k in range(len(pairsDict[Q])):
                    fourNumberSumArray.append([array[i], array[j]] + pairsDict[Q][k])
                    
        for j in range(i):
            if (array[i] + array[j]) not in pairsDict:
                pairsDict[array[i] + array[j]] = [[array[i], array[j]]]
            else:
                pairsDict[array[i] + array[j]].append([array[i], array[j]])
    return fourNumberSumArray

array = [7, 6, 4, -1, 1, 2]
targetSum = 16
fourNumberSum(array, targetSum)
