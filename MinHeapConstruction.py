# Do not edit the class below except for the buildHeap,
# siftDown, siftUp, peek, remove, and insert methods.
# Feel free to add new properties and methods to the class.
class MinHeap:
    def __init__(self, array):
        # Do not edit the line below.
        self.heap = self.buildHeap(array)

    def buildHeap(self, array):
        if len(array) <= 1:
            return array
        else:
            heap = array[:]
            parentIdx = (len(array) - 2) // 2
            
        for idx in reversed(range(parentIdx + 1)):
            heap = self.siftDown(heap, idx)
            
        return heap
        
    def siftDown(self, heap, parentIdx):
        childIdx1 = parentIdx * 2 + 1
        childIdx2 = parentIdx * 2 + 2
        if childIdx1 > len(heap) - 1: childIdx1 = parentIdx 
        if childIdx2 > len(heap) - 1: childIdx2 = parentIdx 
        if heap[childIdx1] <= heap[childIdx2]: 
            childIdx = childIdx1 
        else: 
            childIdx = childIdx2
        
        while heap[parentIdx] > heap[childIdx]:
            heap[parentIdx], heap[childIdx] = heap[childIdx], heap[parentIdx]
            parentIdx = childIdx
            childIdx1 = parentIdx * 2 + 1
            childIdx2 = parentIdx * 2 + 2
            if childIdx1 > len(heap) - 1: childIdx1 = parentIdx 
            if childIdx2 > len(heap) - 1: childIdx2 = parentIdx 
            if heap[childIdx1] <= heap[childIdx2]: 
                childIdx = childIdx1 
            else: 
                childIdx = childIdx2
                
        return heap
        
    def siftUp(self, heap, childIdx):
        # Write your code here.
        parentIdx = (childIdx - 1) // 2 if childIdx > 0 else 0
        while heap[parentIdx] > heap[childIdx]:
            heap[parentIdx], heap[childIdx] = heap[childIdx], heap[parentIdx]
            childIdx = parentIdx
            parentIdx = (childIdx - 1) // 2 if childIdx > 0 else 0 

    def peek(self):
        # Return root value
        return self.heap[0]

    def remove(self):
        # Remove root value - swap root with last value, then sift new root value down
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        valueToRemove = self.heap.pop()
        self.siftDown(self.heap, 0)
        return valueToRemove

    def insert(self, value):
        # Add value to end, then sift it up
        self.heap.append(value)
        self.siftUp(self.heap, len(self.heap) - 1)


array = [2, 3, 1]
x = MinHeap(array)
print(x.heap)