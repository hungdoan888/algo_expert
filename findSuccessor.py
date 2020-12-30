# -*- coding: utf-8 -*-
"""
Created on Sat Dec 26 11:48:46 2020

@author: hungd
"""

# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent

def findSuccessor(tree, node):
    # Write your code here.
    if node.right is not None:
        successor = getSuccessorIfRightSubTree(node.right)
    else:
        successor = getFirstParentFromLeft(node)
    return successor

def getSuccessorIfRightSubTree(node):
    if node.left is None:
        return node
    return getSuccessorIfRightSubTree(node.left)

def getFirstParentFromLeft(node):
    if node.parent is None:
        return None  
    if node.parent.left == node:
        return node.parent
    return getFirstParentFromLeft(node.parent)

root = BinaryTree(1)
root.left = BinaryTree(2)
root.left.parent = root
root.right = BinaryTree(3)
root.right.parent = root
root.left.left = BinaryTree(4)
root.left.left.parent = root.left
root.left.right = BinaryTree(5)
root.left.right.parent = root.left
root.left.left.left = BinaryTree(6)
root.left.left.left.parent = root.left.left

node = root.left.right
successor = findSuccessor(root, node)
successor.value