# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 18:42:22 2021

@author: hungd
"""

# This is an input class. Do not edit.
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


def removeDuplicatesFromLinkedList(head):
    # Write your code here.
    prevNode = None
    node = head
    while node is not None:
        if prevNode is not None and prevNode.value == node.value:
            prevNode.next = node.next
        else:
            prevNode = node
        node = node.next
    return head
            
head= LinkedList(1).addMany([1, 2, 3, 4, 4, 4, 5, 6])
node = removeDuplicatesFromLinkedList(head)

while node is not None:
    print(node.value)
    node = node.next