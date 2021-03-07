# -*- coding: utf-8 -*-
"""
Created on Fri Mar  5 08:49:00 2021

@author: hungd
"""

def generateDivTags(numberOfTags):
    # Write your code here.
    tagCombos = []
    prefix = ""
    openingTags = numberOfTags
    closingTags = numberOfTags
    generateDivTagsHelper(tagCombos, prefix, openingTags, closingTags)
    return tagCombos

def generateDivTagsHelper(tagCombos, prefix, openingTags, closingTags):
    # Write your code here.
    if closingTags == 0:
        tagCombos.append(prefix)
        return 
    
    if openingTags > 0:
        generateDivTagsHelper(tagCombos, prefix + "<div>", openingTags - 1, closingTags)
        
    if closingTags > openingTags: 
        generateDivTagsHelper(tagCombos, prefix + "</div>", openingTags, closingTags - 1)

numberOfTags = 3
generateDivTags(numberOfTags)