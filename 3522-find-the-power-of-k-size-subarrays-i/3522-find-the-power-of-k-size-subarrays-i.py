class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        result = []
        count = 1

        for i in range(1, k-1):
            if nums[i] == nums[i-1] + 1:
                count += 1
            else:
                count = 1
        
        for i in range(k-1, len(nums)):
            if nums[i] == nums[i-1] + 1:
                count += 1
            else:
                count = 1

            if count >= k:
                result.append(nums[i])
            else:
                result.append(-1)
        
        return result


        
        
