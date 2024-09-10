class Solution:
    def stoneGameVI(self, aliceValues: List[int], bobValues: List[int]) -> int:
        heap = []
        alice = 0
        aliceTurn = True

        for i in range(len(aliceValues)):
            heapq.heappush(heap, (-(aliceValues[i]+bobValues[i]), -aliceValues[i], -bobValues[i]))
        
        while heap:
            total, a, b = heapq.heappop(heap)

            if aliceTurn:
                alice-=a
                aliceTurn = False
            else:
                alice+=b
                aliceTurn = True
        
        if alice > 0:
            return 1
        elif alice < 0:
            return -1
        else: 
            return alice
        
        

        
