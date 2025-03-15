class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        prefix = [0]*len(nums)
        prefix[0] = nums[0]
        
        result = float("inf")

        for i in range(1, len(nums)):
            prefix[i] = prefix[i-1] + nums[i]
        
        print(prefix)
        
        for k in range(l, r + 1):
            total = prefix[k - 1]

            if total > 0:
                result = min(result, total)

            for i in range(k, len(nums)):
                total = prefix[i] - prefix[i - k]

                if total > 0:
                    result = min(result, total)
        
        return -1 if result == float('inf') else result
                

              
            
            


