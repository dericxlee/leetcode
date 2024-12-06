class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        banned_n = set(banned)
        sum = 0
        result = 0

        for i in range(1, n + 1):
            if i not in banned_n:
                sum += i

                if sum > maxSum:
                    return result
                
                result += 1

        return result


