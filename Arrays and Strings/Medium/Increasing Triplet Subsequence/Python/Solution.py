class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        n = len(nums)
        max_right = [0]*n
        max_right[-1]=nums[-1]
        for i in range(n-2, -1, -1):
            max_right[i] = max(max_right[i+1], nums[i+1])
        
        min_left = [0]*n
        min_left[0]=nums[0]
        for i in range(0, n-1):
            if min_left[i]<nums[i]<max_right[i]:
                return True
            min_left[i+1] = min(min_left[i], nums[i])
                    
        return False

        