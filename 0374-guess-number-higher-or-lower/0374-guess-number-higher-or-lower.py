# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def binarySearch(self, start, end):
        mid = (start + end) // 2

        if guess(mid) == 0:
            return mid
        elif guess(mid) == 1:
            return self.binarySearch(mid + 1, end)
        else:
            return self.binarySearch(start, mid - 1)

    def guessNumber(self, n: int) -> int:
        return self.binarySearch(0, n)