class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        res = []

        for coord in points:
            x = coord[0]
            y = coord[1]

            dist = x ** 2 + y ** 2

            heapq.heappush(heap, (dist, [x, y]))
        
        for _ in range(k):
            dist, coord = heapq.heappop(heap)
            res.append(coord)
        
        return res