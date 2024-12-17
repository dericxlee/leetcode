class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        freq = Counter(s)
        heap = []
        result = ''

        for value, key in freq.items():
            heapq.heappush(heap, (-ord(value), key))

        while heap:
            x1, y1 = heapq.heappop(heap)
            char1 = chr(-x1)
            times = min(y1, repeatLimit)

            result += char1*times
            y1 -= times

            if y1:
                if not heap: break

                x2, y2 = heapq.heappop(heap)
                char2 = chr(-x2)
                
                result += char2
                y2 -= 1

                heapq.heappush(heap, (x1, y1))
                
                if y2: heapq.heappush(heap, (x2, y2))
            
        return result



            
