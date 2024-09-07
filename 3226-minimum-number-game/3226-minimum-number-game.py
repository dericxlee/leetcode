class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        heapq.heapify(nums)
        res = []

        while nums:
            a = heapq.heappop(nums)
            b = heapq.heappop(nums)

            res.append(b)
            res.append(a)

        return res