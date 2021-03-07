# -*- coding: utf-8 -*-
"""
Created on Sat Mar  6 10:58:06 2021

@author: hungd
"""

def underscorifySubstring(string, substring):
    # Write your code here.
    
    idx_substring = 0
    underscoreLocs = []
    while idx_substring < len(string):
        idx_substring = string.find(substring, idx_substring)
        
        if idx_substring == -1:
            break
        
        if not underscoreLocs:
            underscoreLocs.append(idx_substring)
            underscoreLocs.append(idx_substring + len(substring))
            idx_substring += 1
            continue
        
        if idx_substring <= underscoreLocs[-1]:
            underscoreLocs[-1] = idx_substring + len(substring)
        else:
            underscoreLocs.append(idx_substring)
            underscoreLocs.append(idx_substring + len(substring))
        
        idx_substring += 1
     
    if not underscoreLocs:
        return string
    
    underscoreString = []
    idxUnderscoreLocs = 0
    for i in range(len(string)):
        if idxUnderscoreLocs < len(underscoreLocs) and i == underscoreLocs[idxUnderscoreLocs]:
            underscoreString.append("_")
            idxUnderscoreLocs += 1
        underscoreString.append(string[i])
        
    if underscoreLocs[-1] == len(string):
        underscoreString.append("_")
        
    underscoreString = "".join(underscoreString)
    return underscoreString
        

string = "this is a test to see if it works and test"
substring = "test"

