class Solution:
    def maxArea(self, height: List[int]) -> int:
        point_1 = 0
        point_2 = len(height) - 1

        ans = 0

        while point_1 < point_2:
            if height[point_1] > height[point_2]:
                vol = height[point_2]*(point_2 - point_1)
                ans = max(ans, vol)
                point_2 -= 1
            else:
                vol = height[point_1]*(point_2 - point_1)
                ans = max(ans, vol)
                point_1 += 1

        return ans

