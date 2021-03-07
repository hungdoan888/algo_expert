# -*- coding: utf-8 -*-
"""
Created on Fri Mar  5 08:09:46 2021

@author: hungd
"""

def generateDocument(characters, document):
    # Write your code here.
    chars_dict = {}
    for i in range(len(characters)):
        if characters[i] not in chars_dict:
            chars_dict[characters[i]] = 1
        else:
            chars_dict[characters[i]] += 1
    
    for i in range(len(document)):
        if document[i] not in chars_dict:
            return False
        elif chars_dict[document[i]] == 0:
            return False
        else:
            chars_dict[document[i]] -= 1
    return True

characters = "Bste!hetsi ogEAxpelrt x "
document = "AlgoExpert is the Best!"
generateDocument(characters, document)
