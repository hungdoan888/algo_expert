# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 10:12:14 2020

@author: hungd
"""

def longestPalindromicSubstring(string):
    # Write your code here.
    maxLength = 0
    for i in range(len(string)):
        evenCount, evenSubString = evenPalindrome(string, i)
        oddCount, oddSubString = oddPalindrome(string, i)
        if evenCount > oddCount:
            subpalindromeLength = evenCount
            subString = evenSubString
        else:
            subpalindromeLength = oddCount
            subString = oddSubString
            
        if subpalindromeLength > maxLength:
            maxLength = subpalindromeLength
            maxSubString = subString
            
    return maxSubString

def evenPalindrome(string, index):
    left = index - 1
    right = index
    count = 0
    subString = string[0]
    
    while left >= 0 and right <= len(string) - 1:
        if string[left] == string[right]:
            count += 2
            subString = string[left:right + 1]
        else:
            break
        left -= 1
        right += 1
            
    return count, subString

def oddPalindrome(string, index):
    left = index - 1
    right = index + 1
    count = 1
    subString = string[0]
    
    while left >= 0 and right <= len(string) - 1:
        if string[left] == string[right]:
            count += 2
            subString = string[left:right + 1]
        else:
            break
        left -= 1
        right += 1
            
    return count, subString

string = "noon high it is"
longestPalindromicSubstring(string)