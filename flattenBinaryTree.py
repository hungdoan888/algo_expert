# -*- coding: utf-8 -*-
"""
Created on Sat Mar 13 14:45:05 2021

@author: hungd
"""

# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
        
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


def flattenBinaryTree(root):
    # Write your code here.
    leftMost, _ = flattenBinaryTreeHelper(root)
    return leftMost


def flattenBinaryTreeHelper(node):
    if node.left is None:
        leftMost = node
    else:
        leftNodeInLeft, rightNodeInLeft = flattenBinaryTreeHelper(node.left)
        node.left = rightNodeInLeft
        rightNodeInLeft.right = node
        leftMost = leftNodeInLeft
        
    if node.right is None:
        rightMost = node
    else:
        leftNodeInRight, rightNodeInRight = flattenBinaryTreeHelper(node.right)
        node.right = leftNodeInRight
        leftNodeInRight.left = node
        rightMost = rightNodeInRight
    return leftMost, rightMost

root = BinaryTree(1).insert([2, 3, 4, 5, 6])
root.left.right.left = BinaryTree(7)
root.left.right.right = BinaryTree(8)

node = flattenBinaryTree(root)

while node is not None:
    print(node.value)
    node = node.right
    
    


















