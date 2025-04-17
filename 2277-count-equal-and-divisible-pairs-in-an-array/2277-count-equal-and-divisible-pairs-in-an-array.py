class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        index = defaultdict(list)
        result = 0

        for i, num in enumerate(nums):
            if index[num]:
                for idx in index[num]:
                    prod = i * idx
                    if prod % k == 0:
                        result += 1
            
            index[num].append(i)
        
        return result
            