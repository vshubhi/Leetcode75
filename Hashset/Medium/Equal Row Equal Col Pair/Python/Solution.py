class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        hm = {}

        n = len(grid)
        m = len(grid[0])
        ans = 0
        for i in range(n):
            row = tuple(grid[i])
            if row not in hm:
                hm[row] = 0
            hm[row] += 1
        for i in range(m):
            x = []
            for j in range(n):
                x.append(grid[j][i])
            if tuple(x) in hm:
                ans+=hm.get(tuple(x), 0)
        return ans