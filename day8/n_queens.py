def solveNQueens(n):
    results = []
    board = ['.'*n for _ in range(n)]

    def isValid(board, row, col):
        n = len(board)
        for a in range(n):
            if board[a][col] == "Q":
                return False
        
        i,j = row - 1, col - 1
        while i>=0 and j>=0:
            if board[i][j] == "Q":
                return False
            i-=1
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
            results.append(board[:])
            return
        
        for j in range(n):
            if isValid(board, row, j):
                new_row = board[row][:j] + 'Q' +board[row][j+1:]
                board[row] = new_row
                nqueens(board, row+1, n)
                board[row] = "."*n

    nqueens(board, 0, n)
    return results

    

print(solveNQueens(4))
