class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        count = Counter(arr)
        n = len(arr)
        goal = n // 2
        heap = [-value for value in count.values()]
        heapq.heapify(heap)
        res = 0
        
        while goal > 0:
            goal += heapq.heappop(heap)
            res += 1

        return res
        
