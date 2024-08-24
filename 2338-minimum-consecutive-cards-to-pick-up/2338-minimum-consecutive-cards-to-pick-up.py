class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        count = {}
        res, left = -1, 0

        for right in range(len(cards)):
            count[cards[right]] = count.get(cards[right], 0) + 1

            while count[cards[right]] > 1:
                res = right - left + 1 if res == -1 else min(res, right - left + 1)
                count[cards[left]] -=1
                left+=1

            
    
        return res
            
