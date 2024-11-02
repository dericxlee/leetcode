class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        def dfs(i, j, di, dj):
            if i < 0 or j < 0 or i >= 8 or j >= 8 or board[i][j] == 'B':
                return 0
            
            if board[i][j] == 'p':
                return 1
            
            return dfs(i + di, j + dj, di, dj)
            
        for i in range(8):
            for j in range(8):
                if board[i][j] == 'R':
                    return (
                        dfs(i, j, -1, 0) +
                        dfs(i, j, 1, 0) +
                        dfs(i, j, 0, 1) +
                        dfs(i, j, 0, -1)
                    )



            
