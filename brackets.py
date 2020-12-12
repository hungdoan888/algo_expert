# -*- coding: utf-8 -*-
"""
Created on Sat Nov 21 21:48:40 2020

@author: hungd
"""

def balancedBrackets(string):
    # Write your code here.
    parenthesis = ["(", "[", "{", "}", "]", ")"]
    parDict = {"(":")", "[":"]", "{":"}"}
    queue = []
    for i in range(len(string)):
        if string[i] not in parenthesis:
            continue
        elif string[i] == "(" or string[i] == "[" or string[i] == "{":
            queue.append(string[i])
        else:
            if not queue:
                return False
            elif string[i] == parDict[queue[-1]]:
                queue.pop(-1)
            else:
                return False
        print(queue)
            
    if not queue:
        return True
    else:
        return False
            
string = "([])(){}(())()()"
balancedBrackets(string)