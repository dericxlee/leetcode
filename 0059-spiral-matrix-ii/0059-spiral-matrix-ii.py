class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0] * n for _ in range(n)]
        num = 1

        top, down = 0, n - 1
        left, right = 0, n - 1

        while top <= down and left <= right:
            for i in range(left, right+1):
                matrix[top][i] = num
                num += 1
            
            top += 1

            for i in range(top, down+1):
                matrix[i][right] = num
                num += 1
            
            right -= 1
            
            for i in range(right, left - 1, -1):
                matrix[down][i] = num
                num += 1
            
            down -= 1

            for i in range(down, top - 1, -1):
                matrix[i][left] = num
                num += 1

            left += 1
            
        return matrix