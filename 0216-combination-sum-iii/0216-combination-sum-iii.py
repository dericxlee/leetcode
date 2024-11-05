class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result = []

        def backtrack(k, start, target, array):
            if not k and not target:
                result.append(array)
                return
            
            if target <= 0 or k <= 0:
                return
            
            for i in range(start, 10):
                if i > target:
                    break
                
                backtrack(k-1, i+1, target-i, array+[i])
            
        backtrack(k, 1, n, [])
        return result
            


