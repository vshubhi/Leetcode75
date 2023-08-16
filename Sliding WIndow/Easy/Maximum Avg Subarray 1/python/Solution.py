class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        start = 0
        end = 0
        n = len(nums)
        max_avg_subarr = -inf
        sum_ = 0
        for i in range(n):
            sum_ += nums[end]
            if end-start+1 == k:
                avg = sum_/(k)
                max_avg_subarr = max(max_avg_subarr, avg)
                sum_-=nums[start]
                start+=1
            end+=1
        return max_avg_subarr