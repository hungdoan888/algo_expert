# -*- coding: utf-8 -*-
"""
Created on Thu Dec 24 19:23:04 2020

@author: hungd
"""

#%% Max Heap Class

class MaxHeap:
    def __init__(self, array):
        # Do not edit the line below.
        self.heap = array
        self.heap = self.buildHeap()

    def buildHeap(self):
        array = self.heap
        # Write your code here.
        lastParentIdx = max((len(array) - 2) // 2, 0)
        for i in reversed(range(lastParentIdx + 1)):
            self.siftDown(i)
        return array

    def siftDown(self, parentIdx):
        array = self.heap
        # Write your code here.
        lastParentIdx = (len(array) - 2) // 2
        if parentIdx > lastParentIdx:
            return
        
        childOneIdx = 2 * parentIdx + 1
        childTwoIdx = min(2 * parentIdx + 2, len(array) - 1)
        if array[childOneIdx] >= array[childTwoIdx]:
            childIdx = childOneIdx
        else:
            childIdx = childTwoIdx
            
        if array[childIdx] <= array[parentIdx]:
            return
        
        self.swap(childIdx, parentIdx)
        return self.siftDown(childIdx)

    def siftUp(self, childIdx):
        # Write your code here.
        array = self.heap
        if childIdx == 0:
            return
        
        parentIdx = (childIdx - 1) // 2
        if array[childIdx] <= array[parentIdx]:
            return
        
        self.swap(childIdx, parentIdx)
        return self.siftUp(parentIdx)

    def peek(self):
        array = self.heap
        # Write your code here.
        return array[0]

    def remove(self):
        array = self.heap
        # Write your code here.
        self.swap(0, len(array) - 1)
        value2remove = array.pop()
        self.siftDown(0)
        return value2remove

    def insert(self, value):
        array = self.heap
        # Write your code here.
        array.append(value)
        childIdx = len(array) - 1
        self.siftUp(childIdx)
    
    def swap(self, i, j):
        array = self.heap
        array[i], array[j] = array[j], array[i]

#%% Min Heap Class

class MinHeap:
    def __init__(self, array):
        # Do not edit the line below.
        self.heap = array
        self.heap = self.buildHeap()

    def buildHeap(self):
        array = self.heap
        # Write your code here.
        lastParentIdx = max((len(array) - 2) // 2, 0)
        for i in reversed(range(lastParentIdx + 1)):
            self.siftDown(i)
        return array

    def siftDown(self, parentIdx):
        array = self.heap
        # Write your code here.
        lastParentIdx = (len(array) - 2) // 2
        if parentIdx > lastParentIdx:
            return
        
        childOneIdx = 2 * parentIdx + 1
        childTwoIdx = min(2 * parentIdx + 2, len(array) - 1)
        if array[childOneIdx] <= array[childTwoIdx]:
            childIdx = childOneIdx
        else:
            childIdx = childTwoIdx
            
        if array[childIdx] >= array[parentIdx]:
            return
        
        self.swap(childIdx, parentIdx)
        return self.siftDown(childIdx)

    def siftUp(self, childIdx):
        # Write your code here.
        array = self.heap
        if childIdx == 0:
            return
        
        parentIdx = (childIdx - 1) // 2
        if array[childIdx] >= array[parentIdx]:
            return
        
        self.swap(childIdx, parentIdx)
        return self.siftUp(parentIdx)

    def peek(self):
        array = self.heap
        # Write your code here.
        return array[0]

    def remove(self):
        array = self.heap
        # Write your code here.
        self.swap(0, len(array) - 1)
        value2remove = array.pop()
        self.siftDown(0)
        return value2remove

    def insert(self, value):
        array = self.heap
        # Write your code here.
        array.append(value)
        childIdx = len(array) - 1
        self.siftUp(childIdx)
    
    def swap(self, i, j):
        array = self.heap
        array[i], array[j] = array[j], array[i]

#%% Continuous Median

class ContinuousMedianHandler:
    def __init__(self):
        # Write your code here.
        self.median = None
        self.x = MaxHeap([])
        self.y = MinHeap([])

    def insert(self, number):
        # Write your code here.
        x = self.x
        y = self.y
        
        if not x.heap:
            x.insert(number)
        elif not y.heap:
            if number <= x.peek():
                y.insert(x.remove())
                x.insert(number)
            else:
                y.insert(number)
        elif number <= x.peek():
            x.insert(number)
        else:
            y.insert(number)
        
        if len(x.heap) > len(y.heap) + 1:
            y.insert(x.remove())
        elif len(x.heap) + 1 < len(y.heap):
            x.insert(y.remove())
            
        if (len(x.heap) + len(y.heap)) % 2 == 0:
            self.median = (x.peek() + y.peek()) / 2
        else:
            if len(x.heap) > len(y.heap):
                self.median = x.peek()
            else:
                self.median = y.peek()
        print(x.heap, y.heap, self.median)
        
    def getMedian(self):
        return self.median


array = [48, 12, 24, 7, 8, -5, 24, 391, 24, 56, 2, 6, 8, 41]
z = ContinuousMedianHandler()
