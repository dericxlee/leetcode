class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)
        heap = []
        wait = 0
        res = ''

        for letter, freq in count.items():
            heapq.heappush(heap, (-freq, letter))

        while heap:
            freq, letter = heapq.heappop(heap)
            res+=letter
            freq += 1

            if wait:
                heapq.heappush(heap, wait)
                wait = 0

            if freq != 0:
                wait = (freq, letter)

        if wait:
            return ''
        
        return res
            


            

           
            

            

            

