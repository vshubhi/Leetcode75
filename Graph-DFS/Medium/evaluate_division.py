import collections
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj = collections.defaultdict(list)
        for i, eq in enumerate(equations):
            a, b = eq
            adj[a].append([b, values[i]])
            adj[b].append([a, 1/values[i]])
        

        def bfs(src, target):
            if src not in adj or target not in adj:
                return -1.0
            que, vis = deque(), set()
            que.append([src, 1.0])
            vis.add(src)
            while que:
                n, w = que.popleft()
                if n==target:
                    return w
                for nei in adj[n]:
                    node = nei[0]
                    weight = nei[1]
                    if node not in vis:
                        que.append([node, w*weight])
                        vis.add(node)
            return -1.0
        return [bfs(q[0], q[1]) for q in queries]
        