# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 21:39:11 2021

@author: hungd
"""

def palindromePartitioningMinCuts(string):
    
    if len(string) <= 1:
        return 0
    
    # Create palindrome matrix (True False)
    pMatrix = [[False for i in string] for j in string]
    for i in range(len(string)):
        for j in range(i, len(string)):
            pMatrix[i][j] = isPalindrome(string[i:j + 1])
    
    # Create Values Matrix
    cuts = [[0 for i in string] for j in string]
    
    # Fill in first row of values matrix
    for i in range(1, len(string)):
        if pMatrix[0][i] is False:
            cuts[0][i] = cuts[0][i - 1] + 1
            
    # Fill in the rest of the matrix
    for i in range(1, len(string) - 1):
        cuts[i][i] = cuts[i -1][i]
        for j in range(i + 1, len(string)):
            if pMatrix[i][j] is True:
                cuts[i][j] = cuts[i][i]
            else:
                cuts[i][j] = min(cuts[i - 1][j], cuts[i][j - 1] + 1)
         
    return cuts[-2][-1]
        
    
def isPalindrome(string):
    left = 0
    right = len(string) - 1
    while left <= right:
        if string[left] != string[right]:
            return False
        left += 1
        right -= 1
    return True
    

string = "ababbbabbababa"
palindromePartitioningMinCuts(string)