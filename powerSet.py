# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 08:07:45 2020

@author: hungd
"""

def powerset(array):
    
    if not array:
        return [[]]
    
    return powersetHelper(array, currentSet = [], masterSet = [[]], pointer = 0)

def powersetHelper(array, currentSet = [], masterSet = [[]], pointer = 0):
    
    if pointer >= len(array):
        return
    
    for i in range(pointer, len(array)):
        currentSetTemp = currentSet[:]
        currentSetTemp.append(array[i])
        masterSet.append(currentSetTemp)
        powersetHelper(array, currentSetTemp, masterSet, i + 1)
        
    return masterSet
        
        
array = [1, 2, 3]
asdf = powerset(array)
		
