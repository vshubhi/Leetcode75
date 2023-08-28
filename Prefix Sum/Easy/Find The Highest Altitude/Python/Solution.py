class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        prefix_sum = 0
        max_gain = 0
        for alt in gain:
            prefix_sum += alt
            max_gain = max(max_gain, prefix_sum)
        return max_gain