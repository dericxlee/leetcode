class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        seen = [[False]*col for _ in range(row)]
        result = 0

        def backtrack(i, j, sum):
            nonlocal result

            if i < 0 or j < 0 or i >= row or j >= col or grid[i][j] == 0 or seen[i][j]:
                result = max(result, sum)
                return
            
            seen[i][j] = True

            backtrack(i-1, j, sum+grid[i][j]) 
            backtrack(i+1, j, sum+grid[i][j])
            backtrack(i, j-1, sum+grid[i][j])
            backtrack(i, j+1, sum+grid[i][j])
            
            seen[i][j] = False


        for i in range(row):
            for j in range(col):
                backtrack(i, j, 0)
        
        return result
            

