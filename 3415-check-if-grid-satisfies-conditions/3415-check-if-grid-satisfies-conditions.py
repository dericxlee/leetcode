class Solution:
    def satisfiesConditions(self, grid: List[List[int]]) -> bool:
        row, col = len(grid), len(grid[0])

        def dfs(i, j):
            if i >= row or j >= col:
                return True
            
            if i + 1 < row and grid[i+1][j] != grid[i][j]:
                return False
            
            if j + 1 < col and grid[i][j+1] == grid[i][j]:
                return False
            
            if dfs(i + 1, j) and dfs(i, j + 1):
                return True
            
            return False
        
        return dfs(0, 0)
