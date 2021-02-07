# -*- coding: utf-8 -*-
"""
Created on Sat Feb  6 15:01:04 2021

@author: hungd
"""

def indexEqualsValue(array):
    # Write your code here.
    return indexEqualsValueHelper(array)

def indexEqualsValueHelper(array):
    # Write your code here.
    l = 0
    r = len(array) - 1
    while l <= r:
        m = (l + r) // 2
        if m == array[m] and m == 0:
            return m
        elif m == array[m] and m - 1 > array[m - 1]:
            return m
        elif m <= array[m]:
            r = m - 1
        else:
            l = m + 1
    return -1
    
array =[-12, 1, 2, 3, 12]
indexEqualsValue(array)