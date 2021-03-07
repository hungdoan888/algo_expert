# -*- coding: utf-8 -*-
"""
Created on Sun Mar  7 08:24:04 2021

@author: hungd
"""

def apartmentHunting(blocks, reqs):
    # Write your code here.
    reqTable = createReqTable(blocks, reqs)
    for i in range(len(blocks)):
        for j in range(len(reqs)):
            if blocks[i][reqs[j]] == True:
                reqTable[i][reqs[j]] = 0
            elif i > 0:
                if reqTable[i - 1][reqs[j]] is not None:
                   reqTable[i][reqs[j]] = reqTable[i - 1][reqs[j]] + 1
                   
    for i in reversed(range(len(blocks))):
        for j in range(len(reqs)):
            if blocks[i][reqs[j]] == True:
                continue
            if i < len(blocks) - 1:
                if reqTable[i + 1][reqs[j]] is not None:
                    if reqTable[i][reqs[j]] is not None:
                        reqTable[i][reqs[j]] = min(reqTable[i][reqs[j]], reqTable[i + 1][reqs[j]] + 1)
                    else:
                        reqTable[i][reqs[j]] = reqTable[i + 1][reqs[j]] + 1
    
    minDist = float("inf")    
    minDistIdx = 0                    
    for i in range(len(reqTable)):
        maxDist = float("-inf")
        for j in range(len(reqs)):
            if reqTable[i][reqs[j]] > maxDist:
                maxDist = reqTable[i][reqs[j]]
        if maxDist < minDist:
            minDist = maxDist
            minDistIdx = i
    return minDistIdx
                

def createReqTable(blocks, reqs):
    req4Table = {}
    for i in range(len(reqs)):
        req4Table[reqs[i]] = None
    
    reqTable = []
    for i in range(len(blocks)):
        reqTable.append(req4Table.copy())
    return reqTable

blocks = [
  {
    "gym": False,
    "school": True,
    "store": False
  },
  {
    "gym": True,
    "school": False,
    "store": False
  },
  {
    "gym": True,
    "school": True,
    "store": False
  },
  {
    "gym": False,
    "school": True,
    "store": False
  },
  {
    "gym": False,
    "school": True,
    "store": True
  }
]

reqs = ["gym", "school", "store"]
apartmentHunting(blocks, reqs)