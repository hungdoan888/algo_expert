# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 09:05:47 2020

@author: hungd
"""

def zigzagTraverse(array):
    # Write your code here.
    i = 0
    j = 0
    prevI = -1
    prevJ = -1
    direction = 0
    zigzagArray = [array[i][j]]
    
    while True:
    
        if direction == 0:
            i, j, prevI, prevJ, direction, zigzagArray = down(i, j, prevI, prevJ, direction, array, zigzagArray)
        elif direction == 1:
            i, j, prevI, prevJ, direction, zigzagArray = upRight(i, j, prevI, prevJ, direction, array, zigzagArray)
        elif direction == 2:
            i, j, prevI, prevJ, direction, zigzagArray = right(i, j, prevI, prevJ, direction, array, zigzagArray)
        else:
            i, j, prevI, prevJ, direction, zigzagArray = downLeft(i, j, prevI, prevJ, direction, array, zigzagArray)
    
        if i == len(array) - 1 and j == len(array[0]) - 1:
            return zigzagArray

            
def down(i, j, prevI, prevJ, direction, array, zigzagArray):
    i += 1
    direction = 1
    if (i == prevI and j == prevJ) or i > len(array) - 1:
        return i-1, j, prevI, prevJ, direction, zigzagArray
    zigzagArray.append(array[i][j])
    return i, j, i-1, j, direction, zigzagArray
    
def upRight(i, j, prevI, prevJ, direction, array, zigzagArray):
    i -= 1
    j += 1
    if (i == prevI and j == prevJ) or i < 0 or j > len(array[0]) - 1:
        direction = 2
        return i+1, j-1, prevI, prevJ, direction, zigzagArray
    zigzagArray.append(array[i][j])
    return i, j, i+1, j-1, direction, zigzagArray

def right(i, j, prevI, prevJ, direction, array, zigzagArray):
    j += 1
    direction = 3
    if (i == prevI and j == prevJ) or j > len(array[0]) - 1:
        return i, j-1, prevI, prevJ, direction, zigzagArray
    zigzagArray.append(array[i][j])
    return i, j, i, j-1, direction, zigzagArray
    
def downLeft(i, j, prevI, prevJ, direction, array, zigzagArray):
    i += 1
    j -= 1
    if (i == prevI and j == prevJ) or i > len(array) - 1 or j < 0:
        direction = 0
        return i-1, j+1, prevI, prevJ, direction, zigzagArray
    zigzagArray.append(array[i][j])
    return i, j, i-1, j+1, direction, zigzagArray

array = [[1, 3, 4, 10], [2, 5, 9, 11], [6, 8, 12, 15], [7, 13, 14, 16]]
zigzagArray = zigzagTraverse(array)









