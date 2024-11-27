class Solution:
    def makeFancyString(self, s: str) -> str:
        result = ""
        letter = ""
        count = 0

        for char in s:
            if char != letter:
                result += char
                letter = char
                count = 1
            elif count < 2:
                result += char
                count += 1

        return result 
