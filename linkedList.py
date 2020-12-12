# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14 17:42:38 2020

@author: hungd
"""

# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeKthNodeFromEnd(head, k):
    # Write your code here.
    first = head
    second = head
    
    for _ in range(k):
        second = second.next
        
    if second is None:
        head.value = first.next.value
        head.next = first.next.next
        return

    while second.next is not None:
        first = first.next
        second = second.next
    
    first.next = first.next.next

def printlinkedList(head):
    node = head
    while node is not None:
        print(node.value)
        node = node.next

node0 = LinkedList(0)
node1 = LinkedList(1)
node2 = LinkedList(2)
node3 = LinkedList(3)
# node4 = LinkedList(4)
# node5 = LinkedList(5)
# node6 = LinkedList(6)
# node7 = LinkedList(7)
# node8 = LinkedList(8)
# node9 = LinkedList(9)

node0.next = node1
node1.next = node2
node2.next = node3
node3.next = None
# node4.next = node5
# node5.next = node6
# node6.next = node7
# node7.next = node8
# node8.next = node9
# node9.next = None

head = node0
k = 4

printlinkedList(head)
removeKthNodeFromEnd(head, k)
printlinkedList(head)
