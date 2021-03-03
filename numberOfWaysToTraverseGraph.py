# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 20:40:51 2021

@author: hungd
"""

def numberOfWaysToTraverseGraph(width, height):
    # Write your code here.
    ways = [[1 for j in range(width)] for i in range(height)]
    
    for i in range(1, height):
        for j in range(1, width):
            ways[i][j] = ways[i][j-1] + ways[i-1][j]
    return ways[-1][-1]

width = 4
height = 3
numberOfWaysToTraverseGraph(width, height)