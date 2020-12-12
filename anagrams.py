# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 21:47:50 2020

@author: hungd
"""

def groupAnagrams(words):
    # Write your code here.
    anagrams = []
    while words:
        anagram = []
        word0 = words[0]
        anagram.append(word0)
        popIndex = [0]
        for i in range(1, len(words)):
            wordi = words[i]
            for j in range(len(word0)):
                if word0[j] in wordi:
                    letterIndex = wordi.index(word0[j])
                    if letterIndex == len(wordi) - 1:
                        wordi = wordi[:letterIndex]
                    else:
                        wordi = wordi[:letterIndex] + wordi[letterIndex + 1:]
            if not wordi:
                anagram.append(words[i])
                popIndex.append(i)
        print(popIndex)
        anagrams.append(anagram)
        for i in range(len(popIndex)):
            del words[popIndex[i]]
        print(words)
            
    return anagrams
            
words = ["yo", "act", "flop", "tac", "foo", "cat", "oy", "olfp"]
print(words)
groupAnagrams(words)