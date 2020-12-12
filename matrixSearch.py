# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 09:28:56 2020

@author: hungd
"""

def searchInSortedMatrix(matrix, target):

    H = len(matrix[0]) - 1
    V = 0
    
    while V < len(matrix) and H >= 0:
        
        if matrix[V][H] == target:
            return [V, H]
        elif matrix[V][H] > target:
            H -= 1
        elif matrix[V][H] < target:
            V += 1
    return [-1, -1]


matrix = [
  [1, 4, 7, 12, 15, 1000],
  [2, 5, 19, 31, 32, 1001],
  [3, 8, 24, 33, 35, 1002],
  [40, 41, 42, 44, 45, 1003],
  [99, 100, 103, 106, 128, 1004]
]