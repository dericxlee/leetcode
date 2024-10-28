class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        map = defaultdict(int)
        res = 0

        for i in nums1:
            for j in nums2:
                map[i+j] += 1
        
        for k in nums3:
            for l in nums4:
                res += map[-(k+l)]
        
        return res
