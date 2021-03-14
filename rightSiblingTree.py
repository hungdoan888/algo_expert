# -*- coding: utf-8 -*-
"""
Created on Sat Mar 13 17:43:39 2021

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


def rightSiblingTree(root):
    # Write your code here.
    rightSiblingTreeHelper(root, None, True)
    return root


def rightSiblingTreeHelper(node, parent, leftNode):
    # Write your code here.
    if node.left is not None:
        rightSiblingTreeHelper(node.left, node, True)
        
    rightNode = node.right
    if parent is None:
        node.right = None
    elif leftNode:
        node.right = parent.right
    else:
        if parent.right is not None:
            node.right = parent.right.left
        else:
            node.right = None
    
    if rightNode is not None:
        rightSiblingTreeHelper(rightNode, node, False)
        

root = BinaryTree(1).insert([2, 3, 4, 5, 6, 7, 8, 9])
root.left.right.right = BinaryTree(10)
root.right.left.left = BinaryTree(11)
root.right.right.left = BinaryTree(12)
root.right.right.right = BinaryTree(13)
root.right.left.left.left = BinaryTree(14)
node = rightSiblingTree(root)