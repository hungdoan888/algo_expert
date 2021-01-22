# -*- coding: utf-8 -*-
"""
Created on Thu Jan 21 19:25:56 2021

@author: hungd
"""

def minimumWaitingTime(queries):
    
    queries.sort()
    sumOfQueries = 0
    for i in range(len(queries) - 1):
        sumOfQueries += (sumOfQueries + queries[i])
        print(sumOfQueries)
        
    return sumOfQueries

queries = [3, 2, 1, 2, 6]
minimumWaitingTime(queries)