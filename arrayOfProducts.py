# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 22:25:54 2020

@author: hungd
"""

def arrayOfProducts(array):
    # Write your code here.
    product = array[0]
    for i in range(1, len(array)):
        product = product * array[i]
	
    if product == 0:
        return [0 for _ in range(len(array))]
	
    for i in range(len(array)):
        array[i] = product / array[i]
		
        return array

array = [0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]