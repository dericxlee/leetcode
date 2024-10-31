class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        row = len(obstacleGrid)
        col = len(obstacleGrid[0])
        memo = {}

        def dfs(x, y):
            if x >= row or y >= col or obstacleGrid[x][y] == 1:
                return 0
            
            if (x, y) in memo:
                return memo[(x, y)]

            if x == row - 1 and y == col - 1:
                return 1
            
            memo[(x, y)] = dfs(x + 1, y) + dfs(x, y + 1)
            return memo[(x, y)]

        return dfs(0, 0)
        

