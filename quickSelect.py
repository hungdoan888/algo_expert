# -*- coding: utf-8 -*-
"""
Created on Sat Feb  6 13:35:34 2021

@author: hungd
"""

def quickselect(array, k):
    # Write your code here.
    startIdx = 0
    endIdx = len(array) - 1
    return quickselectHelper(array, k - 1, startIdx, endIdx)

def quickselectHelper(array, k, startIdx, endIdx):
    # Write your code here.9zcxi
    
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
        print(p, l, r)
    swap(array, p, r)
    
    if r == k:
        return array[r]
    elif k < r:
        return quickselectHelper(array, k, startIdx, r - 1)
    elif k > r:
        return quickselectHelper(array, k, r + 1, endIdx)
            
def swap(array, i, j):
    array[i], array[j] = array[j], array[i]
            


array = [8, 5, 2, 9, 7, 6, 3]
k = 3
quickselect(array, k)