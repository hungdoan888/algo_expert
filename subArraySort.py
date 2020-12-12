# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 20:24:25 2020

@author: hungd
"""

def subarraySort(array):
    unsorted_numbers = []
    for i in range(len(array)):
        if i - 1 < 0:
            if array[i] > array[i+1]:
                unsorted_numbers.append(array[i])
        elif i + 1 == len(array):
            if array[i] < array[i-1]:
                unsorted_numbers.append(array[i])
        else:
            if array[i] < array[i-1] or array[i] > array[i+1]:
                unsorted_numbers.append(array[i])
    
    if not unsorted_numbers:
        return [-1, -1]
    
    unsorted_min = min(unsorted_numbers)
    unsorted_max = max(unsorted_numbers)
    
    for i in range(len(array)):
        if array[i] > unsorted_min:
            minIndex = i
            break
        
    for i in reversed(range(len(array))):
        if array[i] < unsorted_max:
            maxIndex = i
            break
        
    return [minIndex, maxIndex]

array = [1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]
subarraySort(array)