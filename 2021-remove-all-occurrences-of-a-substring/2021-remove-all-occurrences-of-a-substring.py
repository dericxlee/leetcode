class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        n = len(part)
        stack = []

        for char in s:
            stack.append(char)

            if "".join(stack[len(stack) - n:]) == part:
                stack = stack[:len(stack) - n]
        
        return "".join(stack)