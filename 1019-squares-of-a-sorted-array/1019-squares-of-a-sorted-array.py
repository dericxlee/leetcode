class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        ans = []
        point_one = 0
        point_two = len(nums) - 1

        while point_one <= point_two:
            s1 = nums[point_one]**2
            s2 = nums[point_two]**2
            if s1 > s2:
                ans.append(s1)
                point_one+=1
            else:
                ans.append(s2)
                point_two-=1
        
        return reversed(ans)
    