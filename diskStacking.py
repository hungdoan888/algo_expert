# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 10:58:33 2020

@author: hungd
"""

def diskStacking(disks):
    # Write your code here.
    disks.sort(key=lambda disk:disk[2])
    heights = [[0, []] for _ in range(len(disks))]
    for i in range(len(disks)):
        maxHeight = disks[i][2]
        maxHeightJ = None
        for j in reversed(range(i)):
            if disks[j][0] < disks[i][0] and \
               disks[j][1] < disks[i][1] and \
               disks[j][2] < disks[i][2]:
                height = disks[i][2] + heights[j][0]
                if height > maxHeight:
                    maxHeight = height
                    maxHeightJ = j
        heights[i][0] = maxHeight
        if maxHeightJ is not None:
            heights[i][1] = heights[maxHeightJ][1] + [disks[i]]
        else:
            heights[i][1] = [disks[i]]
      
    maxHeight = 0
    for i in range(len(heights)):
        if heights[i][0] > maxHeight:
            maxHeightArray = heights[i][1]
            maxHeight = heights[i][0]
            
    return maxHeightArray

disks = [[2, 1, 2], [3, 2, 3], [2, 2, 8], [2, 3, 4], [1, 3, 1], [4, 4, 5]]
diskStacking(disks)