# -*- coding: utf-8 -*-
"""
Created on Sun Apr 25 21:28:56 2021

@author: hungd
"""

def mergeOverlappingIntervals(intervals):
    # Write your code here.
    
    intervals = sorted(intervals, key=lambda x: x[0])
    overlappingIntervals = [intervals[0]]
    for i in range(1, len(intervals)):
    	if intervals[i][0] <= overlappingIntervals[-1][1]:
    		overlappingIntervals[-1][1] = max(intervals[i][1], overlappingIntervals[-1][1])
    	else:
    		overlappingIntervals.append(intervals[i])
    return overlappingIntervals

intervals = [
    [2, 3],
    [4, 5],
    [6, 7],
    [8, 9],
    [1, 10]
  ]
mergeOverlappingIntervals(intervals)
