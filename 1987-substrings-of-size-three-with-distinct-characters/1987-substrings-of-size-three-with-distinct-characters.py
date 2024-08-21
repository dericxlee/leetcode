class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        count = 0
        left = 0

        if len(s) < 3:
            return 0

        counter = Counter(s[0:3])
        
        if len(counter) == 3:
            count+=1

        for right in range(3, len(s)):
            counter[s[left]] -=1

            if counter[s[left]] == 0:
                del counter[s[left]]

            left+=1

            counter[s[right]] = counter.get(s[right], 0) + 1
            
            if len(counter) == 3:
                count+=1

        return count

        