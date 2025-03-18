class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        reverse = ""
        idx = 0

        for i in range(len(word)):
            char = word[i]

            reverse = char + reverse

            if char == ch:
                idx = i + 1
                break
        
        return reverse + word[idx:] if idx else word