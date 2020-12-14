# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 16:37:50 2020

@author: hungd
"""

def sameBsts(arrayOne, arrayTwo):
    # Write your code here.
    return sameBstsHelper(arrayOne, arrayTwo)

def sameBstsHelper(arrayOne, arrayTwo):
    
    if not arrayOne and not arrayTwo:
        return True
    
    if len(arrayOne) != len(arrayTwo):
        return False
    
    if arrayOne[0] != arrayTwo[0]:
        return False
    
    arrayOneLess = []
    arrayTwoLess = []
    arrayOneGreater = []
    arrayTwoGreater = []
    for i in range(1, len(arrayOne)):
        if arrayOne[i] < arrayOne[0]:
            arrayOneLess.append(arrayOne[i])
        else:
            arrayOneGreater.append(arrayOne[i])
            
        if arrayTwo[i] < arrayTwo[0]:
            arrayTwoLess.append(arrayTwo[i])
        else:
            arrayTwoGreater.append(arrayTwo[i])
            
    valueLess = sameBstsHelper(arrayOneLess, arrayTwoLess)
    valueGreater = sameBstsHelper(arrayOneGreater, arrayTwoGreater)
    
    return valueLess and valueGreater
    
arrayOne = [10, 15, 8, 12, 94, 81, 5, 2, 11]
arrayTwo = [10, 8, 5, 15, 2, 12, 11, 94, 81]
sameBsts(arrayOne, arrayTwo)
