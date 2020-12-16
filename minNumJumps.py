# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 08:39:17 2020

@author: hungd
"""

#%% Solution 1

# O(n^2) time | O(n) space
def minNumberOfJumps(array):
    # Write your code here.
    numSteps = [float("inf") for _ in range(len(array))]
    numSteps[0] = 0
    
    i = 0
    while i <= len(array) - 1:
        for j in range(1, array[i] + 1):
            if i+j > len(array) - 1:
                continue
            
            numSteps[i+j] = min(numSteps[i+j], numSteps[i] + 1)
            
        i += 1
        
    return numSteps[-1]

#%% Solution 2

# O(n) time | O(1) space
def minNumberOfJumps2(array):
    
    if len(array) == 1:
        return 0
    
    maxReach = array[0]
    steps = array[0]
    jumps = 0
    for i in range(1, len(array) - 1):
        
        maxReach = max(maxReach, i + array[i])
        steps -= 1
        if steps == 0:
            steps = maxReach - i
            jumps += 1
            
    return jumps + 1


#%% Output 

array = [3, 4, 2, 1, 2, 3, 7, 1, 1, 1, 3]
numSteps = minNumberOfJumps(array)
