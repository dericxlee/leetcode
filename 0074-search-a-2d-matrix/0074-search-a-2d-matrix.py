class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top, bot = 0, len(matrix) - 1

        while top <= bot:
            mid = (top + bot) // 2

            if matrix[mid][0] > target:
                bot = mid - 1
            elif matrix[mid][-1] < target:
                top = mid + 1
            else:
                break
        
        r = (top + bot) // 2

        left, right = 0, len(matrix[0]) - 1

        while left <= right:
            mid = (left + right) // 2

            if matrix[r][mid] == target:
                return True
            
            if matrix[r][mid] > target:
                right = mid - 1
            else:
                left = mid + 1

        return False 