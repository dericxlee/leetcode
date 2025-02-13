class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[1])
        print(points)
        result = 0
        end = float("-inf")

        for point in points:
            if end < point[0]:
                result += 1
                end = point[1]
            
        return result