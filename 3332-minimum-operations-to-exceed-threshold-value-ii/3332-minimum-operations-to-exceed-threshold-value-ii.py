class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        result = 0

        while nums[0] < k:
            first = heapq.heappop(nums)
            second = heapq.heappop(nums)

            result += 1

            num = first*2 + second
            heapq.heappush(nums, num)

        return result


