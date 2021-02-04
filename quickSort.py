# -*- coding: utf-8 -*-
"""
Created on Sat Jan 30 17:35:55 2021

@author: hungd
"""

def quickSort(array):
    # Write your code here.
    return quickSortHelper(array, startIndex = 0, endIndex = len(array) - 1)
    
def quickSortHelper(array, startIndex, endIndex):
    # Write your code here.\
    if startIndex > endIndex:
        return 
    
    p = startIndex
    l = startIndex + 1
    r = endIndex
    
    while r >= l:
        if array[l] > array[p] and array[r] < array[p]:
            swap(array, l, r)
            
        if array[l] <= array[p]:
            l += 1
            
        if array[r] >= array[p]:
            r -= 1
            
    swap(array, p, r)
    
    if len(array[:r]) > 1:
        quickSortHelper(array, startIndex,  r - 1)
        
    if len(array[r + 1:]) > 1:
        quickSortHelper(array, r + 1, endIndex)
    
    return array
            
def swap(array, l, r):
    array[l], array[r] = array[r], array[l]

array = [8, 5, 2, 9, 5, 6, 3]
quickSort(array)