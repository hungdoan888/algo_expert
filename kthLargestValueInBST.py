# -*- coding: utf-8 -*-
"""
Created on Sun Feb 21 21:31:29 2021

@author: hungd
"""

# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
        
class kthLargestNodeValue:
    def __init__(self):
        self.value = None

def findKthLargestValueInBst(tree, k):
    # Write your code here.
    kthLargestValue = kthLargestNodeValue()
    findKthLargestValueInBstHelper(tree, k, kthLargestValue)
    return kthLargestValue.value
    
def findKthLargestValueInBstHelper(node, k, kthLargestValue):
    
    if node is None:
        return 1
    
    kthLargestNodeIndex = findKthLargestValueInBstHelper(node.right, k, kthLargestValue)
    
    if kthLargestValue.value is not None:
        return
    
    if kthLargestNodeIndex == k:
        kthLargestValue.value = node.value
        
    elif kthLargestNodeIndex == k - 1 and node.left is not None:
        kthLargestValue.value = getMaxValue(node.left)
        
    else:   
        return kthLargestNodeIndex + 1
    
def getMaxValue(node):
    if node.right is None:
        return node.value
    return getMaxValue(node.right)
        
tree = BST(20)
tree.left = BST(15)
tree.right = BST(25)
tree.left.left = BST(10)
tree.left.right = BST(19)
tree.right.left = BST(21)
tree.right.right = BST(30)
tree.right.left.right = BST(22)

k = 3
findKthLargestValueInBst(tree, k)