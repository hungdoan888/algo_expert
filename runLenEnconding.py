# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 18:37:09 2020

@author: hungd
"""

def runLengthEncoding(string):
    
    if len(string) == 0:
        return string
    elif len(string) == 1:
        return str(1) + string
    
    count = 1
    newString = ""
    for i in range(1, len(string)):
        
        if string[i] != string[i-1] or count == 9:
            newString = newString + str(count) + string[i-1]
            count = 1
        else:
            count += 1
    
    newString = newString + str(count) + string[-1]
    return newString

string = "aA"
runLengthEncoding(string)