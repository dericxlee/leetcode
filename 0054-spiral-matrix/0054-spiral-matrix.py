class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        left, right = 0, len(matrix[0]) -1
        top, down = 0, len(matrix) -1

        while top <= down and left <= right:
            for i in range(left, right+1):
                result.append(matrix[top][i])

            top += 1
            
            for j in range(top, down+1):
                result.append(matrix[j][right])

            right -= 1

            if top > down:
                break
            
            for k in range(right, left-1, -1):
                result.append(matrix[down][k])
            
            down -= 1

            if left > right:
                break

            for l in range(down, top-1, -1):
                result.append(matrix[l][left])
            
            left += 1
        
        return result


            


