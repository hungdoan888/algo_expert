# -*- coding: utf-8 -*-
"""
Created on Sat Jan 23 14:31:34 2021

@author: hungd
"""

class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

    def addMany(self, values):
        current = self
        while current.next is not None:
            current = current.next
        for value in values:
            current.next = LinkedList(value)
            current = current.next
        return self

    def getNodesInArray(self):
        nodes = []
        current = self
        while current is not None:
            nodes.append(current.value)
            current = current.next
        return nodes
    
def reverseLinkedList(head):
    # Write your code here.
    if head.next is None:
        return head
    
    p1 = None
    p2 = head
    
    while p2 is not None:
        p3 = p2.next
        p2.next = p1
        p1 = p2
        p2 = p3
    
    head = p1
    return head

head = LinkedList(0).addMany([1, 2, 3, 4, 5])
newHead = reverseLinkedList(head)
