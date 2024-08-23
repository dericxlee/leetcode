class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        idx = list('abcdefghijklmnopqrstuvwxyz')
        ans = 0
        curr_sum = 0
        arr = []
        left = 0

        for i in range(len(s)):
            diff = abs(idx.index(s[i]) - idx.index(t[i]))
            arr.append(diff)
        
        for right in range(len(arr)):
            curr_sum += arr[right]

            while curr_sum > maxCost:
                curr_sum -= arr[left]
                left+=1
            
            ans = max(ans, right - left + 1)
        
        return ans

