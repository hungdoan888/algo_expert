# -*- coding: utf-8 -*-
"""
Created on Sat Nov 21 20:01:28 2020

@author: hungd
"""

def threeNumberSort(array, order):
    # Write your code here.
    print(array)
    left = 0
    right = len(array) - 1
    i = 0
    while i <= right:
        if array[right] == order[-1]:
            right -= 1
            continue
        
        if array[i] == order[0]:
            array[i], array[left] = array[left], array[i]
            left += 1
            i += 1
        elif array[i] == order[-1]:
            array[i], array[right] = array[right], array[i]
            right -= 1
        else:
            i += 1
        print(array)
        print(right)
    return array
                
                   
array = [7, 8, 9, 7, 8, 9, 9, 9, 9, 9, 9, 9]
order = [8, 7, 9]
threeNumberSort(array, order)
