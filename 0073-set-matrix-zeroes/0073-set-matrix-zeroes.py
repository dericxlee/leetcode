class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row = set()
        col = set()
    
        for m in range(len(matrix)):
            for n in range(len(matrix[0])):
                if matrix[m][n] == 0:
                    row.add(m)
                    col.add(n)
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i in row or j in col:
                    matrix[i][j] = 0
        
        
