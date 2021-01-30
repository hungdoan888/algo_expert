# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 20:46:26 2021

@author: hungd
"""

def shiftedBinarySearch(array, target):
    # Write your code here.
    return shiftedBinarySearchHelper(array, target, 0, len(array) - 1)

def shiftedBinarySearchHelper(array, target, l, r):
    
    if l > r: 
        return -1
    
    m = (l + r) // 2
    print(l, m, r)
    if array[m] == target:
        return m
    
    if array[l] <= array[m]:
        if target >= array[l] and target <= array[m]:
            return shiftedBinarySearchHelper(array, target, l, m)
        else:
            return shiftedBinarySearchHelper(array, target, m + 1, r)
    else:
        if target > array[m] and target <= array[r]:
            return shiftedBinarySearchHelper(array, target, m + 1, r)
        else:
            return shiftedBinarySearchHelper(array, target, l, m)

array = [72, 73, 0, 1, 21, 33, 37, 45, 61, 71]
target = 72
shiftedBinarySearch(array, target)