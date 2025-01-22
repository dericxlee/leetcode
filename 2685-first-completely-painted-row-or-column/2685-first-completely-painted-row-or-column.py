class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        n = len(mat)
        m = len(mat[0])

        lookup = [(0, 0)]*(len(arr) + 1)
        row = [m]*n
        column = [n]*m

        for i in range(n):
            for j in range(m):
                num = mat[i][j]

                lookup[num] = (i, j)
        
        for i in range(len(arr)):
            num = arr[i]
            x, y = lookup[num]

            row[x] -= 1
            column[y] -= 1

            if not row[x] or not column[y]:
                return i
        
            

