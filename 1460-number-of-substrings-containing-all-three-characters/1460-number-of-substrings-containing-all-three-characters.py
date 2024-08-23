class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        counter = {}
        match = 'abc'
        left = 0
        ans = 0
        n = len(s)

        for right in range(n):
            counter[s[right]] = counter.get(s[right], 0) + 1

            while len(counter) == len(match):
                ans += n - right

                counter[s[left]] -=1

                if counter[s[left]] == 0:
                    del counter[s[left]]
                
                left+=1
    
        return ans

