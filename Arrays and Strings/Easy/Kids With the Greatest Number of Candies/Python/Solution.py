class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        n = len(candies)
        result = []
        greatest_candies = 0
        for i in range(n):
            greatest_candies = max(candies[i], greatest_candies)
        for i in range(n):
            if candies[i]+extraCandies >= greatest_candies:
                result.append(True)
            else:
                result.append(False)
        return result