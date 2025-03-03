class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        n1, n2 = len(nums1), len(nums2)
        l, r = 0, 0
        idx = 0
        result = []

        while l < n1 and r < n2:
            if nums1[l][0] == nums2[r][0]:
                result.append([nums1[l][0], nums1[l][1] + nums2[r][1]])
                l += 1
                r += 1
            elif nums1[l][0] < nums2[r][0]:
                result.append(nums1[l])
                l += 1
            else:
                result.append(nums2[r])
                r += 1
        
        if l < n1:
            result += nums1[l:]
        if r < n2:
            result += nums2[r:]
    
        return result
