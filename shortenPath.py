# -*- coding: utf-8 -*-
"""
Created on Sun Feb  7 12:27:04 2021

@author: hungd
"""

def shortenPath(path):
    # Write your code here.
    root = PathStartsWithSlash(path)
    path = path.split("/")
    path = removeBlankandDot(path)
    path = removeDoubleDots(path, root)
    
    if root:
        path = [""] + path
    path = "/".join(path)
    return path if path != "" else "/"
        
    
def removeDoubleDots(path, root):
    idx = 0
    while idx < len(path):
        if path[idx] != "..":
            idx += 1
            continue
        
        if root and idx == 0:
            path.pop(idx)
            continue
        
        if not root and idx == 0:
            idx += 1
            continue
        
        print(idx, path)
            
        if path[idx - 1] != "..":
            path.pop(idx - 1)
            path.pop(idx - 1)
            idx -= 1
        else:
            idx += 1
    return path
                  
def removeBlankandDot(path):
    idx = 0
    while idx <= len(path) - 1:
        if path[idx] == "" or path[idx] == ".":
            path.pop(idx)
        else:
            idx += 1
    return path

def PathStartsWithSlash(path):
    if len(path) == 0:
        return False
    elif path.startswith("/"):
        return True
    else:
        return False

path = "../../foo/bar/baz"
shortenPath(path)