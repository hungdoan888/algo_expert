# -*- coding: utf-8 -*-
"""
Created on Thu Mar 11 23:51:21 2021

@author: hungd
"""

class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.numNodesToLeft = 0
        
    def insert(self, value, nodesToLeft = 0):
        if value <= self.value:
            self.numNodesToLeft += 1
            if self.left is None:
                self.left = BST(value)
            else:
                nodesToLeft = self.left.insert(value, nodesToLeft)
        else:
            nodesToLeft += self.numNodesToLeft
            nodesToLeft += 1
            if self.right is None:
                self.right = BST(value)
            else:
                nodesToLeft = self.right.insert(value, nodesToLeft)
        return nodesToLeft
                
    
def rightSmallerThan(array):
    # Write your code here.
    if not array:
        return []
    tree = BST(array[-1])
    numsToTheRightSmallerThan = [ 0 for _ in range(len(array))]
    for i in reversed(range(len(array) - 1)):
        numsToTheRightSmallerThan[i] = tree.insert(array[i])
    return numsToTheRightSmallerThan
        
    

array = [0, 1, 1, 2, 3, 5, 8, 13]
rightSmallerThan(array)