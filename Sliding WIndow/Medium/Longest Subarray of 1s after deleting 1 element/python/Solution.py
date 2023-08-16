class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        start = 0
        longest_window = 0
        zero_count = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                zero_count+=1
            if zero_count>1:
                if nums[start] == 0:
                    zero_count-=1
                start+=1
            print(i, start)
            longest_window = max(longest_window, i-start)
        return longest_window