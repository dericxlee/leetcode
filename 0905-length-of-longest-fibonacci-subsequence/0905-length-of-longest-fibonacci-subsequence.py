class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        map = {num: i for i, num in enumerate(arr)}
        dp = {}
        n = len(arr)
        result = 0

        for i in range(n):
            for j in range(i):
                k = map.get(arr[i] + arr[j])

                if k is not None and k > i:
                    dp[i, k] = dp.get((j, i), 2) + 1
                
                    result = max(result, dp[i, k])
        
        return result if result >= 3 else 0



