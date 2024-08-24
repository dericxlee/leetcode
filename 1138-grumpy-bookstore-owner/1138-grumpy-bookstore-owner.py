class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        left, satisfied, unsatisfied, max_unsatisfied = 0, 0, 0, 0, 

        for right in range(len(grumpy)):
            if grumpy[right] == 0:
                satisfied += customers[right]
            else:
                unsatisfied += customers[right]

            while grumpy[right] == 1 and right - left + 1 > minutes:

                if grumpy[left] == 1:
                    unsatisfied -= customers[left]
                
                left+=1
                
            max_unsatisfied = max(max_unsatisfied, unsatisfied)

        return satisfied + max_unsatisfied 
            
            
            
            

            


