class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        freq = Counter(nums[:k])
        l, result = 0, []
        heap = []
        add = 0

        for key, value in freq.items():
            heapq.heappush(heap, (-value, -key))

        for _ in range(x):
            if heap:
                value, key = heapq.heappop(heap)
                add += value*key
        
        result.append(add)

        for r in range(k, len(nums)):
            heap.clear()
            add = 0

            num = nums[r]
            freq[num] = freq.get(num, 0) + 1
            tail = nums[l]
            freq[tail] -= 1
            l += 1

            for key, value in freq.items():
                heapq.heappush(heap, (-value, -key))

            for _ in range(x):
                if heap:
                    value, key = heapq.heappop(heap)
                    add += value*key

            result.append(add)
        
        return result



            


