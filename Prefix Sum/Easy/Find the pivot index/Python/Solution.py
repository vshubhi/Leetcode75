class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        prefix_left = 0
        summ = sum(nums)

        for i in range(0,n):
            if prefix_left == (summ - prefix_left - nums[i]):
                return i
            prefix_left += nums[i]

        return -1
        
            