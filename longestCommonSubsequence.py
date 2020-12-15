# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 20:56:19 2020

@author: hungd
"""

def longestCommonSubsequence(str1, str2):
    # Write your code here.
    str1 = " " + str1
    str2 = " " + str2
    
    strMatrix = [["" for j in range(len(str2))] for i in range(len(str1))]
    for i in range(1, len(str1)):
        for j in range(1, len(str2)):
            if str1[i] == str2[j]:
                strMatrix[i][j] = strMatrix[i-1][j-1] + str1[i]
            else:
                if len(strMatrix[i][j-1]) > len(strMatrix[i-1][j]):
                    strMatrix[i][j] = strMatrix[i][j-1]
                else:
                    strMatrix[i][j] = strMatrix[i-1][j]
                    
    return list(strMatrix[-1][-1])

str1 = "ZXVVYZW"
str2 = "XKYKZPW"
longestCommonSubsequence(str1, str2)