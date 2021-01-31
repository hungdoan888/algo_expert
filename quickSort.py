# -*- coding: utf-8 -*-
"""
Created on Sat Jan 30 17:35:55 2021

@author: hungd
"""

def quickSort(array):
    # Write your code here.
    quickSortHelper(array, p = 0, l = 1, r = len(array) - 1)
    
            

def quickSortHelper(array, p, l, r):
    # Write your code here.
    print(array)
    rEnd = r
    while r >= l:
        if array[l] > array[p] and array[r] < array[p]:
            swap(array, l, r)
            
        if array[l] <= array[p]:
            l += 1
            
        if array[r] >= array[p]:
            r -= 1
            
    swap(array, p, r)
    
    if len(array[:r]) > 1:
        quickSortHelper(array, p, p + 1, r - 1)
        
    if r + 1 < len(array) and len(array[r + 1:]) > 1:
        quickSortHelper(array, r + 1, r + 2, rEnd)
        
    return array
            
def swap(array, l, r):
    array[l], array[r] = array[r], array[l]

array = [8, 5, 2, 9, 5, 6, 3]
quickSortHelper(array, p = 0, l = 1, r = len(array) - 1)