class Solution:
    def minOperations(self, s: str) -> int:
        count1, count2 = 0, 0
        prev1 = '0'
        prev2 = '1'

        for char in s:
            if char != prev1:
                count1 += 1
            else:
                count2 += 1
            
            prev1, prev2 = prev2, prev1
            
        return min(count1, count2)
            
            

