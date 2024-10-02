class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        sumDigits = {}
        res = -1

        for num in nums:
            string = str(num)
            total = 0
            for s in string:
                total += int(s)
            
            if total not in sumDigits:
                sumDigits[total] = []
            
            heapq.heappush(sumDigits[total], num)

            if len(sumDigits[total]) > 2:
                heapq.heappop(sumDigits[total])
        
        for key, value in sumDigits.items():
            if len(value) == 2:
                sum = 0
                sum += heappop(value)
                sum += heappop(value)
                
                res = max(res, sum)

        return res
        
