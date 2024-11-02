class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
            
        phone = {
            '2': ['a', 'b', 'c'], 
            '3': ['d', 'e', 'f'], 
            '4': ['g', 'h', 'i'], 
            '5': ['j', 'k', 'l'], 
            '6': ['m', 'n', 'o'], 
            '7': ['p', 'q', 'r', 's'], 
            '8': ['t', 'u', 'v'], 
            '9': ['w', 'x', 'y', 'z']
            }

        result = []

        def dfs(i, combo):
            if len(combo) == len(digits):
                result.append(combo)
                return
            
            for char in phone[digits[i]]:
                dfs(i+1, combo+char)
            
        dfs(0, '')
        return result


