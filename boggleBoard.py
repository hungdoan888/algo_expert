# -*- coding: utf-8 -*-
"""
Created on Sat Dec 19 08:18:55 2020

@author: hungd
"""

#%% SuffixTrie Class

class SuffixTrie:
    def __init__(self):
        self.root = {}
        self.endSymbol = "*"

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

#%% Boggle Board Traverse

def boggleBoard(board, words):
    
    # Populate Suffix Trie
    trie = SuffixTrie()
    for i in range(len(words)):
        trie.populateSuffixTrieFrom(words[i])
        


# Input
board = [
  ["t", "h", "i", "s", "i", "s", "a"],
  ["s", "i", "m", "p", "l", "e", "x"],
  ["b", "x", "x", "x", "x", "e", "b"],
  ["x", "o", "g", "g", "l", "x", "o"],
  ["x", "x", "x", "D", "T", "r", "a"],
  ["R", "E", "P", "E", "A", "d", "x"],
  ["x", "x", "x", "x", "x", "x", "x"],
  ["N", "O", "T", "R", "E", "-", "P"],
  ["x", "x", "D", "E", "T", "A", "E"]
]

words = [
  "this",
  "is",
  "not",
  "a",
  "simple",
  "boggle",
  "board",
  "test",
  "REPEATED",
  "NOTRE-PEATED"
]


