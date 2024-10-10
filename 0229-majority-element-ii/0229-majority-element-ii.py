class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        freq = Counter(nums)
        res = []

        for key in freq.keys():
            if freq[key] > n/3:
                res.append(key)
        
        return res
