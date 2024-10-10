class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        freq = Counter(nums1)
        res = []

        for num in nums2:
            if num in freq:
                freq[num] -= 1
                res.append(num)
            
            if freq[num] == 0:
                del freq[num]
        
        return res
            