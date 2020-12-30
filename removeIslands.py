# -*- coding: utf-8 -*-
"""
Created on Sat Dec 26 16:50:44 2020

@author: hungd
"""

def removeIslands(matrix):
    # Write your code here.
    visited = [[0 for j in range(len(matrix[0]))] for i in range(len(matrix))]
    
    i = 0
    for j in range(len(matrix[0])):
        matrixTraverse(matrix, visited, i, j)
        
    i = len(matrix) - 1
    for j in range(len(matrix[0])):
        matrixTraverse(matrix, visited, i, j)
        
    j = 0
    for i in range(1, len(matrix)-1):
        matrixTraverse(matrix, visited, i, j)
        
    j = len(matrix[0]) - 1
    for i in range(1, len(matrix)-1):
        matrixTraverse(matrix, visited, i, j)
        
    return visited
        

def matrixTraverse(matrix, visited, i, j):
    if i < 0 or i >= len(matrix):
        return
    
    if j < 0  or j >= len(matrix[0]):
        return
    
    if visited[i][j] == 1:
        return
    
    if matrix[i][j] == 0:
        return
    
    visited[i][j] = 1
    
    matrixTraverse(matrix, visited, i-1, j)  # Up
    matrixTraverse(matrix, visited, i+1, j)  # Down
    matrixTraverse(matrix, visited, i, j-1)  # Left
    matrixTraverse(matrix, visited, i, j+1)  # Right
    

matrix = [
  [1, 0, 0, 0, 0, 0],
  [0, 1, 0, 1, 1, 1],
  [0, 0, 1, 0, 1, 0],
  [1, 1, 0, 0, 1, 0],
  [1, 0, 1, 1, 0, 0],
  [1, 0, 0, 0, 0, 1]
]
removeIslands(matrix)