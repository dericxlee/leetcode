class Solution:
    def stoneGameVI(self, aliceValues: List[int], bobValues: List[int]) -> int:
        heap = []
        alice = 0
        aliceTurn = True

        for i in range(len(aliceValues)):
            heapq.heappush(heap, (-(aliceValues[i]+bobValues[i]), i))
        
        while heap:
            _, i = heapq.heappop(heap)

            if aliceTurn:
                alice+=aliceValues[i]
            else:
                alice-=bobValues[i]

            aliceTurn = not aliceTurn
        
        if alice > 0:
            return 1
        elif alice < 0:
            return -1
        else: 
            return alice