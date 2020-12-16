# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 20:48:48 2020

@author: hungd
"""

def waterArea(heights):
    # Write your code here.
    fromLeft = [0 for _ in range(len(heights))]
    for i in range(1, len(heights)):
        fromLeft[i] = max(fromLeft[i-1], heights[i-1])
        
    fromRight = [0 for _ in range(len(heights))]
    for i in reversed(range(len(heights) - 1)):
        fromRight[i] = max(fromRight[i+1], heights[i+1])
    
    areas = [0  for _ in range(len(heights))]
    for i in range(len(heights)):
        minHeight = min(fromLeft[i], fromRight[i])
        if heights[i] < minHeight:
            areas[i] = minHeight - heights[i]
            
    return sum(areas)


heights = [0, 8, 0, 0, 5, 0, 0, 10, 0, 0, 1, 1, 0, 3]
waterArea(heights)