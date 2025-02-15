class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        n = len(part)
        stack = []

        for char in s:
            stack.append(char)

            if len(stack) >= n and "".join(stack[-n:]) == part:
                stack = stack[:-n]
        
        return "".join(stack)