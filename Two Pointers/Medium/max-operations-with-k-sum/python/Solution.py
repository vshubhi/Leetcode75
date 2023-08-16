class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        start = 0
        end = n-1
        nop = 0
        while start<end:
            sum = nums[start]+nums[end]
            if sum == k:
                nop+=1
                start+=1
                end-=1
            elif sum<k:
                start+=1
            else:
                end-=1
        return nop