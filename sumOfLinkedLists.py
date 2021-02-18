# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 18:53:16 2021

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


def getNodesInArray(output):
    nodes = []
    current = output
    while current is not None:
        nodes.append(current.value)
        current = current.next
    return nodes

def sumOfLinkedLists(ll1, ll2):
    # Write your code here.
    total_ll1 = getSumOfLinkedList(ll1)
    total_ll2 = getSumOfLinkedList(ll2)
    total = str(total_ll1 + total_ll2)
    ll3 = LinkedList(int(total[-1]))
    head = ll3
    print(ll3.value)
    for i in reversed(range(len(total) - 1)):
        ll3.next = LinkedList(int(total[i]))
        ll3 = ll3.next
        print(ll3.value)
    return head
        
def getSumOfLinkedList(ll):
    multiplier = 1
    total = 0
    while ll is not None:
        total += ll.value * multiplier
        ll = ll.next
        multiplier *= 10
    return total
        
    
linkedListOne = LinkedList(2).addMany([4, 7, 1])
linkedListTwo = LinkedList(9).addMany([4, 5])
sumOfLinkedLists(linkedListOne, linkedListTwo)