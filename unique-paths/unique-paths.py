class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        grid = [[None]*n]*m
        grid[0] = [1]*n
        for i in range(1, m):
            grid[i][0] = 1
        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] = grid[i - 1][j] + grid[i][j - 1]
        return grid[m-1][n-1]