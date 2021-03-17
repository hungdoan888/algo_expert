# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 19:52:39 2021

@author: hungd
"""

def maxProfitWithKTransactions(prices, k):
    if not prices:
        return 0
    # Write your code here.
    profits = [[0 for j in range(len(prices))] for i in range(k + 1)]
    
    for i in range(1, k + 1):
        for j in range(1, len(prices)):
            maxProfits = float("-inf")
            for x in range(j):
                if prices[j] - prices[x] + profits[i-1][x] > maxProfits:
                    maxProfits = prices[j] - prices[x] + profits[i-1][x]
            profits[i][j] = max(profits[i][j-1], maxProfits)
    return profits[-1][-1]

prices = [5, 11, 3, 50, 60, 90]
k = 2
maxProfitWithKTransactions(prices, k)