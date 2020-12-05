# This is an input class. Do not edit.
class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


# Feel free to add new properties and methods to the class.
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def setHead(self, nodeToInsert):
        node = self.head
        if node is None:
            self.head = nodeToInsert
            self.tail = nodeToInsert
        else:
            self.insertBefore(node, nodeToInsert)

    def setTail(self, nodeToInsert):
        node = self.tail
        if node is None:
            self.head = nodeToInsert
            self.tail = nodeToInsert
        else:
            self.insertAfter(node, nodeToInsert)
        
    def insertBefore(self, node, nodeToInsert):
        self.remove(nodeToInsert)
        nodeToInsert.next = None
        nodeToInsert.prev = None
        if node.prev is None:
            node.prev = nodeToInsert
            nodeToInsert.next = node
            self.head = nodeToInsert
        else:
            node.prev.next = nodeToInsert
            nodeToInsert.prev = node.prev
            node.prev = nodeToInsert
            nodeToInsert.next = node

    def insertAfter(self, node, nodeToInsert):
        self.remove(nodeToInsert)
        nodeToInsert.next = None
        nodeToInsert.prev = None
        if node.next is None:
            node.next = nodeToInsert
            nodeToInsert.prev = node
            self.tail = nodeToInsert
        else:
            node.next.prev = nodeToInsert
            nodeToInsert.next = node.next
            nodeToInsert.prev = node
            node.next = nodeToInsert

    def insertAtPosition(self, position, nodeToInsert):
        node = self.head
        if node is None:
            node = nodeToInsert
            self.head = nodeToInsert
            self.tail = nodeToInsert
            return
        
        for _ in range(position-1):
            node = node.next
        self.remove(nodeToInsert)
        nodeToInsert.next = None
        nodeToInsert.prev = None
        self.insertBefore(node, nodeToInsert)
        
        
    def removeNodesWithValue(self, value):
        node = self.head
        while node is not None:
            if node.value == value:
                nodeToRemove = node
                node = node.next
                self.remove(nodeToRemove)
            else:
                node = node.next

    def remove(self, node):
        if node.next is None and node.prev is None:
            if node == self.head:
                self.head = None
                self.tail = None
        elif node.next is None:
            node.prev.next = None
            self.tail = node.prev
            node.prev = None
        elif node.prev is None:
            node.next.prev = None
            self.head = node.next
            node.next = None
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
            node.prev = None
            node.next = None

    def containsNodeWithValue(self, value):
        node = self.head
        while node is not None:
            if node.value == value:
                return True
            node = node.next
        return False
    
def printx(x):
    node = x.head
    xlist = []
    while node is not None:
        xlist.append(node.value)
        node = node.next
    print(xlist)
                        
x1 = Node("1")       
x2 = Node("2")
x3 = Node("3")
x4 = Node("4")

x = DoublyLinkedList()

x.setHead(x1)
printx(x)

x.remove(x1)
printx(x)