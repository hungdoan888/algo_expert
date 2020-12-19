# -*- coding: utf-8 -*-
"""
Created on Thu Dec 17 10:59:57 2020

@author: hungd
"""

def dijkstrasAlgorithm(start, edges):
    # Write your code here.
    minDistances = [float("inf") for _ in range(len(edges))]
    minDistances[start] = 0
    visited = {}
    queue = [start]
    while queue:
        i = queue[0]
        if minDistances[i] == float("inf"):
            break
        
        if i in visited:
            queue.pop(0)
            continue
        
        edges[i].sort(key=lambda edge:edge[1])
        for j in range(len(edges[i])):
            
            if minDistances[i] + edges[i][j][1] < minDistances[edges[i][j][0]]:
                minDistances[edges[i][j][0]] = minDistances[i] + edges[i][j][1]
                
            queue.append(edges[i][j][0])
        
        queue.pop(0)
        visited[i] = True
        
    for i in range(len(minDistances)):
        if minDistances[i] == float("inf"):
            minDistances[i] = -1
            
    return minDistances
    

start = 0
edges = [
  [[1, 1], [7, 8]],
  [[2, 1]],
  [[3, 1]],
  [[4, 1]],
  [[5, 1]],
  [[6, 1]],
  [[7, 1]],
  []
]
dijkstrasAlgorithm(start, edges)