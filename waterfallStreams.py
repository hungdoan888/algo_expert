# -*- coding: utf-8 -*-
"""
Created on Mon Mar  8 18:21:47 2021

@author: hungd
"""

def waterfallStreams(array, source):
    # Write your code here.
    visited = [[0 for j in range(len(array[0]))] for i in range(len(array))]
    waterfallStreamsHelper(array, visited, 0, source, 100, True)
    return array[-1]
    
def waterfallStreamsHelper(array, visited, i, j, percent, verticalMovement):
    
    visited = [row[:] for row in visited]
    array[i][j] += percent
    visited[i][j] = 1
    
    if i == len(array) - 1:
        return

    # Try going down
    if i + 1 < len(array) and array[i + 1][j] != 1:
        verticalMovement = True
        waterfallStreamsHelper(array, visited, i+1, j, percent, verticalMovement)
    else:
        if verticalMovement:
            percent /= 2
        verticalMovement = False
        if j - 1 >= 0 and array[i][j - 1] != 1 and visited[i][j - 1] == 0:
            waterfallStreamsHelper(array, visited, i, j-1, percent, verticalMovement)
        
        if j + 1 < len(array[0]) and array[i][j + 1] != 1 and visited[i][j + 1] == 0:
            waterfallStreamsHelper(array, visited, i, j+1, percent, verticalMovement)
        
  
array = [
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0],
  [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

source = 8
waterfallStreams(array, source)
