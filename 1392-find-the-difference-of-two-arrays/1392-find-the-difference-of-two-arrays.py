class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        set2 = set(nums2)
        set1 = set()
        answer = [[], []]

        for num in nums1:
            if num not in set2 and num not in set1:
                answer[0].append(num)
            set1.add(num)
        
        for num in nums2:
            if num not in set1:
                answer[1].append(num)
                set1.add(num)
        
        return answer