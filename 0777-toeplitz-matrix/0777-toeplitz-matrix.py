class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        row, col = len(matrix), len(matrix[0])

        for i in range(col):
            num = matrix[0][i]
            x, y = 1, i + 1

            while x < row and y < col:
                if num != matrix[x][y]:
                    return False
                
                x += 1
                y += 1
        
        for i in range(1, row):
            num = matrix[i][0]
            x, y = i + 1, 1

            while x < row and y < col:
                if num != matrix[x][y]:
                    return False
                
                x += 1
                y += 1
        
        return True






        

