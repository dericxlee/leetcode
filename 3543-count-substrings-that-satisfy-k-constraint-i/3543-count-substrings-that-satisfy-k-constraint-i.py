class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        ans = 0
        left = 0
        counter = {'0': 0, '1': 0}

        if k == 0:
            return 0

        for right in range(len(s)):
            counter[s[right]] = counter.get(s[right], 0) + 1

            while counter['0'] > k and counter['1'] > k:
                counter[s[left]] -=1
                left+=1

            ans += right - left + 1
        
        return ans

