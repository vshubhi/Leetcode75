class Solution:
    def dfs(self, isConnected, node, vis, n):
        vis[node] = True
        for i in range(n):
            if isConnected[node][i] == 1 and i != node and not vis[i]:
                self.dfs(isConnected, i, vis, n)
        
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        vis = [False] * n
        provinces = 0
        for i in range(n):
            if not vis[i]:
                provinces+=1
                self.dfs(isConnected, i, vis, n)
        return provinces
        