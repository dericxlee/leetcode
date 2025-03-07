class Solution:
    def isPrime(self, num: int):
        if num <= 1:
            return False

        if num == 2 or num == 3:
            return True
        
        if num % 2 == 0 or num % 3 == 0:
            return False
        
        sq = int(num**0.5)

        for i in range(5, sq+1, 2):
            if num % i == 0:
                return False
        
        return True


    def closestPrimes(self, left: int, right: int) -> List[int]:
        queue = deque()
        result = [-1, -1]
        diff = float('inf')

        for i in range(left, right+1):
            if self.isPrime(i):
                if queue and i - queue[-1] < diff:
                    result = [queue[-1], i]
                    diff = i - queue[-1]
                
                queue.append(i)
        
        return result