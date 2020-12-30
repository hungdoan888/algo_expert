# -*- coding: utf-8 -*-
"""
Created on Fri Dec 25 21:01:16 2020

@author: hungd
"""

def firstDuplicateValue(array):
    # Write your code here.
    for i in range(len(array)):
        absValue = abs(array[i])
        if array[absValue - 1] < 0:
            return absValue
        array[absValue - 1] *= -1
        print(array)
    return -1

array = [2, 1, 5, 2, 3, 3, 4]
firstDuplicateValue(array)
