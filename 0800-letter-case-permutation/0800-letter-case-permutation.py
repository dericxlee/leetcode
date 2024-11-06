class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        num = '0123456789'
        result = []

        def backtrack(index, string):
            if index >= len(s):
                result.append(string)
                return
            
            if s[index] not in num:
                backtrack(index+1, string+s[index].lower())
                backtrack(index+1, string+s[index].upper())
            else:
                backtrack(index+1, string+s[index])
        
        backtrack(0, "")
        return result
