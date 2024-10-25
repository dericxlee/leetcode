class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        in_stack = set()
        stack = []
        freq = Counter(s)

        for char in s:
            freq[char] -= 1

            if char in in_stack:
                continue

            while stack and stack[-1] > char and freq[stack[-1]] != 0:
                c = stack.pop()
                in_stack.remove(c)
            
            stack.append(char)
            in_stack.add(char)
        
        return ''.join(stack)

