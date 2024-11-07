class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        seen = defaultdict(int)

        def backtrack(i):
            if i >= len(nums):
                return 1 
            
            count = backtrack(i+1)
            
            if not seen[nums[i]+k] and not seen[nums[i]-k]:
                seen[nums[i]] += 1
                count += backtrack(i+1)
                seen[nums[i]] -= 1
            
            return count
        
        return backtrack(0) - 1
        
        