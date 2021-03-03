# -*- coding: utf-8 -*-
"""
Created on Sun Feb 28 21:15:18 2021

@author: hungd
"""

# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
        
class isBalanced:
    def __init__(self):
        self.value = True

def heightBalancedBinaryTree(tree):
    # Write your code here.
    balanced = isBalanced()
    h = 0
    heightBalancedBinaryTreeHelper(tree, h, balanced)
    return balanced.value

def heightBalancedBinaryTreeHelper(node, h, balanced):
    # Write your code here.
    
    if not balanced.value:
        return h
    
    if node is None:
        return h
    
    left = heightBalancedBinaryTreeHelper(node.left, h + 1, balanced)
    right = heightBalancedBinaryTreeHelper(node.right, h + 1, balanced)
    print(node.value, left, right)
    if abs(left - right) > 1:
        balanced.value = False
        
    return max(left, right)
    
tree = BinaryTree(1)
tree.left = BinaryTree(2)
tree.left.left = BinaryTree(4)
tree.left.left.left = BinaryTree(6)
tree.right = BinaryTree(4)
tree.right.right = BinaryTree(5)
heightBalancedBinaryTree(tree)