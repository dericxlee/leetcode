class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        m = len(flowerbed)
        flowerbed.append(0)
        curr = 0

        for i in range(m):
            prev = curr
            curr = flowerbed[i]

            if curr:
                continue

            if not prev and not flowerbed[i+1]:
                n -= 1
                curr = 1
        
        return n <= 0
            