# This first try I did returns only the first valid combination, not all
# Flaws, but learnt from them

def isValid(board, row, col):
    n = len(board)
    for a in range(n):
        if board[row][a] == "Q":
            return False
        if board[a][col] == "Q":
            return False
    
    i,j = row + 1, col + 1
    while i<n and j<n:
        if board[i][j] == "Q":
            return False
        i+=1
        j+=1
    
    i,j = row - 1, col - 1
    while i>=0 and j>=0:
        if board[i][j] == "Q":
            return False
        i-=1
        j-=1
    
    i,j = row + 1, col - 1
    while i<n and j>=0:
        if board[i][j] == "Q":
            return False
        i+=1
        j-=1

    i,j = row - 1, col + 1 
    while i>=0 and j<n:
        if board[i][j] == "Q":
            return False
        i-=1
        j+=1
    
    return True        

def nqueens(board, row, n):
    if row == n:
        return True
    
    for j in range(n):
        if isValid(board, row, j):
            board[row][j] = "Q"
            if(nqueens(board, row+1, n)): return True
            board[row][j] = ""
    return False

#kinda dirty
z = 4
board = [["" for i in range(z)] for j in range(z)]
nqueens(board, 0, z)
print(board)
