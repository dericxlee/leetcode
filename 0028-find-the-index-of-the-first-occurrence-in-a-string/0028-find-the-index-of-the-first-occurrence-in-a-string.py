class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        j = len(needle)

        for i in range(len(haystack)):
            if(haystack[i: i+j]) == needle:
                return i
        
        return -1
                
