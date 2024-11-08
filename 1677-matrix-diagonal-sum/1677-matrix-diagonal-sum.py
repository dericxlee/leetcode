class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        result = 0
        center = 0

        if n % 2 != 0:
            mid = (n-1)/2
            center = mat[int(mid)][int(mid)]

        for i in range(n):
            result += mat[i][i] + mat[i][n-i-1]
        
        return result - center