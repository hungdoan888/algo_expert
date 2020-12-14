# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 17:36:45 2020

@author: hungd
"""

class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, values, i=0):
        if i >= len(values):
            return
        queue = [self]
        while len(queue) > 0:
            current = queue.pop(0)
            if current.left is None:
                current.left = BinaryTree(values[i])
                break
            queue.append(current.left)
            if current.right is None:
                current.right = BinaryTree(values[i])
                break
            queue.append(current.right)
        self.insert(values, i + 1)
        return self


def maxPathSum(tree):
    # Write your code here.
    maxValue, runningValue = maxPathSumHelper(tree)
    return maxValue
    

def maxPathSumHelper(node):
    # Write your code here.
    if node is None:
        return float("-inf"), float("-inf")
    
    leftMax, leftRunning = maxPathSumHelper(node.left)
    rightMax, rightRunning = maxPathSumHelper(node.right)
    
    runningValue = max(leftRunning + node.value, rightRunning + node.value, node.value)
    maxValue = max(leftMax, 
                   rightMax, 
                   node.value,
                   leftRunning + node.value,
                   rightRunning + node.value,
                   leftRunning + rightRunning + node.value)
    
    return maxValue, runningValue

  
node = BinaryTree(-2).insert([-2])
maxPathSum(node)
