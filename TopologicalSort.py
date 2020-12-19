# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 14:25:15 2020

@author: hungd
"""

class jobGraph:
    def __init__(self, jobs, deps):
        self.nodes = []
        self.graph = {}
        self.valid = True
        self.addNodes(jobs)
        self.addPrereqs(deps)
            
    def addNodes(self, jobs):
        for i in range(len(jobs)):
            self.graph[jobs[i]] = jobNode(jobs[i])
            self.nodes.append(self.graph[jobs[i]])
        
    def addPrereqs(self, deps):
        for i in range(len(deps)):
            self.graph[deps[i][1]].prereq.append(deps[i][0])

class jobNode:
    def __init__(self, job):
        self.job = job
        self.prereq = []
        self.visited = False
        self.visiting = False
        
def topologicalSort(jobs, deps):
    # Write your code here.
    nodes = jobGraph(jobs, deps)
    node = nodes.graph[jobs[0]]
    jobOrder = []
    
    for i in range(len(jobs)):
        node = nodes.graph[jobs[i]]
        nodes, jobOrder = topologicalSortHelper(node, nodes, jobOrder)
    
    return jobOrder if nodes.valid is not False else []
    
def topologicalSortHelper(node, nodes, jobOrder):
    
    if node.visited == True:
        return nodes, jobOrder
    
    if node.visiting == True:
        nodes.valid = False
        return nodes, jobOrder
    
    if not node.prereq:
        nodes.graph[node.job].visited = True
        jobOrder.append(node.job)
        return nodes, jobOrder
    
    nodes.graph[node.job].visiting = True
    for i in range(len(node.prereq)):
        nodes, jobOrder = topologicalSortHelper(nodes.graph[node.prereq[i]], nodes, jobOrder)
    
    nodes.graph[node.job].visited = True
    jobOrder.append(node.job)
    return nodes, jobOrder
        
jobs = [1, 2, 3, 4, 5, 6, 7, 8]
deps = [[3, 1], [8, 1], [8, 7], [5, 7], [5, 2], [1, 4], [6, 7], [1, 2], [7, 6]]
topologicalSort(jobs, deps)
