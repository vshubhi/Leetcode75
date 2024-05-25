class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        vis = [False]*len(rooms)
        stack = []
        stack.append(0)
        vis[0] = True
        while stack:
            node = stack.pop()
            for neighbour in rooms[node]:
                if not vis[neighbour]:
                    stack.append(neighbour)
                    vis[neighbour] = True
        return all(vis)