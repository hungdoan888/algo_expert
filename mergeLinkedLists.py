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
    
def mergeLinkedLists(headOne, headTwo):
    # Write your code here.
    p1 = headOne
    p2 = headTwo
    prev = None
    
    while p1 is not None and p2 is not None:      
        if p1.value < p2.value:
            prev = p1
            p1 = p1.next
        else:
            if prev is not None:
                prev.next = p2
            prev = p2
            p2 = p2.next
            prev.next = p1
            
    if p1 is None:
            prev.next = p2
            
    return headOne if headOne.value < headTwo.value else headTwo

def printList(node):
    while node is not None:
        print(node.value)
        node = node.next

headOne = LinkedList(2).addMany([6, 7, 8])
headTwo = LinkedList(1).addMany([3, 4, 5, 9, 10])
node = mergeLinkedLists(headOne, headTwo)
printList(node)
            
            