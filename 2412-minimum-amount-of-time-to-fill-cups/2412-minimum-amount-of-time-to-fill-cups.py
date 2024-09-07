class Solution:
    def fillCups(self, amount: List[int]) -> int:
        heap = [-a for a in amount]
        heapq.heapify(heap)
        res = 0

        while heap and heap[0]:
            res += 1

            a = heapq.heappop(heap) + 1

            if heap[0]:
                b = heapq.heappop(heap) + 1

                heapq.heappush(heap, a)
                heapq.heappush(heap, b)
            else:
                heapq.heappush(heap, a)
            
        return res