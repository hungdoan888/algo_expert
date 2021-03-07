# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 20:39:02 2021

@author: hungd
"""

def sortedSquaredArray(array):
    # Write your code here.
    smallest = float("inf")
    smallest_index = 0
    for i in range(len(array)):
        if abs(array[i]) < smallest:
            smallest = abs(array[i])
            smallest_index = i
            
    left = smallest_index
    right = smallest_index + 1
    
    squaredArray = []
    while True:
        if left < 0:
            squaredArray.append(array[right])
            right += 1
        elif right >= len(array):
            squaredArray.append(array[left])
            left -= 1
        elif abs(array[left]) <= abs(array[right]):
            squaredArray.append(array[left])
            left -= 1
        else:
            squaredArray.append(array[right])
            right += 1
        
        if left < 0 and right >= len(array):
            break
        
        print(squaredArray)
    for i in range(len(squaredArray)):
        squaredArray[i] = squaredArray[i] * squaredArray[i]
        
    return squaredArray
            
            
array = [-10, -5, 0, 5, 10]
sortedSquaredArray(array)