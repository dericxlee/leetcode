class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        result = 0

        def backtrack(i, j, sum, memo):
            nonlocal result

            if i < 0 or j < 0 or i >= row or j >= col or grid[i][j] == 0 or (i, j) in memo:
                result = max(result, sum)
                return
            
            memo.add((i, j))

            backtrack(i-1, j, sum+grid[i][j], memo) 
            backtrack(i+1, j, sum+grid[i][j], memo)
            backtrack(i, j-1, sum+grid[i][j], memo)
            backtrack(i, j+1, sum+grid[i][j], memo)
            
            memo.remove((i, j))


        for i in range(row):
            for j in range(col):
                backtrack(i, j, 0, set())
        
        return result
            

