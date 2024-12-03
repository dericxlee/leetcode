class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        result = ""
        index = set(spaces)

        for i in range(len(s)):
            if i in index:
                result += " "
                
            result += s[i]

        return result