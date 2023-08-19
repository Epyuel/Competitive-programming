class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        n=len(grid)
        def isInvalid(r,c):
            return r<0 or c<0 or r == n or c == n
        
        visited=set()
        change_dir=[(0,1),(0,-1),(1,0),(-1,0)]

        def dfs(row,column):
            if isInvalid(row,column) or (row,column) in visited or not grid[row][column]:
                return
            
            visited.add((row,column))

            for cr,cc in change_dir:
                dfs(row+cr,column+cc)
        
        def bfs():
            res=0
            queue=deque(visited)
            while queue:
                for i in range(len(queue)):
                    node= queue.popleft()
                    if node not in visited and grid[node[0]][node[1]]:
                        return res
                    for changeR,changeC in change_dir:
                        if isInvalid(node[0]+changeR,node[1]+changeC) or (node[0]+changeR,node[1]+changeC)in visited:
                            continue
                        if grid[node[0]+changeR][node[1]+changeC]:
                            return res
                        queue.append((node[0]+changeR,node[1]+changeC))
                        visited.add((node[0]+changeR,node[1]+changeC))
                res+=1

        for rw in range(n):
            for cl in range(n):
                if grid[rw][cl]:
                    dfs(rw,cl)
                    return bfs()

            
                    

            
                

        
