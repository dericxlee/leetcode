class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        check = set()

        for num in nums:
            if num not in check:
                check.add(num)
            else:
                check.remove(num)

        return len(check) == 0