class Solution:
    def countDistinct(self, nums: List[int], k: int, p: int) -> int:
        res = set()
        n = len(nums)

        for i in range(n):
            div = 0
            arr = []
            for j in range(i, n):
                if nums[j] % p == 0:
                    div += 1
                
                if div > k:
                    break
                
                arr.append(nums[j])

                res.add(tuple(arr))
        
        return len(res)
