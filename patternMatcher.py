# -*- coding: utf-8 -*-
"""
Created on Sat Mar  6 14:28:48 2021

@author: hungd
"""

def patternMatcher(pattern, string):
    # Write your code here.
    patternStartsWithXBool = pattern.startswith("x")
    if "x" not in pattern:
        patternStartsWithXBool = False
    pattern = patternStartsWithX(pattern)
    numXandY = findNumXandY(pattern)
    matching = noYs(pattern, string, numXandY)
    
    if matching is not None:
        return matching if patternStartsWithXBool else [matching[1], matching[0]]
    
    matching = yesYs(pattern, string, numXandY)
    return matching if patternStartsWithXBool else [matching[1], matching[0]]
    
# If there are ys
def yesYs(pattern, string, numXandY):
    
    numberOfXsbeforeY = 0
    for i in range(len(pattern)):
        if pattern[i] == "y":
            break
        numberOfXsbeforeY += 1
        
    for i in range(1, len(string)):
        x = string[:i]
        lengthOfX = len(x)
        lengthOfY = (len(string) - numXandY["x"] * lengthOfX) // numXandY["y"]
        
        
        y = string[numberOfXsbeforeY * lengthOfX:numberOfXsbeforeY * lengthOfX + lengthOfY]
        
        newPattern = []
        for j in range(len(pattern)):
            if pattern[j] == "x":
                newPattern.append(x)
            else:
                newPattern.append(y)
                
        if "".join(newPattern) == string:
            return [x, y]
    return []
    
# There are no ys
def noYs(pattern, string, numXandY):
    # if there are no y's
    if numXandY["y"] != 0:
        return 
    lengthOfX = len(string) // numXandY["x"]
    x =  string[:lengthOfX]
    if x * numXandY["x"] == string:
        return [x, ""]
    else:
        return []
        

# Find number of x's and y's
def findNumXandY(pattern):
    numXandY = {}
    numXandY["x"] = 0
    numXandY["y"] = 0
    for i in range(len(pattern)):
        if pattern[i] == "x":
            numXandY["x"] += 1
        else:
            numXandY["y"] += 1
    return numXandY
              

# Ensure pattern starts with x and is a list
def patternStartsWithX(pattern):
    pattern = list(pattern)
    if pattern[0] == "y":
        for i in range(len(pattern)):
            if pattern[i] == "x":
                pattern[i] = "y"
            else:
                pattern[i] = "x"
    return pattern

pattern = "yyxyyx"
string = "gogopowerrangergogopowerranger"
patternMatcher(pattern, string)