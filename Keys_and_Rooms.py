class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited=set()

        def dfs(i):
            if i in visited:
                return

            visited.add(i)

            for nbr in rooms[i]:
                dfs(nbr)
            
        dfs(0)
        if len(visited)==len(rooms):
            return True
        else:
            return False
