# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 10:07:14 2020

@author: hungd
"""

def maxSumIncreasingSubsequence(array):
    
    sums = array[:]
    sequence = [None for _ in range(len(array))]
    for i in range(len(array)):
        for j in range(i):
            if array[i] > array[j]:
                if array[i] + sums[j] > sums[i]:
                    sums[i] = array[i] + sums[j]
                    sequence[i] = j
                    
    maxSum, subsequence = createSubsequence(array, sequence, sums)
    return [maxSum, subsequence]

def createSubsequence(array, sequence, sums):
    maxSumIndex = 0
    maxSum = sums[0]
    for i in range(1, len(sums)):
        if sums[i] > maxSum:
            maxSum = sums[i]
            maxSumIndex = i
        
    i = maxSumIndex
    subsequence = [array[i]]
    while sequence[i] is not None:
        subsequence = [array[sequence[i]]] + subsequence
        i = sequence[i]
    return maxSum, subsequence
    
array = [10, 70, 20, 30, 50, 11, 30]
maxSumIncreasingSubsequence(array)

