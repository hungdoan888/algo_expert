# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 21:05:15 2021

@author: hungd
"""

def solveSudoku(board):
    # Write your code here.
    board_truth = [list(x) for x in board]
    i = 0
    while i < 9:
        j = 0
        while j < 9:
            if board_truth[i][j] != 0:
                j += 1
                continue
            
            # insert value and check if it is ok
            OkToInsert = insertValidValue(board, 1, i, j)
            
            # if it is not possible, backtrack
            if not OkToInsert:
                i, j = backtrack(board, board_truth, i, j)
            j += 1
        i += 1
    return board
            

def backtrack(board, board_truth, row, col):
    
    board[row][col] = 0
    if col == 0:
        col = 9
    else:
        row += 1
        
    for i in reversed(range(row)):
        for j in reversed(range(col)):
            if board_truth[i][j] != 0:
                continue
            
            OkToInsert = insertValidValue(board, board[i][j] + 1, i, j)
            
            # if it is not possible, backtrack
            if not OkToInsert:
                board[i][j] = 0
            else:
                return i, j
        col = 9
                   
# Valid Value
def insertValidValue(board, start, i, j):
    for value in range(start, 10):
        board[i][j] = value
        if isValidInRow(board, i, j) and isValidInCol(board, i, j) and isValidInGrid(board, i, j):
            return True
    return False


# Valid Row checker
def isValidInRow(board, row, col):
    
    for j in range(9):
        if col == j:
            continue
        
        if board[row][col] == board[row][j]:
            return False
    return True


# Valid column checker
def isValidInCol(board, row, col):
    
    for i in range(9):
        if row == i:
            continue
        
        if board[row][col] == board[i][col]:
            return False
    return True
 
    
# Valid Grid Checker     
def isValidInGrid(board, row, col):
    
    # Grid 1
    if row < 3 and col < 3:
        for i in range(3):
            for j in range(3):
                if row == i and col == j:
                    continue
                
                if board[row][col] == board[i][j]:
                    return False
                
    # Grid 2
    elif row < 3 and (col >= 3 and col < 6):
        for i in range(3):
            for j in range(3, 6):
                if row == i and col == j:
                    continue
                
                if board[row][col] == board[i][j]:
                    return False
    
    # Grid 3
    elif row < 3 and col >= 6:
        for i in range(3):
            for j in range(6, 9):
                if row == i and col == j:
                    continue
                
                if board[row][col] == board[i][j]:
                    return False
    
    # Grid 4
    elif (row >= 3 and row < 6) and col < 3:
        for i in range(3, 6):
            for j in range(3):
                if row == i and col == j:
                    continue
                
                if board[row][col] == board[i][j]:
                    return False
    
    # Grid 5
    elif (row >= 3 and row < 6) and (col >= 3 and col < 6):
        for i in range(3, 6):
            for j in range(3, 6):
                if row == i and col == j:
                    continue
                
                if board[row][col] == board[i][j]:
                    return False
    
    # Grid 6
    elif (row >= 3 and row < 6) and col >= 6:
        for i in range(3, 6):
            for j in range(6, 9):
                if row == i and col == j:
                    continue
                
                if board[row][col] == board[i][j]:
                    return False
    
    # Grid 7
    elif row >= 6 and col < 3:
        for i in range(6, 9):
            for j in range(3):
                if row == i and col == j:
                    continue
                
                if board[row][col] == board[i][j]:
                    return False
    
    # Grid 8
    elif row >= 6 and (col >= 3 and col < 6):
        for i in range(6, 9):
            for j in range(3, 6):
                if row == i and col == j:
                    continue
                
                if board[row][col] == board[i][j]:
                    return False
    
    # Grid 9
    else:
        for i in range(6, 9):
            for j in range(6, 9):
                if row == i and col == j:
                    continue
                
                if board[row][col] == board[i][j]:
                    return False
    return True


board = [
  [7, 8, 0, 4, 0, 0, 1, 2, 0],
  [6, 0, 0, 0, 7, 5, 0, 0, 9],
  [0, 0, 0, 6, 0, 1, 0, 7, 8],
  [0, 0, 7, 0, 4, 0, 2, 6, 0],
  [0, 0, 1, 0, 5, 0, 9, 3, 0],
  [9, 0, 4, 0, 6, 0, 0, 0, 5],
  [0, 7, 0, 3, 0, 0, 0, 1, 2],
  [1, 2, 0, 0, 0, 7, 4, 0, 0],
  [0, 4, 9, 2, 0, 6, 0, 0, 7]
]
solveSudoku(board)