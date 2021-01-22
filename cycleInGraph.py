# -*- coding: utf-8 -*-
"""
Created on Thu Jan 21 20:41:01 2021

@author: hungd
"""

def cycleInGraph(edges):
    # Write your code here.
    visited = {}
    
    for i in range(len(edges)):
        containsCycle = cycleInGraphHelper(i, edges, visited, {})
        if containsCycle:
            return True
    return False

def cycleInGraphHelper(node, edges, visited, visiting):
    
    print(node, visited, visiting)
    if node in visiting:
        return True
    
    if node in visited: 
        return False
    
    visited[node] = True
    visiting[node] = True
    for i in range(len(edges[node])):
        containsCycle = cycleInGraphHelper(edges[node][i], edges, visited, dict.copy(visiting))
        
        if containsCycle:
            return True
        
    return False
        
edges = [[1, 3], [2, 3, 4], [0], [], [2, 5], []]
cycleInGraph(edges)