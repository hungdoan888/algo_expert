# -*- coding: utf-8 -*-
"""
Created on Sun Feb 28 10:40:46 2021

@author: hungd
"""

# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
        
class rootValueIdx:
    def __init__(self, value):
        self.value = value

def reconstructBst(preOrderTraversalValues):
    # Write your code here.
    idxClass = rootValueIdx(0)
    return reconstructBstHelper(preOrderTraversalValues, float("-inf"), float("inf"), idxClass)

def reconstructBstHelper(array, lowerBound, upperBound, idxClass):
    
    if idxClass.value >= len(array):
        return
    
    rootValue = array[idxClass.value]
    if rootValue < lowerBound or rootValue >= upperBound:
        return
    
    print(rootValue)
    idxClass.value += 1
    leftBST = reconstructBstHelper(array, lowerBound, rootValue, idxClass)
    rightBST = reconstructBstHelper(array, rootValue, upperBound, idxClass)
    return BST(rootValue, leftBST, rightBST) 
    
preOrderTraversalValues = [10, 4, 2, 1, 5, 17, 19, 18]
head = reconstructBst(preOrderTraversalValues)