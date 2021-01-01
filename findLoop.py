# -*- coding: utf-8 -*-
"""
Created on Tue Dec 29 22:18:07 2020

@author: hungd
"""

# This is an input class. Do not edit.
class StartLinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList(StartLinkedList):
    def addMany(self, values):
        current = self
        while current.next is not None:
            current = current.next
        for value in values:
            current.next = LinkedList(value)
            current = current.next
        return self
    
    def getNthNode(self, n):
            counter = 1
            current = self
            while counter < n:
                current = current.next
                counter += 1
            return current

def findLoop(head):
    # Write your code here.
    node1 = head.next
    node2 = head.next.next
    
    while node1 != node2:
        node1 = node1.next
        node2 = node2.next.next
        
    node1 = head
    while node1 != node2:
        node1 = node1.next
        node2 = node2.next
    
    return node1
    
head = LinkedList(0).addMany([1, 2, 3, 4, 5, 6, 7, 8, 9])
head.getNthNode(10).next = head.getNthNode(5)
findLoop(head)