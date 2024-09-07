class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        heapq.heapify(nums)
        res = []

        while nums:
            a = heapq.heappop(nums)
            res.append(heapq.heappop(nums))
            res.append(a)

        return res