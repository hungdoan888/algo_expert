# -*- coding: utf-8 -*-
"""
Created on Fri Mar  5 14:18:13 2021

@author: hungd
"""

def globMatching(filename, pattern):
    # Write your code here.
    matchTable = initiateMatchTable(filename, pattern)
    
    for i in range(1, len(matchTable)):
        for j in range(1, len(matchTable[0])):
            if pattern[j - 1] == "*":
                matchTable[i][j] = matchTable[i][j-1] or matchTable[i-1][j]
            elif pattern[j - 1] == "?" or pattern[j-1] == filename[i-1]:
                matchTable[i][j] = matchTable[i-1][j-1]
    return matchTable[-1][-1]
            
            
def initiateMatchTable(filename, pattern):
    matchTable = [[False for j in range(len(pattern) + 1)] for i in range(len(filename) + 1)]
    matchTable[0][0] = True
    
    for j in range(1, len(pattern) + 1):
        if pattern[j - 1] == "*":
            matchTable[0][j] = matchTable[0][j-1]
    return matchTable
        
pattern = "a*e?g"
filename = "abcdefg"
globMatching(filename, pattern)