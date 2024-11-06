class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row = len(board)
        col = len(board[0])

        def backtrack(m, n, index, memo):
            if len(memo) == len(word):
                return True

            if m < 0 or n < 0 or m >= row or n >= col or board[m][n] != word[index] or (m, n) in memo:
                return False

            memo.add((m, n))
            
            directions = (
                backtrack(m+1, n, index+1, memo) or
                backtrack(m-1, n, index+1, memo) or
                backtrack(m, n+1, index+1, memo) or
                backtrack(m, n-1, index+1, memo)
            )

            memo.remove((m, n))
            return directions
        
        for i in range(row):
            for j in range(col):
                if backtrack(i, j, 0, set()):
                    return True
        
        return False
        

            

            


