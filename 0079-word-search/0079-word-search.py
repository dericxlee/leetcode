class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row = len(board)
        col = len(board[0])

        def dfs(i, j, index, memo):
            if len(memo) - 1 > len(word) or i < 0 or j < 0 or i >= row or j >= col or board[i][j] != word[index] or (i, j) in memo:
                return False
            
            if index + 1 == len(word):
                return True

            memo.add((i, j))
            index+=1
            
            directions = (
                dfs(i+1, j, index, memo) or
                dfs(i-1, j, index, memo) or
                dfs(i, j+1, index, memo) or
                dfs(i, j-1, index, memo)
            )

            memo.remove((i, j))

            return directions
        
        for i in range(row):
            for j in range(col):
                if dfs(i, j, 0, set()):
                    return True
        
        return False
        
        
        

            



