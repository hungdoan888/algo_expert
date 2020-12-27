# -*- coding: utf-8 -*-
"""
Created on Sat Dec 26 17:24:02 2020

@author: hungd
"""

def sunsetViews(buildings, direction):
    # Write your code here.
    if direction == "EAST":
        output = []
        maxHeight = 0
        for i in reversed(range(len(buildings))):
            if buildings[i] > maxHeight:
                output = [i] + output
                maxHeight = buildings[i]             
    else:
        output = []
        maxHeight = 0
        for i in range(len(buildings)):
            if buildings[i] > maxHeight:
                output.append(i)
                maxHeight = buildings[i]
    return output
        
buildings = [3, 5, 4, 4, 3, 1, 3, 2]
direction = "WEST"
sunsetViews(buildings, direction)