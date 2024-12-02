class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        prefix = set()

        for num in arr:
            if num in prefix:
                return True

            prefix.add(num*2)

            if num % 2 == 0:
                prefix.add(num / 2)

        return False