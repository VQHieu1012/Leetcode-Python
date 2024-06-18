class Solution:

    def totalNQueens(self, n: int) -> int:
        count = 0
        G = [['.'] * n for _ in range(n)]

        def isSafe(row, col, G):
            for i in range(row):
                if G[i][col] == 'Q':
                    return False
            
            for i, j in zip(range(row-1, -1, -1), range(col-1, -1, -1)):
                if G[i][j] == 'Q':
                    return False
            
            for i, j in zip(range(row-1, -1, -1), range(col+1, n)):
                if G[i][j] == 'Q':
                    return False
            return True

        def solve(row):
            nonlocal count
            for i in range(n):
                if isSafe(row, i, G):
                    G[row][i] = 'Q'
                    if row == n - 1:
                        count += 1
                    else:
                        solve(row + 1)
                    G[row][i] = '.'
        solve(0)
        return count



