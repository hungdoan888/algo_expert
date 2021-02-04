# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 20:50:12 2021

@author: hungd
"""

# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def visitedDef(root):
    visited = {}
    visited[root.value] = False
    visitedHelper(root.left, visited)
    visitedHelper(root.right, visited)
    return visited
    
def visitedHelper(node, visited):
    if node is None:
        return
    visited[node.value] = False
    visitedHelper(node.left, visited)
    visitedHelper(node.right, visited)
    
def parentMapDef(root):
    parentMap = {}
    parentMap[root.value] = None
    parentMapHelper(root.left, root, parentMap)
    parentMapHelper(root.right, root, parentMap)
    return parentMap
    
def parentMapHelper(node, parentNode, parentMap):
    if node is None:
        return
    parentMap[node.value] = parentNode
    parentMapHelper(node.left, node, parentMap)
    parentMapHelper(node.right, node, parentMap)

def findTargetNode(node, target):
    if node is None:
        return 
    
    if node.value == target:
        return node
    
    targetNode = findTargetNode(node.left, target)
    if targetNode is not None:
        return targetNode
    targetNode = findTargetNode(node.right, target)
    if targetNode is not None:
        return targetNode

def findNodesDistanceK(tree, target, k):
    # Write your code here.
    parentMap = {}
    visited = {}
    outputArray = []
    node = findTargetNode(tree, target)
    visited = visitedDef(tree)
    parentMap = parentMapDef(tree)
    findNodesDistanceKHelper(node, k, parentMap, visited, outputArray)
    return outputArray
    
def findNodesDistanceKHelper(node, k, parentMap, visited, outputArray):
    if node is None:
        return
    
    if visited[node.value] == True:
        return
    
    if k == 0:
        outputArray.append(node.value)
        return
    
    visited[node.value] = True
    findNodesDistanceKHelper(node.left, k - 1, parentMap, visited, outputArray)
    findNodesDistanceKHelper(node.right, k - 1, parentMap, visited, outputArray)
    findNodesDistanceKHelper(parentMap[node.value], k - 1, parentMap, visited, outputArray)
    
root = BinaryTree(1)
root.left = BinaryTree(2)
root.right = BinaryTree(3)
root.left.left = BinaryTree(4)
root.left.right = BinaryTree(5)
root.right.right = BinaryTree(6)
root.right.right.left = BinaryTree(7)
root.right.right.right = BinaryTree(8)

target = 3
k = 2
findNodesDistanceK(root, target, k)