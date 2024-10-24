class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = defaultdict(set)
        col = defaultdict(set)
        sq = defaultdict(set)

        for i in range(9):
            for j in range(9):
                current = board[i][j]

                if current == '.':
                    continue

                if current in row[i]:
                    return False

                if current in col[j]:
                    return False
                
                if current in sq[i//3, j//3]:
                    return False

                row[i].add(current)
                col[j].add(current)
                sq[i//3, j//3].add(current)
        
        return True
