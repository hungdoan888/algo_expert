# -*- coding: utf-8 -*-
"""
Created on Sat Feb  6 14:24:10 2021

@author: hungd
"""

class rValue:
    def __init__(self, r):
        self.r = r
        
def indexEqualsValue(array):
    # Write your code here.
    startIdx = 0
    endIdx = len(array) - 1
    rVal = rValue(-1)
    indexEqualsValueHelper(array, startIdx, endIdx, rVal)
    return rVal.r

def indexEqualsValueHelper(array, startIdx, endIdx, rVal):
    # Write your code here.
    if startIdx > endIdx:
        return
    
    p = startIdx
    l = startIdx + 1
    r = endIdx
    
    while l <= r:
        if array[l] > array[p] and array[r] < array[p] and array[l] > array[r]:
            swap(array, l, r)
            
        if array[l] < array[p]:
            l += 1
            
        if array[r] > array[p]:
            r -= 1
    swap(array, p, r)
    
    if array[r] == r:
        rVal.r = r
        return
    indexEqualsValueHelper(array, startIdx, r - 1, rVal)
    indexEqualsValueHelper(array, r + 1, endIdx, rVal)
    
def swap(array, i, j):
    array[i], array[j] = array[j], array[i]

array = [-5, -3, 0, 3, 4, 5, 9]
indexEqualsValue(array)