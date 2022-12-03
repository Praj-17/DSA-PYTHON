def N_Queen(N):
    def print_solution(board:list[list]):
        for i in range(N):
            for j in range(N):
                print(board[i][j], end = " ")
            print()
    def isSafe(board, row, col):
        #check one by one the left sides of each row
        
        #1. check in row
        for i in range(col):
            if board[row][i] ==1:
                return False
        
        #2. check in upper diagonal
        for i, j in zip(range(row,-1,-1), range (col, -1,-1)):
            if board[i][j] == 1:
                return False
        #3. check for lower diagonal
        for i, j in zip(range(row,N,1), range (col, -1,-1)):
            if board[i][j] == 1:
                return False
        return True
    def solve(board,col):
        if col >= N:
            return True
        for i in range(N):
            if isSafe(board, i, col):
            # Place this queen in board[i][col]
                board[i][col] = 1
            # recur to place rest of the queens
                if solve(board, col + 1) == True:
                    return True
            
                #if the above recursion is stuck somewhere
                #we will backtrack
                board[i][col] = 0
        return False
    
    
    def main():
        board = [[0 for j in range(N)] for _ in range(N)]
        if solve(board, 0) == False:
            print ("Solution does not exist")
            return False
        print_solution(board)
        return True
    return main()

print(N_Queen(64))
        
    
            
        
        
            
        
        
    