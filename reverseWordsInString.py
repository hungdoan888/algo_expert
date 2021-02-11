# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 20:32:31 2021

@author: hungd
"""

def reverseWordsInString(string):
    # Write your code here.
    newString = ""
    prevI = len(string)
    hasSpaces = False
    for i in reversed(range(len(string))):
        if string[i] == " ":
            newString += string[i:prevI]
            prevI = i
            hasSpaces = True
        
    return newString[1:] + " " + string[:prevI] if hasSpaces else string
            
string = "AlgoExpert is the best!"
reverseWordsInString(string)