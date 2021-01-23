# -*- coding: utf-8 -*-
"""
Created on Fri Jan 22 15:25:01 2021

@author: hungd
"""

class MinHeap:
    def __init__(self, array):
        self.heap = self.buildHeap(array)
        
    def buildHeap(self, array):
        currentIdx = len(array) - 1
        lastParentIdx = (currentIdx - 1) // 2
        for i in reversed(range(lastParentIdx + 1)):
            self.siftDown(i, array)
        return array
            
    def siftDown(self, parentIdx, heap):
        # If parentIdx is not actually a parent, return
        if parentIdx > (len(heap) - 2) // 2:
            return
        
        # Define Children
        child1 = parentIdx * 2 + 1
        if child1 >= len(heap) - 1:
            child2 = child1
        else:
            child2 = parentIdx * 2 + 2
        
        # Choose min child
        if heap[child2] < heap[child1]:
            childIdx = child2
        else:
            childIdx = child1
        
        # Swap if child is smaller than parent
        if heap[childIdx] < heap[parentIdx]:
            self.swap(heap, childIdx, parentIdx)
            self.siftDown(childIdx, heap)
        
    def siftUp(self, childIdx, heap):
        if childIdx == 0:
            return
        
        parentIdx = (childIdx - 1) // 2
        
        if heap[childIdx] < heap[parentIdx]:
            self.swap(heap, childIdx, parentIdx)
            self.siftUp(parentIdx, heap)
            
    def insert(self, value):
        self.heap.append(value)
        self.siftUp(len(self.heap) - 1, self.heap)
     
    def peek(self):
        return self.heap[0]
    
    def remove(self):
        self.swap(self.heap, 0, len(self.heap) - 1)
        valueToRemove = self.heap.pop()
        self.siftDown(0, self.heap)
        return valueToRemove
        
    def swap(self, array, i, j):
        array[i], array[j] = array[j], array[i]
        

def sortKSortedArray(array, k):
    # Write your code here.
    heap = MinHeap(array[:k+1])
    sortedArray = []
    while heap.heap:
        sortedArray.append(heap.remove())
        
        k += 1
        if k <= len(array) - 1:
            heap.insert(array[k])
            
    return sortedArray
            
    
array = [3, 2, 1, 5, 4, 7, 6, 5]
k = 3
sortKSortedArray(array, k)
    
    
        
        