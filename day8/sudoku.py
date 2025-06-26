#differentiate, when to append to results and when to solve in place
def solveSudoku(board):

    def find_start(i):
        if i in [0,1,2]:
            return 0
        elif i in [3,4,5]:
            return 3
        else:
            return 6
        return -1
    
    def isValid(board, i, j, val):
        if board[i][j]==".":
            #row and column checks
            for a in range(9):
                if board[a][j] == val:
                    return False
                if board[i][a] == val:
                    return False
            #box check
            for a in range(find_start(i), find_start(i)+3):
                for b in range(find_start(j), find_start(j)+3):
                    if board[a][b] == val:
                         return False
        return True
    
    def fill_the_board(board):
        for row in range(9):
            for col in range(9):
                if board[row][col] == ".":
                    for num in '123456789':
                        if isValid(board, row, col, num):
                            board[row][col] = num
                            if(fill_the_board(board)): return True
                            board[row][col] = "."
                    return False
        
        return True

    fill_the_board(board)


sudoku_board = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"]
]
solveSudoku(sudoku_board)
print(sudoku_board)

