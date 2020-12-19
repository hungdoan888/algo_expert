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
        node = self.root
        for i in range(len(string)):
            if string[i] not in node:
                node[string[i]] = {}
            node = node[string[i]]
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
        
    # Traverse Board
    wordsInBoard = {}
    for i in range(len(board)):
        for j in range(len(board[0])):
            node = trie.root
            visited = [[False for l in range(len(board[0]))] for k in range(len(board))]
            word = ""
            wordsInBoard = boggleBoardHelper(board, node, visited, word, wordsInBoard, i, j)
    return list(wordsInBoard.keys())

def boggleBoardHelper(board, node, visited, word, wordsInBoard, i, j):
    
    if board[i][j] not in node:
        return wordsInBoard
    
    node = node[board[i][j]]            
    visited[i][j] = True
    word = word + board[i][j]

    if "*" in node:
        if word not in wordsInBoard:
            wordsInBoard[word] = True
    
    neighbors = neighborsList(visited, board, i, j)
    for k in range(len(neighbors)):
        wordsInBoard = boggleBoardHelper(board, 
                                         node, 
                                         visited, 
                                         word, 
                                         wordsInBoard, 
                                         neighbors[k][0], 
                                         neighbors[k][1])
        
    visited[i][j] = False
    return wordsInBoard
        
        
def neighborsList(visited, board, i, j):
    
    neighbors = []
    for k in range(i-1, i+2):
        for l in range(j-1, j+2):
            if k < 0 or l < 0:
                continue
            if k >= len(board) or l >= len(board[0]):
                continue
            if k == i and l == j:
                continue
            if visited[k][l] is True:
                continue
            neighbors.append([k,l])
    return neighbors

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

boggleBoard(board, words)

