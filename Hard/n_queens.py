class Solution:
    def __init__(self) -> None:
        self.result = []

    def solveNQueens(self, n: int):
        if n == 0:
            return []
        if n == 1:
            return ['Q']
        
        G = [['.'] * n for _ in range(n)] 

        def isSafe(row, col, G):
            for i in range(row):
                if G[i][col] == 'Q':
                    return False
            for i, j in zip(range(row - 1, -1, -1), range(col - 1, -1, -1)):
                if G[i][j] == 'Q':
                    return False
            for i, j in zip(range(row - 1, -1, -1), range(col + 1, n)):
                if G[i][j] == 'Q':
                    return False
            return True
    
        def preprocess(G):
            re = []
            for i in G:
                re.append("".join(i))
            return re

        def solve(row):
            for i in range(n):
                if isSafe(row, i, G):
                    G[row][i] = 'Q'
                    if row == n - 1:
                        self.result.append(preprocess(G))
                    else:
                        solve(row + 1)
                    G[row][i] = '.'
        solve(0)
        return self.result