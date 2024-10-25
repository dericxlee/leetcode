class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        map = dict()
        stack = []
        res = [-1]*len(nums1)

        for num in nums2:
            while stack and stack[-1] < num:
                node = stack.pop()
                map[node] = num

            stack.append(num)
        
        for i in range(len(nums1)):
            if nums1[i] in map:
                res[i] = map[nums1[i]]
            
        return res


