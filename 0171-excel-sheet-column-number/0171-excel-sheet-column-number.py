class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        result = 0

        for i in range(len(columnTitle)):
            result *= 26
            char = columnTitle[i]
            result += ord(char) - 64
        
        return result
            