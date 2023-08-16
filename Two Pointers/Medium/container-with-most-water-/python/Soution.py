class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        start = 0
        end = n-1
        max_area = 0
        while(start<end):
            length = min(height[start],height[end])
            width = end-start
            curr_area = length * width
            max_area = max(max_area, curr_area)
            if height[start]<height[end]:
                start+=1
            else:
                end-=1
        return max_area