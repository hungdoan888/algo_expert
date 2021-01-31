# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 14:03:56 2021

@author: hungd
"""

def interweavingStrings(one, two, three):
    # Write your code here.
    if len(three) != len(one) + len(two):
        return False
    
    visited = [[False for j in range(len(two) + 1)] for i in range(len(one) + 1)]
    return interweavingStringsHelper(one, two, three, visited, i = 0, j = 0)

def interweavingStringsHelper(one, two, three, visited, i = 0, j = 0):
    
    if visited[i][j]:
        return False
    
    k = i + j
    if k > len(three) - 1:
        return True 
    
    visited[i][j] = True
    
    if i < len(one) and one[i] == three[k]:
        solutionFound = interweavingStringsHelper(one, two, three, visited, i + 1, j)
        if solutionFound:
            return True
    
    if j < len(two) and two[j] == three[k]:
        solutionFound = interweavingStringsHelper(one, two, three, visited, i, j + 1)
        if solutionFound:
            return True
    
    return False


one = "algoexpert"
two = "your-dream-job"
three = "your-algodream-expertjob"
interweavingStrings(one, two, three)