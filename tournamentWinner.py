# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 20:58:14 2021

@author: hungd
"""

def tournamentWinner(competitions, results):
    # Write your code here.
    compDict = createCompDict(competitions)
    for i in range(len(competitions)):
        if results[i] == 0:
            compDict[competitions[i][1]] += 3
        else:
            compDict[competitions[i][0]] += 3
            
    maxPoints = 0     
    for key, value in compDict.items():
        if value > maxPoints:
            winner = key
            maxPoints = value
    return winner

def createCompDict(competitions):
    compDict = {}
    for i in range(len(competitions)):
        if competitions[i][0] not in compDict:
            compDict[competitions[i][0]] = 0
            
        if competitions[i][1] not in compDict:
            compDict[competitions[i][1]] = 0
    return compDict

competitions =  [
    ["HTML", "Java"],
    ["Java", "Python"],
    ["Python", "HTML"],
    ["C#", "Python"],
    ["Java", "C#"],
    ["C#", "HTML"],
    ["SQL", "C#"],
    ["HTML", "SQL"],
    ["SQL", "Python"],
    ["SQL", "Java"]
  ]
results = [0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1]
tournamentWinner(competitions, results)