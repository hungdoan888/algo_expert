# -*- coding: utf-8 -*-
"""
Created on Mon Mar  8 20:24:51 2021

@author: hungd
"""

class minAreaClass:
    def __init__(self):
        self.area = float("inf")
        
def minimumAreaRectangle(points):
    # Write your code here.
    minArea = minAreaClass()
    rectangle = [[None, None], [None, None], [None, None], [None, None]]
    for i in range(len(points)):
        rectangle[0] = points[i]
        topLeft2topRight(points, rectangle, minArea)
    return minArea.area if minArea.area != float("inf") else 0
    
def topLeft2topRight(points, rectangle, minArea):
    for i in range(len(points)):
        if points[i][1] == rectangle[0][1] and points[i][0] > rectangle[0][0]:
            rectangle[1] = points[i]
            topRight2bottomRight(points, rectangle, minArea)

def topRight2bottomRight(points, rectangle, minArea):
    for i in range(len(points)):
        if points[i][0] == rectangle[1][0] and points[i][1] < rectangle[1][1]:
            rectangle[2] = points[i]
            bottomRight2bottomLeft(points, rectangle, minArea)

def bottomRight2bottomLeft(points, rectangle, minArea):
    for i in range(len(points)):
        if points[i][1] == rectangle[2][1] and points[i][0] == rectangle[0][0]:
            rectangle[3] = points[i]
            
            area = (rectangle[1][0] - rectangle[0][0]) * (rectangle[0][1] - rectangle[3][1])
            if area < minArea.area:
                minArea.area = area
           
points = [
  [1, 5],
  [5, 1],
  [4, 2],
  [2, 4],
  [2, 2],
  [1, 2],
  [4, 5],
  [2, 5],
  [-1, -2]
]
minimumAreaRectangle(points)