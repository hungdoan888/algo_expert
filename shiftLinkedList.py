# -*- coding: utf-8 -*-
"""
Created on Thu Jan 28 19:39:27 2021

@author: hungd
"""

def shiftLinkedList(head, k):
    # Write your code here.
    if k == 0: 
        return head
    
    # Get length of linked list and tail node
    node = head
    lengthLinkedList = 0
    while node is not None:
        lengthLinkedList += 1
        tailNode = node
        node = node.next
        
    # Get newTail (node at length - k)
    newTail = head
    for i in range((lengthLinkedList - k - 1) % lengthLinkedList):
        newTail = newTail.next
        
    tailNode.next = head
    head = newTail.next
    newTail.next = None
    
    return head
    
def tester(head):
    node = head
    while node is not None:
        print(node.value)
        node = node.next
        
# This is the class of the input linked list.
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
    
head = LinkedList(0).addMany([1, 2, 3, 4, 5])
k = 2
head = shiftLinkedList(head, k)
tester(head)