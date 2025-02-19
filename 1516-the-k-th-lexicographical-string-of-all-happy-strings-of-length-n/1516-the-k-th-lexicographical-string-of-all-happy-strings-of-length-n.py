class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        happy = "abc"
        combo = []

        def backtrack(curr):
            if len(curr) == n:
                string = "".join(curr)
                combo.append(string)
                return

            for char in happy:
                if curr and curr[-1] == char:
                    continue
                
                curr.append(char)
                backtrack(curr)
                curr.pop()
            
        backtrack([])

        if len(combo) < k:
            return ""
        else:
            return combo[k-1]
