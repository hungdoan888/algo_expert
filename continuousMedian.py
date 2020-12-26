# -*- coding: utf-8 -*-
"""
Created on Thu Dec 24 19:23:04 2020

@author: hungd
"""

# Do not edit the class below except for the buildHeap,
# siftDown, siftUp, peek, remove, and insert methods.
# Feel free to add new properties and methods to the class.
class MinHeap:
    def __init__(self, array):
        # Do not edit the line below.
        self.heap = self.buildHeap(array)

    def buildHeap(self, array):
        # Write your code here.
        pass

    def siftDown(self, parentIdx, array):
        # Write your code here.
        lastParentIdx = (len(array) - 2) // 2
        if parentIdx > lastParentIdx:
            return
        
        childOneIdx = 2 * parentIdx + 1
        childTwoIdx = max(2 * parentIdx + 2, len(array) - 1)
        
        if array[childOneIdx] <= array[childTwoIdx]:
            childIdx = childOneIdx
        else:
            childIdx = childTwoIdx
            
        if array[childIdx] >= array[parentIdx]:
            return
        
        self.swap(childIdx, parentIdx, array)
        return self.siftDown(childIdx, array)

    def siftUp(self, childIdx, array):
        # Write your code here.
        if childIdx == 0:
            return
        
        parentIdx = (childIdx - 1) // 2
        if array[childIdx] >= array[parentIdx]:
            return
        
        self.swap(childIdx, parentIdx, array)
        return self.siftUp(parentIdx, array)

    def peek(self, array):
        # Write your code here.
        return array[0]

    def remove(self, array):
        # Write your code here.
        self.swap(0, len(array) - 1, array)
        array.pop()

    def insert(self, value, array):
        # Write your code here.
        array.append(value)
        childIdx = len(array) - 1
        self.siftUp(childIdx, array)
    
    def swap(self, i, j, array):
        array[i], array[j] = array[j], array[i]
