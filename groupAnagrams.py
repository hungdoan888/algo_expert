# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 08:02:28 2020

@author: hungd
"""

def groupAnagrams(words):
    # Write your code here.
    anagrams = {}
    for i in range(len(words)):
        sortedWord = "".join(sorted(words[i]))
        if sortedWord in anagrams:
            anagrams[sortedWord].append(words[i])
        else:
            anagrams[sortedWord] = [words[i]]
    
    print(anagrams.values())
    return list(anagrams.values())
    
words = ["cinema", "a", "flop", "iceman", "meacyne", "lofp", "olfp"]
groupAnagrams(words)