# This is an input class. Do not edit.
class AncestralTree:
    def __init__(self, name):
        self.name = name
        self.ancestor = None


def getYoungestCommonAncestor(topAncestor, descendantOne, descendantTwo):
    # Write your code here.
    descendantOne_depth = getNodeDepth(descendantOne)
    descendantTwo_depth = getNodeDepth(descendantTwo)
    
    while descendantOne_depth > descendantTwo_depth:
        descendantOne = descendantOne.ancestor
        descendantOne_depth -= 1
        
    while descendantTwo_depth > descendantOne_depth:
        descendantTwo = descendantTwo.ancestor
        descendantTwo_depth -= 1
        
    while descendantOne.name != descendantTwo.name:
        descendantOne = descendantOne.ancestor
        descendantTwo = descendantTwo.ancestor
        
    return descendantOne
        

def getNodeDepth(descendant):
    depth = 0
    while descendant is not None:
        depth += 1
        descendant = descendant.ancestor
    return depth 
   
topAncestor = AncestralTree('A')   

descendantOne = AncestralTree('E')
descendantOne.ancestor = AncestralTree('B')
descendantOne.ancestor.ancestor = AncestralTree('A')

descendantTwo = AncestralTree('I')
descendantTwo.ancestor = AncestralTree('D')
descendantTwo.ancestor.ancestor = AncestralTree('B')
descendantTwo.ancestor.ancestor.ancestor = AncestralTree('A')

youngestDescendant = getYoungestCommonAncestor(topAncestor, descendantOne, descendantTwo)
youngestDescendant.name
