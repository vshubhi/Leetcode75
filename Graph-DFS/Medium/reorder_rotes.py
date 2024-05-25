class Solution:
    def __init__(self):
        self.count = 0

    def dfs(self, parent, node, adj):
        for edges in adj[node]:

            if edges[0]!=parent:
                self.count+= edges[1]
                self.dfs(node, edges[0], adj)

    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        adj = []
        # count= 0 
        for i in range(n):
            adj.append([])
        #adj[0] -> [[], []]
        for edge in connections:
            adj[edge[0]].append([edge[1], 1])
            adj[edge[1]].append([edge[0], 0])

        # print(adj[1])

        self.dfs(-1,0,adj)
        return self.count



        