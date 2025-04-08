class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        dupe = 0
        freq = defaultdict(int)
        n = len(nums)

        for num in nums:
            freq[num] += 1

            if freq[num] > 1:
                dupe += 1
        
        i = 0
        result = 0
        
        while dupe and n - i >= 3:
            result += 1

            for _ in range(3):
                num = nums[i]

                if freq[num] > 1:
                    dupe -= 1
                
                freq[num] -= 1
                i += 1
        
        return result if not dupe else result + 1