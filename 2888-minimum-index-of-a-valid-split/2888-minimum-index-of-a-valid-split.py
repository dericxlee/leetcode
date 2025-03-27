class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        n = len(nums)
        counter = Counter(nums)
        sorted_counter = counter.most_common()
        match = sorted_counter[0][0]
        total = sorted_counter[0][1]

        count = 0

        for i, num in enumerate(nums):
            if num == match:
                count += 1

            if count > (i + 1) // 2 and total - count > (n - i - 1) // 2:
                return i
        
        return -1
            

