class Solution:
    def clearDigits(self, s: str) -> str:
        digits = set(["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"])
        stack = []

        for char in s:
            if stack and char in digits:
                stack.pop()
            else:
                stack.append(char)
        
        return "".join(stack) if stack else ""
