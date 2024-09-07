import heapq

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        heap = [1]
        seen = {1}
        heapq.heapify(heap)

        for _ in range(n-1):
            num = heapq.heappop(heap)

            for p in [2, 3, 5]:
                if num*p not in seen:
                    heapq.heappush(heap, num*p)
                    seen.add(num*p)
        
        return heapq.heappop(heap)
