# -*- coding: utf-8 -*-
"""
Created on Fri Jan 22 12:09:59 2021

@author: hungd
"""

def taskAssignment(k, tasks):
    # Write your code here.
    
    # O(n) Time | O(n) Space
    taskDict = {}
    for i in range(len(tasks)):
        if tasks[i] not in taskDict:
            taskDict[tasks[i]] = [i]
        else:
            taskDict[tasks[i]].append(i)
      
    # O(nlog(n)) Time | O(1) Space
    tasks.sort()
    
    # (O(n) Time | O(n) Space)
    left = 0
    right = len(tasks) - 1
    outputArray = []
    while left < right:
        
        value1 = taskDict[tasks[left]].pop(0)
        value2 = taskDict[tasks[right]].pop(0)
        outputArray.append([value1, value2])
        left += 1
        right -= 1
        
    return outputArray

k = 3
tasks = [1, 3, 5, 3, 1, 4]
taskAssignment(k, tasks)