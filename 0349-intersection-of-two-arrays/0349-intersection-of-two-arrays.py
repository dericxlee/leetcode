class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        freq = Counter(nums1)
        res = set()

        for num in nums2:
            if num in freq:
                res.add(num)
        
        return res
