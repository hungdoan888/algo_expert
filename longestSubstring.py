# -*- coding: utf-8 -*-
"""
Created on Fri Mar  5 09:04:12 2021

@author: hungd
"""
        
def longestSubstringWithoutDuplication(string):
    longestSubstring = ""
    startIndex = 0
    substringDict = {}
    for i in range(len(string)):
        if string[i] in substringDict and substringDict[string[i]] >= startIndex:
            if i - startIndex > len(longestSubstring):
                longestSubstring = string[startIndex:i]
            startIndex = substringDict[string[i]] + 1
        substringDict[string[i]] = i
        print("longestSubstring: ", longestSubstring)
        print("startIndex: ", startIndex)
        print("Dict: ", substringDict)
        print("")
        
    if string[i] in substringDict and substringDict[string[i]] >= startIndex:
        if i + 1 - startIndex > len(longestSubstring):
            longestSubstring = string[startIndex:len(string)]   
        
    return longestSubstring
                
string = "abcdeabcdefc"
longestSubstringWithoutDuplication(string)
