class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []

        for n in num:
            while stack and int(stack[-1]) > int(n) and k:
                stack.pop()
                k-=1
            
            if not int(n) and not stack:
                continue

            stack.append(n)

        while k and stack:
            stack.pop()
            k-=1
        
        string = ''.join(stack)
        
        if not string:
            return "0"
        
        return string
            