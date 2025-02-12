class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        if not k or not n:
            return []
        
        result = []
        
        def backtrack(start, target, array):
            if len(array) == k and target == 0:
                result.append(array.copy())
                return

            for i in range(start, 10):
                if target < i:
                    break
            
                array.append(i)
                backtrack(i + 1, target - i, array)
                array.pop()
        
        backtrack(1, n, [])
        return result
            