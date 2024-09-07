class Solution:
    def largestInteger(self, num: int) -> int:
        s = str(num)
        idx = []
        even = []
        odd = []
        res = ''

        for char in s:
            if int(char) % 2 == 0:
                heapq.heappush(even, -int(char))
                idx.append(0)
            else:
                heapq.heappush(odd, -int(char))
                idx.append(1)
        
        for i in idx:
            if i == 0:
                n = abs(heapq.heappop(even))
                res += str(n)
            else:
                n = abs(heapq.heappop(odd))
                res += str(n)
        
        return int(res)