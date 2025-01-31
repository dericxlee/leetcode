class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        result = 0

        while l < r:
            con = min(height[l], height[r])
            result = max(result, (r-l)*con)

            if height[l] > height[r]:
                r -= 1
            else:
                l += 1

        return result
