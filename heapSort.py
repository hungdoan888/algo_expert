# -*- coding: utf-8 -*-
"""
Created on Sat Feb  6 15:49:10 2021

@author: hungd
"""

class MinHeap:
    def __init__(self, array):
        self.heap = self.buildHeap(array)
        
    # child1Idx = parentIdx * 2 + 1
    # child2Idx = parentIdx * 2 + 2
    # parentIdx = (childIdx - 1) // 2
    def buildHeap(self, array):
        lastParent = (len(array) - 2) // 2
        for parentIdx in reversed(range(lastParent + 1)):
            self.siftDown(array, parentIdx)
        return array
            
    def siftDown(self, heap, parentIdx):
        lastParent = (len(heap) - 2) // 2
        if parentIdx > lastParent:
            return
        
        child1Idx = parentIdx * 2 + 1
        child2Idx = parentIdx * 2 + 2
        if child2Idx > len(heap) - 1:
            child2Idx = len(heap) - 1
            
        if heap[child1Idx] < heap[child2Idx]:
            childIdx = child1Idx
        else:
            childIdx = child2Idx
            
        if heap[childIdx] < heap[parentIdx]:
            swap(heap, childIdx, parentIdx)
        self.siftDown(heap, childIdx)
    
    def remove(self):
        swap(self.heap, 0, len(self.heap) - 1)
        value2remove = self.heap.pop()
        self.siftDown(self.heap, 0)
        return value2remove
    
def swap(array, i, j):
    array[i], array[j] = array[j], array[i]
        
def heapSort(array):
    # Write your code here.
    heap = MinHeap(array)
    newArray = []
    for i in range(len(heap.heap)):
        newArray.append(heap.remove())
    return newArray

array = [8, 5, 2, 9, 5, 6, 3]
heapSort(array)