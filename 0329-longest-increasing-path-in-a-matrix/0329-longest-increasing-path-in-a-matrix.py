class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        count = 0
        row, col = len(matrix), len(matrix[0])
        seen = defaultdict(int)

        def dfs(i, j, path):
            nonlocal count
            count = max(count, path)

            if seen[(i, j)] > path:
                return
            
            seen[(i, j)] = path

            # left
            if j - 1 >= 0 and matrix[i][j-1] > matrix[i][j]:
                dfs(i, j-1, path+1)
            
            # right
            if j + 1 < col and matrix[i][j+1] > matrix[i][j]:
                dfs(i, j+1, path+1)
            
            # up
            if i - 1 >= 0 and matrix[i-1][j] > matrix[i][j]:
                dfs(i-1, j, path+1)
            
            # down
            if i + 1 < row and matrix[i+1][j] > matrix[i][j]:
                dfs(i+1, j, path+1)
        

        for i in range(row):
            for j in range(col):
                dfs(i, j, 1)

        return count


            