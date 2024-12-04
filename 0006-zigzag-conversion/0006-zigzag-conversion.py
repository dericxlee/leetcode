class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        result = [""]*numRows
        direction = -1
        row = 0

        for char in s:
            result[row] += char

            if row == 0 or row == numRows - 1:
                direction *= (-1)
            
            row += direction
        
        return ''.join(result)


