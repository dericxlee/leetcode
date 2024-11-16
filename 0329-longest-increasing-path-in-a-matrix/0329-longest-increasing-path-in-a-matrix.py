class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        row, col = len(matrix), len(matrix[0])
        memo = defaultdict(int)

        def dfs(i, j):
            if (i, j) in memo:
                return memo[(i, j)]
            
            count = 1

            directions = [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]

            for x, y in directions:
                if x >= 0 and y >= 0 and x < row and y < col and matrix[x][y] > matrix[i][j]:
                    count = max(count, 1 + dfs(x, y)) 
            
            memo[(i, j)] = count
            return count
        
        return max(dfs(i, j) for i in range(row) for j in range(col))
