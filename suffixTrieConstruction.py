# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 13:23:31 2020

@author: hungd
"""

# Do not edit the class below except for the
# populateSuffixTrieFrom and contains methods.
# Feel free to add new properties and methods
# to the class.
class SuffixTrie:
    def __init__(self, string):
        self.root = {}
        self.endSymbol = "*"
        self.populateSuffixTrieFrom(string)

    def populateSuffixTrieFrom(self, string):
        # Write your code here.
        for i in range(len(string)):
            self.populateSuffixTrieFromHelper(string, i)
            
    def populateSuffixTrieFromHelper(self, string, i):
        node = self.root
        for j in range(i, len(string)):
            if string[j] not in node:
                node[string[j]] = {}
            node = node[string[j]]
        node[self.endSymbol] = True

    def contains(self, string):
        # Write your code here.
        node = self.root
        for i in range(len(string)):
            if string[i] not in node:
                return False
            node = node[string[i]]
        if self.endSymbol not in node:
            return False
        else:
            return True

string = "abcdba"
x = SuffixTrie(string)