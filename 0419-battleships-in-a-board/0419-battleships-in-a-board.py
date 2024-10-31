class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        res = 0
        seen = set()

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "." or (i, j) in seen:
                    continue
                
                res +=1
                seen.add((i, j))

                row = i
                col = j
                
                while row < len(board) - 1 and board[row+1][col] == "X":
                    seen.add((row+1, col))
                    row+=1
                
                while col < len(board[0]) - 1 and board[row][col+1] == "X":
                    seen.add((row, col+1))
                    col+=1
            
        return res