class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        point_1 = 0
        point_2 = len(numbers) - 1

        while point_1 < point_2:
            if numbers[point_1] + numbers[point_2] > target:
                point_2 -= 1
            elif numbers[point_1] + numbers[point_2] < target:
                point_1 += 1
            else:
                return [point_1 + 1, point_2 + 1]
    
