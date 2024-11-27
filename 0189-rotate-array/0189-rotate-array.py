class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        times = k % n

        for _ in range(times):
            num = nums.pop()
            nums.insert(0, num)

