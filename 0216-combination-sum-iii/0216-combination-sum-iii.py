class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        if not k or not n:
            return []
        
        result = []
        
        def backtrack(i, target, array):
            if len(array) == k and target == 0:
                result.append(array.copy())
                return
            
            if len(array) == k or target <= 0 or i > 9:
                return

            backtrack(i+1, target, array)
            
            target -= i
            array.append(i)

            backtrack(i+1, target, array)

            target += i
            array.pop()
        
        backtrack(1, n, [])
        return result
            