# -*- coding: utf-8 -*-
"""
Created on Fri Mar 12 13:37:05 2021

@author: hungd
"""

class BinaryTree:
    def __init__(self, value, parent=None):
        self.value = value
        self.left = None
        self.right = None
        self.parent = parent
        
        
def iterativeInOrderTraversal(tree, callback):
    # Write your code here.
    currNode = tree
    prevNode = tree.parent
    while currNode is not None:
        if prevNode == currNode.parent:
            if currNode.left is not None:
                prevNode = currNode
                currNode = currNode.left
            else:
                print("=>", currNode.value)
                callback(currNode)
                if currNode.right is not None:
                    prevNode = currNode
                    currNode = currNode.right
                else:
                    currNode, prevNode = prevNode, currNode
        elif prevNode == currNode.left:
            print("=>", currNode.value)
            callback(currNode)
            if currNode.right is not None:
                prevNode = currNode
                currNode = currNode.right
            else:
                prevNode = currNode
                currNode = currNode.parent
        else:
            prevNode = currNode
            currNode = currNode.parent
            
def testCallback(testArray, tree):
    if tree is None:
        return
    testArray.append(tree.value)
            
tree = BinaryTree(1)
tree.left = BinaryTree(2, parent=tree)
tree.left.left = BinaryTree(4, parent=tree.left)
tree.left.left.right = BinaryTree(9, parent=tree.left.left)
tree.right = BinaryTree(3, parent=tree)
tree.right.left = BinaryTree(6, parent=tree.right)
tree.right.right = BinaryTree(7, parent=tree.right)

testArray = []
callback = lambda x: testCallback(testArray, x)
        
iterativeInOrderTraversal(tree, callback)