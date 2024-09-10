class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        heap = []
        n = len(matrix)

        for i in range(n):
            heapq.heappush(heap, (matrix[i][0], i, 0))
        
        while k > 1:
            num, i, j = heapq.heappop(heap)

            if j + 1 < n:
                heapq.heappush(heap, (matrix[i][j+1], i, j+1))
            
            k-=1

        return heap[0][0]
            