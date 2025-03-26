class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        array = []

        for arr in grid:
            array += arr
        
        sorted_array = array.sort()

        mid = len(array) // 2
        base = array[mid]

        result = 0

        for num in array:
            diff = abs(base - num)

            if diff % x != 0:
                return -1
            
            result += diff // x
    
        return result

        
        
