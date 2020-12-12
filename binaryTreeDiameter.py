# -*- coding: utf-8 -*-
"""
Created on Sat Nov 21 15:24:18 2020

@author: hungd
"""

# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def binaryTreeDiameter(tree):
    # Write your code here.
    depth, currMax = binaryTreeDiameterHelper(tree)
    return max(depth, currMax)

def binaryTreeDiameterHelper(tree):
    
    if tree is None:
        return -1, -1
    
    depthLeft, maxLeft = binaryTreeDiameterHelper(tree.left)
    depthRight, maxRight = binaryTreeDiameterHelper(tree.right)
    
    depth = max(depthLeft, depthRight) + 1
    currMax = max(maxLeft, maxRight)
    currMax = max(depthLeft + depthRight + 2, currMax)
    print(depth, currMax)
    return depth, currMax
    

root = BinaryTree(1)
root.left = BinaryTree(3)
root.left.left = BinaryTree(7)
root.left.left.left = BinaryTree(8)
root.left.left.left.left = BinaryTree(9)
root.left.right = BinaryTree(4)
root.left.right.right = BinaryTree(5)
root.left.right.right.right = BinaryTree(6)
root.right = BinaryTree(2)

binaryTreeDiameter(root)
