class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        phone = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        result = []

        def backtrack(i, combo):
            if i >= len(digits):
                result.append(combo)
                return
            
            for char in phone[digits[i]]:
                backtrack(i+1, combo+char)
        
        backtrack(0, "")
        return result
            

