class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        memo = set()

        def backtrack(idx, x, y):
            if idx == len(word):
                return True
            
            for dx, dy in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                if 0 <= dx < m and 0 <= dy < n and (dx, dy) not in memo and board[dx][dy] == word[idx]:
                    memo.add((dx, dy))
                    if backtrack(idx + 1, dx, dy):
                        return True
                    memo.remove((dx, dy))
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    memo.add((i, j))
                    if backtrack(1, i, j):
                        return True
                    memo.remove((i, j))

        return False