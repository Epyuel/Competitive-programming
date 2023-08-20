class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n=len(isConnected)
        graph={}
        visited=set()
        res=0

        for i in range(n):
            for j in range(n):
                if isConnected[i][j]:
                    if i not in graph:
                        graph[i]=[j]
                    else:
                        graph[i].append(j)
                    if j not in graph:
                        graph[j]=[i]
                    else:
                        graph[j].append(i)

        def dfs(node):
            if node in visited:
                return 
            visited.add(node)
            for child in graph[node]:
                dfs(child)

        for i in graph:
            len_visited=len(visited)
            dfs(i)
            if len_visited < len(visited):
                res+=1

        return res
