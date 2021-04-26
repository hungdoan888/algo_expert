# -*- coding: utf-8 -*-
"""
Created on Sun Apr 25 22:15:51 2021

@author: hungd
"""

def sortStack(stack):
	
    if not stack:
        return stack
    
    top = stack.pop()
    sortStack(stack)
    insertInSortedOrder(stack, top)
    return stack

def insertInSortedOrder(stack, value):
	
    if not stack or value >= stack[-1]:
        stack.append(value)
        return
	
    top = stack.pop()
    insertInSortedOrder(stack, value)
    stack.append(top)


stack = [-5, 2, -2, 4, 3, 1]
sortStack(stack)
