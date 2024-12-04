class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        pointer = 0
        n = len(str2)

        for char in str1:
            if pointer >= n:
                break

            num1 = ord(char)
            num2 = ord(str2[pointer])

            if num1 == num2 or (num1 - 96) % 26 == num2 - 97:
                pointer += 1
        
        return n == pointer

