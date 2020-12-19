# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 09:28:17 2020

@author: hungd
"""

def knapsackProblem(items, capacity):
    # Write your code here.
    # return [
    #   10, // total value
    #   [1, 2], // item indices
    # ]
    items = [[0, 0]] + items
    capacity = list(range(capacity + 1))
    values = [[0 for j in range(len(capacity))] for i in range(len(items))]

    for i in range(1, len(items)):
        v = items[i][0]
        w = items[i][1]
        for j in range(1, len(capacity)):
            
            if w <= capacity[j]:
                values[i][j] = max(values[i-1][j], values[i-1][j-w]+v)
            else:
                values[i][j] = values[i-1][j]
                
    savedValues = getItemsUsed(values, items)
    return [values[-1][-1], savedValues]
       
def getItemsUsed(values, items):
    i = len(values) - 1
    j = len(values[0]) - 1
    valueSum = 0
    savedValues = []
    capacity = values[i][j]
    
    while valueSum < capacity: 
        if values[i-1][j] != values[i][j]:
            valueSum += items[i][0]
            savedValues = [i-1] + savedValues
            j -= items[i][1]
            i -= 1
        else:
            i -= 1
        print(i)
    return savedValues
        
         
items = [
  [465, 100],
  [400, 85],
  [255, 55],
  [350, 45],
  [650, 130],
  [1000, 190],
  [455, 100],
  [100, 25],
  [1200, 190],
  [320, 65],
  [750, 100],
  [50, 45],
  [550, 65],
  [100, 50],
  [600, 70],
  [240, 40]
]
capacity = 200
knapsackProblem(items, capacity)