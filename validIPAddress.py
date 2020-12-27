# -*- coding: utf-8 -*-
"""
Created on Sat Dec 26 18:16:09 2020

@author: hungd
"""

def validIPAddresses(string):
    # Write your code here.
    output = []
    for i in range(1, 4):
        if not criteriaMet(string, 0, i):
            continue
        
        max_j = i + 4
        for j in range(i, max_j):
            if not criteriaMet(string, i, j):
                continue
            
            max_k = j + 4
            for k in range(j, max_k):
                if not criteriaMet(string, j, k):
                    continue
                
                if not criteriaMet(string, k, len(string)):
                    continue
                
                output.append(string[:i] + "." + 
                              string[i:j] + "." + 
                              string[j:k] + "." +
                              string[k:])
    return output if output else []
                
def criteriaMet(string, i, j):
    
    if i > len(string) or j > len(string) or i == j:
        return False
    
    str_1 = string[i:j]
    num_1 = int(str_1)
    
    if num_1 > 255:
        return False
    
    if len(str_1) > 1 and str_1[0] == "0":
        return False
    return True
    
string = "1921680"
validIPAddresses(string)