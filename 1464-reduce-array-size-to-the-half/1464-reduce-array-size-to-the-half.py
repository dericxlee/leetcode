class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        count = Counter(arr)
        n = len(arr)
        removed = 0
        heap = []
        nums = set()

        for num, freq in count.items():
            heapq.heappush(heap, (-freq, num))
        
        while removed < n * (0.5):
            freq, num = heapq.heappop(heap)
            removed -= freq
            nums.add(num)

        return len(nums)
        
