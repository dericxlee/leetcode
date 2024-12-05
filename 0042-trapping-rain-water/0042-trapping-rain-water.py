class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        l_height, r_height = 0, 0
        water = 0

        while left < right:
            if height[left] < height[right]:
                if height[left] >= l_height:
                    l_height = height[left]
                else:
                    water += l_height - height[left]
                
                left += 1
            
            else:
                if height[right] >= r_height:
                    r_height = height[right]
                else:
                    water += r_height - height[right]
                
                right -= 1

        return water
    