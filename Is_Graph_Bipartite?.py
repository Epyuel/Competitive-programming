class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color= [0 for _ in range(len(graph))]
        
        def bfs(i):
            if color[i]!=0:
                return True
            queue= deque([i])
            color[i]= -1
            while queue:
                node= queue.popleft()

                for nbr in graph[node]:
                    if color[nbr] == color[node]:
                        return False
                    elif color[nbr] == 0:
                        color[nbr]=-1*color[node]
                        queue.append(nbr)
            return True
        
        for i in graph:
            for j in i:
                if not bfs(j):
                    return False
        return True

