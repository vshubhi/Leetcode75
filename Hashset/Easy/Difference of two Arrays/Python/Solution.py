class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        a1, a2 = [], []
        for num in nums1:
            if num not in nums2 and num not in a1:
                a1.append(num)
        for num in nums2:
            if num not in nums1 and num not in a2:
                a2.append(num)
        return [a1, a2]