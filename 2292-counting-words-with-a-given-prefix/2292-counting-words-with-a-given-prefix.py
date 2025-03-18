class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        def isPrefix(word: str):
            n = len(word)
            for i in range(len(pref)):
                if i >= n or word[i] != pref[i]:
                    return False
            
            return True

        count = 0
        
        for word in words:
            if isPrefix(word):
                count += 1
        
        return count