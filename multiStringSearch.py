# -*- coding: utf-8 -*-
"""
Created on Sat Mar  6 16:56:35 2021

@author: hungd
"""

# Do not edit the class below except for the
# populateSuffixTrieFrom and contains methods.
# Feel free to add new properties and methods
# to the class.
class SuffixTrie:
    def __init__(self, smallStrings):
        self.root = {}
        self.endSymbol = "*"
        self.contained = self.createArray(smallStrings)
        
    def createArray(self, smallStrings):
        smallStringsContained = [False for i in range(len(smallStrings))]
        return smallStringsContained

    def populateSuffixTrieFrom(self, string, index):
        # Write your code here.
        node = self.root
        for i in range(len(string)):
            if string[i] not in node:
                node[string[i]] = {}
            node = node[string[i]]
        node[self.endSymbol] = index
            
    def contains(self, string):
        # Write your code here.
        node = self.root
        for i in range(len(string)):
            print(node)
            print("")
            if self.endSymbol in node:
                self.contained[node[self.endSymbol]] = True
                
            if string[i] not in node:
                return
            node = node[string[i]]
        if self.endSymbol in node:
            self.contained[node[self.endSymbol]] = True

def multiStringSearch(bigString, smallStrings):
    # Write your code here.
    trie = SuffixTrie(smallStrings)
    for i in range(len(smallStrings)):
        trie.populateSuffixTrieFrom(smallStrings[i], i)
        
    for i in range(len(bigString)):
        trie.contains(bigString[i:])
        
    return trie.contained
            
    
bigString = "this is a big string"
smallStrings = ["this", "yo", "is", "a", "bigger", "string", "kappa"]
smallStringsContained = multiStringSearch(bigString, smallStrings)
smallStringsContained
