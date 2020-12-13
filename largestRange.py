# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def largestRange(array):
    
    T_hash = {}
    for i in range(len(array)):
        T_hash[array[i]] = True
    
    minRange = None
    maxRange = None
    maxlength = 0
    for i in range(len(array)):
        
        if T_hash[array[i]] == False:
            continue
        
        minRange_temp = array[i]
        maxRange_temp = array[i]
        maxlength_temp = 1
        T_hash[array[i]] = False
        
        # Going Down
        neighbor = array[i] - 1
        while True:
            if neighbor not in T_hash:
                break
            
            T_hash[neighbor] = False
            minRange_temp = neighbor
            maxlength_temp += 1   
            neighbor -= 1
        
        # Going Up
        neighbor = array[i] + 1
        while True:
            if neighbor not in T_hash:
                break
            
            T_hash[neighbor] = False
            maxRange_temp = neighbor
            maxlength_temp += 1 
            neighbor += 1
        
        if maxlength_temp > maxlength:
            minRange = minRange_temp
            maxRange = maxRange_temp
            maxlength = maxlength_temp
    
    return [minRange, maxRange]

array = [1]
largestRange(array)
