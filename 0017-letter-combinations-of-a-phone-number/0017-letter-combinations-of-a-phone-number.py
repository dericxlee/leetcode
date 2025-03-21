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
                result.append("".join(combo))
                return
            
            for char in phone[digits[i]]:
                combo.append(char)
                backtrack(i+1, combo)
                combo.pop()
        
        backtrack(0, [])
        return result
            

