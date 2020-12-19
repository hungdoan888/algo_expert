# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 18:12:45 2020

@author: hungd
"""

def numbersInPi(pi, numbers):
    # Write your code here.
    numbersDict = {number:True for number in numbers}
    cache = {}
    idx = 0
    spaces = getSpaces(pi, numbersDict, cache, idx)
    return -1 if spaces == float("inf") else spaces
    
def getSpaces(pi, numbersDict, cache, idx):
    
    if idx == len(pi):
        return -1
    
    if idx in cache:
        return cache[idx]
    
    minSpaces = float("inf")
    for i in range(idx, len(pi)):
        prefix = pi[idx:i+1]
        if prefix in numbersDict:
            spaces = getSpaces(pi, numbersDict, cache, i+1)
            minSpaces = min(minSpaces, spaces + 1)
    cache[idx] = minSpaces
    return cache[idx]
    
    
pi = "3141592653589793238462643383279"
numbers = [
  "314159265358979323846",
  "26433",
  "8",
  "3279",
  "314159265",
  "35897932384626433832",
  "79"
]
numbersInPi(pi, numbers)