class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        heap = []
        res = []

        for j in range(min(k, len(nums2))):
            heapq.heappush(heap, (nums1[0] + nums2[j], 0, j))
        
        while k > 0 and heap:
            add, i, j = heapq.heappop(heap)
            res.append([nums1[i], nums2[j]])

            if i+ 1 < len(nums1):
                heapq.heappush(heap, (nums1[i+1] + nums2[j], i + 1, j))
            
            k-=1

        return res 

