# -*- coding: utf-8 -*-
"""
Created on Mon Mar 15 19:40:52 2021

@author: hungd
"""

# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
    
def allKindsOfNodeDepths(root):
    # Write your code here.
    edges, nodes, sumOfEdges = allKindsOfNodeDepthsHelper(root)
    return sumOfEdges


def allKindsOfNodeDepthsHelper(node):
    # Write your code here.
    if node.left is None and node.right is None:
        return 0, 1, 0
    
    if node.left is not None:
        leftEdges, leftNodes, sumLeft = allKindsOfNodeDepthsHelper(node.left)
    else:
        leftEdges, leftNodes, sumLeft = 0, 0, 0
        
    if node.right is not None:
        rightEdges, rightNodes, sumRight = allKindsOfNodeDepthsHelper(node.right)
    else:
        rightEdges, rightNodes, sumRight = 0, 0, 0
        
    edges = leftEdges + leftNodes + rightEdges + rightNodes
    nodes = leftNodes + rightNodes + 1
    sumOfEdges = sumLeft + sumRight + edges
    return edges, nodes, sumOfEdges


root = BinaryTree(1)
root.left = BinaryTree(2)
root.left.left = BinaryTree(4)
root.left.left.left = BinaryTree(8)
root.left.left.right = BinaryTree(9)
root.left.right = BinaryTree(5)
root.right = BinaryTree(3)
root.right.left = BinaryTree(6)
root.right.right = BinaryTree(7)
allKindsOfNodeDepths(root)