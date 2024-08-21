class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        ans = 0
        counter = {}
        max_count = 0

        for right in range(len(s)):
            counter[s[right]] = counter.get(s[right], 0) + 1

            max_count = max(max_count, counter[s[right]])

            while (right-left+1) - max_count > k and left <= right:
                counter[s[left]] -=1
                left+=1
            
            ans = max(ans, right-left+1)

        return ans
