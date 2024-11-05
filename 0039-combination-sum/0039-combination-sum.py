class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        def dfs(sum, arr):
            if sum > target:
                return 
            
            if sum == target:
                result.append(arr)
                return
            
            for candidate in candidates:
                if not arr or arr[-1] <= candidate:
                    dfs(sum+candidate, arr + [candidate])
        
        dfs(0, [])
        return result

            