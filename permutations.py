# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14 19:56:59 2020

@author: hungd
"""

def getPermutations(array):
    
    if not array:
        return []
    
    perm = []
    master = []
    getPermutationsHelper(array, perm, master)
    return master

def getPermutationsHelper(array, perm, master):
    
    if not array:
        return master.append(perm)
    
    for i in range(len(array)):
        
        tempArray = array[:]
        tempPerm = perm[:]
        
        tempPerm.append(tempArray.pop(i))
        
        getPermutationsHelper(tempArray, tempPerm, master)
        