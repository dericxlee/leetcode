class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        arr = s.split(' ')
        match = {}

        if len(arr) != len(pattern):
            return False
        
        for i in range(len(arr)):
            if pattern[i] not in match and arr[i] not in match.values():
                match[pattern[i]] = arr[i]
            
            if pattern[i] not in match or match[pattern[i]] != arr[i]:
                return False

        return True