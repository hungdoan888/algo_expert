# -*- coding: utf-8 -*-
"""
Created on Sat Feb  6 15:49:10 2021

@author: hungd
"""

def buildHeap(array):
    lastParent = (len(array) - 2) // 2
    for parentIdx in reversed(range(lastParent + 1)):
        siftDown(array, parentIdx, len(array))
    return array
        
def siftDown(heap, parentIdx, lengthArray):
    lastParent = (lengthArray - 2) // 2
    if parentIdx > lastParent:
        return
    
    child1Idx = parentIdx * 2 + 1
    child2Idx = parentIdx * 2 + 2
    if child2Idx > lengthArray - 1:
        child2Idx = lengthArray - 1
        
    if heap[child1Idx] > heap[child2Idx]:
        childIdx = child1Idx
    else:
        childIdx = child2Idx
        
    if heap[childIdx] > heap[parentIdx]:
        swap(heap, childIdx, parentIdx)
    siftDown(heap, childIdx, lengthArray)
    
def swap(array, i, j):
    array[i], array[j] = array[j], array[i]
        
def heapSort(array):
    # Write your code here.
    buildHeap(array)
    for i in range(1, len(array)):
        swap(array, 0, len(array) - i)
        siftDown(array, 0, len(array) - i)
    return array

array = [8, 5, 2, 9, 5, 6, 3]
heapSort(array)