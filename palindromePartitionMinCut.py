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
    cuts = [float("inf") for i in range(len(string))]
    cuts[0] = 0
    for j in range(1, len(cuts)):
        if pMatrix[0][j]:
            cuts[j] = 0
        else:
            cuts[j] = cuts[j - 1] + 1
            for i in range(1, j):
                if pMatrix[i][j] and cuts[i - 1] + 1 < cuts[j]:
                    cuts[j] = cuts[i - 1] + 1
    return cuts[-1]
        
    
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