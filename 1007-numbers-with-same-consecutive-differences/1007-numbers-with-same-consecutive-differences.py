class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        result = set()

        def backtrack(num):
            if len(str(num)) == n:
                result.add(num)
                return 

            rem = num % 10

            if rem + k < 10:
                backtrack(num*10 + rem + k)
            
            if rem - k >= 0:
                backtrack(num*10 + rem - k)

        for i in range(1, 10):
            if i + k < 10 or i - k >= 0:
                backtrack(i)
        
        return list(result)


