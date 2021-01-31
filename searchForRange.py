# -*- coding: utf-8 -*-
"""
Created on Sat Jan 30 11:21:06 2021

@author: hungd
"""

def searchForRange(array, target):
    # Write your code here.
    rangeLeft = searchForRangeLeft(array, target, l = 0, r = len(array) - 1)
    rangeRight = searchForRangeRight(array, target, l = 0, r = len(array) - 1)
    return rangeLeft, rangeRight

def searchForRangeLeft(array, target, l, r):
    
    if l > r: 
        return -1
    
    m = (l + r) // 2
    print("left", l, m, r)
    if array[m] == target and m == 0:
        return m
    
    if array[m] == target and array[m - 1] != target:
        return m
    
    if target <= array[m]:
        return searchForRangeLeft(array, target, l, m - 1)
    else:
        return searchForRangeLeft(array, target, m + 1, r)

def searchForRangeRight(array, target, l, r):
    
    if l > r: 
        return -1
    
    m = (l + r) // 2
    print("right", l, m, r)
    if array[m] == target and m == len(array) - 1:
        return m
    
    if array[m] == target and array[m + 1] != target:
        return m
    
    if target >= array[m]:
        return searchForRangeRight(array, target, m + 1, r)
    else:
        return searchForRangeRight(array, target, l, m - 1)
    
array = [5, 7, 7, 8, 8, 10]
target = 10
searchForRange(array, target)