# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 18:33:44 2021

@author: hungd
"""

def classPhotos(redShirtHeights, blueShirtHeights):
    # Write your code here.
    redShirtHeights.sort()
    blueShirtHeights.sort()
    
    if redShirtHeights[0] == blueShirtHeights[0]:
        return False
    elif redShirtHeights[0] > blueShirtHeights[0]:
        return heightComparison(blueShirtHeights, redShirtHeights)
    else:
        return heightComparison(redShirtHeights, blueShirtHeights)
        
def heightComparison(front, back):
    for i in range(len(front)):
        if front[i] >= back[i]:
            return False
    return True

redShirtHeights = [5, 8, 1, 3, 4]
blueShirtHeights = [6, 9, 2, 4, 5]
classPhotos(redShirtHeights, blueShirtHeights)