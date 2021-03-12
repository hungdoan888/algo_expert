# -*- coding: utf-8 -*-
"""
Created on Thu Mar 11 22:52:58 2021

@author: hungd
"""

def lineThroughPoints(points):
    # Write your code here.
    if len(points) == 1:
        return 1
    
    maxPoints = 0
    for i in range(len(points) - 1):
        pointsOnSameLine = {}
        for j in range(i + 1, len(points)):
            if points[i][0] == points[j][0]:
                m = float("inf")
            else:
                m = (points[j][1] - points[i][1]) / (points[i][0] - points[j][0])
                
            if m in pointsOnSameLine:
                pointsOnSameLine[m] += 1
            else:
                pointsOnSameLine[m] = 2
                
            if pointsOnSameLine[m] > maxPoints:
                maxPoints = pointsOnSameLine[m]
                
            print(pointsOnSameLine)
    return maxPoints

points = [
  [1, 1],
  [2, 2],
  [3, 3],
  [0, 4],
  [-2, 6],
  [4, 0],
  [2, 1]
]
lineThroughPoints(points)