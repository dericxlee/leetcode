class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        left = 0
        res = 0
        counter = {}

        for right in range(len(fruits)):
            counter[fruits[right]] = counter.get(fruits[right], 0) + 1
            
            while len(counter) > 2:
                counter[fruits[left]] -=1

                if counter[fruits[left]] == 0:
                    del counter[fruits[left]]
                
                left+=1
            
            res = max(res, right - left + 1)
        
        return res
            
