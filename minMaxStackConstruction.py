# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 09:43:57 2020

@author: hungd
"""

# Feel free to add new properties and methods to the class.
class MinMaxStack:
    
    def __init__(self):
        self.stack = []
        self.min = []
        self.max = []
        
    def peek(self):
        return self.stack[-1]

    def pop(self):
        self.min.pop()
        self.max.pop()
        return self.stack.pop()

    def push(self, number):
        if self.stack:
            self.min.append(min(self.min[-1], number))
            self.max.append(max(self.max[-1], number))
            self.stack.append(number)
        else:
            self.min.append(number)
            self.max.append(number)
            self.stack.append(number)

    def getMin(self):
        return self.min[-1]

    def getMax(self):
        return self.max[-1]
    

x = MinMaxStack()
x.push(1)
