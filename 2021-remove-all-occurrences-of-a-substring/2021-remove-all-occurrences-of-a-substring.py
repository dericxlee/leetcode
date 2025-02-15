class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        n = len(part)
        stack = ""

        for char in s:
            stack += char

            if stack[len(stack) - n:] == part:
                stack = stack[:len(stack) - n]
        
        return stack