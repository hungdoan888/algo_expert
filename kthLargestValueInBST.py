# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
        
class kthLargestValueClass:
    def __init__(self):
        self.value = None


def findKthLargestValueInBst(tree, k):
    # Write your code here.
    l = 0
    kthLargestValue = kthLargestValueClass()
    findKthLargestValueInBstHelper(tree, k, l, kthLargestValue)
    return kthLargestValue.value

def findKthLargestValueInBstHelper(node, k, l, kthLargestValue):
    # Write your code here.
    if node is None:
        return l
    
    if kthLargestValue.value is not None:
        return l
    
    # right
    l = findKthLargestValueInBstHelper(node.right, k, l, kthLargestValue)
    
    # visit
    l += 1
    if l == k:
        kthLargestValue.value = node.value
        return l
    
    # left
    return findKthLargestValueInBstHelper(node.left, k, l, kthLargestValue)
    
    
tree = BST(15)
tree.left = BST(5)
tree.left.left = BST(2)
tree.left.left.left = BST(1)
tree.left.left.right = BST(3)
tree.left.right = BST(5)
tree.right = BST(20)
tree.right.left = BST(17)
tree.right.right = BST(22)
k = 3
findKthLargestValueInBst(tree, k)